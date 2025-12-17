from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# reading the data 
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# instantiating the dash app 
app = Dash()

# Layout consists of Title, dropdown and graph
app.layout = [
    html.H1(children='Population from 1950 - 2007', style={'textAlign':'center'}),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

"""
Callbacks allows data to flow between components 
i.e. from the dropdown -> graph via user interaction
i.e. select a different country 


Syntax of Callback parameters (registers an output and input component for data flow)

Output(id, property)
Input(id, property)

Output('graph-content', 'figure'),
Input('dropdown-selection', 'value')

This @callback decorator applies to the update_graph

your function needs def update_
below it's called update_graph


"""

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
# value from the drop down specified in the input
def update_graph(value):

    # filter dataframe by value 
    dff = df[df.country==value]

    # make plotply lineplot 
    ln_plt_fig = px.line(dff, x='year', y='pop')

    return ln_plt_fig

if __name__ == '__main__':
    app.run(debug=True)
