Supply Chain Performance Analytics

Project Overview

Supply Chain Performance Analytics is an end-to-end data analytics project designed to analyze operational performance across the supply chain ecosystem. The project combines Python, SQL, Excel, and Power BI to transform raw supply chain data into actionable business insights.

The objective of this project is to evaluate revenue generation, supplier contribution, warehouse utilization, inventory management, shipping performance, and fulfillment efficiency to support data-driven decision making.

---

Business Problem

Organizations generate thousands of supply chain transactions every day. Without proper analysis, businesses face challenges such as:

- Delivery delays
- High shipping costs
- Inventory imbalances
- Supplier inefficiencies
- Warehouse underutilization
- Reduced profitability

This project addresses these challenges through data analysis and KPI monitoring.

---

Project Objectives

The primary objectives are:

- Analyze revenue performance.
- Monitor operational KPIs.
- Evaluate supplier contribution.
- Measure warehouse efficiency.
- Improve inventory visibility.
- Track fulfillment performance.
- Support business decision making.

---

Dataset Information

The project contains multiple datasets:

Orders Dataset

- Order ID
- Product ID
- Supplier ID
- Warehouse ID
- Order Date
- Delivery Date
- Quantity
- Unit Price
- Shipping Cost
- Order Status

Products Dataset

Contains product-level information.

Suppliers Dataset

Contains supplier information.

Warehouses Dataset

Contains warehouse information.

Inventory Dataset

Contains inventory records and stock levels.

---

Tools & Technologies

Tool| Purpose
Python| Data Cleaning & Analysis
Pandas| Data Manipulation
NumPy| Numerical Operations
SQL| Business Analytics Queries
Excel| Data Validation
Power BI| Dashboard Development
Matplotlib| Data Visualization
GitHub| Project Management

---

Project Architecture

Raw Data

↓

Data Cleaning

↓

Exploratory Data Analysis

↓

KPI Development

↓

SQL Analytics

↓

Business Insights

↓

Dashboard Design

↓

Strategic Recommendations

---

Data Cleaning

The data cleaning process includes:

- Missing Value Analysis
- Duplicate Removal
- Data Type Conversion
- Revenue Calculation
- Delivery Time Calculation
- Data Standardization

Python Script:

src/data_cleaning.py

---

Exploratory Data Analysis

EDA focuses on identifying trends and patterns.

Analysis Areas:

- Revenue Analysis
- Product Performance
- Supplier Performance
- Warehouse Performance
- Monthly Trends
- Order Status Analysis

Python Script:

src/eda.py

---

KPI Analysis

Key Performance Indicators developed:

Revenue KPIs

- Total Revenue
- Revenue by Product
- Revenue by Supplier

Operational KPIs

- Total Orders
- Fulfillment Rate
- Average Delivery Time

Cost KPIs

- Total Shipping Cost
- Average Shipping Cost

Python Script:

src/kpi_analysis.py

---

SQL Analytics

The project includes 30+ SQL business queries.

Analysis Areas:

- Revenue Analysis
- Supplier Ranking
- Warehouse Performance
- Order Status Tracking
- Fulfillment Monitoring
- Shipping Cost Analysis
- Monthly Business Trends

SQL File:

sql/supply_chain_queries.sql

---

Business Insights

Business insights generated from the analysis include:

- Top revenue-generating products.
- Supplier contribution evaluation.
- Warehouse utilization assessment.
- Inventory optimization opportunities.
- Shipping cost reduction opportunities.
- Fulfillment performance monitoring.

Documentation:

docs/business_insights.md

---

Project Report

A detailed project report is included covering:

- Methodology
- KPIs
- Findings
- Recommendations
- Business Impact

Documentation:

docs/project_report.md

---

Key Findings

1. Revenue is concentrated among top-performing products.
2. Supplier performance varies significantly.
3. Warehouse utilization is uneven.
4. Shipping costs impact profitability.
5. Delivery performance directly affects customer satisfaction.
6. Inventory optimization can improve operational efficiency.

---

Strategic Recommendations

Short-Term

- Reduce delivery delays.
- Monitor supplier performance.
- Improve order fulfillment tracking.

Medium-Term

- Improve inventory planning.
- Balance warehouse utilization.
- Develop supplier scorecards.

Long-Term

- Implement predictive analytics.
- Deploy automated KPI monitoring.
- Develop demand forecasting models.

---

Folder Structure

Supply-Chain-Performance-Analytics
│
├── docs
│   ├── business_insights.md
│   └── project_report.md
│
├── sql
│   └── supply_chain_queries.sql
│
├── src
│   ├── data_cleaning.py
│   ├── eda.py
│   └── kpi_analysis.py
│
├── orders.csv
├── products.csv
├── suppliers.csv
├── inventory.csv
├── warehouses.csv
│
├── requirements.txt
│
└── README.md

---

Future Improvements

Future enhancements may include:

- Machine Learning Forecasting
- Inventory Optimization Models
- Demand Prediction
- Supplier Risk Scoring
- Real-Time Dashboard Integration
- Automated Reporting Pipelines

---

Business Impact

This project demonstrates how analytics can improve:

- Revenue Visibility
- Inventory Management
- Supplier Performance
- Warehouse Efficiency
- Operational Decision Making
- Customer Satisfaction

---

Author

Shivam Adhana

Data Analyst | Python | SQL | Power BI | Excel

GitHub Repository:
Supply-Chain-Performance-Analytics
