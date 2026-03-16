import dash
from dash import html, dcc, dash_table
import pandas as pd

import table_cb.py

dash.register_page(__name__, path="/table")

df = pd.read_csv("datas/avocado.csv")

regions = sorted(df["region"].unique())
types = sorted(df["type"].unique())

layout = html.Div([

    html.H2("Table des ventes d'avocats"),

    html.Div([

        html.Div([
            html.Label("Région"),
            dcc.Dropdown(
                id="region-dropdown",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0]
            )
        ], style={"width": "45%", "display": "inline-block"}),

        html.Div([
            html.Label("Type"),
            dcc.Dropdown(
                id="type-dropdown",
                options=[{"label": t, "value": t} for t in types],
                value=types,
                multi=True
            )
        ], style={"width": "45%", "display": "inline-block"}),

    ]),

    dash_table.DataTable(
        id="table-avocado",
        page_size=10
    )

])

