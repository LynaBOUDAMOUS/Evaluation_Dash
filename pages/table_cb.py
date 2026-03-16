from dash import callback, Input, Output
import pandas as pd

df = pd.read_csv("datas/avocado.csv")

colonnes_a_supprimer = [
    "Unnamed: 0", "4046", "4225", "4770",
    "Small Bags", "Large Bags", "XLarge Bags"
]

@callback(
    Output("table-avocado", "data"),
    Output("table-avocado", "columns"),
    Input("region-dropdown", "value"),
    Input("type-dropdown", "value")
)
def update_table(region, type_avocat):
    dff = df[df["region"] == region]

    if type_avocat != "Tous":
        dff = dff[dff["type"] == type_avocat]

    dff = dff.drop(columns=colonnes_a_supprimer)

    return dff.to_dict("records"), [{"name": c, "id": c} for c in dff.columns]
