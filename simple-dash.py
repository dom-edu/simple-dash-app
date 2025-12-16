from dash import Dash, html, dcc # core components
import pandas as pd 
import plotly.express as px

# import plotly lineplot

AAPL_URL = "https://raw.githubusercontent.com/matplotlib/sample_data/refs/heads/master/aapl.csv"

# load the data in via pandas 
aapl_df = pd.read_csv(AAPL_URL)

# convert Date to Date time 
aapl_df['Date'] = pd.to_datetime(aapl_df['Date'])

# sort the values by Date
aapl_df.sort_values(by="Date", inplace=True) # 1984 - 2007 

# make figures
line_plot = px.line(aapl_df, x="Date", y="Close", title='Apple Stock Closing Price (USD) 1984 - 2008')

# instantiating the app 
app = Dash()

# adding elements to the app
app.layout = [

    html.H1(children='Apple Stock App', style={'textAlign':'center'}), 
    dcc.Graph(id='graph-content', figure=line_plot)

]

if __name__ == '__main__':
    app.run(debug=True)
