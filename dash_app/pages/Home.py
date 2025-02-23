import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import os
# from index import *




# Load Disappeared Planes dataset
path = os.path.dirname(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'disappeared_complete.csv'))

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
KPI_2 = int(round(df['aboard_total'].sum(), 0)) # nb of people missing 
KPI_3 = df['operator'].mode()[0] # most frequently missing plane by airline

# Replace 'united states' with U.S.A
df["country"] = df["country"].replace("united states", "U.S.")

KPI_4 = df['country'].value_counts().idxmax() # most common country

def get_news_ticker():
    return dbc.Row([
        # Using style dictionary instead of html.Style
        html.Div([
            html.Link(
                rel='stylesheet',
                href='/assets/news_ticker.css'  # You'll need to create this file in your assets folder
            ),
            dbc.Col([
                html.Div([
                    html.Div([
                        html.Span("Latest News", className="d-flex align-items-center")
                    ], className="news"),
                    html.Div(
                        html.Div(id='ticker-content', className="news-scroll-content"),
                        className="news-scroll"
                    ),
                ], className="breaking-news")
            ], width=12)
        ])
    ])

# Define the layout
layout = dbc.Container(
    fluid=False,
    children=[
        dbc.Row(
    [
        # Title in the center
        dbc.Col(
            html.H1(
                "Where Planes Go When They 'Disappear'",
                className="text-center bg-black text-white py-3",
            ),
            width=9,  # Takes most of the space in the row
            className="bg-black py-2 text-white",
            style={"fontSize": "16px"},
        ),
        # Image in the far right corner
        dbc.Col(
            html.Img(
                src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDhhZ2NuZjU2dWNieW94cDYyanJrbmZtNzUyZW93amY2eHh3Z2ZtZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/d3mlE7uhX8KFgEmY/giphy.gif",
                style={
                    "width": "200px",  # Small size
                    "height": "100px",  # Small size
                    "float": "right",  # Align to the far right
                },
            ),
            width=3,  # Takes remaining space for alignment
            className="bg-black",
        ),
    ],
    className="align-items-center",  # Vertically center-aligns the content
),
        dbc.Row(
            dbc.Row([
                get_news_ticker(),
                html.Hr(),
            ]), className="news-container mt-3"
        ),
        # Main Content
        dbc.Row(
            [
                # Left Column
                dbc.Col(
                    [
                        # Meme/Gif News Section
                        html.Img(
                            src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzZxbnVqdGJxdmMycmF4ZG8waWlrNHdnNzcydHNuZGZqajNuZ3E0dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/DwlFRgKo87zDW/giphy.gif",
                            style={
                              "width": "300px",
                              "height": "300px" 
                            }
                        ),
                        
                        html.Img(
                            src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHJuNTl1aTVqcmY4NmR6dHcyeWdkMzJ6bGtndjFzOHd4dmpjNzFqMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9Ft3NkG47dwmA/giphy.gif",
                            style={
                              "width": "300px",
                              "height": "300px" 
                            }
                        )
                        
                        # dbc.Card(
                        #     dbc.CardBody(
                        #         [
                        #             html.H4(
                        #                 "Latest News",
                        #                 className="card-title text-white"
                        #             ),
                        #             html.Div(
                        #                 id="industry-news-scroll",
                        #                 className="scroll-area text-white",
                        #                 style={
                        #                     "height": "500px",
                        #                     "overflowY": "scroll",
                        #                     # "border": "1px solid #ccc",
                        #                     "padding": "10px",
                        #                 },
                        #             ),
                        #             dcc.Interval(
                        #                 id="news-update-interval",
                        #                 interval=10 * 60 * 1000,  # Update every 10 minutes
                        #                 n_intervals=0
                        #             )
                        #         ]                                     
                        #     ),
                        #     className="mb-2 mt-5",
                        # ),
                    ],
                    width=3,
                ),

                # Center Column
                dbc.Col(
                    [
                        html.Div(
                            [
                                # html.H3(
                                #     "Poof, and they're gone",
                                #     className="text-center text-white mb-6",
                                # ),
                                dcc.Graph(figure=fig),  # Plane disappearances map
                            ],
                            className="text-center mt-1",
                        ),
                    ],
                    width=9,
                ),
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
                                        html.H5(f"🔥 {KPI_1} Vanished Flights 🔥", className="card-title text-center"),
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
                                        html.H5(f" {KPI_2} Missing People 🕳🚶🏻‍♂️", className="card-title text-center"),
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
                                        html.H5(f"DON'T FLY {KPI_3} 🇷🇺 ", className="card-title text-center"),
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
                                        html.H5(f"{KPI_4} gov has secrets 👹", className="card-title text-center"),
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
    news_items = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'google_news_compact .csv'))
    print(news_items)
    
    
    return [
        html.Div([
            html.A(news["title"], href=news['url'], target="_blank", className="d-block mb-2")
        ]) for idx, news in news_items.iterrows()
    ]

@callback(
    Output('ticker-content', 'children'),
    Input('ticker-content', 'id'))



def update_news_ticker(_):
    news_display = []
    news_items = pd.read_csv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'google_news_compact .csv'))
    # news_items = [news["title"] for idx, news in news_items.iterrows()]
    news_items_sample = news_items.sample(7)
    for i, item in news_items_sample.iterrows():
        news_display.extend([
            html.A(item['title'], href="#"),
            html.Span(className="dot") if i < len(news_items) - 1 else None
        ])
    return news_display


# Run the app
# if __name__ == "__main__":
#     app.run_server(debug=True)