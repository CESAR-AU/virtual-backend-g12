import { Router } from "express";
import { registrarUsuario, login } from "../controllers/usuarios.controller.js";

export const usuarioRouter = Router();

usuarioRouter.post('/registro', registrarUsuario);
usuarioRouter.post('/login', login);