import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
# from index import *

# Load Disappeared Planes dataset
df = pd.read_csv("/Users/Issy/Code/isabelorchard/dash_app/disappeared_complete.csv")

dash.register_page(__name__, path='/')

# Create the map figure
fig = px.scatter_mapbox(
    df,
    lat="lat",
    lon="lon",
    hover_name="date",  # Replace with the relevant column for tooltip
    hover_data=["aboard_total", "flight_type"],  # Replace with relevant columns
    zoom=1,
    height=600,
)

# Update mapbox style
fig.update_layout(
    mapbox_style="carto-darkmatter",  # Choose a mapbox style
    margin={"r": 0, "t": 0, "l": 0, "b": 0},  # Remove extra padding around the map
)


# KPI Calulations
KPI_1 = df['date'].count() # nb of disappearances 
KPI_2 = df['aboard_total'].sum() # nb of people missing 
KPI_3 = df['operator'].mode()[0] # most frequently missing plane by airline
KPI_4 = df['country'].value_counts().idxmax() # most common country


# Define the layout
layout = dbc.Container(
    fluid=False,
    children=[
        # Header
        # dbc.Row(
        #     [
        #     ],
        #     className="bg-black py-2 text-white",
        #     style={"fontSize": "16px", "height": "25px"},
        # ),

        # Main Content
        dbc.Row(
            [
                # Left Column
                dbc.Col(
                    [
                        # Industry News Section
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.H4(
                                        "Latest News",
                                        className="card-title text-white"
                                    ),
                                    html.Div(
                                        id="industry-news-scroll",
                                        className="scroll-area text-white",
                                        style={
                                            "height": "600px",
                                            "overflowY": "scroll",
                                            # "border": "1px solid #ccc",
                                            "padding": "10px",
                                        },
                                    ),
                                    dcc.Interval(
                                        id="news-update-interval",
                                        interval=10 * 60 * 1000,  # Update every 10 minutes
                                        n_intervals=0
                                    )
                                ]                                     
                            ),
                            className="mb-2",
                        ),
                    ],
                    width=3,
                ),

                # Center Column
                dbc.Col(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Poof, and they're gone",
                                    className="text-center text-white mb-6",
                                ),
                                dcc.Graph(figure=fig),  # Plane disappearances map
                            ],
                            className="text-center mt-5",
                        ),
                    ],
                    width=9,
                ),

                # # Right Column
                # dbc.Col(
                #     [
                        # Aircraft Model Section
                        # dbc.Card(
                        #     dbc.CardBody(
                        #         [
                        #             html.H4(
                        #                 "Aircraft Model Of The Week",
                        #                 className="card-title text-white"
                        #             ),
                        #             html.Div(
                        #                 id="aircraft-model-image",
                        #                 children=[
                        #                     html.Img(
                        #                         src="images/vintage_plane.png",
                        #                         alt="Aircraft Model",
                        #                         className="img-fluid mx-auto d-block mt-3",
                        #                         style={"maxWidth": "100%"},
                        #                     )
                        #                 ],
                        #             ),
                        #         ]
                        #     ),
                        #     className="mb-4",
                        # ),
        #             ],
        #             width=3,
        #         ),
            ],
            className="my-4",
        ),

        # Footer
        dbc.Row(
            [
                # Scorecard KPIs
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5(KPI_1, className="card-title text-center"),
                                        html.P("'disappeared' flights", className="text-center"),
                                        # style={"display": "flex", "flexDirection": "column", "justifyContent": "center", "alignItems": "center"},
                                    ]
                                ),
                                className="bg-dark text-white",
                                # style={"width": "200px", "height": "150px"},
                            ),
                            width=3,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5(KPI_2, className="card-title text-center"),
                                        html.P("people missing 🕳🚶🏻‍♂️", className="text-center"),
                                    ]
                                ),
                                className="bg-dark text-white",
                                # style={"width": "200px", "height": "150px"},
                            ),
                            width=3,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5(KPI_3, className="card-title text-center"),
                                        html.P("🇷🇺 🪆", className="text-center"),
                                    ]
                                ),
                                className="bg-dark text-white",
                                # style={"width": "200px", "height": "150px"},
                            ),
                            width=3,
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H5(KPI_4, className="card-title text-center"),
                                        html.P("👹", className="text-center"),
                                    ]
                                ),
                                className="bg-dark text-white",
                            ),
                            width=3,
                        ),
                    ],
                    className="mb-3",  # Adds spacing below the KPIs
                ),
                # Footer Text
                dbc.Row(
                    dbc.Col(
                        html.Div(
                            className="text-white text-center bg-dark py-1",
                            style={"fontSize": "12px"},
                            children=[
                                html.P("Created By Isabel Orchard")
                            ],
                        )
                    )
                ),
            ]
        ),
    ],
    style={"border": "5px solid #0000ff"}
)

# Callback to update industry news dynamically
@callback(
    Output("industry-news-scroll", "children"),
    [Input("news-update-interval", "n_intervals")]
)
def update_news(n_intervals):
    print("Callback triggered")
    news_items = pd.read_csv('/Users/Issy/Code/isabelorchard/dash_app/google_news_compact .csv')
    print(news_items)
    
    
    return [
        html.Div([
            html.A(news["title"], href=news['url'], target="_blank", className="d-block mb-2")
        ]) for idx, news in news_items.iterrows()
    ]


# Run the app
# if __name__ == "__main__":
#     app.run_server(debug=True)