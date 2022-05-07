// import { libroSchema } from './../models/usuarios.models.js'
import { LibroRequestDTO } from "../dtos/libro.request.dto.js";
import { Usuario } from "../models/usuarios.models.js";

export const agregarLibro = async (req, res) => {
  try {
    const libro = LibroRequestDTO(req.body);
    const usuarioActual = req.user;

    usuarioActual.libros.push(libro);
    await usuarioActual.save();

    return res.status(201).json({
      message: "Libro agregado exitosamente",
      data: usuarioActual.libros,
    });
  } catch (ex) {
    return res.status(400).json({
      message: "Error al agregar libro",
      error: ex.message,
    });
  }
};

export const actualizarLibro = (req, res) => {
  const data = req.body;

  return res.status(200).json({
    message: "Libro actualizado",
    data: data,
  });
};

export const eliminarLibro = (req, res) => {
  const data = req.body;

  return res.status(200).json({
    message: "Libro eliminado",
    data: data,
  });
};

export const optenerLibro = async (req, res) => {
  const { _id: idLibro } = req.params;
  const libro0 = req.user.libros.filter((libro) => libro._id == idLibro)

  console.log(req.user._id.toString());
  console.log(idLibro.toString());

  const libro1 = await Usuario.findOne(
    {
    //   _id: req.user._id,
      libros: { avance: 'INCOMPLETO' },
    },
    { "libros.$": 1 }
  );

  const libro2 = await Usuario.findOne(
    {
    //   _id: req.user._id,
        'libros._id': idLibro,
    },
    { "libros.$": 1 }
  );

  return res.status(200).json({
    message: "El Libro es",
    libro0,
    libro1,
    libro2
  });
};

export const listarLibros = (req, res) => {
  return res.status(200).json({
    message: "Lista de Libros",
    data: req.user.libros,
  });
};
