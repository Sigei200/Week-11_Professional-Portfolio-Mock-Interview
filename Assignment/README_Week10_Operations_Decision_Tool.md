# AI-Powered Operational Decision Tool & Supply Chain Optimization Suite
## Interactive Multi-Scenario Inventory Simulation, Supplier SLA Performance & Safety Stock Optimizer

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An interactive, multi-scenario operational decision-support tool engineered for supply chain directors, inventory planners, and procurement officers. The application allows stakeholders to stress-test replenishment policies, simulate supplier lead-time shocks, evaluate vendor SLA reliability scores, and dynamically optimize safety stock levels against holding vs. stockout penalty trade-offs.

---

## 📌 Key Capabilities & Features

### 1. Dynamic Safety Stock & Reorder Point (ROP) Calculator
- Incorporates demand uncertainty ($\sigma_D$) and lead-time variability ($\sigma_{LT}$) under normal and log-normal distributions.
- Configurable service levels ($90\%$, $95\%$, $99\%$) with instant holding cost vs. stockout risk curves.

### 2. Multi-Vendor SLA & Lead-Time Variance Tracker
- Ingests delivery histories across 12 primary suppliers.
- Computes vendor on-time delivery rate (OTD), fulfillment fill-rate, and lead-time deviation penalties.

### 3. Interactive Scenario Simulation Engine
- Stress-tests supply chain networks against simulated Black Swan disruptions (e.g., port strikes, seasonal disease surges, transit delays).
- Visualizes daily stock trajectory and buffer breach probabilities over 30/60/90-day simulation horizons.

---

## 🏗️ Architecture & Component Flow

```
[ Historical Inbound & Consumption Logs ]
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│ INVENTORY OPTIMIZATION ENGINE                               │
│ • Economic Order Quantity (EOQ) Calculation                 │
│ • Dynamic Safety Stock: SS = Z × sqrt(L*sD^2 + D^2*sL^2)    │
│ • Service-Level Cost Optimization Curves                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ REACTIVE DASHBOARD INTERFACE (STREAMLIT / DASH)             │
│ • Parameter Tuning Sliders (Lead Time, Service Level, Cost) │
│ • Monte Carlo Simulation Graphs (1,000 runs)                │
│ • Turnkey Purchase Order Generation & Rebalancing Alerts    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/Sigei200/Week-10_AI-Powered-Operational-Tool-Product-Dem.git
cd Week-10_AI-Powered-Operational-Tool-Product-Dem

# Install dependencies
pip install -r requirements.txt

# Launch interactive tool
streamlit run week10_ops_tool/app.py
```

---

## 👤 Author
**Brian Sigei** — *Operational Data Analyst & Analytics Engineer*  
GitHub: [@Sigei200](https://github.com/Sigei200) | LinkedIn: [brian-sigei-58a590288](https://www.linkedin.com/in/brian-sigei-58a590288)

