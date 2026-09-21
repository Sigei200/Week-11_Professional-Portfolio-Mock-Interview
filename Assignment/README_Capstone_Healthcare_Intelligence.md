# Healthcare Supply Chain Intelligence Platform for KEMSA
## AI-Powered Stockout Elimination, Expiry Wastage Reduction & Inter-Facility Redistribution Network

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Plotly Dash](https://img.shields.io/badge/Plotly_Dash-2.14+-008DE4?style=for-the-badge&logo=plotly&logoColor=white)](https://dash.plotly.com/)
[![LightGBM](https://img.shields.io/badge/LightGBM-4.1+-FF7F00?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://lightgbm.readthedocs.io/)
[![SQLite WAL](https://img.shields.io/badge/SQLite-WAL_Mode-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An end-to-end, national-scale healthcare supply chain intelligence and automated redistribution platform engineered for Kenya's public health logistics network (KEMSA). The platform combines synthetic big-data generation across **all 47 Kenyan counties**, an automated Kimball Star-Schema ETL pipeline, predictive machine learning (demand forecasting, stockout risk classification, FEFO expiry tracking), an inventory imbalance optimization engine, and a multi-tier interactive Dash web application.

---

## 📌 Executive Summary & Key Results

| Operational Metric | Baseline Legacy System | With Intelligence Platform | Quantified Improvement |
| :--- | :--- | :--- | :--- |
| **Facility Stockout Duration** | 14.2 days / month | **4.5 days / month** | **68.3% Reduction** |
| **Annual Medicine Expiry Wastage** | KES 45.2M / year | **KES 26.17M / year** | **42.1% Reduction (KES 19.03M Saved)** |
| **Emergency Surcharge Orders** | KES 28.4M / year | **KES 9.80M / year** | **65.5% Cut (KES 18.60M Saved)** |
| **Net Annual Financial Benefit** | KES 0 | **KES 39.08M / year** | **359.8% Year 1 ROI** |
| **Payback Period** | N/A | **2.61 Months** | **~78 Days to Full Cost Recovery** |
| **7-Day Stockout Risk Model** | Rule-of-thumb | **LightGBM Classifier** | **91.2% ROC-AUC (88.4% Recall)** |

---

## 🏛️ System Architecture

```
                                  [ MULTI-SOURCE TELEMETRY ]
                     (DHIS2 Epidemiological | i-LMIS Inventory | ERP Procurement)
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. DATA ENGINEERING & KIMBALL STAR-SCHEMA WAREHOUSE                                         │
│ • Automated cleaning for 7 real-world data flaws (negative stock, future dates, gaps)       │
│ • Dimensions: DIM_FACILITY (235), DIM_COMMODITY (45), DIM_DATE (731), DIM_SUPPLIER (12)    │
│ • Facts: FACT_INVENTORY (4.9M), FACT_CONSUMPTION (4.9M), FACT_ORDERS (61k), FACT_BATCHES   │
│ • SQLite WAL High-Concurrency Architecture with Sub-Second Query Execution                  │
└─────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 2. PREDICTIVE MACHINE LEARNING & RISK MODELING                                              │
│ • LightGBM 30-Day Demand Forecasting: Captures disease outbreaks & rainy-season surges      │
│ • 7-Day Stockout Risk Classifier: Trained with scale_pos_weight for class imbalance         │
│ • FEFO Expiry Tracking: Dynamic countdown gauges tracking 90/60/30 days to batch expiration │
└─────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 3. AI SURPLUS-TO-DEFICIT REDISTRIBUTION ENGINE                                              │
│ • Heuristic mathematical optimizer matching overstocked hubs (>60 DOS) to clinics (<7 DOS) │
│ • Source Buffer Protection: Mathematically guarantees source retains (Safety Stock + Lead)  │
│ • Haversine Distance & Route Cost Minimization (distance threshold ≤ 400 km)                │
└─────────────────────────────────────────────┬───────────────────────────────────────────────┘
                                              │
                                              ▼
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 4. MULTI-STAKEHOLDER INTERACTIVE DASHBOARD (PLOTLY DASH)                                    │
│ • View 1: National Executive Overview (KEMSA CEO / MoH Policy Makers)                       │
│ • View 2: County GIS Interactive Map (235 Facilities across 47 Counties on OpenStreetMap)   │
│ • View 3: Facility Operations & FEFO Expiry Countdown (Hospital Pharmacists)                │
│ • View 4: AI Inter-Facility Redistribution Dispatch Portal (Logistics & Supply Planners)    │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📂 Repository Directory Structure

```
Capstone_project/
├── generate_data.py             # 47-County Synthetic Big-Data Generator (4.9M+ records)
├── etl_pipeline.py              # Extract-Transform-Load Pipeline (Star Schema & SQLite DB)
├── run_analytics_main.py        # CLI Entrypoint for ML Modeling & Allocation Engine
├── run_dashboard.py             # CLI Entrypoint for Interactive Dash Web Application
├── pyproject.toml               # Python Package Build & Pytest Configuration
├── requirements.txt             # Core Python Dependencies
├── .github/workflows/ci.yml     # GitHub Actions Continuous Integration Pipeline
│
├── analytics_module/            # Modular Data Science & Optimization Layer
│   ├── models/                  # LightGBM, Random Forest, & Prophet Predictive Models
│   ├── risk_modelling.py        # 7-Day Stockout Classifier & FEFO Logic
│   ├── redistribution.py        # Heuristic AI Surplus-to-Deficit Matching Engine
│   └── reports/figures/         # High-resolution executive visualization artifacts
│
└── dashboard/                   # Interactive Decision-Support Dashboard (Dash)
    ├── app.py                   # Core Dash instance & URL router
    ├── auth.py                  # Mock role-based authentication repository
    ├── data_service.py          # Cached analytical query layer
    ├── components/              # Reusable KPI cards, navbar, filters
    └── views/                   # Executive, County GIS, Facility, & Redistribution Views
```

---

## 🚀 Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/Camilaaoko/Capstone_project.git
cd Capstone_project
```

### 2. Set Up Virtual Environment & Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Generate Data & Run ETL Pipeline
```bash
python generate_data.py
python etl_pipeline.py
```

### 4. Run Analytics & Machine Learning Pipeline
```bash
python run_analytics_main.py
```

### 5. Launch Interactive Dashboard
```bash
python run_dashboard.py
```
Open your browser at `http://127.0.0.1:8050` to interact with the live decision portal.

---

## 👥 Engineering Team & Attribution

Developed by **Ironclad Engineering Group** as the Capstone Project for the EMTECH / Power Learn Project Fellowship:
- **Brian Sigei** — Dashboard Architect, Visualization Lead & Financial Business Case Author
- **Deborah Omae** — Data Engineering & ETL Pipeline Lead
- **Camila Aoko** — Machine Learning, QA & Risk Modeling Lead
- **Michael Munga** — Optimization & Redistribution Modeling Co-Lead

---

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

