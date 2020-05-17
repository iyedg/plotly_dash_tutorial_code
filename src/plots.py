import plotly.express as px
import json
from pyprojroot import here


def get_geojson():
    with open(here("data/tunisia.geojson"), mode="r") as f:
        geojson = json.load(f)
    return geojson


def plot_part_of_daily_active_cases(df, indicator="cas"):
    fig = px.choropleth(
        df.reset_index(),
        geojson=get_geojson(),
        featureidkey="properties.CIRC_ID",
        projection="mercator",
        locations="CIRC_ID",
        color=indicator,
        hover_data=[indicator, "gouvernorat"],
        template="plotly_white",
        animation_frame="date",
        color_continuous_scale=list(
            reversed(["#ffffcc", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494"])
        ),
    )
    fig.update_geos(fitbounds="locations", visible=False)

    return fig


def plot_daily_cumulative_active_cases(df, indicator="cas", log_y=False, limit=None):
    if limit:
        df = df.pipe(
            lambda df: df.set_index("gouvernorat").loc[
                df.groupby("gouvernorat")
                .agg({indicator: "sum"})
                .sort_values(indicator, ascending=False)[:limit]
                .index
            ]
        ).reset_index()
    return df.pipe(
        lambda df: px.line(
            df,
            x="date",
            y=indicator,
            color="gouvernorat",
            template="plotly_white",
            log_y=log_y,
        )
    )


def plot_race_plot_of_cumulative_daily_active_cases(df, indicator):
    fig = df.pipe(
        lambda df: px.bar(
            df,
            y="gouvernorat",
            x=indicator,
            animation_frame="date",
            orientation="h",
            height=600,
            template="plotly_white",
        )
    )
    fig.update_layout(yaxis={"categoryorder": "total ascending"})
    return fig
