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
fig = px.bar(
    df,
    x="hour_of_day",
    y="total_order",
    color="channel",
    barmode="group",
    title="Total Order Volume by Hour and Sales Channel (21 Sep – 1 Nov 2026)",
    labels={
        "hour_of_day": "Clock Hour",
        "total_order": "Total Orders Across All Recorded Days",
        "channel": "Sales Channel"
    }
)

fig.update_layout(
    xaxis_title="Clock Hour",
    yaxis_title="Total Orders (21 Sep – 1 Nov 2026)",
    legend_title="Sales Channel",
    template="plotly_white"
)


# App Layout
app.layout = html.Div(
    children=[
        html.H1("Bubble Tea Sales Dashboard"),
        html.H2("Rush Hour Analysis"),
        html.P(
            "Total accumulated orders across all recorded days "
            "(21 September – 1 November 2026), not average daily orders."
        ),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)


