import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)


# Define the layout
layout = dbc.Container(html.H1("Aircraft Model Of The Week"))