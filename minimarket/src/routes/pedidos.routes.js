import { Router } from 'express';

import { crearPedido, listarPedido } from '../controllers/pedidos.controller.js';
import { validarCliente, verificartToken } from '../utils/validador.js';

export const pedidosRouter = Router();

pedidosRouter
.route('/pedidos')
.all(verificartToken, validarCliente)
.post( crearPedido )
.get( listarPedido );