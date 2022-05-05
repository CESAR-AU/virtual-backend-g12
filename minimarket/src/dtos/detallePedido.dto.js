import validator from "validator";
import modelPrisma from "@prisma/client";

export const crearDetallePedidoRequestDTO = (data) => {
  const errores = [];
  let detalle = {
    cantidad: -1,
    unidadMedida: "",
    productoId: -1,
    pedidoId: -1,
  };
  const campos = Object.keys(detalle);

  campos.forEach((pro) => {
    if (!data.hasOwnProperty(pro)) {
      errores.push(`Falta el campo '${pro}'.`);
    }
  });
  if (errores.length != 0) {
    throw new Error(errores);
  }

  detalle = { ...data };
   console.log(detalle)
   console.log(detalle.cantidad.toString())
  if (
    validator.isEmpty(detalle.cantidad.toString()) ||
    !validator.isNumeric(detalle.cantidad.toString())
  ) {
    errores.push("La cantidad no puede estar vacio.");
  }
  
  if (
    validator.isEmpty(detalle.productoId.toString()) ||
    !validator.isNumeric(detalle.productoId.toString())
  ) {
    errores.push("El productoId no puede estar vacio.");
  }
  if (
    validator.isEmpty(detalle.pedidoId.toString()) ||
    !validator.isNumeric(detalle.pedidoId.toString())
  ) {
    errores.push("El pedidoId no puede estar vacio.");
  }

  if (
    detalle.unidadMedida !== modelPrisma.UNIDAD_MEDIDA.KG &&
    detalle.unidadMedida !== modelPrisma.UNIDAD_MEDIDA.UNIDAD
  ) {
    errores.push(
      `El rol puede ser ${modelPrisma.UNIDAD_MEDIDA.KG} o ${modelPrisma.UNIDAD_MEDIDA.UNIDAD}`
    );
  }

  if (errores.length != 0) {
    throw new Error(errores);
  } else {
    return { ...detalle };
  }
};
