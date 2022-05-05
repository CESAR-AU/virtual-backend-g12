import mercadopago from "mercadopago";
import { Prisma } from "../prisma.js";

export const crearPreferencia = async (req, res) => {
  try {
    const { pedidoId } = req.body;

    const pedidoEncontrado = await Prisma.pedido.findUnique({
      where: { id: pedidoId },
      rejectOnNotFound: true,
      include: {
        cliente: true,
        detallePedidos: { include: { producto: true } },
      },
    });

    const preferencia = await mercadopago.preferences.create({
      auto_return: "approved",
      back_urls: {
        failure: "http://localhost:3000/pago-fallido",
        pending: "http://localhost:3000/pago-pendiente",
        success: "http://localhost:3000/pago-exitoso",
      },
      metadata: {
        nombre: "Prueba",
      },
      payer: {
        name: pedidoEncontrado.cliente.nombre,
        // surname: "Ramos",
        // address: {
        //   zip_code: "04002",
        //   street_name: "Calle Los Angeles",
        //   street_number: 1458,
        // },
        email: "test_user_46542185@testuser.com",
      },
      items: pedidoEncontrado.detallePedidos.map((datallePedido) => ({
        id: datallePedido.pedidoId,
        //   category_id: "456",
        currency_id: "PEN",
        title: datallePedido.producto.nombre,
        //   description: "Zapatillas de Outdoor",
        //   picture_url: "https://imagenes.com",
        quantity: datallePedido.cantidad,
        unit_price: datallePedido.producto.precio,
      })),
      notification_url: "https://e34a-190-237-34-201.sa.ngrok.io/mp-webhooks"
    });

    const pedidoActualizado = await Prisma.pedido.update({
      data:{ process_id: preferencia.body.id, estado: 'CREADO'},
      where: {id: pedidoId },
    });
    // console.log(preferencia);

    return res.json({
      message: "Preferencia generada exitosamente",
      pedidoEncontrado,
      preferencia,
      pedidoActualizado,
    });
  } catch (ex) {
    return res.status(404).json({
      message: "Error al crear preferencia",
      error: ex.message,
    });
  }
};

export const mercadoPagoWebhooks = async (req, res) =>{
  console.log('====BODY====')
  console.log(req.body)
  console.log('====PARAMS====')
  console.log(req.params)
  console.log('====HEADERS====')
  console.log(req.headers)
  console.log('====QUERY====')
  console.log(req.query)

  if(req.query.topic === 'merchant_order'){
    const {id} = req.query
    const orden_comercial = await mercadopago.merchant_orders.get(id);
    console.log('La orden es: ', orden_comercial)

    const pedido = await Prisma.pedido.findFirst({
      where: { process_id: orden_comercial.body.preference_id}
    })

    if(!pedido){
      console.log('Pedido incorrecto')
    }

    if(orden_comercial.body.order_status === 'paid'){
      await Prisma.pedido.updateMany({
        where: { process_id: orden_comercial.body.preference_id },
        data: { estado: 'PAGADO' },
      })
    }
  }

  return res.status(201).json({
    message:'Webhook recibido exitosamente'
  })
}