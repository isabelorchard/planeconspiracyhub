import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

# Initialize the app
# app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

dash.register_page(__name__)


# Define the layout
layout = dbc.Container(html.H1("Aircraft Model Of The Week"))