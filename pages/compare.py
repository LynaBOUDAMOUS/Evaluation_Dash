import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

dash.register_page(__name__, path="/compare")

df = pd.read_csv("datas/avocado.csv")

regions = sorted(df["region"].unique())

layout = dbc.Container([

    html.H3("Prix moyen dans le temps"),

    dbc.Row([

        dbc.Col([
            html.Label("Région 1"),
            dcc.Dropdown(
                id="region1",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[0]
            )
        ]),

        dbc.Col([
            html.Label("Région 2"),
            dcc.Dropdown(
                id="region2",
                options=[{"label": r, "value": r} for r in regions],
                value=regions[1]
            )
        ])

    ]),

    html.Br(),

    dbc.Row([

        dbc.Col(dcc.Graph(id="graph1")),
        dbc.Col(dcc.Graph(id="graph2"))

    ])

])