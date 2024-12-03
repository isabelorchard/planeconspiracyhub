import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px

dash.register_page(__name__)

# Load Disappeared Planes dataset
df = pd.read_csv("/Users/Issy/Code/isabelorchard/dash_app/disappeared_complete.csv")

dash.register_page(__name__, path='/')

# Create the map figure
fig_2 = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    hover_name="date",  # Replace with the relevant column for tooltip
    hover_data=["aboard_total", "flight_type"],  # Replace with relevant columns
    zoom=1,
    height=600,
)

# Update mapbox style
fig_2.update_layout(
    mapbox_style="carto-darkmatter",  # Choose a mapbox style
    margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove extra padding around the map
)


# Define the layout
layout = dbc.Container(
    children[
        # Header
        dbc.Row(
            [
            ],
            className="bg-black py-2 text-white",
            style={"fontSize": "16px", "height": "25px"},
        ),

        Main Content
    ]
    html.H1("Flights That Disappeared")
    dbc.Col(
        [
            html.Div(
                [
                    dcc.Graph(figure=fig),  # Plane disappearances map
                    ],
                className="text-center mt-5",
                ),
            ],
        width=9,
        ),
    )