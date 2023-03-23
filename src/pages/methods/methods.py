from dash import dcc
from dash import html


layout = html.Div([
    html.H1('Функционал'),
    html.Hr(),
    html.H3('Связь с backend'),
    html.Hr(),
    html.H5('Скачать данные для Dash'),
    html.Button('Скачать данные', id='btn-download'),
    html.Div(id="download-status"),
    dcc.Store('dataframe'),
    html.Hr(),
    html.H5('Обработка Данных'),
    dcc.Upload(
        id='upload-dataP',
        children=html.Button('Загрузить Файл'),
        multiple=False
    ),
    html.Div(id='output-dataP'),
    dcc.Download(id='output-dataP-file'),
    html.Hr(),
    html.H5('Обучение модели'),
    dcc.Upload(
        id='upload-fit',
        children=html.Button('Загрузить Файл'),
        multiple=False
    ),
    html.Div(id='output-fit'),
    html.Hr(),
    html.H5('Предсказание'),
    dcc.Upload(
        id='upload-predict',
        children=html.Button('Загрузить Файл'),
        multiple=False
    ),
    html.Div(id='output-predict'),
    dcc.Download(id='output-predict-file'),
    html.Hr(),
    html.H3('Визуализации Dash'),
    dcc.Tabs(id="tabs-visualisation", value='tab-1-example-graph', children=[
        dcc.Tab(label='Ящик с усами', value='box'),
        dcc.Tab(label='Круговая диаграмма', value='pie'),
    ]),
    html.Div(id='tab-content')
])




