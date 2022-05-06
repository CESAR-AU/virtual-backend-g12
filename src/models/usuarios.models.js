import mongoose from "mongoose";
import bcryptjs from "bcryptjs";

const usuarioSchema = new mongoose.Schema({
  correo: {
    type: mongoose.Schema.Types.String,
    required: true,
    lowercase: true,
    maxlength: 100,
  },
  nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
  },
  telefono: mongoose.Schema.Types.Number,
  password: {
      type: mongoose.Schema.Types.String,
      set: (valor)=> bcryptjs.hashSync(valor, 10),
    //   get: (valor) => null,
      
  }
});

export const Usuario = mongoose.model('usuarios', usuarioSchema);
