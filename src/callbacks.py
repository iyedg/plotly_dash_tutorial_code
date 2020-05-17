from dash.dependencies import Input, Output
import dash_core_components as dcc
from .app import app

from .plots import (
    plot_daily_cumulative_active_cases,
    plot_part_of_daily_active_cases,
    plot_race_plot_of_cumulative_daily_active_cases,
)
from .data import targa_covid_df, geo_targa_covid_df


@app.callback(
    Output("main_graph", "figure"),
    [Input("content_view_selector", "value"), Input("indicator_selector", "value")],
)
def update_main_content(view, indicator):
    if view == "map" or view is None:
        return plot_part_of_daily_active_cases(geo_targa_covid_df, indicator)
    elif view == "line":
        return plot_daily_cumulative_active_cases(geo_targa_covid_df, indicator)
    else:
        return plot_race_plot_of_cumulative_daily_active_cases(
            geo_targa_covid_df, indicator
        )
