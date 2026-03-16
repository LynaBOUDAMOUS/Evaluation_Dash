from dash import html, register_page
import dash_mantine_components as dmc

register_page(__name__, path="/markdown", name="Documentation")

layout = html.Div(
    style={"padding": "20px"},
    children=[
        html.H2("Documentation Markdown"),

        dmc.Accordion(
            id="accordion-md",
            children=[
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Explication 1"),
                        dmc.AccordionPanel("Contenu 1")
                    ],
                    value="ex1"
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Explication 2"),
                        dmc.AccordionPanel("Contenu 2")
                    ],
                    value="ex2"
                ),
                dmc.AccordionItem(
                    [
                        dmc.AccordionControl("Explication 3"),
                        dmc.AccordionPanel("Contenu 3")
                    ],
                    value="ex3"
                ),
            ]
        ),

        html.Div(id="markdown-content", style={"marginTop": "20px"})
    ]
)
