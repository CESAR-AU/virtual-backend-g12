import { crearPedidoRequetsDTO } from "../dtos/pedidos.dto.js";
import { Prisma } from "../prisma.js";

export const crearPedido = async (req, res) => {
    try{
        const { clienteId } = crearPedidoRequetsDTO({clienteId: req.user.id})
        console.log(req.user.id.toString());
        console.log(clienteId);

        const pedidoCreado = await Prisma.pedido.create({
            data:{
                estado: "CREADO",
                fecha: new Date(),
                total: 0.00,
                clienteId
            },
            select:{id:true, },
        })

        return res.status(201).json({
            message: 'Pedido creado exitosamente',
            success: true,
            data: pedidoCreado,
        });

    }catch(ex){
        if (ex instanceof Error){
            return res.status(400).json({
                message: 'Error al crear el pedido',
                success: false,
                error: ex.message,
            });
        }
    }
}

export const listarPedido = async (req, res) => {
    try{
        const pedidos = await Prisma.pedido.findMany({
            select:{
                id:true, 
                cliente: {select: {nombre:true, }}, 
                detallePedidos: {select: {id:true, cantidad:true, producto:true, subTotal:true}}, 
                estado:true, 
                fecha: true, 
                total:true}
        })

        return res.status(201).json({
            message: 'Lista de pedidos',
            success: true,
            data: pedidos,
        });

    }catch(ex){
        if (ex instanceof Error){
            return res.status(400).json({
                message: 'Error al listar los pedidos',
                success: false,
                error: ex.message,
            });
        }
    }
}