import dash
import dash_bootstrap_components as dbc

from src.layout.layout import layout

from src.utils.external_assets import FONT_AWSOME

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        FONT_AWSOME,
    ],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

app.layout = layout
