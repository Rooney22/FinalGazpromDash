from dash import html
from dash import dcc

from src.layout.sidebar.sidebar import sidebar


content = html.Div(id="page-content")

layout = html.Div([dcc.Location(id="url"), sidebar, content, dcc.Store(id="jwttoken", storage_type='session')])
