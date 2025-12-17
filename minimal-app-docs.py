from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# reading the data 
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# make pivot table 
pop_pivot_df = pd.pivot_table(df,index='year', columns='country', values='pop') 

# instantiating the dash app 
app = Dash()

# Layout consists of Title, dropdown and graph
app.layout = [
    html.H1(children='Population from 1950 - 2007', style={'textAlign':'center'}, id="graph-title"),
    dcc.Dropdown(df.country.unique(), 
                'Canada', 
                id='dd-country-sel-1'),
    dcc.Graph(id='graph-content-1'),

    # second graphic  
    dcc.Dropdown(df.country.unique(), 
                ['United States', 'France'], 
                placeholder="Select Countries..",
                id='dd-country-sel-2',
                multi= True
                ),

    # Exercise : add another drop down to select a year 
    dcc.Dropdown(df.year.unique(), 
                2007, 
                placeholder='Select Year...',
                id='dd-year-sel-1',
                ),

    dcc.Graph(id='graph-content-2')
    
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
    Output('graph-content-1', 'figure'),
    Input('dd-country-sel-1', 'value')
)
# value from the drop down specified in the input
def update_graph(value):
    """
    Docstring for update_graph
    
    :param value: Description
    """

    # filter dataframe by value 
    dff = df[df.country==value]

    # make plotply lineplot 
    ln_plt_fig = px.line(dff, x='year', y='pop')

    return ln_plt_fig

# make a new dropdown that changes the title 
@callback(
    Output('graph-title', 'children'),
    Input('dd-country-sel-1', 'value')
)
def update_title(value):
    """
    Docstring for update_title
    
    :param value: Description
    """

    # make a new string 
    new_str = f"Population of {value} between 1950-2007"
    return new_str


# Exercise: Write a callback that makes our bar chart that we made in collab 
@callback(
    Output('graph-content-2', 'figure'),
    Input('dd-country-sel-2', 'value'),
    Input('dd-year-sel-1', 'value')
)
def update_graph2(countries_, year_):
    """
    Docstring for update_graph2
    :param values: 
    countries_ = list of countries from dd-country-sel-2
    year_  = dd-year-sel-1
    """ 
    print("update2 graph:",countries_)
    print("update2 graph:",year_)
    # get  population values
    pop_vals = pop_pivot_df[countries_].loc[year_].tolist()

    bar_chart = px.bar(x=countries_, 
             y=pop_vals, 
             title=f"Population Comparison for {year_}",
             labels={
                     "x": "Countries",
                     "y": "Population",
                    
                 },)
    return bar_chart


# Exercise: Refactor code to update the title for the year in the bar chart

if __name__ == '__main__':
    app.run(debug=True)
