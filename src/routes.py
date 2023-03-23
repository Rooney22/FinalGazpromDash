import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

from src.app import app

from utils.constants import home_page_location, authorization_page_location, methods_page_location

from src.pages.authorization import authorization

from src.pages.home import home

from src.pages.methods import methods


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def render_page_content(pathname):
    if pathname == home_page_location:
        return home.layout
    elif pathname == authorization_page_location:
        return authorization.layout
    elif pathname == methods_page_location:
        return methods.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
