# Importation des bibliothèques
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


df = pd.read_csv("datas/avocado.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')


regions_disponibles = sorted(df['region'].dropna().unique())


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container([
    # Titre de la page
    dbc.Row([
        dbc.Col([
            html.H1("Prix moyen dans le temps", className="text-center my-4")
        ], width=12)
    ]),

    
    dbc.Row([
      
        dbc.Col([
            html.Label("Sélectionnez la première région :"),
            dcc.Dropdown(
                id='region1-dropdown',
                options=[{'label': r, 'value': r} for r in regions_disponibles],
                value=regions_disponibles[0], # Première région par défaut
                clearable=False
            ),
            #premier graphique
            dcc.Graph(id='graph-region1')
        ], width=6), 

        dbc.Col([
            html.Label("Sélectionnez la deuxième région :"),
            dcc.Dropdown(
                id='region2-dropdown',
                options=[{'label': r, 'value': r} for r in regions_disponibles],
                
                value=regions_disponibles[1] if len(regions_disponibles) > 1 else regions_disponibles[0], 
                clearable=False
            ),
         
            dcc.Graph(id='graph-region2')
        ], width=6)
    ])
], fluid=True) 


@app.callback(
    [Output('graph-region1', 'figure'),
     Output('graph-region2', 'figure')],
    [Input('region1-dropdown', 'value'),
     Input('region2-dropdown', 'value')]
)
def update_graphs(region1, region2):
    
    df1 = df[df['region'] == region1]
    df1_grouped = df1.groupby('Date')['AveragePrice'].mean().reset_index()  
    fig1 = px.line(df1_grouped, x='Date', y='AveragePrice', title=f"Prix moyen - {region1}")
    
    
    df2 = df[df['region'] == region2]
    df2_grouped = df2.groupby('Date')['AveragePrice'].mean().reset_index()
    fig2 = px.line(df2_grouped, x='Date', y='AveragePrice', title=f"Prix moyen - {region2}")
    return fig1, fig2


if __name__ == "__main__":
    app.run(debug=True)