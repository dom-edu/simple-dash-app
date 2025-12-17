from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# DATA
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
pop_pivot_df = pd.read_csv('data/population-data.csv')

# instantiating the dash app 
app = Dash()

# COMPONENTS 
dd1 = dcc.Dropdown(df.country.unique(), 
    'Canada', 
    id='dd-country-sel-1'
)

dd2 = dcc.Dropdown(df.country.unique(), 
    ['United States', 'France'], 
    placeholder="Select Countries..",
    id='dd-country-sel-2',
    multi= True
)

dd3 = dcc.Dropdown(df.year.unique(), 
    2007, 
    placeholder='Select Year...',
    id='dd-year-sel-2',
)


# LAYOUT
app.layout = [
    html.H1(children='Population from 1950 - 2007', style={'textAlign':'center'}, id="graph-title"),
    dd1,
    dcc.Graph(id='graph-content-1'),
    dd2,
    dd3,
    dcc.Graph(id='graph-content-2')
]

# CALLBACKS

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
