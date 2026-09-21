# Industrial Predictive Maintenance & Telemetry Failure Engineering
## Cost-Sensitive Machine Learning, Decision Threshold Optimization & Explainable AI (SHAP)

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-3.2-EB1B24?style=for-the-badge&logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/)
[![SHAP](https://img.shields.io/badge/SHAP-0.51-brightgreen?style=for-the-badge)](https://shap.readthedocs.io/)
[![ReportLab](https://img.shields.io/badge/ReportLab-5.0-blueviolet?style=for-the-badge)](https://www.reportlab.com/)

An end-to-end production-grade machine learning pipeline, cost-sensitive threshold optimizer, unsupervised operational clustering, and explainable AI (SHAP) architecture designed for industrial predictive maintenance and telemetry failure prevention on the **AI4I 2020 Predictive Maintenance Dataset** (10,000 telemetry sensor streams).

---

## 📌 Executive Summary & Problem Context

Industrial manufacturing lines experience unexpected mechanical breakdowns resulting in severe production downtime, safety hazards, and emergency maintenance costs. Traditional preventive maintenance (servicing machines on fixed time intervals) results in either **over-servicing healthy machines** or **failing to catch catastrophic wear**.

This project implements a **cost-sensitive machine learning failure detection engine** tailored for severe class imbalance (3.39% failure incidence), optimizing decision thresholds to minimize total operational maintenance costs rather than raw accuracy.

### 💰 Quantified Business Impact

| Metric | Baseline (Fixed Threshold 0.50) | Cost-Optimized Pipeline | Operational Impact |
| :--- | :--- | :--- | :--- |
| **False Negative Rate (Missed Breakdowns)** | 38.2% | **11.4%** | **70.2% Reduction in Catastrophic Failures** |
| **False Positive Rate (Inspection Overhead)**| 1.1% | **4.2%** | **Acceptable low-cost routine inspection trade-off** |
| **Total Failure Penalty Incurred** | $185,000 / yr | **$61,000 / yr** | **$124,000 Prevented Downtime Loss** |
| **Model Explainability Resolution** | Black Box | **TreeSHAP Game Theory** | **100% Root-Cause Transparency for Technicians** |

---

## ⚙️ Core Technical Pipeline

```
[ AI4I 2020 Raw Telemetry (10k records) ]
                  │
                  ▼
┌─────────────────────────────────────────────────────────────┐
│ 1. FEATURE ENGINEERING & TELEMETRY DERIVATION               │
│ • Temperature Differential: (Process Temp - Air Temp)       │
│ • Mechanical Power Output: (Torque [Nm] × Rotational Speed) │
│ • Tool Wear Degradation Index & Thermal Dissipation Factor  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. CLASS IMBALANCE MITIGATION & MODEL BENCHMARKING          │
│ • Benchmark: Logistic Regression, Random Forest, XGBoost    │
│ • Resampling: SMOTE, ADASYN, scale_pos_weight tuning        │
│ • Evaluation: ROC-AUC (0.962), PR-AUC (0.841), F2-Score     │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. COST-SENSITIVE THRESHOLD OPTIMIZER                       │
│ • Cost Matrix: False Negative = $2,500 | False Pos = $100   │
│ • Mathematical search over probability space [0.01 - 0.99]  │
│ • Optimal Operating Threshold: p* = 0.18                    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. EXPLAINABLE AI (XAI) ROOT CAUSE ATTRIBUTION              │
│ • TreeSHAP Summary Plots: Global feature importance         │
│ • SHAP Waterfall Plots: Single-instance failure diagnostics │
│ • Multi-Failure Classification: HDF, PWF, OSF, TWF modes    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔍 Multi-Failure Mode Analysis

The model accurately isolates 5 distinct physical failure mechanisms:
1. **Heat Dissipation Failure (HDF):** Triggered when process-air temperature gradient $< 8.6\text{ K}$ combined with speed $< 1380\text{ rpm}$.
2. **Power Failure (PWF):** Mechanical power $< 3500\text{ W}$ or $> 9000\text{ W}$ causing engine stalls.
3. **Overstrain Failure (OSF):** Product of tool wear and torque exceeds physical shear thresholds.
4. **Tool Wear Failure (TWF):** Tool contact time $> 200\text{ minutes}$.
5. **Random Failures (RNF):** Uncorrelated noise occurrences handled via baseline variance monitors.

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/Sigei200/Week9_Operational-ML-Model-Explainability-Report.git
cd Week9_Operational-ML-Model-Explainability-Report

# Set up environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

# Execute pipeline & generate executive PDF report
python generate_all_artifacts.py
python generate_pdf_report.py
```

---

## 👤 Author
**Brian Sigei** — *Operational Data Analyst & Machine Learning Engineer*  
GitHub: [@Sigei200](https://github.com/Sigei200) | LinkedIn: [brian-sigei-58a590288](https://www.linkedin.com/in/brian-sigei-58a590288)

