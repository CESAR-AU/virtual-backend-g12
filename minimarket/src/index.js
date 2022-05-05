import express, {json} from 'express'
import { productosRouter } from './routes/productos.routes.js';
import { usuarioRouter } from './routes/usuarios.routes.js';
import { pedidosRouter } from './routes/pedidos.routes.js'
import { detallePedidoRouter } from './routes/pedidoDetalle.routes.js'
import { pagosRouter } from './routes/pagos.routes.js';

//MERCADO PAGO 
import mercadopago from 'mercadopago';



console.log(process.env.EMAIL_HOST_USER)

const app = express();

mercadopago.configure({
    access_token: process.env.MP_ACCESS_TOCKEN,
    integrator_id: process.env.MP_INTEGRATOR_ID
});

app.use(json())

const PORT = process.env.PORT ?? 3000;

app.get('/', (req,res)=>{
    res.json({
        message:'Bienbenido a mi API del minimarket'
    })
})

//Rutas definidas en otro archivos
app.use(productosRouter, usuarioRouter, pedidosRouter, detallePedidoRouter, pagosRouter);

app.listen(PORT, ()=>{
    console.log(`Servidor corriendo en el puesto ${PORT}`)
})

