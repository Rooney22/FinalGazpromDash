from dash.dependencies import Input, Output, State

from src.core.settings import settings

from src.app import app

import requests


@app.callback(
    [
        Output('login-status', 'children'),
        Output('jwttoken', 'data')
    ],
    [
        Input('login-button', 'n_clicks'),
        State("username", "value"),
        State("password", "value"),
    ]
)
def authorize(n_clicks, username, password):
    if n_clicks:
        url = f"{settings.back_url}authorization/authorize"
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            return "Вы авторизованы", response.json()['access_token']
        return 'Не удалось авторизоваться', None
    return None, None
