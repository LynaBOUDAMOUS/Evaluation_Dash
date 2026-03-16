from dash import Dash, html, dcc
import dash


app = Dash(__name__, use_pages=True)

app.layout = html.Div(
    children=[
        html.H1("Application Avocado — Dash"),

        html.Div(
            style={"display": "flex", "gap": "20px"},
            children=[
                dcc.Link("Tableau", href="/"),
                dcc.Link("Comparaison", href="/compare"),
                dcc.Link("Markdown", href="/markdown"),
            ]
        ),

        html.Hr(),

        dash.page_container
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
