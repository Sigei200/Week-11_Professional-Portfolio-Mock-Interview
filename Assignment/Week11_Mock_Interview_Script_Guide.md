# Week 11 Mock Interview Master Script & Highlight Reel Guide

**Candidate:** Brian Sigei  
**Target Role:** Operational Data Analyst & Analytics Engineer  
**Interview Scenario:** 30-Minute Executive Board Pitch & Technical Cross-Examination  
**Focus Area:** KEMSA Healthcare Supply Chain Intelligence & Redistribution Platform  
**Video File Deliverable:** `Week11_Mock_Interview.mp4`

---

## 📋 Interview Structure & Time Allocation

| Section | Topic & Focus Area | Duration | Objective |
| :--- | :--- | :--- | :--- |
| **Part 1** | **Executive Introduction & Career Narrative** | 00:00 - 05:30 | Establish professional identity, domain expertise, and executive communication. |
| **Part 2** | **Data Engineering & Kimball Star Schema** | 05:31 - 12:45 | Defend data pipeline scalability, cleaning rules for 4.9M records, and SQLite WAL speed. |
| **Part 3** | **Machine Learning & Class Imbalance Defense** | 12:46 - 19:15 | Explain LightGBM algorithm choice, `scale_pos_weight`, and 91.2% ROC-AUC evaluation. |
| **Part 4** | **Operational Problem Solving & Optimization** | 19:16 - 25:00 | Justify AI surplus-to-deficit redistribution, Haversine routing, and safety stock guards. |
| **Part 5** | **CFO Business Case Defense & "GO" Ask** | 25:01 - 30:00 | Walk through financial math: 2.6-month payback, 359.8% ROI, KES 39.08M net savings. |

---

## 🎙️ Complete Transcript & STAR Method Model Answers

### Part 1: Executive Introduction & Career Narrative (00:00 - 05:30)

**Interviewer:**  
> *"Brian, welcome. To start us off, please introduce yourself and walk us through the capstone analytics project you led for Kenya's healthcare supply chain."*

**Brian Sigei (Response):**  
> *"Thank you. I am an Operational Data Analyst and Analytics Engineer with a background in software systems and operations research. My core passion lies at the intersection of high-frequency data engineering, predictive machine learning, and C-suite financial decision-making.*  
>  
> *In Kenya's public health sector, we observed a devastating dual crisis: Level 2 and 3 rural dispensaries face a 30%+ average stockout duration for essential antibiotics and antimalarials, while regional referral hospitals simultaneously incur KES 45.2M annually in expired medicines.*  
>  
> *As the analytics engineering and visualization lead for the Ironclad team, I architected the **Healthcare Supply Chain Intelligence Platform**. Our system ingests 4.9M daily transaction records across all 47 counties, models 7-day stockout risks using LightGBM with 91.2% ROC-AUC, and deploys an AI redistribution engine that cut stockout durations by 68.3%, generating KES 39.08M in annual net recurring savings with a 2.6-month payback period."*

---

### Part 2: Data Engineering & Star Schema Architecture (05:31 - 12:45)

**Interviewer:**  
> *"Operating across 47 counties means dealing with paper registries, missing entries, and delayed reporting. How did your data pipeline handle these real-world data flaws?"*

**Brian Sigei (Response):**  
> *"We designed a Kimball Star-Schema Data Warehouse comprising 5 Dimension tables and 6 Star Fact tables running in SQLite WAL (Write-Ahead Logging) mode for zero-lock analytical concurrency.*  
>  
> *To guarantee referential integrity and reliability, we implemented automated transformation rules for 7 real-world data flaws:*  
> 1. **Negative Stock Imputation:** Reconciled negative entries back to physical batch balances.  
> 2. **Temporal Validation:** Stripped future-dated transactions and corrected 14-day reporting lags.  
> 3. **Missing Consumption Imputation:** Derived missing daily consumption logs by multiplying sub-county patient visit demand indices against commodity median utilization rates.  
> 4. **Pre-Aggregated KPI Tables:** Pre-computed multi-dimensional aggregations so our executive Dash interface renders complex geographic queries in under 200 milliseconds."*

---

### Part 3: Machine Learning & Class Imbalance (12:46 - 19:15)

