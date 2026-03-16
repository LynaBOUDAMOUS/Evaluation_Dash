from dash import html, dcc, register_page
import pandas as pd

# Enregistrement de la page multipages
register_page(
    __name__,
    path="/compare",
    name="Comparaison des régions"
)

# Chargement du dataset
df = pd.read_csv("datas/avocado.csv")

# Liste des régions
regions = sorted(df["region"].unique())

# Layout de la page
layout = html.Div(
    style={"padding": "20px"},
    children=[

        html.H2("Comparaison du prix moyen des avocats entre deux régions"),

        # -----------------------------
        # Ligne 1 : 2 menus déroulants
        # -----------------------------
        html.Div(
            style={
                "display": "flex",
                "flexWrap": "wrap",
                "gap": "20px",
                "marginBottom": "30px"
            },
            children=[
                html.Div(
                    style={"minWidth": "250px"},
                    children=[
                        html.Label("Région 1"),
                        dcc.Dropdown(
                            id="region1-dropdown",
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
                            id="region2-dropdown",
                            options=[{"label": r, "value": r} for r in regions],
                            value=regions[1],
                            clearable=False
                        )
                    ]
                )
            ]
        ),

        # -----------------------------
        # Ligne 2 : 2 graphiques côte à côte
        # -----------------------------
        html.Div(
            style={
                "display": "flex",
                "flexWrap": "wrap",
                "gap": "20px"
            },
            children=[
                html.Div(
                    style={"flex": "1", "minWidth": "350px"},
                    children=[
                        html.H4("Évolution du prix moyen — Région 1"),
                        dcc.Graph(id="graph-region1")
                    ]
                ),
                html.Div(
                    style={"flex": "1", "minWidth": "350px"},
                    children=[
                        html.H4("Évolution du prix moyen — Région 2"),
                        dcc.Graph(id="graph-region2")
                    ]
                )
            ]
        )
    ]
)
