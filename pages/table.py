# Importation des bibliothèques
from dash import Dash, dash_table, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd


df = pd.read_csv("datas/avocado.csv") 
df.drop(["4046", "4225", "Unnamed: 0", "4770" ,"Small Bags", "Large Bags", "XLarge Bags"], axis=1, inplace=True )      


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([
    # Ligne pour le titre
    dbc.Row([
        dbc.Col([
            html.H1("Tableau de données sur les avocats", className="text-center my-4")
        ], width=12)
    ]),
    
 
    dbc.Row([
        dbc.Col([
            html.Label("Sélectionnez la région :"),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': r, 'value': r} for r in sorted(df['region'].dropna().unique())],
                value=df['region'].dropna().unique()[0], # Valeur par défaut
                clearable=False
            )
        ], width=6),
        
      
        dbc.Col([
            html.Label("Sélectionnez le type d'avocat :"),
            dcc.Dropdown(
                id='type-dropdown',
                options=[{'label': t, 'value': t} for t in sorted(df['type'].dropna().unique())],
                value=df['type'].dropna().unique()[0], # Valeur par défaut
                clearable=False
            )
        ], width=6)
    ], className="mb-4"), 
    

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id="our-data-table",
                page_size=10,
                style_table={'overflowX': 'auto'} 
            )
        ], width=12)
    ])
])


@app.callback(
    [Output('our-data-table', 'data'),
     Output('our-data-table', 'columns')],
    [Input('region-dropdown', 'value'),
     Input('type-dropdown', 'value')]
)
def update_table(selected_region, selected_type):
    
    filtered_df = df[(df['region'] == selected_region) & (df['type'] == selected_type)]
    data = filtered_df.to_dict('records')
    columns = [{"name": i, "id": i} for i in filtered_df.columns]
    
    return data, columns


if __name__ == "__main__":
    app.run(debug=True)