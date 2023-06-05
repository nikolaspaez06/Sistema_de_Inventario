# Proyecto de CRUD de Películas - FastAPI

<img src="nicolas.jpg" alt="Logo sistema de inventario">

## Descripción

Este proyecto es un ejemplo de una API RESTful desarrollada con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de productos 

## Funcionalidades

- Obtener todos los productos
- Obtener una producto por su ID
- Crear una nuevo provedor 
- Actualizar un producto existente
- Eliminar un producto y provedor 

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic

## Instalación

1. Clona este repositorio en tu máquina local:

git clone https://github.com/nikolaspaez06/Sistema_de_Inventario


2. Navega al directorio del proyecto:

cd sistema de inventario

3. Tu o uno de tus companeros debe cambiar el origen del repositorio 

git remote -v

git remote remove origin

git remote add origin <nueva_url_del_repositorio>

4. Ahora, tus compañeros deben clonar tu repositorio y tú debes darles permiso para editarlo

Desde el repositorio en GitHub, ve a "Settings" y luego a la sección de "Collaborators" para agregarlos. Esto tiene como objetivo permitirles realizar cambios. No te preocupes, realizaremos este proceso en clase."

5. Instala las dependencias necesarias:

pip install -r requirements.txt


## Uso

1. Inicia la aplicación:

uvicorn main:app --reload


2. Accede a la documentación de la API en tu navegador:

http://localhost:8000/docs


3. Prueba las diferentes rutas disponibles para realizar operaciones CRUD en las del sistema de inventario




