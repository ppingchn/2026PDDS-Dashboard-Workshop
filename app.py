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
        "total_order": "Total Orders",
        "channel": "Sales Channel"
    },
    color_discrete_map = {
        "Walk-in": "#2E7D32",
        "Foodpanda": "#D81B60"
    }
)

fig.update_layout(
    font={"family": "Segoe UI, Arial, sans-serif", "color": "#1E293B"},
    title_font={"size": 18, "weight": "bold"},
    plot_bgcolor="white",
    paper_bgcolor="white",
    hovermode="x unified",
    margin={"t": 60, "r": 20, "b": 40, "l": 40},
    legend={
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "right",
        "x": 1,
        "title_text": ""
    },
    xaxis={
        "tickangle": 0,
        "showline": True,
        "linecolor": "#E2E8F0"
    },
    yaxis={
        "showgrid": True,
        "gridcolor": "#F1F5F9",
        "zeroline": False
    }
)

fig.update_traces(marker_line_width=0, opacity=0.92)

# App Layout
app.layout = html.Div(
    style = {
        "backgroundColor": "#F8FAFC",
        "minHeight": "100vh",
        "padding": "40px 20px",
        "fontFamily": "'Segoe UI', Roboto, Arial, sans-serif",
        "color": "#0F172A"
    },
    children = [
        # Main Container
        html.Div(
            style = {
                "maxWidth": "960px",
                "margin": "0 auto"
            },
            children = [
                # Header Section
                html.Div(
                    style={"marginBottom": "24px"},
                    children=[
                        html.H1(
                            "Bubble Tea Store Analytics",
                            style={
                                "fontSize": "28px",
                                "fontWeight": "700",
                                "margin": "0 0 6px 0",
                                "color": "#0F172A"
                            }
                        ),
                        html.P(
                            "Comparing Walk-in vs. Foodpanda rush hours for shift scheduling",
                            style={
                                "fontSize": "15px",
                                "color": "#64748B",
                                "margin": "0"
                            }
                        )
                    ]
                ),

                # Chart Card
                html.Div(
                    style={
                        "backgroundColor": "#FFFFFF",
                        "borderRadius": "12px",
                        "padding": "24px",
                        "boxShadow": "0 1px 3px rgba(0, 0, 0, 0.08)",
                        "border": "1px solid #E2E8F0"
                    },
                    children=[
                        dcc.Graph(
                            id="rush-hours-graph",
                            figure=fig,
                            config={"displayModeBar": False}
                        )
                    ]
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run(debug = True)