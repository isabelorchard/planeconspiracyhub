import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import os

dash.register_page(__name__)

# Load Disappeared Planes dataset
df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '78_real_story.csv'))

dash.register_page(__name__)

# Create the map figure
fig_2 = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    hover_name="date",
    hover_data=["aboard_total", "flight_type"],
    zoom=1,
)
fig_2.update_layout(mapbox_style="carto-darkmatter")  # Change the map style if needed
fig_2.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})  # Remove map margins


# Define the layout
layout = html.Div(
    style={"display": "flex", "flexDirection": "row", "height": "100vh"},
    children=[
        # Map Section (Fullscreen)
        html.Div(
            dcc.Graph(
                id="map",
                figure=fig_2,
                style={"height": "100%", "width": "100%"}
            ),
            style={"flex": "4"}
        ),
        # Sidebar for Incident Details
        html.Div(
            id="sidebar",
            style={
                "flex": "1",
                "backgroundColor": "#111",
                "color": "white",
                "padding": "50px",
                "display": "flex",
                "flexDirection": "column",
                "justifyContent": "center",
                "alignItems": "center",
                "overflowY": "auto"
            },
            children=[
                html.H3("Incident Details", className="text-center"),
                html.Div(
                    id="incident-details",
                    style={
                        # "marginTop": "5px",
                        "textAlign": "center",
                        "top": "50px"
                        }
                ),
                html.H5(
                    "based on sumbissions from the tinfoil hat community",
                    className="text-center",
                    style={
                        "marginTop": "auto",
                        "textAlign": "center",
                        "bottom": "50px",
                        "font-size": "10px"
                        }
                )
            ]
        ),
    ]
)

# Callback to update the sidebar content
@callback(
    Output("incident-details", "children"),
    Input("map", "clickData")
)
def display_incident_details(click_data):
    if click_data is None:
        return "Click on a point to find out what ", html.I("really"), " happened",

    # Extract information from the clicked point
    point = click_data["points"][0]
    lat = point["lat"]  # Latitude from the clicked point
    lon = point["lon"]  # Longitude from the clicked point

    # Retrieve the corresponding row in the dataframe
    incident = df[(df["lat"] == lat) & (df["lon"] == lon)].iloc[0]

    # Extract information from the clicked point
    point = click_data["points"][0]
    date = point["hovertext"]
    aboard_total = point["customdata"][0]
    flight_type = point["customdata"][1]
    summary_x = incident["summary_x"]
    real_reason = incident["real_reason"]


    # Return formatted details
    return [
        html.P(f"Date: {date}", style={"fontSize": "18px"}),
        html.P(f"Aboard Total: {aboard_total}", style={"fontSize": "18px"}),
        html.P(f"Flight Type: {flight_type}", style={"fontSize": "18px"}),
        html.P(f"Narrative: {summary_x}", style={"fontSize": "18px"}),
        html.H1(".", style={"color": "black"}),
        html.H1(".", style={"color": "black"}),
        html.H1(".", style={"color": "black"}),
        html.H1(".", style={"color": "black"}),
        html.P(
            f"What We Think: {real_reason}",
            style={
                "fontSize": "18px",
                "marginTop": "auto",
                "textAlign": "center"}
            ),
        ]
    
