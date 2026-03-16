from dash import callback, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("datas/avocado.csv")

@callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Input("region1", "value"),
    Input("region2", "value")
)
def update_graphs(r1, r2):
    d1 = df[df["region"] == r1]
    d2 = df[df["region"] == r2]

    ymin = min(d1["AveragePrice"].min(), d2["AveragePrice"].min())
    ymax = max(d1["AveragePrice"].max(), d2["AveragePrice"].max())

    fig1 = px.line(d1, x="Date", y="AveragePrice", title=f"Prix moyen — {r1}")
    fig2 = px.line(d2, x="Date", y="AveragePrice", title=f"Prix moyen — {r2}")

    fig1.update_yaxes(range=[ymin, ymax])
    fig2.update_yaxes(range=[ymin, ymax])

    return fig1, fig2
