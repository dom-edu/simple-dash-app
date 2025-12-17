from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

# DATA
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


# if wanted to filter the df by some years 
# df = df[df.year >= 2000] say 2000 - 2007 
# TAKE AWAY -> Don't hardcode values that can be data driven

pop_pivot_df = pd.pivot_table(df,index='year', columns='country', values='pop')  

min_year_ = df['year'].min()
max_year_ = df['year'].max()

# instantiating the dash app 
app = Dash()

# COMPONENTS 
dd2 = dcc.Dropdown(df.country.unique(), 
    ['United States', 'France'], 
    placeholder="Select Countries..",
    id='dd-country-sel-2',
    multi= True
)

dd3 = dcc.Dropdown(df.year.unique(), 
    2007, 
    placeholder='Select Year...',
    id='dd-year-sel-1',
)


# LAYOUT
app.layout = [
    html.H1(children=f'Population Stats: {min_year_} - {max_year_}', style={'textAlign':'center'}, id="graph-title"),
    dcc.Graph(id='graph-content-1'),
    dd2,
    dd3,
    dcc.Graph(id='graph-content-2'),
    dcc.Graph(id="graph-content-3")
]

# CALLBACKS

@callback(
    Output('graph-content-1', 'figure'),
    Input('dd-country-sel-2', 'value')
)
# value from the drop down specified in the input
def update_graph(countries_):
    """
    Docstring for update_graph
    
    :param value: Description
    """

    # filter dataframe by value 
    filter_ = df.country.isin(countries_) 
    dff = df[filter_]

    # make title 
    title_ = f'Population of {", ".join(countries_)} between {min_year_} - {max_year_}'

    # make plotply lineplot 
    ln_plt_fig = px.line(dff, 
                    x='year', 
                    y='pop', 
                    title=title_, 
                    color='country')

    return ln_plt_fig




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


# Exercise: Add another call back / graph for GDP percentage
# https://plotly.com/python/basic-charts/, pick a basic chart 

@callback(
    Output('graph-content-3', 'figure'),
    Input('dd-year-sel-1', 'value')
)
def update_tree_map(year_):

    filter_ = df.year == year_

    fig = px.treemap( df[filter_], 
                     path=[px.Constant("world"), 'continent', 'country'], 
                     values='gdpPercap',
                     title=f"GDP of the World {year_}")

    # formatting the treemap 
    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

    return fig

if __name__ == '__main__':
    app.run(debug=True)
