import { Router } from "express";
import {
  actualizarProducto,
  buscarProducto,
  crearProducto,
  eliminarProducto,
  listarProductos,
} from "../controllers/productos.controller.js";
import { validarAdmin, verificartToken } from "../utils/validador.js";

export const productosRouter = Router();
productosRouter
  .route("/productos")
  .post(verificartToken, validarAdmin, crearProducto)
  .get(listarProductos);
productosRouter
  .route("/producto/:id")
  .get(buscarProducto)
  .all(verificartToken, validarAdmin)
  .put(actualizarProducto)
  .delete(eliminarProducto);
