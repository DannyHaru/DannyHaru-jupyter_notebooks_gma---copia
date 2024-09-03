# Manual de Manipulación de la Aplicación Dashboard con Bootstrap

## Introducción
Este manual proporciona instrucciones detalladas sobre cómo utilizar y manipular la aplicación dashboard diseñada con Bootstrap. 

## Tabla de Contenidos
1. [Requisitos Previos](#requisitos-previos)
2. [Estructura de la Aplicación](#estructura-de-la-aplicación)
    - [Descripción de Archivos](#descripción-de-archivos)
    - [Organización del Código](#organización-del-código)
3. [Configuración Inicial](#configuración-inicial)
    - [Clonar el Repositorio](#clonar-el-repositorio)
    - [Instalar Dependencias](#instalar-dependencias)
    - [Configuración del Entorno](#configuración-del-entorno)
4. [Navegación por la Interfaz](#navegación-por-la-interfaz)
    - [Barra de Navegación](#barra-de-navegación)
    - [Desplegables y Selectores](#desplegables-y-selectores)
    - [Interacción con los Gráficos](#interacción-con-los-gráficos)
5. [Manipulación de Datos](#manipulación-de-datos)
    - [Cargar Nuevos Datos](#cargar-nuevos-datos)
    - [Filtrar Datos](#filtrar-datos)
    - [Actualizar Gráficos](#actualizar-gráficos)
6. [Personalización de la Interfaz](#personalización-de-la-interfaz)
    - [Cambiar Temas](#cambiar-temas)
    - [Personalizar Gráficos](#personalizar-gráficos)
    - [Modificar la Disposición](#modificar-la-disposición)
7. [Exportación de Gráficos y Datos](#exportación-de-gráficos-y-datos)
    - [Exportar Gráficos](#exportar-gráficos)
    - [Descargar Datos](#descargar-datos)
8. [Solución de Problemas Comunes](#solución-de-problemas-comunes)
    - [El Dashboard No Carga](#el-dashboard-no-carga)
    - [Problemas con el Estilo](#problemas-con-el-estilo)
    - [Errores al Cargar Datos](#errores-al-cargar-datos)

## Requisitos Previos
- **Entorno de Desarrollo**: Asegúrese de tener instalados los siguientes componentes:
  - Python <img src="assetsMD/python.png" alt="Python" width="100"/>
  - Dash <img src="assetsMD/dash.png" alt="Dash" width="100"/>
  - Bootstrap <img src="assetsMD/bootstrap.png" alt="Bootstrap" width="100"/>
- **Conocimientos Básicos**:
  - HTML/CSS <img src="assetsMD/html_css.png" alt="HTML/CSS" width="100"/>
  - Bootstrap <img src="assetsMD/bootstrap.png" alt="Bootstrap" width="100"/>
  - Python <img src="assetsMD/python.png" alt="Python" width="100"/>

## Estructura de la Aplicación
La aplicación se organiza en los siguientes archivos y directorios:

- ### Descripción de Archivos

El codigo de la pagina principal se encuentra del repositorio, con el nombre y extension de: "app.py".

Dentro de este codigo de la pagina principal, se encuentra las distintas selecciones de paginas como ser: dashboard, indicadores(linea roja), grafico_ingreso, grafico_salida, partidas.

Son paginas dentro de la carpeta "pages" que estan organizadas de la siguiente manera:
- Dashboard OTs, con el nombre y extension de: "dashboard.py".
- Indicadores por linea de Interrupciones, con el nombre y extension de: "linearoja.py".
- Dashboard de Ingresos, con el nombre y extension de: "grafico_ingreso".
- Dashboard de Salidas, con el nombre y extension de: "grafico_salida".
- Gestion de Partidas Presupuestarias, con el nombre y extension de: "partidas.py".

### Organización del Código
app.py
- #Importacion de librerias necesarias para que arranque la aplicacion.
- #Crear instancia de la aplicación Dash y agregar hoja de estilo CSS
- #Crear la barra lateral deslizable (Offcanvas)
- #Crear la barra superior con un botón tipo "sandwich"
- #Imagen para mostrar en la pantalla principal
- #Definir el diseño principal de la aplicación
- #Callback para controlar la apertura y cierre del Offcanvas
- #Definir la lógica de enrutamiento para mostrar el contenido de la página

dashboard.py
- #Importacion de librerias necesarias para que arranque la aplicacion.
- #Ruta al archivo de Excel en la misma carpeta del proyecto
- #Leer datos de la hoja "dashboard" de Excel
- #Convertir la columna 'created_at' a datetime y hacerla tz-naive
- #Definir nombres de líneas
- #Definir los colores personalizados para las categorías
- #Definir el layout de la aplicación
    - #Checklist para seleccionar líneas y selector de rango de fechas
- #Callback para el llamado del grafico, la lista de lineas, rango de fechas, seleccion de graficos

grafico_ingreso.py
- #Importacion de librerias necesarias para que arranque la aplicacion.
- #Cargar las variables de entorno desde el archivo .env
- #Obtener los detalles de la conexión desde el archivo .env
- #Crear la URL de conexión
- #Crear el motor de conexión con SQLAlchemy
- #Cargar datos desde la tabla 'ingreso' en un DataFrame
- #Convertir la columna 'fecha_ingreso' a tipo de datos datetime
- #Obtener opciones únicas para el combobox de 'codigo_item', 'descripcion' y 'anio'
- #Crear la aplicación Dash
- #Agregar el selector de tipo de gráfico en el diseño
- #Crear gráfico inicial sin filtro
- #Callback para actualizar el gráfico y las etiquetas según las selecciones

    - #Crear una copia del DataFrame original para filtrar
    - #Filtrar datos según el 'codigo_item' seleccionado
    - #Filtrar datos según la 'descripcion' seleccionada
    - #Filtrar datos según la 'fecha_ingreso' seleccionada
    - #Filtrar datos según el 'anio' seleccionado
    - #Crear gráfico según el tipo seleccionado
        - #Gráfico por defecto (si no se selecciona tipo)
    - #Sumar la cantidad total y calcular el precio unitario máximo

- #Callback para generar la imagen con el texto

    - #Inicializar el DataFrame filtrado
    - #Filtrar el DataFrame según el código de ítem seleccionado
    - #Filtrar el DataFrame según la descripción seleccionada (si no hay código de ítem)
    - #Verificar si hay datos después de filtrar
    - #Crear la imagen con el texto utilizando Plotly

- #Callback para generar un pdf del grafico


## Configuración Inicial
TEXTO

## Navegación por la interfaz
TEXTO

## Manipulación de Datos
TEXTO

## Personalización de la Interfaz
TEXTO

## Exportación de Gráficos y Datos
TEXTO

## Solución de Problemas Comunes
TEXTO
