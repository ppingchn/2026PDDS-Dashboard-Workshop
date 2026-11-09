# services/db_service.py

# Library Setup
import os
import sqlite3
import pandas as pd

# Automatic resolve absolute path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "BubbleTeaDB_2026.db")

# Fetches hourly order counts grouped by sales channel
def get_rush_hours_data() -> pd.DataFrame:
    # Code your query here
    query = """
        SELECT
            strftime('%H:00', order_time) AS hour_of_day,
            channel,
            COUNT(order_id) AS total_order
        FROM Orders
        GROUP BY __ , __
        ORDER BY __;
    """

    with sqlite3.connect(DB_PATH) as conn:
        df = pd.read_sql_query(query, conn)
    return df