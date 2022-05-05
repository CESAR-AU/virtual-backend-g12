import { Prisma } from "../prisma.js";
import { crearDetallePedidoRequestDTO } from "../dtos/detallePedido.dto.js";

export const crearDetallePedido = async (req, res) => {
    try{
        const data = crearDetallePedidoRequestDTO(req.body);
        // const nuevoDetalle = {};
        const pedido = {};
        /*await Prisma.$transaction([
            /*nuevoDetalle = await Prisma.detallePedido.create({data}),
            pedido = Prisma.pedido.update({
                data: { total: 10.00},
                where: { id: data.pedidoId },
            }),

            const { precio } = await Prisma.producto.findUnique({

            })
        ]);*/
        
        await Prisma.$transaction( async ()=>{
            //busqueda del producto
            const { precio } = await Prisma.producto.findUnique({
                where: {id: data.productoId},
                rejectOnNotFound: true,
                select: {precio:true},
            });
            //busqueda del pedido
            const {id, total } = await Prisma.pedido.findUnique({
                where: {id: data.pedidoId},
                select: {id:true, total:true},
                rejectOnNotFound:true,
            });
            //crear detalle del pedido encontrado
            const {subTotal} = await Prisma.detallePedido.create({
                data: {...data, subTotal: precio * data.cantidad },
                select: { subTotal:true},
            });
            //actualizacion del pedido encontrado
            await Prisma.pedido.update({
                data: { total: total + subTotal },
                where: { id },
            });
        })

        
        return res.status(201).json({
            message: 'Detalle creado exitosamente',
            data: {}
        })
    }
    catch(ex){
        if (ex instanceof Error){
            return res.status(400).json({
                message: 'Error al crear el detalle del pedido',
                success: false,
                error: ex.message,
            });
        }
    }
}