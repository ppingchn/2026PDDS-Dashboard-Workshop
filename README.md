# 2026 PDDS Dashboard Workshop: Bubble Tea Analytics

Welcome to the **2026 PDDS Dashboard Workshop**! In this hands-on workshop, you will build an end-to-end interactive web analytics dashboard for a Bubble Tea business using **SQLite**, **Python**, **Pandas**, **Plotly**, and **Dash**.

---

## 📌 Project Overview

The objective of this project is to analyze hourly order volume across different sales channels (`Walk-in` vs. `Foodpanda`) to identify peak rush hours and operational patterns.

By completing this workshop, you will learn how to:
1. Extract and aggregate relational data from an SQLite database using SQL & Pandas.
2. Structure a Python service layer (`db_service.py` in `services/`).
3. Create interactive data visualizations using **Plotly Express**.
4. Build and deploy a reactive web dashboard using **Plotly Dash**.

---

## 📁 Directory Structure

```text
2026PDDS-Dashboard-Workshop/
│
├── BubbleTeaDB_2026.db         # SQLite database containing store orders and sales records
├── requirements.txt            # Python dependencies (Dash, Pandas, Plotly, Gunicorn)
├── app.py                      # Main Dash web application and layout definition
├── services/
│   └── db_service.py           # Database service layer for queries and data retrieval
├── venv/                       # Python virtual environment (ignored in git)
├── .gitignore                  # Git ignore rules for virtual environments and caches
└── README.md                   # Project documentation and student instructions
```

### Component Details
- **`BubbleTeaDB_2026.db`**: Pre-populated SQLite database with sales data (Orders, Items, Drinks, Channels, etc.).
- **`db_service.py`** (located in `services/`): Encapsulates all SQL query logic and returns ready-to-use Pandas DataFrames to keep the codebase modular.
- **`app.py`**: Entry point for the Dash application. Configures the visualizations, builds the user interface, and hosts the local development server.
- **`requirements.txt`**: Lists all required Python packages.

---

## 🗄️ Database Schema Reference

The database `BubbleTeaDB_2026.db` consists of the following core tables:

| Table | Primary Key | Key Columns / Description |
| :--- | :--- | :--- |
| **`Orders`** | `order_id` | `order_time` (DATETIME: `YYYY-MM-DD HH:MM`), `channel` (`Walk-in`, `Foodpanda`), `staff_id` |
| **`OrderItem`** | (`order_id`, `drink_id`) | `quantity`, `unit_price` |
| **`Drink`** | `drink_id` | `drink_name`, `current_price`, `availability_status`, `category_id`, `supplier_id` |
| **`Category`** | `category_id` | `category_name` (e.g. Milk Tea, Fruit Tea, Latte) |
| **`Staff`** | `staff_id` | `staff_name`, `role` (Shift lead, Owner, etc.) |
| **`Supplier`** | `supplier_id` | `supplier_name`, `contact_info` |
| **`Promotion`**| `promotion_id` | `start_date`, `end_date`, `discount_rate`, `drink_id` |

> [!NOTE]
> For this workshop, the primary table you will interact with is **`Orders`**.

---

## 🚀 Environment Setup

### 1. Clone the Repository & Navigate to Project
```bash
git clone <repository-url>
cd 2026PDDS-Dashboard-Workshop
```

### 2. Create and Activate Virtual Environment

* **Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
  *(If PowerShell gives an execution policy error, run: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then reactivate)*

* **Windows (Command Prompt):**
  ```cmd
  python -m venv venv
  .\venv\Scripts\activate.bat
  ```

* **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Verify that the packages (`dash`, `pandas`, `plotly`, `gunicorn`) are installed:
```bash
pip list
```

---

## 🎯 Workshop Checkpoints

Complete the tasks sequentially through each checkpoint:

- **Checkpoint 1**: Complete SQL Query (`db_service.py` in `services/`)
- **Checkpoint 2**: Build Plotly Visualization (`app.py`)
- **Checkpoint 3**: Construct Dash Layout (`app.py`)
- **Checkpoint 4**: Run & Verify Dashboard locally (`http://127.0.0.1:8050`)
- **Bonus Checkpoint**: Customization & Production Deployment

---

### 📍 Checkpoint 1: Complete SQL Query in Database Service
**Target File**: `db_service.py` (located in `services/`)

Open `db_service.py` in `services/`. You will find the function `get_rush_hours_data()`. The SQL query has missing clauses marked with `__`:

