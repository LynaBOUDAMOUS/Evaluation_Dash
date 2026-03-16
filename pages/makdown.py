from dash import html, dcc, register_page

register_page(__name__, path="/markdown", name="Documentation")

layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H2("Documentation Markdown"),

        dcc.Accordion(
            id="accordion-md",
            items=[
                {"label": "Explication 1", "value": "ex1"},
                {"label": "Explication 2", "value": "ex2"},
                {"label": "Explication 3", "value": "ex3"},
            ]
        ),

        html.Div(id="markdown-content", style={"marginTop": "20px"})
    ]
)
