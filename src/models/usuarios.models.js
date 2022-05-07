import mongoose from "mongoose";
import bcryptjs from "bcryptjs";

const libroSchema = new mongoose.Schema({
  nombre: {type: mongoose.Schema.Types.String, required: true},
  avance: {type: mongoose.Schema.Types.String, enum: ['COMPLETO', 'INCOMPLETO',], required: true},
  numPagina: {
    type: mongoose.Schema.Types.Number,
    min:1,
    name: 'num_pagina'
  }
}, {
  // _id: false, //para no crear automaticamente el id
  timestamps: {updatedAt: 'fecha_actualizacion'}
}) 

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
      
  },
  // libro: libroSchema
  libros: [libroSchema]
});

export const Usuario = mongoose.model('usuarios', usuarioSchema);
