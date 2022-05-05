import { Router } from 'express';

import { crearDetallePedido } from '../controllers/detallePedido.controller.js';
import { validarCliente, verificartToken } from '../utils/validador.js';

export const detallePedidoRouter = Router();

detallePedidoRouter.route('/detalle-pedido')
.all(verificartToken, validarCliente)
.post(crearDetallePedido);