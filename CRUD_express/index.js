import express from "express";
import cors from 'cors'
// const express = require('express')

const servidor = express()
// middleware
servidor.use(express.json())
servidor.use(express.raw())
servidor.use(express.urlencoded({extended:true}))
servidor.use(cors({origin:['http://localhost'], methods: ['POST', 'PUT', 'DELETE'], allowedHeaders:['Content-Type', 'Authorization']}))

const productos = [{
    id:1,
    nombre:'platano',
    precio: 1.80,
    desponible:true
}]

servidor.get('/', (req, res)=>{
    res.status(200).json({
        message:'Bienvenido a mi API de productos',
        data: productos,
        error:req.headers,
        error1:req.rawTrailers,
    })
})

servidor.post('/productos', (req, res)=>{
    console.log(req.body)
    let data = req.body
    data.id = productos.length + 1
    productos.push(data)
    return res.status(200).json({
        message: 'Producto agregado exitosamente',
        data: productos
    })
})

servidor.get('/productos', (req, res)=>{
    const data = productos
    return res.json({
        message: 'Lista de productos',
        data: data
    })
})

servidor.route('/producto/:id')
.get((req, res)=>{
    const { id } = req.params
    const producto = productos.filter((producto)=>{return producto.id == id})
    if(producto.length <= 0 || producto.length == undefined){
        return res.status(400).json({
            message: 'El producto no existe'
        })
    }
    else{
        return res.json({
            message: 'Producto encontrado',
            data: producto
        })
    }
    
})
.put((req, res)=>{
    const { id } = req.params
    const producto = productos.filter((producto)=>{return producto.id == id})
    
    if(producto.length <= 0){
        return res.status(400).json({
            message: 'El producto a actualizar no existe'
        })
    }
    else{

        const actualizado = productos.filter((producto, index)=>{
            if(producto.id == id){
                productos[index] = req.body
                productos[index].id = producto.id
                console.log('Actualizado: ', productos[index])
                const actualizado = productos[index]
                return actualizado
            }
        })

        return res.json({
            message: 'Producto actualizado exitosamente',
            data: actualizado
        })
    }
    
})
.delete((req, res)=>{
    const { id } = req.params
    const producto = productos.filter((producto)=>{return producto.id == id})
    console.log(producto)
    if(producto.length <= 0){
        return res.status(400).json({
            message: 'El producto a eliminar no existe'
        })
    }
    else{

        const eliminado = productos.filter((producto, index)=>{
            if(producto.id == id){
                productos.splice(index,1)
                return producto
            }
        })

        return res.json({
            message: 'Producto eliminado exitosamente',
            data: eliminado
        })
    }
})

servidor.listen(3000, ()=>{
    console.log('Servidor corriendo en el puerto: 3000')
})