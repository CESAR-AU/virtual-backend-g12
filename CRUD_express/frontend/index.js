const BASE_URL = 'http://localhost:3000'
const root = document.getElementById('root')

const GetProductos = async () => {
    const respuesta = await fetch(`${BASE_URL}/productos`, {method:'GET'})
    const data = await respuesta.json()
    console.log(data)
    let lista = ''
    data.forEach(producto => {
        lista += `<li>${producto.nombre}</li>`
    });
    root.innerHTML = lista
}

GetProductos()