from dash import Dash, dash_table, dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from dash import html, dcc, dash_table, register_page
import pandas as pd



register_page(
    __name__,
    path="/table",
    name="Tableau des données"
)

# Chargement du dataset
df = pd.read_csv("datas/avocado.csv")


cols_to_hide = [
    "Unnamed: 0", "4046", "4225", "4770",
    "Small Bags", "Large Bags", "XLarge Bags"
]

df_visible = df.drop(columns=[c for c in cols_to_hide if c in df.columns])


regions = sorted(df["region"].unique())
types_avocats = ["Tous"] + sorted(df["type"].unique())

# Layout de la page
layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H2("Tableau des ventes d’avocats"),

        # Menus déroulants
        html.Div(
            style={
                "display": "flex",
                "flexWrap": "wrap",
                "gap": "20px",
                "marginBottom": "20px"
            },
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
                            options=[{"label": t, "value": t} for t in types_avocats],
                            value="Tous",
                            clearable=False
                        )
                    ]
                )
            ]
        ),

        # Tableau
        dash_table.DataTable(
            id="table-avocado",
            columns=[{"name": col, "id": col} for col in df_visible.columns],
            data=df_visible.to_dict("records"),
            page_size=15,
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "left", "padding": "5px"},
            style_header={"fontWeight": "bold"}
        )
    ]
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = layout
if __name__ == "__main__":
    app.run_server(debug=True)
