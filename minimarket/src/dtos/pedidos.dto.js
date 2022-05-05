import validator from 'validator';

export const crearPedidoRequetsDTO = (data) => {
    const errores = [];
    let pedido = {clienteId:''}
    const campos = Object.keys(pedido);
    // console.log('CAMPOSS ',campos)
    
    campos.forEach((pro)=>{
        if(!data.hasOwnProperty(pro)){ errores.map(`Falta el campo '${pro}'.`); }
    })
    if(errores.length != 0){ throw new Error(errores) }
    
    pedido = {...data};
    
    if(validator.isEmpty(pedido.clienteId.toString())){ errores.map('El clienteId no puede estar vacio.'); }

    if(errores.length != 0){ throw new Error(errores) }
    else{ return { ...pedido }; }
}