import { Prisma } from '../prisma.js'

export const crearProducto = async (req, res) => {
    try{
        const nuevoProducto = await Prisma.producto.create({ data: req.body });
        console.log(nuevoProducto)
        return res.json({
            message:'Producto agregado exitosamente',
            data: nuevoProducto
        })
    } catch(ex){
        console.log(ex)
        return res.json({
            message:'Error al crear producto',
            error: {}
        })
    }
    /*await nuevoProducto.then((res)=>{
        console.log(res.nombre)
        return res.json({
            message:'Producto agregado exitosamente',
            data: {res}
        })
    }).catch((err)=>{
        console.log(`Error: ${err}`)
        return res.status(404).json({
            message:'Errores',
            error:err
        })
    })*/
}

export const listarProductos = async (req, res) => {
    try{
        const productos = await Prisma.producto.findMany({})
        return res.json({
            message:'Lista de productos',
            success: true,
            data: productos
        })
    }catch(ex){
        return res.json({
            message:'Error al listar productos',
            success: true,
        })
    }
}

export const actualizarProducto = async (req, res) => {
    try{
        const { id } = req.params
        // const producto = await Prisma.producto.findUnique({where:{id: parseInt(id)}})
        const producto = await Prisma.producto.findUnique(
            {
                where:{id: +id}, 
                select: { id:true }, 
                rejectOnNotFound:true
            }
        )
        const productoActualizado = await Prisma.producto.update({data: req.body, where: {id: producto.id}})
        return res.json({
            message:'Producto actualizado',
            success: true,
            data: productoActualizado
        })
        
    }catch(ex){
        return res.json({
            message:'Error al actualizar el producto',
            success: false,
            error:ex
        })
    }
}

export const eliminarProducto = async (req, res) => {
    try{
        const { id } = req.params
        const producto = await Prisma.producto.findUnique( { where: {id: +id}, select:{ id:true }, rejectOnNotFound:true} )
        const productoEliminado = await Prisma.producto.delete({ where: { id: producto.id }} )
        return res.json({
            message:'Producto eliminado',
            success: true,
            data: productoEliminado
        })
        
    }catch(ex){
        return res.json({
            message:'Error al eliminar el producto',
            success: false,
            error:ex
        })
    }
}

export const buscarProducto = async (req, res) => {
    try{
        const { id } = req.params
        const producto = await Prisma.producto.findUnique({where:{id: Number(id)}, rejectOnNotFound:true})
        return res.json({
            message:'Producto encontrado',
            success: true,
            data: producto
        })
        
    }catch(ex){
        return res.json({
            message:'Error al buscar el producto',
            success: false,
            error:ex
        })
    }
}