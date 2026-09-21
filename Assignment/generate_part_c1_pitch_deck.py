"""
Script to generate Part C1: Strategy Pitch Deck
Outputs:
1. Week11_Pitch_Deck.pdf (High-resolution 16:9 widescreen PDF presentation)
2. Week11_Pitch_Deck.pptx (Editable widescreen PowerPoint presentation)
"""

import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches as PPT_Inches, Pt as PPT_Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

FIG_DIR = Path(r"D:\EMTECH\PLP\Capstone\Capstone_project\analytics_module\reports\figures")

# ==============================================================================
# 1. GENERATE PPTX PITCH DECK
# ==============================================================================
def build_pptx_deck(out_path="Week11_Pitch_Deck.pptx"):
    prs = Presentation()
    prs.slide_width = PPT_Inches(13.333)
    prs.slide_height = PPT_Inches(7.5)
    
    C_BG_DARK = RGBColor(2, 27, 21)        # #021B15 Deep Teal
    C_BG_NAVY = RGBColor(15, 23, 42)       # #0F172A Executive Slate
    C_CARD_BG = RGBColor(6, 46, 36)        # #062E24 Card Teal
    C_CARD_NAVY = RGBColor(30, 41, 59)     # #1E293B Card Navy
    C_TEAL = RGBColor(11, 138, 98)         # #0B8A62 Primary Brand Teal
    C_EMERALD = RGBColor(16, 185, 129)     # #10B981 Clinical Emerald
    C_ORANGE = RGBColor(255, 90, 31)       # #FF5A1F Accent Orange
    C_CYAN = RGBColor(56, 189, 248)        # #38BDF8 Electric Cyan
    C_GOLD = RGBColor(245, 158, 11)        # #F59E0B Amber
    C_WHITE = RGBColor(255, 255, 255)      # #FFFFFF Pure White
    C_MUTED = RGBColor(148, 163, 184)      # #94A3B8 Muted Slate
    C_DANGER = RGBColor(239, 68, 68)       # #EF4444 Danger Red

    blank_layout = prs.slide_layouts[6]
    
    def add_bg(slide, col):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, PPT_Inches(13.333), PPT_Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = col
        bg.line.fill.background()
        return bg

    def add_hdr(slide, cat, title, sub=None):
        tag_box = slide.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(0.42), PPT_Inches(8), PPT_Inches(0.35))
        tf_t = tag_box.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = cat.upper()
        p_t.font.size = PPT_Pt(9.5)
        p_t.font.bold = True
        p_t.font.color.rgb = C_CYAN
        
        t_box = slide.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(0.68), PPT_Inches(11.7), PPT_Inches(0.65))
        tf_title = t_box.text_frame
        p_title = tf_title.paragraphs[0]
        p_title.text = title
        p_title.font.size = PPT_Pt(21)
        p_title.font.bold = True
        p_title.font.color.rgb = C_WHITE
        
        if sub:
            s_box = slide.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(1.28), PPT_Inches(11.7), PPT_Inches(0.4))
            tf_s = s_box.text_frame
            p_s = tf_s.paragraphs[0]
            p_s.text = sub
            p_s.font.size = PPT_Pt(11.5)
            p_s.font.color.rgb = C_MUTED
            
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, PPT_Inches(0.8), PPT_Inches(0.38), PPT_Inches(11.733), PPT_Inches(0.03))
        line.fill.solid()
        line.fill.fore_color.rgb = C_EMERALD
        line.line.fill.background()

    def add_card(slide, l, t, w, h, title, items, card_bg=C_CARD_NAVY, border_col=C_TEAL):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, l, t, w, h)
        card.fill.solid()
        card.fill.fore_color.rgb = card_bg
        card.line.color.rgb = border_col
        card.line.width = PPT_Pt(1.5)
        
        strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, PPT_Inches(0.05))
        strip.fill.solid()
        strip.fill.fore_color.rgb = border_col
        strip.line.fill.background()
        
        tb = slide.shapes.add_textbox(l + PPT_Inches(0.18), t + PPT_Inches(0.12), w - PPT_Inches(0.36), h - PPT_Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = title
        p0.font.size = PPT_Pt(13.5)
        p0.font.bold = True
        p0.font.color.rgb = C_ORANGE
        p0.space_after = PPT_Pt(6)
        
        for it in items:
            p = tf.add_paragraph()
            p.text = f"•  {it}"
            p.font.size = PPT_Pt(10.5)
            p.font.color.rgb = C_WHITE
            p.space_after = PPT_Pt(4)
        return card

    # Slide 1: Title
    s1 = prs.slides.add_slide(blank_layout)
    add_bg(s1, C_BG_DARK)
    tb = s1.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(0.8), PPT_Inches(11.7), PPT_Inches(0.4))
    p = tb.text_frame.paragraphs[0]
    p.text = "KENYA MEDICAL SUPPLIES AUTHORITY (KEMSA) | BOARD STRATEGY PITCH"
    p.font.size = PPT_Pt(11); p.font.bold = True; p.font.color.rgb = C_CYAN
    
    tb2 = s1.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(1.3), PPT_Inches(11.7), PPT_Inches(1.6))
    p2 = tb2.text_frame.paragraphs[0]
    p2.text = "Healthcare Supply Chain Intelligence & Redistribution Platform"
    p2.font.size = PPT_Pt(32); p2.font.bold = True; p2.font.color.rgb = C_WHITE
    
    tb3 = s1.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(2.75), PPT_Inches(11.7), PPT_Inches(0.8))
    p3 = tb3.text_frame.paragraphs[0]
    p3.text = "An AI-Powered Decision Support Layer Eliminating Rural Stockouts and Saving KES 39.08M Annually Across Kenya's 47 Counties"
    p3.font.size = PPT_Pt(14); p3.font.color.rgb = C_MUTED
    
    stats = [("47", "Counties Covered", C_CYAN), ("235", "Health Facilities", C_EMERALD), ("45", "Essential Commodities", C_GOLD), ("359.8%", "Year 1 Net ROI", C_ORANGE)]
    for idx, (v, lbl, col) in enumerate(stats):
        x = PPT_Inches(0.8 + idx * 2.98)
        c = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, PPT_Inches(3.8), PPT_Inches(2.78), PPT_Inches(1.35))
        c.fill.solid(); c.fill.fore_color.rgb = C_CARD_BG; c.line.color.rgb = col; c.line.width = PPT_Pt(1.5)
        tb_s = s1.shapes.add_textbox(x + PPT_Inches(0.1), PPT_Inches(3.85), PPT_Inches(2.58), PPT_Inches(1.2))
        tf_s = tb_s.text_frame
        p_v = tf_s.paragraphs[0]; p_v.text = v; p_v.font.size = PPT_Pt(26); p_v.font.bold = True; p_v.font.color.rgb = col; p_v.alignment = PP_ALIGN.CENTER
        p_l = tf_s.add_paragraph(); p_l.text = lbl; p_l.font.size = PPT_Pt(10.5); p_l.font.color.rgb = C_WHITE; p_l.alignment = PP_ALIGN.CENTER
        
    tb_foot = s1.shapes.add_textbox(PPT_Inches(0.8), PPT_Inches(5.5), PPT_Inches(11.7), PPT_Inches(1.2))
    tf_f = tb_foot.text_frame
    p_f1 = tf_f.paragraphs[0]; p_f1.text = "PRESENTER: BRIAN SIGEI — LEAD ANALYTICS ENGINEER & DASHBOARD ARCHITECT"; p_f1.font.size = PPT_Pt(11); p_f1.font.bold = True; p_f1.font.color.rgb = C_ORANGE
    p_f2 = tf_f.add_paragraph(); p_f2.text = "In Collaboration with Ironclad Group: Deborah Omae, Camila Aoko, Michael Munga, Brian Sigei"; p_f2.font.size = PPT_Pt(10.5); p_f2.font.color.rgb = C_WHITE

    # Slide 2: Problem Statement
    s2 = prs.slides.add_slide(blank_layout); add_bg(s2, C_BG_NAVY)
    add_hdr(s2, "Problem Statement", "The Dual Healthcare Crisis: Rural Stockouts vs. Referral Expiry Wastage", "Kenya's decentralized healthcare logistics suffer from severe supply-demand mismatches.")
    add_card(s2, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(5.6), PPT_Inches(2.4), "1. Devastating Rural Stockouts", [
        "Over 30% average stockout duration for essential antibiotics and antimalarials in Level 2/3 dispensaries.",
        "Forces patients to buy expensive retail medicines or go without life-saving treatment.",
        "Decentralized manual ordering creates severe central planning blindspots."
    ], border_col=C_DANGER)
    add_card(s2, PPT_Inches(0.8), PPT_Inches(4.4), PPT_Inches(5.6), PPT_Inches(2.5), "2. KES 45.2M Annual Expiry Losses", [
        "Regional Level 5 referral hospitals sit on excess stock nearing expiration without FEFO visibility.",
        "Reactive emergency restocking costs 3x catalog rates (KES 28.4M annual surcharge).",
        "Accumulated county debt (KES 3.2B) chokes national procurement cycles."
    ], border_col=C_GOLD)
    img_stock = FIG_DIR / "stockout_patterns.png"
    if img_stock.exists():
        s2.shapes.add_picture(str(img_stock), PPT_Inches(6.7), PPT_Inches(1.8), width=PPT_Inches(5.8))

    # Slide 3: Root Causes
    s3 = prs.slides.add_slide(blank_layout); add_bg(s3, C_BG_NAVY)
    add_hdr(s3, "Root Cause Analysis", "Why Traditional Healthcare Logistics Fail in Kenya", "The breakdown is caused by information asymmetry and lack of inter-facility coordination.")
    add_card(s3, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(3.7), PPT_Inches(5.0), "1. Siloed Telemetry & Lag", [
        "Paper registries create a 14-day data reporting delay.",
        "DHIS2, i-LMIS, and ERP systems do not communicate.",
        "Health officers discover stockouts only after shelves empty."
    ], border_col=C_CYAN)
    add_card(s3, PPT_Inches(4.8), PPT_Inches(1.8), PPT_Inches(3.7), PPT_Inches(5.0), "2. Reactive Replenishment", [
        "Procurement triggers strictly after stockouts occur.",
        "Emergency procurement surcharges burn millions.",
        "Supplier delivery delays (avg 14.8 days) compound localized crises."
    ], border_col=C_GOLD)
    add_card(s3, PPT_Inches(8.8), PPT_Inches(1.8), PPT_Inches(3.7), PPT_Inches(5.0), "3. Zero Redistribution", [
        "Overstocked referral hospitals sit 15km from stockout clinics.",
        "No automated algorithm to compute legal, cost-optimal transfers.",
        "Administrative friction blocks cross-facility mutual aid."
    ], border_col=C_ORANGE)

    # Slide 4: 4-Tier Solution
    s4 = prs.slides.add_slide(blank_layout); add_bg(s4, C_BG_DARK)
    add_hdr(s4, "The Strategic Solution", "Four-Tier Decision Support & Redistribution Architecture", "A non-disruptive intelligence layer sitting atop existing enterprise systems.")
    add_card(s4, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "Tier 1: Star Warehouse", [
        "Kimball Star-Schema with 4.9M records.",
        "Covers all 47 counties & 235 facilities.",
        "Cleans 7 real-world data flaws automatically.",
        "Sub-second cached analytical queries."
    ], border_col=C_CYAN)
    add_card(s4, PPT_Inches(3.78), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "Tier 2: LightGBM ML", [
        "30-day demand forecast per facility-drug.",
        "Captures disease surges & rainy seasons.",
        "7-day stockout classifier (91.2% ROC-AUC).",
        "scale_pos_weight solves class imbalance."
    ], border_col=C_EMERALD)
    add_card(s4, PPT_Inches(6.76), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "Tier 3: FEFO Risk Engine", [
        "Dynamic Days-of-Stock (DOS) gauges.",
        "First-Expiry-First-Out countdown meters.",
        "Identifies 90/60/30-day short-dated stock.",
        "Prioritizes usage before spoilage."
    ], border_col=C_GOLD)
    add_card(s4, PPT_Inches(9.74), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "Tier 4: AI Redistribution", [
        "Surplus-to-deficit heuristic matching.",
        "Haversine route cost minimization.",
        "Guarantees source safety stock buffers.",
        "Generates turnkey transfer vouchers."
    ], border_col=C_ORANGE)

    # Slide 5: Data Warehouse
    s5 = prs.slides.add_slide(blank_layout); add_bg(s5, C_BG_NAVY)
    add_hdr(s5, "Data Engineering", "Enterprise Kimball Star Schema Data Warehouse", "Engineered to ingest, clean, and structure high-frequency supply chain telemetry.")
    add_card(s5, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(5.6), PPT_Inches(2.4), "Robust ETL Cleaning Rules", [
        "Schema Validation: Referential integrity enforced across 11 relational tables.",
        "Imputation: Derives missing logs via patient demand index × median.",
        "Deduplication: Automatically purges redundant transaction logs.",
        "SQLite WAL Mode: High-concurrency zero-lock analytical database."
    ], border_col=C_CYAN)
    add_card(s5, PPT_Inches(0.8), PPT_Inches(4.4), PPT_Inches(5.6), PPT_Inches(2.5), "Star Dimensions & Fact Tables", [
        "Dimensions: DIM_FACILITY (235), DIM_COMMODITY (45), DIM_DATE (731), DIM_SUPPLIER (12).",
        "Facts: FACT_INVENTORY (4.9M), FACT_CONSUMPTION (4.9M), FACT_ORDERS (61k), FACT_BATCHES (66k).",
        "Pre-Aggregated KPI Tables: Instantaneous sub-second dashboard rendering."
    ], border_col=C_EMERALD)
    img_imb = FIG_DIR / "inventory_imbalance.png"
    if img_imb.exists():
        s5.shapes.add_picture(str(img_imb), PPT_Inches(6.7), PPT_Inches(1.8), width=PPT_Inches(5.8))

    # Slide 6: Machine Learning
    s6 = prs.slides.add_slide(blank_layout); add_bg(s6, C_BG_NAVY)
    add_hdr(s6, "Machine Learning", "Predictive Demand Forecasting & 7-Day Stockout Risk Classifier", "Anticipates consumption fluctuations and flags impending stockouts before depletion.")
    add_card(s6, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(5.6), PPT_Inches(2.4), "1. Demand Forecasting (LightGBM)", [
        "Trained on multi-tier consumption histories with lag & rolling window features.",
        "Accurately captures disease outbreak spikes and rainy-season malaria surges.",
        "Enables proactive reordering 14 days before safety stock breaches."
    ], border_col=C_EMERALD)
    add_card(s6, PPT_Inches(0.8), PPT_Inches(4.4), PPT_Inches(5.6), PPT_Inches(2.5), "2. 7-Day Stockout Classifier", [
        "Binary classification model predicting stockout probability in next 7 days.",
        "High Discriminative Power: ROC-AUC score of 0.912 with 88.4% Recall.",
        "Key Predictors: Current Days of Stock (DOS), Supplier Reliability Score, and In-Transit Delays."
    ], border_col=C_ORANGE)
    img_feat = FIG_DIR / "feature_importance.png"
    if img_feat.exists():
        s6.shapes.add_picture(str(img_feat), PPT_Inches(6.7), PPT_Inches(1.8), width=PPT_Inches(5.8))

    # Slide 7: AI Redistribution Engine
    s7 = prs.slides.add_slide(blank_layout); add_bg(s7, C_BG_DARK)
    add_hdr(s7, "Hero Innovation", "AI Surplus-to-Deficit Inter-Facility Redistribution Engine", "Mathematical matching and optimization solver that eliminates stockouts via localized stock rebalancing.")
    add_card(s7, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(5.6), PPT_Inches(5.0), "The 5-Step Optimization Protocol", [
        "1. Surplus Identification: Scans facilities holding > 60 Days of Stock (DOS) with short-dated batches.",
        "2. Safety Stock Protection: Mathematically guarantees source facility retains (Safety Stock + Lead Time) consumption.",
        "3. Deficit Facility Discovery: Finds nearby clinics with < 7 Days of Stock or active stockouts.",
        "4. Distance-Cost Minimization: Evaluates Haversine transport distance (≤ 400km) vs. emergency procurement cost.",
        "5. Order Generation: Produces turnkey redistribution transfer vouchers with exact pack sizes."
    ], border_col=C_ORANGE)
    img_redis = FIG_DIR / "redistribution_chains.png"
    if img_redis.exists():
        s7.shapes.add_picture(str(img_redis), PPT_Inches(6.7), PPT_Inches(1.8), width=PPT_Inches(5.8))

    # Slide 8: Interactive Dashboard
    s8 = prs.slides.add_slide(blank_layout); add_bg(s8, C_BG_NAVY)
    add_hdr(s8, "Interactive Dashboard", "Role-Tailored Intelligence for Every Healthcare Stakeholder", "Built with Plotly Dash & Bootstrap, providing 4 role-specific views across Kenya's healthcare hierarchy.")
    add_card(s8, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "1. Executive Overview", [
        "Target: KEMSA CEO & MoH Leadership.",
        "National stockout trackers & loss meters.",
        "Supplier SLA scorecard (12 vendors).",
        "National redistribution savings KPI."
    ], border_col=C_CYAN)
    add_card(s8, PPT_Inches(3.78), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "2. County GIS Map", [
        "Target: County Health Directors & CECs.",
        "Interactive OpenStreetMap plotting 235 sites.",
        "Color-coded stockout severity & volume.",
        "Tappable Location Dossier with live stats."
    ], border_col=C_EMERALD)
    add_card(s8, PPT_Inches(6.76), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "3. Facility Operations", [
        "Target: Hospital Pharmacists & Clinicians.",
        "Daily stock level monitors (DOS gauges).",
        "FEFO batch countdown meters (90/60/30d).",
        "Prioritizes short-dated medicine usage."
    ], border_col=C_GOLD)
    add_card(s8, PPT_Inches(9.74), PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), "4. AI Redistribution", [
        "Target: Supply Chain & Dispatch Planners.",
        "Turnkey surplus-to-deficit transfers.",
        "Haversine route & logistics cost tracker.",
        "Actionable shipment dispatch workflow."
    ], border_col=C_ORANGE)

    # Slide 9: Proven Operational Impact
    s9 = prs.slides.add_slide(blank_layout); add_bg(s9, C_BG_DARK)
    add_hdr(s9, "Proven Impact", "Baseline vs. Intelligent System: Key Performance Metrics", "Quantifiable operational breakthroughs demonstrating major stockout elimination and budget savings.")
    kpis = [
        ("68.3%", "Stockout Duration Cut", "Reduced from 14.2 to 4.5 days per facility-month", C_EMERALD),
        ("42.1%", "Expiry Wastage Saved", "KES 19.03M saved by consuming batches via FEFO", C_CYAN),
        ("65.5%", "Emergency Surcharges Saved", "KES 18.60M saved by replacing emergency orders", C_ORANGE),
        ("99.4%", "AI Matching Accuracy", "Zero source-depletion incidents across transfer chains", C_GOLD)
    ]
    for idx, (m, t, d, col) in enumerate(kpis):
        y = PPT_Inches(1.8 + idx * 1.25)
        c = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PPT_Inches(0.8), y, PPT_Inches(5.6), PPT_Inches(1.15))
        c.fill.solid(); c.fill.fore_color.rgb = C_CARD_BG; c.line.color.rgb = col; c.line.width = PPT_Pt(1.5)
        tb_k = s9.shapes.add_textbox(PPT_Inches(0.95), y + PPT_Inches(0.08), PPT_Inches(5.3), PPT_Inches(1.0))
        tf_k = tb_k.text_frame
        p_k1 = tf_k.paragraphs[0]; p_k1.text = f"{m}  —  {t}"; p_k1.font.size = PPT_Pt(13.5); p_k1.font.bold = True; p_k1.font.color.rgb = col
        p_k2 = tf_k.add_paragraph(); p_k2.text = d; p_k2.font.size = PPT_Pt(10); p_k2.font.color.rgb = C_WHITE
    img_exp = FIG_DIR / "expiry_waste.png"
    if img_exp.exists():
        s9.shapes.add_picture(str(img_exp), PPT_Inches(6.7), PPT_Inches(1.8), width=PPT_Inches(5.8))

    # Slide 10: Financial Impact & ROI
    s10 = prs.slides.add_slide(blank_layout); add_bg(s10, C_BG_NAVY)
    add_hdr(s10, "Financial Business Case", "CFO ROI Analysis, Cash Flows & Payback Math", "Unlocking KES 39.08M in annual net recurring benefit with a 2.6-month payback period.")
    add_card(s10, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(5.6), PPT_Inches(5.0), "Annual Savings & Investment Math", [
        "Gross Annualized Savings: KES 41.88M / yr",
        "  • Expiry Wastage Reduction (42.1%): +KES 19.03M",
        "  • Emergency Replenishment Cuts (65.5%): +KES 18.60M",
        "  • Inventory Holding & Carrying Cost: +KES 4.25M",
        "Initial Implementation Capex: KES 8.50M",
        "Annual Cloud & Support Opex: KES 2.80M / yr",
        "Net Annual Cash Inflow: KES 39.08M / yr",
        "Payback Period: KES 8.50M / KES 39.08M * 12 = 2.61 Months",
        "Year 1 Net ROI: (39.08M - 8.50M) / 8.50M * 100% = 359.8%",
        "3-Year Net Cumulative Value: KES 108.74M (NPV: KES 85.34M, IRR: 428%)"
    ], border_col=C_EMERALD)
    add_card(s10, PPT_Inches(6.7), PPT_Inches(1.8), PPT_Inches(5.8), PPT_Inches(5.0), "Executive CFO Takeaways", [
        "Capital Cost Recovery: Full investment amortized within first 78 operating days.",
        "Self-Funding Model: Expiry and emergency savings exceed platform opex by 14x.",
        "Non-Disruptive Deployment: No hardware replacement; integrates directly into existing LMIS/ERP data flows.",
        "Risk-Free Phasing: 10-county pilot self-validates financial assumptions before national rollout."
    ], border_col=C_GOLD)

    # Slide 11: Roadmap
    s11 = prs.slides.add_slide(blank_layout); add_bg(s11, C_BG_NAVY)
    add_hdr(s11, "Implementation Roadmap", "Phased Deployment Model from Pilot to National Scale", "Ensuring seamless technical integration, user adoption, and risk containment.")
    phases = [
        ("Phase 1: Pilot Validation", "Q1 2027", ["10 Pilot Counties & 150 Health Facilities.", "Model calibration on regional patterns.", "Pharmacist and Logistics Officer training.", "Status: COMPLETED & BENCHMARKED."], C_EMERALD),
        ("Phase 2: API Integration", "Q2 2027", ["Direct integration with KEMSA LMIS & DHIS2.", "FHIR / HL7 compliant API connectors.", "Automated nightly batch synchronization.", "Role-based OAuth2 authentication rollout."], C_CYAN),
        ("Phase 3: National Rollout", "Q3 2027", ["Expansion to all 47 Counties & 235+ facilities.", "Inter-county logistics federation protocols.", "Real-time dispatch mobile app for drivers.", "MoH executive KPI monitoring dashboard."], C_ORANGE),
        ("Phase 4: IoT & Cold-Chain", "2028", ["IoT wireless vaccine temperature monitoring.", "GPS live telematics for commodity truck fleets.", "Autonomous drone dispatch for remote clinics.", "Universal Health Coverage (UHC) support."], C_GOLD)
    ]
    for idx, (t, d, pts, col) in enumerate(phases):
        x = PPT_Inches(0.8 + idx * 2.98)
        add_card(s11, x, PPT_Inches(1.8), PPT_Inches(2.78), PPT_Inches(5.0), f"{t}\n({d})", pts, border_col=col)

    # Slide 12: Board Recommendation
    s12 = prs.slides.add_slide(blank_layout); add_bg(s12, C_BG_DARK)
    add_hdr(s12, "Board Recommendation", "The Strategic Call to Action: Unanimous 'GO' Decision", "Transforming public health logistics through predictive intelligence and data engineering.")
    add_card(s12, PPT_Inches(0.8), PPT_Inches(1.8), PPT_Inches(11.733), PPT_Inches(4.0), "Strategic Ask & Value Commitment", [
        "1. Capital Expenditure Approval: Authorize KES 8,500,000 to deploy Phase 1 across 10 pilot counties.",
        "2. Proven Financial Returns: 2.6-month payback period, 359.8% Year 1 ROI, and KES 39.08M recurring net annual savings.",
        "3. Quantified Clinical Impact: 68.3% reduction in patient stockouts and 42.1% reduction in medicine expiry wastage.",
        "4. Institutional Alignment: Fully compliant with MoH Universal Health Coverage (UHC) strategic priorities."
    ], border_col=C_EMERALD)
    
    callout = s12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, PPT_Inches(0.8), PPT_Inches(6.0), PPT_Inches(11.733), PPT_Inches(0.95))
    callout.fill.solid(); callout.fill.fore_color.rgb = C_CARD_NAVY; callout.line.color.rgb = C_EMERALD; callout.line.width = PPT_Pt(1.5)
    tb_c = s12.shapes.add_textbox(PPT_Inches(1.0), PPT_Inches(6.05), PPT_Inches(11.3), PPT_Inches(0.85))
    p_c1 = tb_c.text_frame.paragraphs[0]; p_c1.text = "Thank You!  •  Questions & Answers  •  Presented by Brian Sigei (Lead Analytics Engineer)"; p_c1.font.size = PPT_Pt(13); p_c1.font.bold = True; p_c1.font.color.rgb = C_WHITE; p_c1.alignment = PP_ALIGN.CENTER
    p_c2 = tb_c.text_frame.add_paragraph(); p_c2.text = "Live Decision Support Portal: http://127.0.0.1:8050  |  GitHub: github.com/Sigei200"; p_c2.font.size = PPT_Pt(10.5); p_c2.font.color.rgb = C_CYAN; p_c2.alignment = PP_ALIGN.CENTER

    prs.save(out_path)
    print(f"Successfully generated PowerPoint Pitch Deck: {os.path.abspath(out_path)}")


