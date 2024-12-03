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
        html.H1("Where Planes Go When They 'Disappear'", className="text-center bg-black text-white py-3"),
        html.Div([

            html.Div(
                dcc.Link(f"{page['name']}", href=page['relative_path']),
                className="greenbutton mb-4"
            ) for page in dash.page_registry.values()
            ], className='page_headings'),
        dash.page_container
          # Dynamically loads the current page
    ])
    # fluid=True,
if __name__ == "__main__":
    app.run_server(debug=True)
