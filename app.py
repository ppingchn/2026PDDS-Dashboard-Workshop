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

fig = px.bar(
    df,
    x = "hour_of_day",
    y = "total_orders",
    color = "channel",
    barmode = "group",
    title = "Daily Peak Hours: Walk-in vs. Foodpanda",
    labels = {
        "hour_of_day": "Hour of Day",
        "total_orders": "Total Orders",
        "channel": "Channel"
    },
    color_discrete_map = {
        "Walk-in": "#2E7D32",
        "Foodpanda": "#D81B60"
    }
)

fig.update_layout(
    xaxis_tickangle = -45,
    plot_bgcolor = "white",
    hovermode = "x unified"
)

# App Layout
app.layout = html.Div(

)

if __name__ == "__main__":
    app.run(debug = True)