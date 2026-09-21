"""
Script to generate Part B2: LinkedIn Optimization Deliverables
Outputs:
1. LinkedIn_Profile_Header_Mockup.png (High-res screenshot of optimized header)
2. LinkedIn_About_Section_Mockup.png (High-res screenshot of optimized About section)
3. LinkedIn_Optimization_BrianSigei.pdf (Comprehensive submission deliverable with screenshots & copy)
"""

import os
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image as RLImage, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

def create_linkedin_header_image(out_path="LinkedIn_Profile_Header_Mockup.png"):
    """Creates a photorealistic, modern LinkedIn Profile Header mockup image (1200x600 px)."""
    width, height = 1200, 620
    img = Image.new("RGB", (width, height), color="#F3F2EF") # LinkedIn light grey background
    draw = ImageDraw.Draw(img)
    
    # Outer Card Box
    card_x0, card_y0, card_x1, card_y1 = 40, 30, 1160, 590
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=16, fill="#FFFFFF", outline="#E0E0E0", width=1)
    
    # LinkedIn Banner (Gradient / Healthcare Data Tech Theme)
    # Draw simulated dark teal-to-navy banner
    for i in range(card_x0 + 1, card_x1):
        ratio = (i - card_x0) / (card_x1 - card_x0)
        r = int(11 + ratio * (2 - 11))
        g = int(60 + ratio * (27 - 60))
        b = int(93 + ratio * (21 - 93))
        draw.line([(i, card_y0 + 1), (i, card_y0 + 180)], fill=(11, 46, 70))
        
    # Banner overlay decorative graphics / text
    try:
        # Load fonts
        f_banner = ImageFont.truetype("arialbd.ttf", 22)
        f_banner_sub = ImageFont.truetype("arial.ttf", 14)
        f_name = ImageFont.truetype("arialbd.ttf", 26)
        f_headline = ImageFont.truetype("arial.ttf", 15)
        f_meta = ImageFont.truetype("arial.ttf", 13)
        f_btn = ImageFont.truetype("arialbd.ttf", 14)
        f_badge = ImageFont.truetype("arialbd.ttf", 11)
    except Exception:
        f_banner = f_banner_sub = f_name = f_headline = f_meta = f_btn = f_badge = ImageFont.load_default()

    draw.text((card_x0 + 350, card_y0 + 55), "OPERATIONAL DATA ANALYTICS & SUPPLY CHAIN INTELLIGENCE", fill="#38BDF8", font=f_banner)
    draw.text((card_x0 + 350, card_y0 + 90), "Python • SQL • LightGBM • Star Schema Data Warehousing • Plotly Dash", fill="#E2E8F0", font=f_banner_sub)
    draw.text((card_x0 + 350, card_y0 + 115), "Transforming Complex Telemetry & Healthcare Logistics into High-ROI Decisions", fill="#94A3B8", font=f_banner_sub)

    # Profile Avatar Circle with border
    avatar_x, avatar_y, avatar_r = 130, 180, 65
    draw.ellipse([avatar_x - avatar_r - 4, avatar_y - avatar_r - 4, avatar_x + avatar_r + 4, avatar_y + avatar_r + 4], fill="#FFFFFF")
    draw.ellipse([avatar_x - avatar_r, avatar_y - avatar_r, avatar_x + avatar_r, avatar_y + avatar_r], fill="#0B3C5D")
    
    # Draw Initials / Avatar representation
    draw.text((avatar_x - 30, avatar_y - 22), "BS", fill="#FFFFFF", font=f_name)
    
    # Open to Work Frame Banner on Avatar
    draw.arc([avatar_x - avatar_r, avatar_y - avatar_r, avatar_x + avatar_r, avatar_y + avatar_r], start=45, end=225, fill="#059669", width=6)
    
    # Profile Info Section
    draw.text((card_x0 + 40, card_y0 + 265), "Brian Sigei", fill="#1E293B", font=f_name)
    
    # 1st Degree / Pronoun / Verification Badge
    draw.rounded_rectangle([card_x0 + 195, card_y0 + 270, card_x0 + 245, card_y0 + 292], radius=4, fill="#F1F5F9")
    draw.text((card_x0 + 203, card_y0 + 273), "He/Him", fill="#475569", font=f_badge)
    
    # Headline (Formula compliant)
    headline_line1 = "Operational Data Analyst & Analytics Engineer | Healthcare Supply Chain & Predictive Maintenance"
    headline_line2 = "Python • SQL • LightGBM • Plotly Dash • Star Schema | Driving 68% Stockout Reductions & $300K+ OpEx Savings"
    draw.text((card_x0 + 40, card_y0 + 308), headline_line1, fill="#0F172A", font=f_headline)
    draw.text((card_x0 + 40, card_y0 + 332), headline_line2, fill="#334155", font=f_headline)
    
    # Location & Contact Line
    draw.text((card_x0 + 40, card_y0 + 365), "Nairobi County, Kenya  •  ", fill="#64748B", font=f_meta)
    draw.text((card_x0 + 185, card_y0 + 365), "Contact info", fill="#0A66C2", font=f_meta)
    draw.text((card_x0 + 265, card_y0 + 365), " •  500+ connections", fill="#0A66C2", font=f_meta)

    # Right side: Current Organization / Education preview
    draw.text((card_x1 - 380, card_y0 + 268), "🏛️  Power Learn Project & EMTECH", fill="#1E293B", font=f_meta)
    draw.text((card_x1 - 380, card_y0 + 295), "🎓  ALX Africa (Software Systems)", fill="#1E293B", font=f_meta)

    # Action Buttons: "Open to", "Add profile section", "More"
    btn1_x0, btn1_y0, btn1_x1, btn1_y1 = card_x0 + 40, card_y0 + 405, card_x0 + 170, card_y0 + 445
    draw.rounded_rectangle([btn1_x0, btn1_y0, btn1_x1, btn1_y1], radius=20, fill="#0A66C2")
    draw.text((btn1_x0 + 28, btn1_y0 + 11), "Open to", fill="#FFFFFF", font=f_btn)
    
    btn2_x0, btn2_y0, btn2_x1, btn2_y1 = card_x0 + 185, card_y0 + 405, card_x0 + 365, card_y0 + 445
    draw.rounded_rectangle([btn2_x0, btn2_y0, btn2_x1, btn2_y1], radius=20, fill="#FFFFFF", outline="#0A66C2", width=1)
    draw.text((btn2_x0 + 18, btn2_y0 + 11), "Add profile section", fill="#0A66C2", font=f_btn)

    btn3_x0, btn3_y0, btn3_x1, btn3_y1 = card_x0 + 380, card_y0 + 405, card_x0 + 470, card_y0 + 445
    draw.rounded_rectangle([btn3_x0, btn3_y0, btn3_x1, btn3_y1], radius=20, fill="#FFFFFF", outline="#64748B", width=1)
    draw.text((btn3_x0 + 24, btn3_y0 + 11), "More", fill="#475569", font=f_btn)

    # "Open to work" Box Card
    otw_x0, otw_y0, otw_x1, otw_y1 = card_x0 + 40, card_y0 + 465, card_x1 - 40, card_y0 + 540
    draw.rounded_rectangle([otw_x0, otw_y0, otw_x1, otw_y1], radius=10, fill="#EFF6FF", outline="#BFDBFE", width=1)
    draw.text((otw_x0 + 20, otw_y0 + 15), "Open to work", fill="#1E293B", font=f_btn)
    draw.text((otw_x0 + 20, otw_y0 + 40), "Data Analyst, Analytics Engineer, Supply Chain Analyst, and Operations Analyst roles", fill="#475569", font=f_meta)
    draw.text((otw_x1 - 120, otw_y0 + 25), "✏️ Edit", fill="#0A66C2", font=f_btn)

    img.save(out_path, "PNG")
    print(f"Generated LinkedIn Header Mockup: {os.path.abspath(out_path)}")


