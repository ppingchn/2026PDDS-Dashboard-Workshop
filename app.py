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
    y = "total_order",
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
    style = {
        "fontFamily": "Arial, sans-serif",
        "maxWidth": "900px",
        "margin": "0 auto",
        "padding": "20px"
    },
    children = [
        html.H1(
            "Bubble Tea Store Analytics",
            style = {
                "textAlign": "center"
            }
        ),
        html.P(
            "Comparing Walk-in vs. Foodpanda Rush Hours for Shift Scheduling",
            style = {
                "textAlign" : "center",
                "color": "#666"
            }
        ),
        dcc.Graph(
            id = "rush-hours-graph",
            figure = fig
        )
    ]
)

if __name__ == "__main__":
    app.run(debug = True)