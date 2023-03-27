from dash.dependencies import Input, Output, State

from dash import dcc

from src.app import app

from src.core.settings import settings

import requests

import pandas as pd

import plotly.express as px

import io

import base64


@app.callback(
    [
        Output('dataframe', 'data'),
        Output('download-status', 'children')
    ],
    Input('btn-download', 'n_clicks'),
    State('jwttoken', 'data')
)
def download_data(n_clicks, jwttoken):
    url = f"{settings.back_url}methods/download"
    if n_clicks:
        response = requests.post(url, headers={'Authorization': f'Bearer {jwttoken}'})
        if response.status_code == 200:
            data = io.BytesIO(response.content)
            df = pd.read_csv(data)
            return df.to_dict('records'), 'Файл скачан'
        elif response.status_code == 401:
            return None, 'ошибка авторизации'
        return 'Error: ' + response.text
    return None, None


@app.callback(
    Output('tab-content', 'children'),
    Input('tabs-visualisation', 'value'),
    State('dataframe', 'data')
)
def tab_visualization(tab, df_dict):
    if df_dict is None:
        return 'Данные не скачаны'
    if tab == 'box':
        df = pd.DataFrame(df_dict)
        return dcc.Graph(figure=px.box(df, x="Usage_kWh"))
    elif tab == 'pie':
        df = pd.DataFrame(df_dict)
        df_group = df.groupby('Day_of_week')['Usage_kWh'].mean().reset_index()
        return dcc.Graph(figure=px.pie(df_group, values='Usage_kWh', names='Day_of_week'))
    elif tab == 'histo':
        df = pd.DataFrame(df_dict)
        df_group = df.groupby('Load_Type')['Usage_kWh'].mean().reset_index()
        return dcc.Graph(figure=px.histogram(df_group, x="Usage_kWh", y='Load_Type', labels={'x': 'mean Usage_kWh', 'y':'Load_Type'}))


@app.callback([Output('output-dataP', 'children'),
               Output('output-dataP-file','data')],
              Input('upload-dataP', 'contents'),
              State('jwttoken', 'data'))
def data_processing(contents, jwttoken):
    if contents is not None:
        url = f"{settings.back_url}methods/dataProcessing"
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        files = {'file': ('data.csv', decoded)}
        response = requests.post(url=url, files=files,
                                 headers={'Authorization': f'Bearer {jwttoken}'})
        if response.status_code == 200:
            df = pd.read_csv(io.BytesIO(response.content))
            return 'Успешное выполнение', dcc.send_data_frame(df.to_csv, "dataProcessed.csv")
        return 'Error: ' + response.text, None
    return None, None


@app.callback([Output('output-predict', 'children'),
               Output('output-predict-file','data')],
              Input('upload-predict', 'contents'),
              State('jwttoken', 'data'))
def predict(contents, jwttoken):
    if contents is not None:
        url = f"{settings.back_url}methods/predict"
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        files = {'file': ('predict_data.csv', decoded)}
        response = requests.post(url=url, files=files,
                                 headers={'Authorization': f'Bearer {jwttoken}'})
        if response.status_code == 200:
            df = pd.read_csv(io.BytesIO(response.content))
            return 'Успешное выполнение', dcc.send_data_frame(df.to_csv, "predicted.csv")
        return 'Error: ' + response.text, None
    return None, None


@app.callback(Output('output-fit', 'children'),
              Input('upload-fit', 'contents'),
              State('jwttoken', 'data'))
def predict(contents, jwttoken):
    if contents is not None:
        url = f"{settings.back_url}methods/fit"
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        files = {'file': ('train_data.csv', decoded)}
        response = requests.post(url=url, files=files,
                                 headers={'Authorization': f'Bearer {jwttoken}'})
        if response.status_code == 200:
            return 'Модель успешно обучена'
        return 'Error: ' + response.text
