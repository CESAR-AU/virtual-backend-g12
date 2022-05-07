import express from "express";
import morgan from "morgan";
import mongoose from "mongoose";
import { usuarioRouter } from "./routers/usuario.routes.js";
import { librosRouter } from "./routers/libros.routes.js";

const app = express();
// https://www.npmjs.com/package/morgan
const logger = morgan("dev");
// morgan es un middleware que me ayuda a poder hacer seguimiento a las peticiones a mi API
app.use(logger);
app.use(express.json())
app.use(usuarioRouter, librosRouter);

const PORT = process.env.PORT ?? 3000;
console.log("APPPPPPPPPPP");
mongoose
  .connect(process.env.MONGO_URL, {dbName: process.env.DBNAME})
  .then((value) => {
    console.log("Conectado a la DB ✔");
  })
  .catch((error) => {
    console.log("Error al conectarse a la DB ❌");
  });



app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
