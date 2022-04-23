const URL_BACKEND = "http://localhost:8000"


// Peticion normal
async function pedirPlatos() {
  const respuesta = await fetch(URL_BACKEND + `/menu/`, { method: "GET" });
  const data = await respuesta.json();
  console.log(data);
}

async function login() {
  const respuesta = await fetch(URL_BACKEND + "/auth/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      correo: "mozo@c-innova.pe",
      password: "123456",
    }),
  });
  const data = await respuesta.json();
  listarStock(data.access);
  console.log(data);
}

// Usando Bearer Token
async function listarStock(token) {
  const respuesta = await fetch(URL_BACKEND + "/menu/stock", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  const data = await respuesta.json();
  console.log(data);
}

pedirPlatos();
login();