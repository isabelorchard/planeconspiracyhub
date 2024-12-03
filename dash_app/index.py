# from dash import dcc, html
# from dash.dependencies import Input, Output
# from app import app  # Import app instance
# from navbar import navbar  # Import navbar component
# from pages import disappeared, Home, model  # Import your page layouts

# # Must add this line in order for the app to be deployed successfully on Heroku
# from app import server
# from app import app

# # Embedding the navigation bar
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False),
#     get_navbar(),  # Fetch the navbar lazily
#     html.Div(id='page-content'),
# ])

# @app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
# def display_page(pathname):
#     if pathname == '/disappeared':
#         return disappeared.layout
#     elif pathname == '/model':
#         return model.layout
#     elif pathname == '/Home' or pathname == '/':
#         return Home.layout
#     else:
#         return html.Div("404: Page not found")
    
# # Navbar toggle callback
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# for i in [2]:
#     app.callback(
#         Output(f"navbar-collapse{i}", "is_open"),
#         [Input(f"navbar-toggler{i}", "n_clicks")],
#         [State(f"navbar-collapse{i}", "is_open")],
#     )(toggle_navbar_collapse)
