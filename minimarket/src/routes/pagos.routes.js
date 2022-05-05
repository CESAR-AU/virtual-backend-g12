import { Router } from "express";
import { crearPreferencia, mercadoPagoWebhooks } from "../controllers/pagos.controller.js";

export const pagosRouter =  Router();

pagosRouter.post("/generar-pago", crearPreferencia);
pagosRouter.post('/mp-webhooks', mercadoPagoWebhooks);