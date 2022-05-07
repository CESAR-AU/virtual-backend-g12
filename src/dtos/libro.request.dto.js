import validator from 'validator';

export const LibroRequestDTO = (data) => {
    let libro = {nombre:'', avance: '', numPagina: ''}
    const errores = []
    const propiedades = Object.keys(libro);
    propiedades.forEach((prop)=>{
        if(!data.hasOwnProperty(prop)){ errores.push(`Falta el campo '${prop}'.`); }
    })
    if(errores.length !== 0){ throw new Error(errores) }

    libro = {...data}

    if(validator.isEmpty(libro.nombre)){
        errores.push('nombre no puede estar vacio')
    }

    if(libro.avance !== 'COMPLETO' && libro.avance !== 'INCOMPLETO'){
        errores.push('avance debe ser COMPLETO o INCOMPLETO')
    }

    if(libro.avance === 'INCOMPLETO'){
        if(validator.isEmpty(libro.numPagina.toString()) || !libro.numPagina){
            errores.push('numPagina no puede ser vacio si el aance es INCOMPLETO')
        }
    }

    if(errores.length !== 0){
        throw Error(errores);
    }else{
        return {...libro}
    }
}