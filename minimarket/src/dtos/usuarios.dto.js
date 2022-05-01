import modelPrisma from '@prisma/client';
import validator from 'validator'
import { Prisma } from '../prisma.js'

export function usuarioRequestDTO(data){
    const errores = [];
    let user = {nombre:'', email:'', password:'', rol:''}
    const campos = Object.keys(user);
    // const camposs = {...Prisma.usuario};
    // console.log('CAMPOSS ',camposs)
    
    campos.find((pro)=>{
        console.log(pro)
        if(!data.hasOwnProperty(pro)){ errores.push(`Falta el campo '${pro}'.`); }
    })
        
    if(errores.length != 0){ throw new Error(errores) }

    user = {...data};

    if(validator.isEmpty(user.email)){ errores.push('El email no puede estar vacio.'); }
    if(!validator.isEmail(user.email)){ errores.push('El email no es un correo valido'); }
    if(validator.isEmpty(user.password)){ errores.push('El password no puede estar vacio.'); }
    if(validator.isEmpty(user.nombre)){ errores.push('El nombre no puede estar vacio.'); }
    if(user.rol !== modelPrisma.USUARIO_ROL.ADMINISTRADOR && user.rol !== modelPrisma.USUARIO_ROL.CLIENTE){
        errores.push(`El rol puede ser ${modelPrisma.USUARIO_ROL.ADMINISTRADOR} o ${modelPrisma.USUARIO_ROL.CLIENTE}`)
    }

    if(errores.length != 0){ throw new Error(errores) }
    else{ return {...user}; }
}

export function loginRequestDTO({email, password}){
    const errores = [];
    if(validator.isEmpty(email)){ errores.push('El email no puede estar vacio.'); }
    if(!validator.isEmail(email)){ errores.push('El email no es un correo valido'); }
    if(validator.isEmpty(password)){ errores.push('El password no puede estar vacio.'); }

    if(errores.length != 0){ throw new Error(errores) }
    else{ return { email, password }; }
}

export function verificarCuentaRequestDTO(data){
    const errores = [];
    let user = {hash:''}
    const campos = Object.keys(user);
    // console.log('CAMPOSS ',camposs)
    
    campos.forEach((pro)=>{
        if(!data.hasOwnProperty(pro)){ errores.push(`Falta el campo '${pro}'.`); }
    })
        
    if(errores.length != 0){ throw new Error(errores) }

    user = {...data};

    if(validator.isEmpty(user.hash)){ errores.push('El password no puede estar vacio.'); }

    if(errores.length != 0){ throw new Error(errores) }
    else{ return { ...user }; }
}

export function hashDataRequestDTO(data){
    const errores = [];
    let user = {nombre:'', email:''}
    const campos = Object.keys(user);
    // console.log('CAMPOSS ',camposs)
    
    campos.forEach((pro)=>{
        if(!data.hasOwnProperty(pro)){ errores.push(`Falta el campo '${pro}'.`); }
    })
        
    if(errores.length != 0){ throw new Error(errores) }

    user = {...data};

    if(!validator.isEmail(user.email)){ errores.push('El email no es un correo valido.'); }
    if(validator.isEmpty(user.nombre)){ errores.push('El nombre no puede estar vacio.'); }

    if(errores.length != 0){ throw new Error(errores) }
    else{ return { ...user }; }
}