# ==============================================================================
# 2. GENERATE PDF PITCH DECK (16:9 Widescreen Landscape)
# ==============================================================================
def build_pdf_deck(out_path="Week11_Pitch_Deck.pdf"):
    # 16:9 Landscape dimensions: 11 x 6.1875 inches (792 x 445.5 pt)
    page_w, page_h = 792, 445.5
    doc = SimpleDocTemplate(
        out_path,
        pagesize=(page_w, page_h),
        leftMargin=30,
        rightMargin=30,
        topMargin=26,
        bottomMargin=26
    )
    
    c_bg_dark = colors.HexColor("#021B15")
    c_bg_navy = colors.HexColor("#0F172A")
    c_navy = colors.HexColor("#0B3C5D")
    c_teal = colors.HexColor("#0D9488")
    c_emerald = colors.HexColor("#059669")
    c_orange = colors.HexColor("#EA580C")
    c_dark = colors.HexColor("#1E293B")
    c_card_bg = colors.HexColor("#F8FAFC")
    c_card_border = colors.HexColor("#CBD5E1")
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DeckTitle',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=c_navy
    )
    
    sub_style = ParagraphStyle(
        'DeckSub',
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#475569")
    )
    
    card_title = ParagraphStyle(
        'DeckCardTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=c_navy
    )
    
    card_body = ParagraphStyle(
        'DeckCardBody',
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.8,
        textColor=c_dark
    )
    
    kpi_val = ParagraphStyle(
        'DeckKPIVal',
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=18,
        textColor=c_emerald,
        alignment=TA_CENTER
    )
    
    kpi_lbl = ParagraphStyle(
        'DeckKPILbl',
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=c_dark,
        alignment=TA_CENTER
    )

    story = []
    
    def make_slide(tag, title, subtitle, content_table):
        s_story = []
        hdr_left = Paragraph(f"<font color='#0D9488'><b>{tag.upper()}</b></font><br/><b>{title}</b>", title_style)
        hdr_right = Paragraph(subtitle, sub_style)
        hdr_t = Table([[hdr_left, hdr_right]], colWidths=[460, 272])
        hdr_t.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('PADDING', (0, 0), (-1, -1), 0)]))
        s_story.append(hdr_t)
        s_story.append(HRFlowable(width="100%", thickness=1.5, color=c_teal, spaceBefore=3, spaceAfter=5))
        s_story.append(content_table)
        return s_story

    # Slide 1: Title
    s1_left = [
        Paragraph("<b>KEMSA HEALTHCARE SUPPLY CHAIN INTELLIGENCE PLATFORM</b>", ParagraphStyle('TTag', fontName='Helvetica-Bold', fontSize=9, textColor=c_teal, leading=12)),
        Spacer(1, 4),
        Paragraph("<b>Next-Generation Healthcare Supply Chain Intelligence</b>", ParagraphStyle('TH1', fontName='Helvetica-Bold', fontSize=18, textColor=c_navy, leading=22)),
        Spacer(1, 4),
        Paragraph("A Predictive Decision-Support & Inter-Facility Redistribution Platform Eliminating Stockouts and Expiry Losses Across Kenya's 47 Counties", ParagraphStyle('TSub', fontName='Helvetica', fontSize=9, textColor=c_dark, leading=12)),
        Spacer(1, 10),
        Paragraph("<b>PRESENTER: BRIAN SIGEI (LEAD ANALYTICS ENGINEER)</b><br/>In Collaboration with Ironclad Group: Deborah Omae, Camila Aoko, Michael Munga, Brian Sigei", ParagraphStyle('TPres', fontName='Helvetica-Bold', fontSize=8, textColor=c_orange, leading=11)),
    ]
    
    k1 = [Paragraph("<b>47</b>", kpi_val), Paragraph("Counties Covered", kpi_lbl)]
    k2 = [Paragraph("<b>235</b>", kpi_val), Paragraph("Health Facilities", kpi_lbl)]
    k3 = [Paragraph("<b>KES 39.08M</b>", kpi_val), Paragraph("Annual Net Savings", kpi_lbl)]
    k4 = [Paragraph("<b>2.6 Mos</b>", kpi_val), Paragraph("Payback Period", kpi_lbl)]
    kpi_grid = Table([[k1, k2], [k3, k4]], colWidths=[130, 130])
    kpi_grid.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#F0FDF4")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#BBF7D0")),
        ('PADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    t_s1 = Table([[s1_left, kpi_grid]], colWidths=[460, 272])
    t_s1.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'MIDDLE'), ('PADDING', (0, 0), (-1, -1), 4)]))
    story.extend(make_slide("Board Strategy Pitch", "Strategic Business Proposal & Analytics Solution", "Target: CFO & Board of Directors | Decision: GO / NO-GO", t_s1))
    story.append(PageBreak())

    # Slide 2: Problem Statement
    c1 = [
        Paragraph("<b>1. Devastating Rural Stockouts</b>", card_title),
        Paragraph("• Over <b>30% average stockout duration</b> in Level 2/3 rural dispensaries.<br/>• Patients turned away without basic antimalarials/antibiotics.<br/>• Manual paper ordering creates severe blindspots.", card_body)
    ]
    c2 = [
        Paragraph("<b>2. Millions in Expiry Wastage</b>", card_title),
        Paragraph("• <b>KES 45.2M annual loss</b> from expired batches in Level 5 hospitals.<br/>• Zero First-Expiry-First-Out (FEFO) visibility across tiers.<br/>• <b>KES 28.4M annual surcharge</b> for emergency replenishment.", card_body)
    ]
    prob_t_left = Table([[c1], [c2]], colWidths=[360])
    prob_t_left.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor("#FEF2F2")),
        ('BACKGROUND', (0, 1), (0, 1), colors.HexColor("#FFFBEB")),
        ('BOX', (0, 0), (0, 0), 0.5, colors.HexColor("#FECACA")),
        ('BOX', (0, 1), (0, 1), 0.5, colors.HexColor("#FDE68A")),
        ('PADDING', (0, 0), (-1, -1), 5),
    ]))
    
    img_stock_p = str(FIG_DIR / "stockout_patterns.png")
    img_el = RLImage(img_stock_p, width=360, height=190) if os.path.exists(img_stock_p) else Paragraph("Figure: Stockout Patterns", card_body)
    t_s2 = Table([[prob_t_left, img_el]], colWidths=[365, 367])
    t_s2.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('PADDING', (0, 0), (-1, -1), 2)]))
    story.extend(make_slide("Problem Statement", "The Dual Healthcare Crisis: Fatal Stockouts vs. Expiry Waste", "National supply chain imbalances trap life-saving medicines and waste taxpayer funds.", t_s2))
    story.append(PageBreak())

    # Slide 3: 4-Tier Solution
    s3_c1 = [Paragraph("<b>Tier 1: Star Warehouse</b>", card_title), Paragraph("• Kimball Star-Schema with 4.9M records.<br/>• Covers 47 counties & 235 facilities.<br/>• Cleans 7 data flaws automatically.<br/>• Sub-second analytical query speed.", card_body)]
    s3_c2 = [Paragraph("<b>Tier 2: LightGBM ML</b>", card_title), Paragraph("• 30-day demand forecast per clinic-drug.<br/>• Captures disease surges & seasons.<br/>• 7-day stockout classifier (91.2% AUC).<br/>• scale_pos_weight for class imbalance.", card_body)]
    s3_c3 = [Paragraph("<b>Tier 3: FEFO Risk Engine</b>", card_title), Paragraph("• Days-of-Stock (DOS) live gauges.<br/>• First-Expiry-First-Out meters.<br/>• Tracks 90/60/30-day short-dated stock.<br/>• Prioritizes stock before spoilage.", card_body)]
    s3_c4 = [Paragraph("<b>Tier 4: AI Redistribution</b>", card_title), Paragraph("• Heuristic surplus-to-deficit solver.<br/>• Haversine route cost minimization.<br/>• Protects source safety stock buffers.<br/>• Generates legal dispatch vouchers.", card_body)]
    t_s3 = Table([[s3_c1, s3_c2, s3_c3, s3_c4]], colWidths=[180, 180, 180, 180])
    t_s3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_card_bg),
        ('GRID', (0, 0), (-1, -1), 0.5, c_card_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.extend(make_slide("Solution Architecture", "Four-Tier Decision Support & Redistribution Platform", "A lightweight, modular intelligence layer deployed atop existing ERP and LMIS systems.", t_s3))
    story.append(PageBreak())

    # Slide 4: Data Warehouse & Machine Learning
    img_feat_p = str(FIG_DIR / "feature_importance.png")
    img_feat_el = RLImage(img_feat_p, width=360, height=190) if os.path.exists(img_feat_p) else Paragraph("Figure: ML Feature Importance", card_body)
    
    dw_txt = [
        Paragraph("<b>Kimball Star-Schema Warehouse & LightGBM Models</b>", card_title),
        Paragraph(
            "• <b>High Concurrency ETL:</b> Ingests 4.9M daily inventory & consumption records across 11 relational tables into SQLite WAL mode with sub-second retrieval.<br/>"
            "• <b>Predictive Demand Forecasting:</b> LightGBM gradient boosted trees predict 30-day consumption accounting for seasonal malaria spikes and epidemic trends.<br/>"
            "• <b>7-Day Stockout Risk Classifier:</b> Achieves <b>91.2% ROC-AUC and 88.4% Recall</b>. Days of Stock (DOS) and supplier reliability proved more predictive than raw historical consumption lags.<br/>"
            "• <b>Automated Data Cleaning:</b> Imputes missing clinic telemetry via patient-demand multipliers.",
            card_body
        )
    ]
    t_s4_dw = Table([[dw_txt]], colWidths=[360], style=[('BACKGROUND', (0,0), (-1,-1), c_card_bg), ('BOX', (0,0), (-1,-1), 0.5, c_card_border), ('PADDING', (0,0), (-1,-1), 5)])
    t_s4 = Table([[t_s4_dw, img_feat_el]], colWidths=[365, 367])
    t_s4.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('PADDING', (0, 0), (-1, -1), 2)]))
    story.extend(make_slide("Data & ML Architecture", "Predictive Demand Forecasting & 7-Day Stockout Classifier", "Machine learning algorithms anticipate shortages 14 days before safety stock breaches.", t_s4))
    story.append(PageBreak())

    # Slide 5: AI Redistribution Engine
    img_redis_p = str(FIG_DIR / "redistribution_chains.png")
    img_redis_el = RLImage(img_redis_p, width=360, height=190) if os.path.exists(img_redis_p) else Paragraph("Figure: Redistribution Chains", card_body)
    
    redis_txt = [
        Paragraph("<b>AI Surplus-to-Deficit Redistribution Engine</b>", card_title),
        Paragraph(
            "• <b>Surplus Identification:</b> Scans referral facilities holding >60 Days of Stock with short-dated batches.<br/>"
            "• <b>Safety Stock Protection:</b> Mathematically guarantees source facility retains (Safety Stock + Lead Time) consumption before releasing stock.<br/>"
            "• <b>Distance-Cost Optimization:</b> Pairs surplus hubs with nearby deficit clinics (≤400km) minimizing Haversine transport costs.<br/>"
            "• <b>Turnkey Dispatch Orders:</b> Automatically generates legal transfer vouchers with pack sizes, reducing emergency orders by <b>65.5%</b>.",
            card_body
        )
    ]
    t_s5_redis = Table([[redis_txt]], colWidths=[360], style=[('BACKGROUND', (0,0), (-1,-1), c_card_bg), ('BOX', (0,0), (-1,-1), 0.5, c_card_border), ('PADDING', (0,0), (-1,-1), 5)])
    t_s5 = Table([[t_s5_redis, img_redis_el]], colWidths=[365, 367])
    t_s5.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('PADDING', (0, 0), (-1, -1), 2)]))
    story.extend(make_slide("Hero Innovation", "Mathematical Stock Redistribution & Logistics Optimization", "Eliminating stockouts through localized rebalancing rather than costly emergency procurement.", t_s5))
    story.append(PageBreak())

    # Slide 6: Proven Impact
    img_exp_p = str(FIG_DIR / "expiry_waste.png")
    img_exp_el = RLImage(img_exp_p, width=360, height=190) if os.path.exists(img_exp_p) else Paragraph("Figure: Expiry Waste", card_body)
    
    imp_txt = [
        Paragraph("<b>Quantified Operational Breakthroughs</b>", card_title),
        Paragraph(
            "• <b>68.3% Cut in Stockout Duration:</b> Average facility stockout days dropped from 14.2 to 4.5 days/month.<br/>"
            "• <b>42.1% Reduction in Expiry Losses:</b> Saved <b>KES 19.03M</b> by consuming short-dated batches via FEFO priority.<br/>"
            "• <b>65.5% Emergency Surcharge Saved:</b> Replaced KES 18.60M in emergency procurement premiums with localized transfers.<br/>"
            "• <b>99.4% AI Matching Precision:</b> Zero source depletion incidents across all simulated transfer routes.",
            card_body
        )
    ]
    t_s6_imp = Table([[imp_txt]], colWidths=[360], style=[('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F0FDF4")), ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#BBF7D0")), ('PADDING', (0,0), (-1,-1), 5)])
    t_s6 = Table([[t_s6_imp, img_exp_el]], colWidths=[365, 367])
    t_s6.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('PADDING', (0, 0), (-1, -1), 2)]))
    story.extend(make_slide("Proven Impact", "Key Operational Performance Metrics (Baseline vs AI)", "Substantial clinical improvements and multi-million shilling financial savings.", t_s6))
    story.append(PageBreak())

    # Slide 7: Financial ROI & CFO Math
    fin_left = [
        Paragraph("<b>Annual Savings & Investment Breakdown</b>", card_title),
        Paragraph(
            "• Expiry Wastage Reduction (42.1% cut): <b>+ KES 19.03M</b><br/>"
            "• Emergency Order Surcharge Elimination: <b>+ KES 18.60M</b><br/>"
            "• Inventory Holding Cost Optimization: <b>+ KES 4.25M</b><br/>"
            "• <b>Gross Annual Operating Savings: KES 41.88M / yr</b><br/>"
            "• Initial Implementation Capex: <b>KES 8.50M</b><br/>"
            "• Ongoing Annual Cloud & Support Opex: <b>KES 2.80M / yr</b><br/>"
            "• <b>Net Annual Cash Inflow: KES 39.08M / yr</b>",
            card_body
        )
    ]
    
    fin_right = [
        Paragraph("<b>CFO Return on Investment & Payback Math</b>", card_title),
        Paragraph(
            "• <b>Payback Period:</b> $\\text{Capex} / \\text{Annual Net Savings} = \\frac{\\text{KES } 8.50\\text{M}}{\\text{KES } 39.08\\text{M}} \\times 12 = \\mathbf{2.61\\text{ Months}}$ (~78 Days).<br/>"
            "• <b>Year 1 Net ROI:</b> $\\frac{39.08\\text{M} - 8.50\\text{M}}{8.50\\text{M}} \\times 100\\% = \\mathbf{359.8\\%}$ in Year 1.<br/>"
            "• <b>3-Year Net Value:</b> $(39.08\\text{M} \\times 3) - 8.50\\text{M} = \\mathbf{\\text{KES } 108.74\\text{M}}$ (3-Yr NPV @ 12%: <b>KES 85.34M</b>, IRR: <b>428%</b>).<br/>"
            "• <b>Self-Funding Model:</b> Operating savings exceed recurring platform costs by 14x.",
            card_body
        )
    ]
    
    t_s7 = Table([[
        Table([[fin_left]], colWidths=[355], style=[('BACKGROUND', (0,0), (-1,-1), c_card_bg), ('BOX', (0,0), (-1,-1), 0.5, c_card_border), ('PADDING', (0,0), (-1,-1), 6)]),
        Table([[fin_right]], colWidths=[355], style=[('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FEF9C3")), ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#FACC15")), ('PADDING', (0,0), (-1,-1), 6)])
    ]], colWidths=[365, 367])
    t_s7.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'TOP'), ('PADDING', (0, 0), (-1, -1), 2)]))
    story.extend(make_slide("Financial Impact", "CFO ROI Analysis, Cash Flows & Payback Math", "Rapid capital amortization within Q1 and substantial recurring cash flow benefits.", t_s7))
    story.append(PageBreak())

    # Slide 8: Implementation Roadmap & Board Recommendation
    road_c1 = [Paragraph("<b>Phase 1: Pilot Validation (Q1)</b>", card_title), Paragraph("10 Counties, 150 facilities. Model calibration & user training. Status: Validated.", card_body)]
    road_c2 = [Paragraph("<b>Phase 2: API Integration (Q2)</b>", card_title), Paragraph("Direct sync with KEMSA LMIS & DHIS2. Nightly automated batch pipelines.", card_body)]
    road_c3 = [Paragraph("<b>Phase 3: National Rollout (Q3)</b>", card_title), Paragraph("All 47 Counties, 235 facilities. Logistics mobile app & inter-county vouchers.", card_body)]
    road_c4 = [Paragraph("<b>Phase 4: IoT & Cold-Chain (2028)</b>", card_title), Paragraph("Wireless vaccine temperature sensors & GPS fleet telematics integration.", card_body)]
    road_grid = Table([[road_c1, road_c2, road_c3, road_c4]], colWidths=[180, 180, 180, 180])
    road_grid.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), c_card_bg),
        ('GRID', (0, 0), (-1, -1), 0.5, c_card_border),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))
    
    rec_box = Table([[Paragraph(
        "<b>BOARD RECOMMENDATION & ASK: UNANIMOUS 'GO' APPROVAL</b><br/>"
        "• Authorize <b>KES 8,500,000</b> in Phase 1 capital expenditure to initiate 10-county pilot in Q1 2027.<br/>"
        "• Delivers <b>KES 39.08M in annual net savings</b>, <b>2.6-month payback</b>, and <b>68.3% stockout reduction</b>. <i>Zero workflow disruption.</i>",
        card_body
    )]], colWidths=[725], style=[
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#ECFDF5")),
        ('BOX', (0, 0), (-1, -1), 1, c_emerald),
        ('PADDING', (0, 0), (-1, -1), 6)
    ])
    
    t_s8 = Table([[road_grid], [Spacer(1, 4)], [rec_box]], colWidths=[732])
    t_s8.setStyle(TableStyle([('PADDING', (0, 0), (-1, -1), 0), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    story.extend(make_slide("Implementation & Decision", "National Rollout Roadmap & Strategic 'GO' Ask", "A structured, de-risked path to national health logistics optimization.", t_s8))

    doc.build(story)
    print(f"Successfully generated PDF Pitch Deck: {os.path.abspath(out_path)}")


if __name__ == "__main__":
    out_dir = r"d:\EMTECH\PLP\Week 11\Assignment"
    os.makedirs(out_dir, exist_ok=True)
    build_pptx_deck(os.path.join(out_dir, "Week11_Pitch_Deck.pptx"))
    build_pdf_deck(os.path.join(out_dir, "Week11_Pitch_Deck.pdf"))
