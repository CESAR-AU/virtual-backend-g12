import { Router } from "express";
import { agregarLibro, actualizarLibro, eliminarLibro, optenerLibro, listarLibros } from "../controllers/libros.controllers.js";
import { validadorToken } from "../utils/validator.js";

export const librosRouter = Router();

librosRouter.route('/libros')
.all(validadorToken)
.post(agregarLibro)
.put(actualizarLibro)
.get(listarLibros)

librosRouter.route('/libro/:_id')
.all(validadorToken)
.get(optenerLibro)
.delete(eliminarLibro)