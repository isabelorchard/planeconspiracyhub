import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import os

dash.register_page(__name__)


# Define the layout
layout = dbc.Container(
    children=[
        dbc.Row(
            html.H1(
                "Aircraft Model Of The Week",
                className="text-center",
            )
        ),
        
        dbc.Row(
            html.Img(
                src="/assets/vintage_plane.png",
                style={
                    "width": "750px",
                    "height": "750px",
                    "margin": "auto",  # Center the image horizontally
                },
            )
        ),
        
        dbc.Row(
            html.H2(
                "Bristol F.2 Fighter",
                className="text-center"
            )
        ),
        
        dbc.Row(
            html.H5(
                "British First World War two-seat biplane fighter and reconnaissance aircraft developed by Frank Barnwell at the British and Colonial Aeroplane Company later known as the Bristol Aeroplane Company. It is often simply called the Bristol Fighter, 'Brisfit or Biff'",
                className="text-center"
                )
            ),
        ],
    fluid=False,
    )
    
