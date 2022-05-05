import prisma from '@prisma/client';
import jsonwebtoken from 'jsonwebtoken';
import { Prisma } from '../prisma.js';

export async function verificartToken(req, res, next){
    try{
        if(!req.headers.authorization){
            return res.status(401).json({
                message:'Se necesita un token para realizar esta peticion.'
            });
        }

        const token = req.headers.authorization.split(' ')[1]
        const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET_KEY);

        const usuarioEncontrado = await Prisma.usuario.findUnique({
            where:{id: payload.id},
            rejectOnNotFound:true,
        });

        req.user = usuarioEncontrado;

        next();
    }catch(ex){
        return res.status(400).json({
            message:'Token invalida',
            data: ex.message
        })
    }

}

export const validarAdmin = async (req, res, next) => {
    //
    if(req.user.rol !== prisma.USUARIO_ROL.ADMINISTRADOR){
        return res.status(401).json({
            message:'El usuario no tiene los privilegios para realizar esta operacion'
        });
    }else{ next(); }
}

export const validarCliente = async (req, res, next) => {
    //
    console.log(req.user.rol)
    console.log(req.user)
    if(req.user.rol !== prisma.USUARIO_ROL.CLIENTE){
        return res.status(401).json({
            message:'El usuario no tiene los privilegios para realizar esta operacion'
        });
    }else{ next(); }
}