import { Router } from 'express'
import { crearUsuario, login, confirmarCuenta, perfil } from '../controllers/usuarios.controller.js';
import { verificartToken } from '../utils/validador.js';

export const usuarioRouter = Router();

usuarioRouter.route('/registro').post(crearUsuario);
usuarioRouter.post('/login', login);
usuarioRouter.post('/confirmar-cuenta', confirmarCuenta);
usuarioRouter.get('/perfil',verificartToken, perfil);