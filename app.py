# Library Setup
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Initialize Dash Application
app = Dash(__name__)
server = app.server


if __name__ == "__main__":
    app.run(debug = True)