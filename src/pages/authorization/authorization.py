from dash import dcc
from dash import html

from src.pages.authorization import authorization_callbacks

layout = html.Div([
    html.H1("Авторизация"),
    dcc.Input(id="username", type="text", placeholder="Username"),
    dcc.Input(id="password", type="password", placeholder="Password"),
    html.Button("Login", id="login-button"),
    html.Div(id="login-status"),
])
