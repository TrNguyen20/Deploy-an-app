## What this is

A minimal Manufacturing Execution System (MES) prototype built with Streamlit that tracks production orders and actual output against planned quantities. Users update production volumes through a web form, and the app displays real-time status dashboards with SQLite persistence.

### Stack
- **Language:** Python
- **Framework / runtime:** Streamlit (lightweight web app framework)
- **Notable libraries:** pandas (data manipulation), plotly (visualization), sqlite3 (embedded database)

## How it's organized

```
.devcontainer/        Dev container configuration for consistent environments
app.py               Streamlit web app (main entry point) — production tracking UI
db.py                Database initialization script — creates MES schema
schema.sql           Database schema — orders, production_plan, production_actual tables
requirements.txt     Python dependencies (Streamlit, pandas, plotly)
README.md            Minimal placeholder
LICENSE              MIT license
files.zip            Supplementary files (deployment-related)
```

**How it fits together:** When `app.py` runs, it initializes a local SQLite database (`mes_mvp.db`) with an `orders` table and serves a Streamlit UI. Users submit order IDs and actual production quantities through a form; the app persists updates via SQLite upserts and renders the table of all orders with their cumulative actual quantities. The code comments are in Vietnamese, indicating a production context for a Vietnamese manufacturing facility.

## How to run it

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

The app will open at `http://localhost:8501` with a form to update order quantities and a display table of all orders.

## Try asking

- How does the UPSERT logic in app.py accumulate actual quantities for repeated orders?
- What's the difference between the schema in db.py and the table in app.py—which one should be used?
- Is plotly imported but unused, or is visualization functionality planned?
