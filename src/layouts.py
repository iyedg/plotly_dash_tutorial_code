import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import numpy as np

from .data import geo_targa_covid_df, by_gov_indicators, last_update
from .plots import plot_part_of_daily_active_cases


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

MAIN_CONTAINER_STLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "height": "100vh",
}

detail_selector = html.Div(
    [
        html.H4("Detail level"),
        dcc.RadioItems(
            id="detail_level_selector",
            options=[
                {"label": "By Governorate", "value": "governorate"},
                {"label": "Country wide", "value": "country"},
            ],
            value="governorate",
            labelStyle={"display": "block"},
        ),
    ]
)

view_selector = html.Div(
    [
        html.H4("Dashboard view"),
        dcc.RadioItems(
            id="content_view_selector",
            options=[
                {"label": "Map view", "value": "map"},
                {"label": "Line chart view", "value": "line"},
                {"label": "Bar race chart view", "value": "bar_race"},
            ],
            value="map",
            labelStyle={"display": "block"},
        ),
    ]
)

indicator_selector = html.Div(
    [
        html.H4("Indicator"),
        dcc.Dropdown(
            id="indicator_selector",
            options=[
                {"label": indicator, "value": indicator}
                for indicator in by_gov_indicators
            ],
            value=by_gov_indicators[0],
            clearable=False,
        ),
    ]
)

info = html.Div(
    [
        html.H4("Information"),
        html.Span("This dashboard has been created by "),
        html.A("Iyed Ghedamsi.", href="https://iyed.me"),
        html.Span("For information on how it was built refer to this "),
        html.A("blog post.", href="https://iyed.me"),
        html.Hr(),
        html.Span("The"),
        html.A(
            " data about indicators by governorates",
            href="https://docs.google.com/spreadsheets/d/1RoRjMglIY37gL1shEj-8T_EeyiWa1Oa9Vmt-8T5amq0",
        ),
        html.Span(" has been kindly shared by"),
        html.A(" Targa Consult", href="http://www.targa-consult.com/"),
        html.Span(". The"),
        html.A(
            " geojson data ",
            href="https://www.data4tunisia.org/en/datasets/decoupage-de-la-tunisie-geojson-et-shapefile/",
        ),
        html.Span(" has been kindly shared by"),
        html.A(" Data For Tunisia", href="https://www.data4tunisia.org/en/"),
    ],
    style={"padding-top": "3rem"},
)
sidebar = html.Div(
    [
        html.H3("COVID19 dashboard for cases in Tunisia"),
        html.Hr(),
        view_selector,
        html.Hr(),
        indicator_selector,
        info,
        html.Hr(),
        html.P(f"Last update: {last_update}"),
    ],
    style=SIDEBAR_STYLE,
)

random_df_data = np.random.randint(0, 100, 1000).reshape((500, 2))
header = dbc.Alert(
    [
        html.H5("Disclaimer", className="alert-heading"),
        html.Span(
            "This dashboard is intended to show how to use Plotly Dash"
            " for the creation of custom dashboards."
            " it has no scientific value with regards to the COVID 19 pandemic and"
            " should not be used to draw conlusions or to spread information about it."
            " For the official source of information please refer to "
        ),
        html.A(
            "https://covid-19.tn/",
            href="https://covid-19.tn/",
            className="alert-link",
            style={"display": "inline-block"},
        ),
    ],
    color="warning",
    dismissable=4000,
)

main_container = dbc.Container(
    [
        header,
        dcc.Loading(
            dcc.Graph(
                id="main_graph",
                figure=plot_part_of_daily_active_cases(geo_targa_covid_df),
            )
        ),
    ],
    style=MAIN_CONTAINER_STLE,
    id="main_container",
)

layout = dbc.Container([sidebar, main_container], fluid=True)
