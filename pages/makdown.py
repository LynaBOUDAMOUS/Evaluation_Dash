from dash import Input, Output, callback
import pandas as pd
import plotly.express as px


df = pd.read_csv("datas/avocado.csv")

@app.callback(
    Output("graph1", "figure"),
    Output("graph2", "figure"),
    Input("region1", "value"),
    Input("region2", "value"),
)
def update_graphs(r1, r2):

    df1 = df[df["region"] == r1]
    df2 = df[df["region"] == r2]

    fig1 = px.line(df1, x="Date", y="AveragePrice", title=r1)
    fig2 = px.line(df2, x="Date", y="AveragePrice", title=r2)

    return fig1, fig2