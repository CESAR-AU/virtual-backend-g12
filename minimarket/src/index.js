import express, {json} from 'express'
import { productosRouter } from './routes/productos.routes.js';
import { usuarioRouter } from './routes/usuarios.routes.js';

console.log(process.env.EMAIL_HOST_USER)

const app = express();

app.use(json())

const PORT = process.env.PORT ?? 3000;

app.get('/', (req,res)=>{
    res.json({
        message:'Bienbenido a mi API del minimarket'
    })
})

//Rutas definidas en otro archivos
app.use(productosRouter, usuarioRouter);

app.listen(PORT, ()=>{
    console.log(`Servidor corriendo en el puesto ${PORT}`)
})

