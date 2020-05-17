from pyprojroot import here
import pandas as pd
import geopandas as gpd


def rename_geo_df_columns(geo_df):
    return geo_df.pipe(
        lambda gdf: gdf.rename(
            columns={"NAME_EN": "gouvernorat", "NAME_AR": "gouvernorat_ar"}
        )
    )


def merge_covid_geo(covid_df, geo_df):
    return covid_df.merge(geo_df, on=["gouvernorat"]).pipe(
        lambda df: df.assign(date=df["date"].astype(str))
    )


geo_df = gpd.read_file(here("data/tunisia.geojson")).pipe(rename_geo_df_columns)
targa_covid_df = pd.read_csv(here("data/targa_covid_cumulative_no_neg.csv"))
official_covid_df = pd.read_csv(here("data/official_covid.csv"))
geo_targa_covid_df = merge_covid_geo(targa_covid_df, geo_df)

by_gov_indicators = targa_covid_df.columns.difference(["gouvernorat", "date"])
country_wide_indicators = official_covid_df.columns.difference(["dates"])
governorates = targa_covid_df["gouvernorat"].unique()

last_update = targa_covid_df["date"].max()


if __name__ == "__main__":
    print(geo_targa_covid_df.columns)