```python
def get_rush_hours_data() -> pd.DataFrame:
    query = """
        SELECT
            strftime('%H:00', order_time) AS hour_of_day,
            channel,
            COUNT(order_id) AS total_order
        FROM Orders
        GROUP BY __ , __
        ORDER BY __;
    """
    ...
```

#### Task:
1. Complete the `GROUP BY` clause so that orders are aggregated by both the extracted hour of day and the sales channel.
2. Complete the `ORDER BY` clause to order the output chronologically by hour and by channel.
3. **Expected columns in returned DataFrame**:
   - `hour_of_day`: String representing the hour (e.g., `'11:00'`, `'12:00'`).
   - `channel`: String (`'Walk-in'` or `'Foodpanda'`).
   - `total_order`: Integer representing the count of orders.

#### ✅ Verification:
Test your query by running a quick inline command:
```bash
python -c "from services.db_service import get_rush_hours_data; df = get_rush_hours_data(); print(df.head()); print('Total rows:', len(df))"
```
*Expected Output Check*: You should see rows grouped by hour (e.g., `11:00`, `12:00` ...) with order counts for each channel.

---

### 📍 Checkpoint 2: Create Plotly Visualization
**Target File**: `app.py`

Open `app.py`. Under `# Create Plotly Visualization`, use `plotly.express` to generate a chart.

#### Task:
Create a grouped bar chart (or line chart) that highlights the order volumes across hours of the day:
- **X-axis**: `hour_of_day`
- **Y-axis**: `total_order`
- **Color**: `channel`
- **Bar mode**: `barmode='group'`
- **Labels & Title**: Provide descriptive titles and axes names (e.g., `"Hourly Order Volume by Sales Channel"`).

*Example Snippet:*
```python
fig = px.bar(
    df,
    x="hour_of_day",
    y="total_order",
    color="channel",
    barmode="group",
    title="Hourly Order Volume by Sales Channel (Rush Hours Analysis)",
    labels={
        "hour_of_day": "Hour of Day",
        "total_order": "Total Number of Orders",
        "channel": "Sales Channel"
    }
)
```

---

### 📍 Checkpoint 3: Assemble Dash App Layout
**Target File**: `app.py`

#### Task:
Define `app.layout` using `html.Div` and `dcc.Graph` to display your visualization in the web browser.

*Requirements*:
1. An `html.H1` main title for the dashboard (e.g., `"Bubble Tea Store Analytics"`).
2. An informative description or subtitle (`html.P`).
3. A `dcc.Graph` component linking to the figure `fig` created in Checkpoint 2 (with an `id="rush-hour-chart"`).
4. Clean container styling (e.g., standard margins, padding, and centered text).

*Example Structure:*
```python
app.layout = html.Div(
    style={"padding": "30px", "fontFamily": "Arial, sans-serif"},
    children=[
        html.H1("🧋 Bubble Tea Sales Dashboard", style={"textAlign": "center"}),
        html.P(
            "Analyzing peak rush hours and distribution across sales channels.",
            style={"textAlign": "center", "color": "#666"}
        ),
        dcc.Graph(id="rush-hour-chart", figure=fig)
    ]
)
```

---

### 📍 Checkpoint 4: Run and Test Locally

#### Task:
Launch the Dash development server:
```bash
python app.py
```

Open your browser and navigate to:
```
http://127.0.0.1:8050/
```

#### ✅ Acceptance Criteria:
- [ ] Web page loads successfully without Python traceback errors.
- [ ] Main title and descriptive text are visible.
- [ ] Interactive grouped bar chart displays hours on the horizontal axis and order volume on the vertical axis.
- [ ] Legend allows toggling channels (`Walk-in` / `Foodpanda`) on and off.
- [ ] Hover tooltips show exact counts for each hour and channel.

---

## 🛠️ Troubleshooting & FAQ

- **PowerShell Script Execution Error (`Activate.ps1 cannot be loaded`)**:
  Run PowerShell as Administrator or set process scope:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
- **`ModuleNotFoundError: No module named 'dash'`**:
  Ensure your virtual environment is activated (you should see `(venv)` in your terminal prompt) and run `pip install -r requirements.txt`.
- **Port 8050 Already In Use**:
  Change the port in `app.py`:
  ```python
  if __name__ == "__main__":
      app.run(debug=True, port=8055)
  ```
- **Database Path Issues**:
  `db_service.py` (in `services/`) uses `os.path.abspath` to resolve the root folder automatically. Ensure `BubbleTeaDB_2026.db` remains in the project root.
