from dash import html, dcc, register_page
import pandas as pd

register_page(__name__, path="/compare", name="Comparaison")

df = pd.read_csv("datas/avocado.csv")
regions = sorted(df["region"].unique())

layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H2("Comparaison du prix moyen entre deux régions"),

        html.Div(
            style={"display": "flex", "gap": "20px", "flexWrap": "wrap"},
            children=[
                html.Div(
                    style={"minWidth": "250px"},
                    children=[
                        html.Label("Région 1"),
                        dcc.Dropdown(
                            id="region1",
                            options=[{"label": r, "value": r} for r in regions],
                            value=regions[0],
                            clearable=False
                        )
                    ]
                ),
                html.Div(
                    style={"minWidth": "250px"},
                    children=[
                        html.Label("Région 2"),
                        dcc.Dropdown(
                            id="region2",
                            options=[{"label": r, "value": r} for r in regions],
                            value=regions[1],
                            clearable=False
                        )
                    ]
                )
            ]
        ),

        html.Br(),

        html.Div(
            style={"display": "flex", "gap": "20px", "flexWrap": "wrap"},
            children=[
                html.Div(
                    style={"flex": 1, "minWidth": "350px"},
                    children=[dcc.Graph(id="graph1")]
                ),
                html.Div(
                    style={"flex": 1, "minWidth": "350px"},
                    children=[dcc.Graph(id="graph2")]
                )
            ]
        )
    ]
)
