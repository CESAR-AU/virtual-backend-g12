import { hashSync, compareSync } from 'bcrypt'
import jsonwebtoken from 'jsonwebtoken'
import { Prisma } from '../prisma.js'
import { loginRequestDTO, usuarioRequestDTO, verificarCuentaRequestDTO, hashDataRequestDTO } from '../dtos/usuarios.dto.js'
import { enviarCorreoValidacion } from '../utils/sendMail.js'

import cryptojs from 'crypto-js'

export const crearUsuario = async (req, res) => {
    try{
        const data = usuarioRequestDTO(req.body);
        data.password = hashSync(data.password, 10);

        const nuevoUsuario = await Prisma.usuario.create({
            data: {...data},
            select: {id:true, nombre:true, email:true, rol:true, validado:true},
        });

        // crear txt encriptado
        const hash = cryptojs.AES.encrypt(
            JSON.stringify({nombre: nuevoUsuario.nombre, email: nuevoUsuario.email}),
            process.env.LLAVE_ENCRIPTACION
        ).toString();
        
        await enviarCorreoValidacion({destino:nuevoUsuario.email, hash:hash})
        return res.status(201).json({
            message: 'Usuario creado exitosamente',
            success: true,
            data: nuevoUsuario
        });
    }catch(ex){
        //Error de la clase Error
        if (ex instanceof Error){
            return res.status(400).json({
                message: 'No fue posible crear el usuario',
                success: false,
                error: ex.message,
            });
        }        
    }
}

export const login = async (req,res)=> {
    try{
        const data = loginRequestDTO(req.body)
        const usuario = await Prisma.usuario.findFirst({ 
            where:{email: req.email},
            rejectOnNotFound:true
        })
        // validar password
        if(compareSync(data.password, usuario.password)){
            const token = jsonwebtoken.sign({
                id: usuario.id, 
                message: 'API de Minimarket',
            }, process.env.JWT_SECRET_KEY, { expiresIn: '12h'})
            return res.status(200).json({
                message: `Bienvenido ${usuario.nombre}`,
                success: true,
                token,
            });
        }else{
            throw new Error('Credenciales incorrectas')
        }
    }catch(ex){
        if (ex instanceof Error){
            return res.status(400).json({
                message: 'Error al hacer el inicio de login',
                success: false,
                error: ex.message,
            });
        } 
    }
}

export const confirmarCuenta = async (req,res) =>{
    try{
        const data = verificarCuentaRequestDTO(req.body);
        const dataInfo = cryptojs.AES.decrypt(data.hash, process.env.LLAVE_ENCRIPTACION).toString(cryptojs.enc.Utf8);
        if(dataInfo == ''){ throw Error('Credenciales incorrectas'); }
        const jsonData = JSON.parse(dataInfo);
        const data_valido = hashDataRequestDTO(jsonData);

        const usuarioEncontrado = await Prisma.usuario.findFirst({ 
            where:{ email: data_valido.email, validado:false, },
            select: { id:true }
        })

        if( !usuarioEncontrado ){ throw Error('Su cuenta ya esta verificada.') }

        // const usuarioActualizado = await Prisma.usuario.update({data: {...usuarioEncontrado, validado: true}, where: {id: usuarioEncontrado.id}})
        const usuarioActualizado = await Prisma.usuario.update({data: {validado: true}, where: {id: usuarioEncontrado.id}})
        console.log(usuarioActualizado);

        return res.status(200).json({
            message: 'Cuenta verificada correctamente',
            success: true,
            data: data_valido,
            ddd: usuarioActualizado
        });
    }catch(ex){
        if (ex instanceof Error){
            return res.status(400).json({
                message: 'Error al verificar la cuenta',
                success: false,
                error: ex.message,
            });
        } 
    }
}

//controlado protegida con JWT
export const perfil = async (req,res) =>{
    console.log(req.user);

    return res.json({
        message:'Bienvenido',
        data: req.user,
    })
}