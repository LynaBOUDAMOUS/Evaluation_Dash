from dash import html, dcc, register_page
import pandas as pd
import dash_table

register_page(__name__, path="/", name="Tableau")

df = pd.read_csv("datas/avocado.csv")

regions = sorted(df["region"].unique())
types = sorted(df["type"].unique())
types.insert(0, "Tous")

layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H2("Tableau des ventes d’avocats"),

        html.Div(
            style={"display": "flex", "flexWrap": "wrap", "gap": "20px"},
            children=[
                html.Div(
                    style={"minWidth": "250px"},
                    children=[
                        html.Label("Région"),
                        dcc.Dropdown(
                            id="region-dropdown",
                            options=[{"label": r, "value": r} for r in regions],
                            value=regions[0],
                            clearable=False
                        )
                    ]
                ),
                html.Div(
                    style={"minWidth": "250px"},
                    children=[
                        html.Label("Type d’avocat"),
                        dcc.Dropdown(
                            id="type-dropdown",
                            options=[{"label": t, "value": t} for t in types],
                            value="Tous",
                            clearable=False
                        )
                    ]
                )
            ]
        ),

        html.Br(),

        dash_table.DataTable(
            id="table-avocado",
            page_size=15,
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "center"},
        )
    ]
)
