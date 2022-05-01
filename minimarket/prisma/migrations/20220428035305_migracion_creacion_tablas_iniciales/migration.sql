-- CreateEnum
CREATE TYPE "USUARIO_ROL" AS ENUM ('ADMINISTRADOR', 'CLIENTE');

-- CreateEnum
CREATE TYPE "UNIDAD_MEDIDA" AS ENUM ('KG', 'UNIDAD');

-- CreateEnum
CREATE TYPE "CATEGORIA_PRODUCTO" AS ENUM ('VERDURA', 'FRUTA', 'ELECTRODOMESTICO', 'LIMPIEZA', 'OTROS');

-- CreateEnum
CREATE TYPE "PEDIDO_ESTADO" AS ENUM ('CREADO', 'ACEPTADO', 'PAGADO', 'ERROR');

-- CreateTable
CREATE TABLE "tbl_usuarios" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "rol" "USUARIO_ROL" NOT NULL DEFAULT E'CLIENTE',
    "validado" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "tbl_usuarios_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tbl_productos" (
    "id" SERIAL NOT NULL,
    "nombre" TEXT NOT NULL,
    "precio" DOUBLE PRECISION NOT NULL,
    "unidad_medida" "UNIDAD_MEDIDA" NOT NULL DEFAULT E'UNIDAD',
    "categoria" "CATEGORIA_PRODUCTO" NOT NULL DEFAULT E'OTROS',

    CONSTRAINT "tbl_productos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tbl_pedidos" (
    "id" SERIAL NOT NULL,
    "fecha" DATE NOT NULL,
    "total" DOUBLE PRECISION NOT NULL,
    "estado" "PEDIDO_ESTADO" NOT NULL DEFAULT E'CREADO',
    "process_id" TEXT,
    "clienteId" INTEGER NOT NULL,

    CONSTRAINT "tbl_pedidos_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "tbl_detalle_pedidos" (
    "id" SERIAL NOT NULL,
    "cantidad" DOUBLE PRECISION NOT NULL,
    "sub_total" DOUBLE PRECISION NOT NULL,
    "unidad_medida" "UNIDAD_MEDIDA" NOT NULL DEFAULT E'UNIDAD',
    "producto_id" INTEGER NOT NULL,
    "pedido_id" INTEGER NOT NULL,

    CONSTRAINT "tbl_detalle_pedidos_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "tbl_usuarios_id_key" ON "tbl_usuarios"("id");

-- CreateIndex
CREATE UNIQUE INDEX "tbl_usuarios_email_key" ON "tbl_usuarios"("email");

-- CreateIndex
CREATE UNIQUE INDEX "tbl_productos_id_key" ON "tbl_productos"("id");

-- CreateIndex
CREATE UNIQUE INDEX "tbl_pedidos_id_key" ON "tbl_pedidos"("id");

-- CreateIndex
CREATE UNIQUE INDEX "tbl_detalle_pedidos_id_key" ON "tbl_detalle_pedidos"("id");

-- AddForeignKey
ALTER TABLE "tbl_pedidos" ADD CONSTRAINT "tbl_pedidos_clienteId_fkey" FOREIGN KEY ("clienteId") REFERENCES "tbl_usuarios"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tbl_detalle_pedidos" ADD CONSTRAINT "tbl_detalle_pedidos_producto_id_fkey" FOREIGN KEY ("producto_id") REFERENCES "tbl_productos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "tbl_detalle_pedidos" ADD CONSTRAINT "tbl_detalle_pedidos_pedido_id_fkey" FOREIGN KEY ("pedido_id") REFERENCES "tbl_pedidos"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
