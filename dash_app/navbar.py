# import dash_bootstrap_components as dbc
# from dash import html

# # Lazy import for navbar
# def get_navbar():
#     from index import navbar
#     return navbar

# navbar = dbc.Navbar(
#     dbc.Container(
#         [
#             html.A(
#                 dbc.Row(
#                     [
#                         dbc.Col(html.Img(src="/assets/logo.png", height="30px")),
#                         dbc.Col(dbc.NavbarBrand("App Name", className="ml-2")),
#                     ],
#                     align="center",
#                     class_name="g-0",
#                 ),
#                 # href="/Home",
#             ),
#             dbc.NavbarToggler(id="navbar-toggler"),
#             dbc.Collapse(
#                 dbc.Nav(
#                     [
#                         dbc.DropdownMenu(
#                             label="Explore",
#                             nav=True,
#                             in_navbar=True,
#                             children=[
#                                 # dbc.DropdownMenuItem("Home", href="/Home"),
#                                 dbc.DropdownMenuItem("Page 1", href="/page1"),
#                                 dbc.DropdownMenuItem("Page 2", href="/page2"),
#                             ],
#                         ),
#                     ],
#                     className="ml-auto",  # Align to the right
#                     navbar=True,
#                 ),
#                 id="navbar-collapse",
#                 navbar=True,
#             ),
#         ]
#     ),
#     color="dark",
#     dark=True,
#     className="mb-4",
# )

# # Building the navigation bar
# dropdown = dbc.DropdownMenu(
#     children=[
#         # dbc.DropdownMenuItem("Home", href="pages/Home"),
#         # dbc.DropdownMenuItem("Disappearance", href="pages/disappeared"),
#         # dbc.DropdownMenuItem("Model", href="pages/model"),
#     ],
#     nav=True,
#     in_navbar=True,
#     label="Explore",
# )
