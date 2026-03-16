from dash import Input, Output, callback
import pandas as pd

df = pd.read_csv("datas/avocado.csv")

columns_to_remove = [
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags"
]

df = df.drop(columns=[c for c in columns_to_remove if c in df.columns])


@callback(
    Output("table-avocado", "data"),
    Output("table-avocado", "columns"),
    Input("region-dropdown", "value"),
    Input("type-dropdown", "value"),
)
def update_table(region, types):

    dff = df[df["region"] == region]

    if types:
        dff = dff[dff["type"].isin(types)]

    return (
        dff.to_dict("records"),
        [{"name": i, "id": i} for i in dff.columns],
    )