import { Router } from 'express'
import { actualizarProducto, buscarProducto, crearProducto, eliminarProducto, listarProductos } from '../controllers/productos.controller.js'

export const productosRouter = Router()
productosRouter.route('/productos').post(crearProducto).get(listarProductos);
productosRouter.route('/producto/:id').put(actualizarProducto).delete(eliminarProducto).get(buscarProducto);