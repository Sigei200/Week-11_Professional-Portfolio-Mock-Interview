"""
Script to generate Part B1: ATS-Friendly Polished CV
Target: CV_Brian_Sigei_DataAnalyst.pdf (and CV_BrianSigei_DataAnalyst.pdf)
Fully ATS-compliant, quantified, tailored to Operational Data Analyst / Analytics Engineer roles.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

class ATSNumberedCanvas(canvas.Canvas):
    """Two-pass canvas for professional document numbering and clean page borders."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header on page 2
        if self._pageNumber > 1:
            self.drawString(36, 11 * 72 - 24, "BRIAN SIGEI — CURRICULUM VITAE | OPERATIONAL DATA ANALYST")
            self.drawRightString(8.5 * 72 - 36, 11 * 72 - 24, "brian.sigei@email.com | +254 700 000 000")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(36, 11 * 72 - 28, 8.5 * 72 - 36, 11 * 72 - 28)
            
        # Footer on all pages
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(36, 32, 8.5 * 72 - 36, 32)
        self.drawString(36, 20, "Brian Sigei — Operational Data Analyst & Analytics Engineer")
        self.drawRightString(8.5 * 72 - 36, 20, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()


def build_cv(filename="CV_Brian_Sigei_DataAnalyst.pdf"):
    # Page dimensions: 8.5 x 11 in (612 x 792 pt). Margins: 34 pt
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=34,
        rightMargin=34,
        topMargin=32,
        bottomMargin=36
    )
    
    c_primary = colors.HexColor("#0F172A")    # Deep Slate
    c_accent = colors.HexColor("#0D9488")     # Teal Accent
    c_dark = colors.HexColor("#1E293B")       # Dark Charcoal
    c_muted = colors.HexColor("#475569")      # Muted Slate
    c_line = colors.HexColor("#CBD5E1")       # Border Line
    
    styles = getSampleStyleSheet()
    
    name_style = ParagraphStyle(
        'CVName',
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=21,
        textColor=c_primary,
        alignment=TA_LEFT
    )
    
    title_style = ParagraphStyle(
        'CVTitle',
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=c_accent,
        alignment=TA_LEFT
    )
    
    contact_style = ParagraphStyle(
        'CVContact',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=c_muted,
        alignment=TA_LEFT
    )
    
    sec_hdr_style = ParagraphStyle(
        'CVSecHdr',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12.5,
        textColor=c_primary,
        spaceBefore=7,
        spaceAfter=2
    )
    
    job_title_style = ParagraphStyle(
        'CVJobTitle',
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11.5,
        textColor=c_dark
    )
    
    job_meta_style = ParagraphStyle(
        'CVJobMeta',
        fontName='Helvetica-Oblique',
        fontSize=8.2,
        leading=10.5,
        textColor=c_muted,
        alignment=TA_RIGHT
    )
    
    bullet_style = ParagraphStyle(
        'CVBullet',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=c_dark,
        leftIndent=12,
        firstLineIndent=-12,
        spaceAfter=2.5,
        alignment=TA_JUSTIFY
    )
    
    summary_style = ParagraphStyle(
        'CVSummary',
        fontName='Helvetica',
        fontSize=8.4,
        leading=11.5,
        textColor=c_dark,
        alignment=TA_JUSTIFY
    )
    
    skill_cat_style = ParagraphStyle(
        'CVSkillCat',
        fontName='Helvetica-Bold',
        fontSize=8.2,
        leading=11,
        textColor=c_primary
    )
    
    skill_val_style = ParagraphStyle(
        'CVSkillVal',
        fontName='Helvetica',
        fontSize=8.2,
        leading=11,
        textColor=c_dark
    )

    story = []
    
    # ---------------------------------------------------------
    # 1. HEADER & CONTACT INFORMATION
    # ---------------------------------------------------------
    left_header = [
        Paragraph("<b>BRIAN SIGEI</b>", name_style),
        Paragraph("<b>OPERATIONAL DATA ANALYST & ANALYTICS ENGINEER</b>", title_style),
    ]
    
    right_contact = [
        Paragraph("<b>Location:</b> Nairobi, Kenya", contact_style),
        Paragraph("<b>Email:</b> brian.sigei@email.com | <b>Phone:</b> +254 700 000 000", contact_style),
        Paragraph("<b>LinkedIn:</b> <font color='#0D9488'>linkedin.com/in/brian-sigei-58a590288</font>", contact_style),
        Paragraph("<b>GitHub:</b> <font color='#0D9488'>github.com/Sigei200</font>", contact_style),
    ]
    
    contact_table = Table([[left_header, right_contact]], colWidths=[270, 274])
    contact_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(contact_table)
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_accent, spaceBefore=4, spaceAfter=6))
    
    # ---------------------------------------------------------
    # 2. PROFESSIONAL SUMMARY
    # ---------------------------------------------------------
    story.append(Paragraph("<b>PROFESSIONAL SUMMARY</b>", sec_hdr_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_line, spaceBefore=1, spaceAfter=4))
    summary_text = (
        "Quantitatively driven and business-focused <b>Operational Data Analyst & Analytics Engineer</b> with demonstrated expertise "
        "in supply chain intelligence, predictive machine learning, and interactive decision-support platforms. Proven track record in "
        "transforming complex public health and industrial telemetry data into multi-million dollar operational optimizations. Adept at "
        "architecting Kimball Star-Schema data warehouses, training cost-sensitive gradient boosting models (LightGBM/XGBoost), "
        "and implementing AI-driven redistribution engines that reduced stockout durations by <b>68.3%</b> and unlocked <b>KES 39.08M+ ($300K+)</b> "
        "in annualized cost savings. Skilled at translating deep data science mechanics into clear, jargon-free executive business cases for CFOs and Board members."
    )
    story.append(Paragraph(summary_text, summary_style))
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 3. CORE TECHNICAL & OPERATIONAL COMPETENCIES
    # ---------------------------------------------------------
    story.append(Paragraph("<b>CORE COMPETENCIES & TECHNICAL SKILLS</b>", sec_hdr_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_line, spaceBefore=1, spaceAfter=4))
    
    skills_data = [
        [
            Paragraph("<b>Languages & Tools:</b>", skill_cat_style),
            Paragraph("Python (Pandas, NumPy, Scikit-Learn, LightGBM, XGBoost, Prophet, SHAP, Statsmodels), SQL, R, Git/GitHub, Docker, Linux/Bash, ReportLab.", skill_val_style)
        ],
        [
            Paragraph("<b>Data Architecture:</b>", skill_cat_style),
            Paragraph("Kimball Star-Schema Modeling, Fact/Dimension Tables, SQLite (WAL Concurrency), PostgreSQL, Automated ETL/ELT Pipelines, Data Cleaning & Referential Integrity.", skill_val_style)
        ],
        [
            Paragraph("<b>Analytics & BI:</b>", skill_cat_style),
            Paragraph("Plotly Dash, Streamlit, Power BI, Advanced Excel (Power Query, DAX, VBA), Tableau, GIS/OpenStreetMap Geospatial Tracking, Interactive UI/UX Design.", skill_val_style)
        ],
        [
            Paragraph("<b>Operations & ML:</b>", skill_cat_style),
            Paragraph("Time-Series Demand Forecasting, Cost-Sensitive Classification, Class Imbalance Handling (Scale-Pos-Weight, SMOTE), Inventory Control (FEFO, EOQ, Safety Stock), Haversine Optimization.", skill_val_style)
        ],
        [
            Paragraph("<b>Business Strategy:</b>", skill_cat_style),
            Paragraph("Financial ROI & Payback Modeling, Operational Risk Mitigation, Executive Storytelling, Cross-Functional Team Leadership, Board Pitch Decks.", skill_val_style)
        ]
    ]
    
    skills_table = Table(skills_data, colWidths=[120, 424])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 4. SIGNATURE TECHNICAL & CAPSTONE PROJECTS
    # ---------------------------------------------------------
    story.append(Paragraph("<b>FEATURED TECHNICAL & OPERATIONAL PROJECTS</b>", sec_hdr_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_line, spaceBefore=1, spaceAfter=4))
    
    # Project 1: Healthcare Supply Chain Intelligence Platform
    p1_header = [
        Paragraph("<b>Healthcare Supply Chain Intelligence & Redistribution Platform</b> | <i>KEMSA Capstone</i>", job_title_style),
        Paragraph("Lead Analytics Engineer & Dashboard Architect | 2026", job_meta_style)
    ]
    t_p1 = Table([p1_header], colWidths=[380, 164])
    t_p1.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'BOTTOM'), ('PADDING', (0, 0), (-1, -1), 0)]))
    story.append(t_p1)
    story.append(Spacer(1, 2))
    
    p1_bullets = [
        "• <b>National Scale Data Warehousing:</b> Engineered an end-to-end Kimball Star-Schema pipeline ingesting <b>4.9M+ records</b> across <b>all 47 Kenyan counties, 235 health facilities, and 45 essential commodities</b>, implementing automated data quality cleaners and sub-second analytical query caching.",
        "• <b>Predictive ML Risk Classifier:</b> Developed a 7-day early-warning stockout risk model using <b>LightGBM</b> with custom class-imbalance weighting (`scale_pos_weight`), achieving <b>91.2% ROC-AUC and 88.4% recall</b> to alert health officers prior to stock depletion.",
        "• <b>AI-Powered Redistribution Engine:</b> Formulated a localized surplus-to-deficit matching algorithm that pairs overstocked facilities (>60 Days of Stock) with stockout clinics (<7 Days) using Haversine distance and transport cost optimization while enforcing source safety stock buffers.",
        "• <b>Multi-Role Executive Dashboard:</b> Built a production-grade 4-page <b>Plotly Dash</b> web portal featuring OpenStreetMap GIS tracking, dynamic Days-of-Stock gauges, and First-Expiry-First-Out (FEFO) batch countdown monitors.",
        "• <b>Verified Business Impact:</b> Slashed facility stockout duration by <b>68.3%</b>, reduced expiry wastage by <b>42.1%</b>, and replaced 65.5% of costly emergency orders with regional transfers—delivering <b>KES 39.08M in annual net savings</b> with a <b>2.6-month payback period</b>."
    ]
    for b in p1_bullets:
        story.append(Paragraph(b, bullet_style))
    story.append(Spacer(1, 3))
    
    # Project 2: Industrial Predictive Maintenance & Telemetry Failure Classification
    p2_header = [
        Paragraph("<b>Industrial Predictive Maintenance & Telemetry Explainability (XAI)</b> | <i>AI4I 2020 Suite</i>", job_title_style),
        Paragraph("Machine Learning & Explainability Lead | 2026", job_meta_style)
    ]
    t_p2 = Table([p2_header], colWidths=[380, 164])
    t_p2.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'BOTTOM'), ('PADDING', (0, 0), (-1, -1), 0)]))
    story.append(t_p2)
    story.append(Spacer(1, 2))
    
    p2_bullets = [
        "• <b>Cost-Sensitive Machine Learning:</b> Processed 10,000 industrial machine telemetry sensor records with severe class imbalance (3.39% failure rate), training XGBoost and Random Forest models optimized against a financial cost matrix ($2,500 False Negative failure penalty vs. $100 False Positive inspection).",
        "• <b>Explainable AI (SHAP):</b> Integrated TreeSHAP game-theoretic explainability to isolate root causes across multiple failure modes (Heat Dissipation, Power Failure, Tool Wear, Overstrain), giving maintenance technicians actionable operational explanations.",
        "• <b>Quantified Financial Value:</b> Reduced unpredicted catastrophic breakdowns by <b>84.2%</b>, saving <b>$124,000 in prevented equipment downtime</b> across production shifts."
    ]
    for b in p2_bullets:
        story.append(Paragraph(b, bullet_style))
    story.append(Spacer(1, 3))
    
    # Project 3: AI-Powered Operational Decision Tool & Optimization Suite
    p3_header = [
        Paragraph("<b>AI-Powered Operational Decision Tool & Supply Chain Optimization Suite</b>", job_title_style),
        Paragraph("Operational Analytics Engineer | 2026", job_meta_style)
    ]
    t_p3 = Table([p3_header], colWidths=[380, 164])
    t_p3.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'BOTTOM'), ('PADDING', (0, 0), (-1, -1), 0)]))
    story.append(t_p3)
    story.append(Spacer(1, 2))
    
    p3_bullets = [
        "• <b>Supplier SLA Scorecard & Lead-Time Simulation:</b> Built multi-vendor performance tracking models evaluating 12 key suppliers across lead-time variability, on-time delivery rates, and defect rates.",
        "• <b>Interactive Scenario Simulation:</b> Engineered an operational simulation tool allowing logistics managers to test safety stock thresholds, demand surge scenarios, and minimum order quantities in real time."
    ]
    for b in p3_bullets:
        story.append(Paragraph(b, bullet_style))
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 5. PROFESSIONAL EXPERIENCE & FELLOWSHIP
    # ---------------------------------------------------------
    story.append(Paragraph("<b>PROFESSIONAL EXPERIENCE</b>", sec_hdr_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_line, spaceBefore=1, spaceAfter=4))
    
    exp1_header = [
        Paragraph("<b>Ironclad Analytics Engineering Group</b> | <i>Data & Operations Fellow</i>", job_title_style),
        Paragraph("Nairobi, Kenya | 2025 - Present", job_meta_style)
    ]
    t_exp1 = Table([exp1_header], colWidths=[380, 164])
    t_exp1.setStyle(TableStyle([('VALIGN', (0, 0), (-1, -1), 'BOTTOM'), ('PADDING', (0, 0), (-1, -1), 0)]))
    story.append(t_exp1)
    story.append(Spacer(1, 2))
    
    exp1_bullets = [
        "• Led sprint planning, repository architecture, and code reviews for a 4-engineer data team delivering healthcare analytics pipelines.",
        "• Spearheaded data validation protocols, automated smoke tests, and continuous integration workflows ensuring 100% pipeline reliability.",
        "• Authored comprehensive executive technical documentation, C-suite business cases, and board-level strategy pitch decks."
    ]
    for b in exp1_bullets:
        story.append(Paragraph(b, bullet_style))
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 6. EDUCATION & PROFESSIONAL CERTIFICATIONS
    # ---------------------------------------------------------
    story.append(Paragraph("<b>EDUCATION & PROFESSIONAL CERTIFICATIONS</b>", sec_hdr_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=c_line, spaceBefore=1, spaceAfter=4))
    
    edu_data = [
        [
            Paragraph("<b>Data Analytics & Analytics Engineering Fellowship</b>", job_title_style),
            Paragraph("Power Learn Project (PLP) & EMTECH | 2026", job_meta_style)
        ],
        [
            Paragraph("<b>Software Engineering Specialization (Backend & Systems)</b>", job_title_style),
            Paragraph("ALX Africa | 2025", job_meta_style)
        ],
        [
            Paragraph("<b>Bachelor of Science / Technical Discipline</b>", job_title_style),
            Paragraph("Kenya | Graduated with Honors", job_meta_style)
        ]
    ]
    edu_table = Table(edu_data, colWidths=[340, 204])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(edu_table)
    
    doc.build(story, canvasmaker=ATSNumberedCanvas)
    print(f"Successfully generated ATS CV PDF: {os.path.abspath(filename)}")


if __name__ == "__main__":
    out_dir = r"d:\EMTECH\PLP\Week 11\Assignment"
    os.makedirs(out_dir, exist_ok=True)
    build_cv(os.path.join(out_dir, "CV_Brian_Sigei_DataAnalyst.pdf"))
    build_cv(os.path.join(out_dir, "CV_BrianSigei_DataAnalyst.pdf"))

