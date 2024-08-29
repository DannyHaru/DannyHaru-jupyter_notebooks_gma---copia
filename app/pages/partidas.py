import pandas as pd
from dash import dcc, html, Input, Output, callback, dash_table, State
import dash_bootstrap_components as dbc

# Leer el archivo de Excel
excel_file = 'Partidas_20240826.120509.xlsx'
df = pd.read_excel(excel_file, sheet_name='Partidas_20240826.120509', skiprows=0, usecols='A:H', nrows=423)

# Definir el layout de la sección del botón
layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('Gestión de Partidas Presupuestarias', className='text-center my-4')),
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label('Buscar por:', className='form-label'),
            dcc.Dropdown(
                id='search-column',
                options=[{'label': col, 'value': col} for col in df.columns],
                placeholder='Selecciona una columna para filtrar',
                clearable=False,
                className='mb-2'
            ),
            dcc.Input(id='search-input', type='text', placeholder='Escribe tu búsqueda...', className='form-control mb-2'),
            dbc.Button('Buscar', id='search-button', color='primary', className='mb-4'),
        ], width=4),
    ], justify='center'),
    
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='table',
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=df.to_dict('records'),
                page_size=20,
                style_table={'overflowX': 'auto'},
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '5px',
                    'whiteSpace': 'normal',
                    'height': 'auto'
                },
            ),
        ], width=10),
    ], justify='center'),
    
    # Fila para el contador de elementos
    dbc.Row([
        dbc.Col([
            html.P(id='element-counter', children=f'Total: {len(df)} Elemento(s)', className='text-start mt-2'),
        ], width=10),
    ], justify='center'),
], fluid=True)

# Definir el callback para actualizar la tabla y el contador de elementos
@callback(
    [Output('table', 'data'),
     Output('element-counter', 'children')],
    [Input('search-button', 'n_clicks')],
    [State('search-column', 'value'),
     State('search-input', 'value')]
)
def update_table_and_counter(n_clicks, search_column, search_value):
    if n_clicks and search_column and search_value:
        filtered_df = df[df[search_column].astype(str).str.contains(search_value, case=False, na=False)]
        counter_text = f'Total: {len(filtered_df)} Elemento(s)'
        return filtered_df.to_dict('records'), counter_text
    counter_text = f'Total: {len(df)} Elemento(s)'
    return df.to_dict('records'), counter_text
