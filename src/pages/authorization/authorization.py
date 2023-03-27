from dash import dcc
from dash import html

import dash_bootstrap_components as dbc
from src.pages.authorization import authorization_callbacks

layout = html.Div([
    html.H1("Авторизация"),
    dcc.Input(id="username", type="text", placeholder="Username"),
    dcc.Input(id="password", type="password", placeholder="Password"),
    dbc.Button("Login", id="login-button"),
    html.Div(id="login-status"),
])
