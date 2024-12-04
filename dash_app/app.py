import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
# from navbar import navbar

# Initialize the app with `use_pages=True`
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server

# Define the layout
app.layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']}", href=page['relative_path'], className="greenbutton mb-4"),
                ) for page in dash.page_registry.values()
            ],
            className="page_headings",
        ),
        dash.page_container,  # Dynamically loads the current page
        
         # Top left GIF
        html.Img(
            src="https://media.giphy.com/media/oiPZ1CkwdWCOUi0JiA/giphy.gif",
            style={
                "position": "absolute",
                "top": "10px",
                "left": "10px",
                "width": "120px",
                "zIndex": "10",
            },
        ),
        # Top right GIF
        html.Img(
            src="https://media.giphy.com/media/l4Ki8RhZm0dSjfbj2/giphy.gif?cid=ecf05e477q6va0k10adgr7g6jivw657tbuy2r5fjmgse1xc4&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            style={
                "position": "absolute",
                "top": "10px",
                "right": "30px",
                "width": "100px",
                "zIndex": "10",
            },
        ),
    ],
    fluid=True,
)
if __name__ == "__main__":
    app.run_server(debug=True)
