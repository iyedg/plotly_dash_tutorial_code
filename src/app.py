import dash

import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.YETI, "custom.css"],
    # suppress_callback_exceptions=True,
)
