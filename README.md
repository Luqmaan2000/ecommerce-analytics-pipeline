# 🛒 Ecommerce Analytics Pipeline

An end-to-end data project that simulates an e-commerce analytics pipeline. This project combines Python, SQL, API integration, and Power BI to clean, enrich, and visualize user order data in a business-ready format.

---

## 📦 What This Project Does

- Extracts data from CSVs (users, products, orders)
- Pulls real-time currency exchange rates via API
- Enriches order data with GBP-converted values
- Loads everything into a SQLite database
- Exports the final dataset for use in Power BI
- Delivers a fully interactive BI dashboard with KPIs

---

## 🛠 Technologies Used

- **Python** (ETL scripting, pandas, requests)
- **SQLite** (database storage and queries)
- **SQL** (data enrichment and aggregation)
- **Power BI** (visualization and dashboarding)
- **REST API** ([Frankfurter.app](https://www.frankfurter.app/)) for live currency rates

---

## 📁 Project Structure
ecommerce-analytics-pipeline/

├── etl/
│ └── etl_pipeline.py # Runs the full data pipeline
├── analysis/
│ └── analysis_queries.py # SQL queries for insights
├── dashboard/
│ ├── orders_enriched.csv # Final export for Power BI
│ └── ecommerce_dashboard.pbix # Power BI dashboard file
├── data/
│ ├── users.csv # User info including currency
│ ├── products.csv # Product catalog
│ └── orders.csv # Raw orders
├── sql/
│ └── schema.sql # Database table definitions
├── ecommerce.db # SQLite database (generated)
└── README.md


The Power BI dashboard includes:

- 💷 **Total Sales in GBP** (KPI card)
- 🌍 **Total Spent by Country** (bar chart)
- 🕒 **Order Volume Over Time** (line chart)
- 📦 **Top Products by Revenue** (table)

### 📥 [Download Dashboard (.pbix)](dashboard/ecommerce_dashboard.pbix) -----------------------------------------------------------------------

---

## 🚀 How to Run This Project

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/ecommerce-analytics-pipeline.git

2. Run The ETL script:
    python etl/etl_pipeline.py

3. Run SQL queries and view insights:
    python analysis/analysis_queries.py