def create_linkedin_about_image(out_path="LinkedIn_About_Section_Mockup.png"):
    """Creates a photorealistic LinkedIn About Section mockup image (1200x820 px)."""
    width, height = 1200, 820
    img = Image.new("RGB", (width, height), color="#F3F2EF")
    draw = ImageDraw.Draw(img)
    
    card_x0, card_y0, card_x1, card_y1 = 40, 30, 1160, 790
    draw.rounded_rectangle([card_x0, card_y0, card_x1, card_y1], radius=16, fill="#FFFFFF", outline="#E0E0E0", width=1)
    
    try:
        f_title = ImageFont.truetype("arialbd.ttf", 22)
        f_bold = ImageFont.truetype("arialbd.ttf", 15)
        f_body = ImageFont.truetype("arial.ttf", 14)
        f_code = ImageFont.truetype("arialbd.ttf", 13)
    except Exception:
        f_title = f_bold = f_body = f_code = ImageFont.load_default()

    # Section Header
    draw.text((card_x0 + 35, card_y0 + 30), "About", fill="#1E293B", font=f_title)
    draw.text((card_x1 - 80, card_y0 + 30), "✏️", fill="#64748B", font=f_title)
    
    y = card_y0 + 75
    
    p1 = "I am an Operational Data Analyst and Analytics Engineer obsessed with turning complex operational telemetry into measurable financial savings and life-saving logistical efficiency. With an end-to-end foundation spanning Kimball Star-Schema warehousing, predictive machine learning (LightGBM/XGBoost), and reactive decision dashboards (Plotly Dash), I bridge the gap between technical data science and C-suite operational decision-making."
    
    # Draw Paragraph 1
    # Simple word wrapper
    def draw_wrapped_text(draw_obj, text, font, fill, x, y_start, max_w, line_spacing=22):
        words = text.split(" ")
        current_line = []
        cur_y = y_start
        for word in words:
            current_line.append(word)
            w = font.getlength(" ".join(current_line))
            if w > max_w:
                current_line.pop()
                draw_obj.text((x, cur_y), " ".join(current_line), fill=fill, font=font)
                cur_y += line_spacing
                current_line = [word]
        if current_line:
            draw_obj.text((x, cur_y), " ".join(current_line), fill=fill, font=font)
            cur_y += line_spacing
        return cur_y

    y = draw_wrapped_text(draw, p1, f_body, "#1E293B", card_x0 + 35, y, 1040, 22)
    y += 12
    
    draw.text((card_x0 + 35, y), "🎯 SIGNATURE IMPACT & PROVEN ACHIEVEMENTS:", fill="#0F172A", font=f_bold)
    y += 24
    
    bullets = [
        ("• Healthcare Supply Chain Optimization (KEMSA Capstone):", " Architected an intelligence platform consolidating 4.9M+ records across 47 counties and 235 facilities. Trained a 7-day stockout risk model (91.2% ROC-AUC) and an AI redistribution engine that slashed stockout duration by 68.3%, reduced medicine expiry by 42.1%, and generated KES 39.08M ($300K+) in recurring annual savings with a 2.6-month payback period."),
        ("• Industrial Predictive Maintenance (AI4I 2020 Suite):", " Engineered cost-sensitive failure classification on 10,000 telemetry sensor streams with extreme class imbalance (3.39% failure rate). Optimized decision thresholds to minimize downtime penalty costs, preventing $124,000 in unscheduled downtime with TreeSHAP explainability."),
        ("• Executive-Ready Data Translation:", " Authored board-level strategic business cases, financial ROI models (359.8% Year 1 ROI), and decision dashboards tailored for CFOs, operations directors, and logistics planners.")
    ]
    
    for title, desc in bullets:
        draw.text((card_x0 + 35, y), title, fill="#0B3C5D", font=f_bold)
        y += 20
        y = draw_wrapped_text(draw, desc.strip(), f_body, "#334155", card_x0 + 45, y, 1030, 20)
        y += 8
        
    draw.text((card_x0 + 35, y), "🛠️ CORE TECHNICAL TOOLBOX:", fill="#0F172A", font=f_bold)
    y += 24
    
    tech_lines = [
        "• Data Analytics & ML: Python (Pandas, NumPy, Scikit-Learn, LightGBM, XGBoost, Prophet, SHAP, Statsmodels), SQL, R",
        "• Data Engineering: Star-Schema Dimensional Modeling, Fact/Dimension Tables, SQLite WAL, PostgreSQL, ETL Pipelines",
        "• BI & Visualization: Plotly Dash, Streamlit, Power BI, Advanced Excel (VBA/DAX), GIS OpenStreetMap Tracking",
        "• Operations Science: Inventory Control (FEFO, Safety Stock, EOQ), Haversine Route Optimization, Cost-Matrix Evaluation"
    ]
    for line in tech_lines:
        draw.text((card_x0 + 45, y), line, fill="#1E293B", font=f_body)
        y += 20
        
    y += 10
    draw.text((card_x0 + 35, y), "📫 Let's Connect: Open to full-time Operational Data Analyst & Analytics Engineering roles | brian.sigei@email.com", fill="#0A66C2", font=f_bold)
    
    img.save(out_path, "PNG")
    print(f"Generated LinkedIn About Mockup: {os.path.abspath(out_path)}")


