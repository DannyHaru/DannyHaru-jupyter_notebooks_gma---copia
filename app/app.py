from dash import Dash, dcc, html, Input, Output, callback
from pages import linearoja
from starlette.middleware.wsgi import WSGIMiddleware

# Crear instancia de la aplicación Dash y agregar hoja de estilo CSS
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootswatch@5.3.0/dist/morph/bootstrap.min.css"]
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

server = app.server  # Esta es la instancia Flask subyacente

# Definir el diseño principal de la aplicación
app.layout = html.Div([
    # Barra de navegación con botones a las diferentes páginas
    html.Div([
        dcc.Link(
            'Indicadores',
            href='/linearoja',
            className='btn btn-primary me-2'  # Usar clases de Bootstrap para estilo de botón
        )
        #dcc.Link(
        #    'Resumen',
        #    href='/resumentotal',
        #    className='btn btn-primary me-2'  # Usar clases de Bootstrap para estilo de botón
        #)
                
    ], style={
        'padding': '10px',
        'background-color': '#f0f0f0',
        'border-bottom': '1px solid #ccc',
        'display': 'flex',  # Usar flexbox para alinear los botones
        'gap': '10px'  # Espacio entre los botones
    }),

    # Área para mostrar el contenido de las páginas
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Definir la lógica de enrutamiento para mostrar el contenido de la página
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
    prevent_initial_call=True
)
def display_page(pathname):
    """
    Esta función muestra el contenido de la página correspondiente según la ruta.
    """
    # Registrar la ruta recibida para depuración
    print(f'Pathname recibido: {pathname}')

    # Enrutar la página según la ruta recibida
    if pathname in ('/', '/linearoja'):
        return linearoja.layout
    #elif pathname == '/resumentotal': 
        #return resumentotal.layout
    ##elif pathname == '/ingresos': return ingresos.layout
    else:
        # Manejar rutas no encontradas
        return '404 - Página no encontrada'

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=8080)
