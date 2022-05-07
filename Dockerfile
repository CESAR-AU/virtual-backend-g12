FROM node:17-alpine
# ruta de almacen de la app
WORKDIR /app
#copiar archivos locales al contenedor
# COPY package.json /app/
# COPY package-lock.json /app/
COPY . /app/
#instalar las dependencias
RUN npm install

# COPY /src/ /app/src/

#comando para iniciar el proyecto
CMD ["npm", "run", "start:dev"]