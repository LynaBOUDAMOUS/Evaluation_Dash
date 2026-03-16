import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([

    html.H1("Dashboard Avocado", className="title"),

    dbc.Nav(
        [
            dbc.NavLink("Table", href="/table"),
            dbc.NavLink("Compare", href="/compare"),
            dbc.NavLink("Markdown", href="/markdown"),
        ],
        pills=True
    ),

    dash.page_container

], fluid=True)

if __name__ == "__main__":
    app.run(debug=True)