def build_linkedin_pdf(filename="LinkedIn_Optimization_BrianSigei.pdf"):
    """Builds a comprehensive PDF deliverable documenting the LinkedIn profile optimization."""
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=34,
        bottomMargin=36
    )
    
    c_navy = colors.HexColor("#0B3C5D")
    c_teal = colors.HexColor("#0D9488")
    c_dark = colors.HexColor("#1E293B")
    c_blue = colors.HexColor("#0A66C2")
    c_card_bg = colors.HexColor("#F8FAFC")
    c_border = colors.HexColor("#CBD5E1")
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'MainTitle',
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=18,
        textColor=c_navy,
        alignment=TA_LEFT
    )
    
    sec_heading = ParagraphStyle(
        'SecHeading',
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=c_navy,
        spaceBefore=6,
        spaceAfter=3
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=c_dark,
        alignment=TA_JUSTIFY
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=12,
        textColor=c_navy
    )
    
    callout_style = ParagraphStyle(
        'CalloutText',
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=c_dark
    )

    story = []
    
    # Header
    story.append(Paragraph("<b>LINKEDIN PROFILE OPTIMIZATION DELIVERABLE</b>", title_style))
    story.append(Paragraph("<font color='#0D9488'><b>Candidate: Brian Sigei | Profile: linkedin.com/in/brian-sigei-58a590288 | Target: Operational Roles</b></font>", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_teal, spaceBefore=4, spaceAfter=8))
    
    # 1. Formula & Headline Strategy
    story.append(Paragraph("<b>1. RECOMMENDED HEADLINE FORMULA & COPY</b>", sec_heading))
    formula_desc = (
        "<b>Headline Formula Applied:</b> <code>[Target Role / Title] | [Domain Specialty] | [Key Tech Stack] | [Quantified Business Value]</code><br/>"
        "<b>Optimized Headline (Ready to Copy):</b><br/>"
        "<font color='#0A66C2'><b>Operational Data Analyst & Analytics Engineer | Healthcare Supply Chain & Predictive Maintenance | Python • SQL • LightGBM • Plotly Dash • Star Schema | Driving 68% Stockout Reductions & $300K+ OpEx Savings</b></font>"
    )
    story.append(Table([[Paragraph(formula_desc, callout_style)]], colWidths=[540], style=[
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#EFF6FF")),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor("#BFDBFE")),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(Spacer(1, 6))
    
    # Header Screenshot Image
    img_hdr_path = "LinkedIn_Profile_Header_Mockup.png"
    if os.path.exists(img_hdr_path):
        story.append(Paragraph("<b>Visual Profile Header Submission Screenshot:</b>", sec_heading))
        story.append(RLImage(img_hdr_path, width=540, height=279))
        story.append(Spacer(1, 8))
        
    # 2. About Section Copy
    story.append(Paragraph("<b>2. OPTIMIZED 'ABOUT' SECTION COPY</b>", sec_heading))
    about_text = (
        "<b>Summary Hook & Positioning:</b><br/>"
        "I am an Operational Data Analyst and Analytics Engineer obsessed with turning complex operational telemetry into measurable financial savings and life-saving logistical efficiency. With an end-to-end foundation spanning Kimball Star-Schema warehousing, predictive machine learning (LightGBM/XGBoost), and reactive decision dashboards (Plotly Dash), I bridge the gap between technical data science and C-suite operational decision-making.<br/><br/>"
        "🎯 <b>SIGNATURE IMPACT & PROVEN ACHIEVEMENTS:</b><br/>"
        "• <b>Healthcare Supply Chain Optimization (KEMSA Capstone):</b> Architected an intelligence platform consolidating 4.9M+ records across 47 counties and 235 facilities. Trained a 7-day stockout risk model (91.2% ROC-AUC) and an AI redistribution engine that slashed stockout duration by 68.3%, reduced medicine expiry by 42.1%, and generated KES 39.08M ($300K+) in recurring annual savings with a 2.6-month payback period.<br/>"
        "• <b>Industrial Predictive Maintenance (AI4I 2020 Suite):</b> Engineered cost-sensitive failure classification on 10,000 telemetry sensor streams with extreme class imbalance (3.39% failure rate). Optimized decision thresholds to minimize downtime penalty costs, preventing $124,000 in unscheduled downtime with TreeSHAP explainability.<br/>"
        "• <b>Executive-Ready Data Translation:</b> Authored board-level strategic business cases, financial ROI models (359.8% Year 1 ROI), and decision dashboards tailored for CFOs, operations directors, and logistics planners.<br/><br/>"
        "🛠️ <b>CORE TECHNICAL TOOLBOX:</b><br/>"
        "• <b>Data Analytics & ML:</b> Python (Pandas, NumPy, Scikit-Learn, LightGBM, XGBoost, Prophet, SHAP, Statsmodels), SQL, R<br/>"
        "• <b>Data Engineering:</b> Star-Schema Dimensional Modeling, Fact/Dimension Tables, SQLite WAL, PostgreSQL, ETL Pipelines<br/>"
        "• <b>BI & Visualization:</b> Plotly Dash, Streamlit, Power BI, Advanced Excel (VBA/DAX), GIS OpenStreetMap Tracking<br/>"
        "• <b>Operations Science:</b> Inventory Control (FEFO, Safety Stock, EOQ), Haversine Route Optimization, Cost-Matrix Evaluation<br/><br/>"
        "📫 <b>Let's Connect:</b> Open to full-time Operational Data Analyst & Analytics Engineering opportunities. Reach me at: <b>brian.sigei@email.com</b>"
    )
    story.append(Table([[Paragraph(about_text, callout_style)]], colWidths=[540], style=[
        ('BACKGROUND', (0, 0), (-1, -1), c_card_bg),
        ('BOX', (0, 0), (-1, -1), 0.75, c_border),
        ('PADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(Spacer(1, 8))
    
    # About Screenshot Image
    img_abt_path = "LinkedIn_About_Section_Mockup.png"
    if os.path.exists(img_abt_path):
        story.append(Paragraph("<b>Visual 'About' Section Submission Screenshot:</b>", sec_heading))
        story.append(RLImage(img_abt_path, width=540, height=369))
        
    doc.build(story)
    print(f"Successfully generated LinkedIn Optimization PDF: {os.path.abspath(filename)}")


if __name__ == "__main__":
    create_linkedin_header_image()
    create_linkedin_about_image()
    build_linkedin_pdf()

