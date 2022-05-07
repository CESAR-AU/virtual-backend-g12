import { Usuario } from "../models/usuarios.models.js";
import bcriptjs from "bcryptjs";
import jwt from 'jsonwebtoken'

export const registrarUsuario = async (req, res) => {
  try {
    const data = req.body;
    const nuevoUsuario = await Usuario.create(data);
    // const respuesta = {...nuevoUsuario._doc, password: ""}
    delete nuevoUsuario["_doc"]["password"];

    const result = nuevoUsuario.toJSON();
    delete result["password"];

    return res.status(201).json({
      message: "Usuario creado exitosamente",
      data: result, // nuevoUsuario
    });
  } catch (ex) {
    return res.status(400).json({
      message: "Error al crear usuario",
      error: ex.message,
    });
  }
};

export const login = async (req, res) => {
  try {
    const data = req.body;

    const usuarioEncontrado = await Usuario.findOne({ correo: data.correo });

    if (!usuarioEncontrado) {
      return res.status(400).json({
        message: "Credenciales incorrectas",
      });
    }

    console.log(usuarioEncontrado)

    if (bcriptjs.compareSync(data.password, usuarioEncontrado.password)) {
      const token = jwt.sign(
        {_id: usuarioEncontrado._id},
        process.env.JWT_SECRET,
        { expiresIn: "12h" }
      );

      return res.status(200).json({
        message: "Bienvenido",
        data: token
      });
    } else {
      return res.status(400).json({
        message: "Credenciales incorrectas",
      });
    }
  } catch (ex) {
    return res.status(400).json({
      message: "Credenciales incorrectas",
      error: ex.message,
    });
  }
};
