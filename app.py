# Library Setup
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Import function from db_service.py
from services.db_service import get_rush_hours_data

# Initialize Dash Application
app = Dash(__name__)
server = app.server # Required for deployment

# Fetching a data via db_service
df = get_rush_hours_data()

# Create Plotly Visualization
"""
TODO: Create a chart that show volume of each channel in each hour
"""


# App Layout
app.layout = html.Div(

)

if __name__ == "__main__":
    app.run(debug = True)