**Interviewer:**  
> *"Why did you select LightGBM over standard time-series or deep learning models, and how did you tackle the severe class imbalance in stockouts?"*

**Brian Sigei (Response):**  
> *"We selected LightGBM (Gradient Boosting Decision Trees) for three operational reasons:*  
> 1. **Histogram-Based Efficiency:** Enabled rapid training across hundreds of individual facility-commodity pairs without GPU bottlenecks.  
> 2. **Native Categorical & Non-Linear Handling:** Efficiently ingested tabular facility tiers, county regions, and supplier reliability ratings without exploding one-hot encoding dimensionalities.  
> 3. **Native Class Imbalance Weighting:** In healthcare supply chains, stockouts represent a critical minority class (~3-8% of daily records). Standard accuracy is a misleading metric. We utilized `scale_pos_weight = n_negative / n_positive` to heavily penalize False Negatives (missed stockouts) and tuned decision thresholds using F1-maximization on validation sets.  
>  
> *This achieved **91.2% ROC-AUC and 88.4% Recall**. Interestingly, feature importance analysis revealed that Days-of-Stock (DOS) and supplier reliability scores were substantially stronger predictors of impending stockouts than historical consumption lags."*

---

### Part 4: Algorithmic Optimization & Logistics (19:16 - 25:00)

**Interviewer:**  
> *"Stock redistribution sounds great in theory, but what prevents a donor hospital from running out of medicines after transferring stock to a clinic?"*

**Brian Sigei (Response):**  
> *"That was our primary engineering constraint. We formulated a **5-step heuristic optimization algorithm** with hard mathematical safeguards:*  
> 1. **Source Safety Stock Guarantee:** Before a facility is classified as a surplus candidate, the algorithm calculates its projected consumption over `(Safety Stock Days + Supplier Lead Time Days)`. Stock is only marked as surplus if the current inventory exceeds this dynamic threshold (typically $>60$ DOS).  
> 2. **FEFO Priority Matching:** The algorithm specifically targets batches with 30-90 days remaining shelf life for transfer.  
> 3. **Haversine Distance & Route Minimization:** Surplus hubs are paired with deficit facilities ($<7$ DOS) within a 400km radius, comparing the localized transport cost against emergency catalog surcharges.  
>  
> *Across our simulations, this eliminated 100% of donor secondary depletion incidents while cutting emergency replenishment surcharges by 65.5%."*

---

### Part 5: CFO Business Case Defense & Strategic "GO" Ask (25:01 - 30:00)

**Interviewer:**  
> *"As CFO, I care about cash flow and payback. Walk us through the financial math. Why should the Board approve KES 8.5M for this project today?"*

**Brian Sigei (Response):**  
> *"Here is the exact financial breakdown:*  
>  
> 1. **Annual Gross Savings:**  
>    • Expiry wastage reduction (42.1% cut on KES 45.2M baseline): **+ KES 19.03M**  
>    • Emergency replenishment surcharge elimination (65.5% replacement): **+ KES 18.60M**  
>    • Holding cost optimization: **+ KES 4.25M**  
>    • **Total Gross Savings:** **KES 41.88M / year**  
>  
> 2. **Net Operating Cash Flow:**  
>    • Deducting annual cloud and maintenance opex of KES 2.80M yields a **Net Annual Benefit of KES 39.08M / year**.  
>  
> 3. **Payback Period Math:**  
>    $$\text{Payback Period} = \frac{\text{Capex}}{\text{Annual Net Cash Inflow}} \times 12 = \frac{\text{KES } 8.50\text{M}}{\text{KES } 39.08\text{M}} \times 12 = \mathbf{2.61\text{ Months}}$$  
>    *The entire capital investment is fully recouped in approximately 78 operating days.*  
>  
> 4. **Year 1 Net ROI:**  
>    $$\text{ROI} = \frac{39.08\text{M} - 8.50\text{M}}{8.50\text{M}} \times 100\% = \mathbf{359.8\%}$$  
>    *With a 3-Year NPV of **KES 85.34M** at a 12% discount rate and an IRR of **428%**.*  
>  
> *Our recommendation is an immediate, unanimous **'GO' decision** to authorize KES 8.50M for the Q1 10-county pilot, unlocking self-funding operational savings with zero clinical workflow disruption."*

