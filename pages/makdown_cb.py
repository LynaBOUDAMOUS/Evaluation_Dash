from dash import callback, Input, Output, dcc

@callback(
    Output("markdown-content", "children"),
    Input("accordion-md", "value")
)
def display_md(selected):
    if selected is None:
        return ""

    filename = {
        "ex1": "datas/expli1.md",
        "ex2": "datas/expli2.md",
        "ex3": "datas/expli3.md"
    }[selected]

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()

    return dcc.Markdown(content)
