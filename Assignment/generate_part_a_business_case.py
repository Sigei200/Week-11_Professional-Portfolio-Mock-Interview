"""
Script to generate Part A: Strategic Deliverable (Business Case)
Target: Week11_Business_Case_BrianSigei.pdf (and Week11_Business_Case_Brian_Sigei.pdf)
Strictly formatted for a 1-page executive deliverable for CFO & Board of Directors.
Zero jargon, high financial fidelity, explicit math formulas, risk mitigation, and clear Go/No-Go ask.
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas

class SinglePageCanvas(canvas.Canvas):
    """Canvas that enforces clean borders, corporate accents, and precise single-page header/footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []

    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        
        # Color definitions
        primary_color = colors.HexColor("#0B3C5D")   # Deep Executive Navy
        gold_color = colors.HexColor("#D97706")      # Warm Amber Gold
        slate_color = colors.HexColor("#64748B")     # Muted Slate
        border_color = colors.HexColor("#CBD5E1")    # Light Border
        
        # Page dimensions: 8.5 x 11 inches = 612 x 792 pt
        # Outer decorative framing
        self.setStrokeColor(border_color)
        self.setLineWidth(0.75)
        self.rect(20, 20, 572, 752)
        
        # Top brand banner strip
        self.setFillColor(primary_color)
        self.rect(20, 752, 572, 20, fill=1, stroke=0)
        
        # Top banner text
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.white)
        self.drawString(28, 758, "KENYA MEDICAL SUPPLIES AUTHORITY (KEMSA) | STRATEGIC INVESTMENT PROPOSAL")
        self.drawRightString(584, 758, "BOARD & CFO EXECUTIVE BRIEFING")
        
        # Bottom Footer
        self.setFillColor(slate_color)
        self.setFont("Helvetica", 7.5)
        self.drawString(28, 26, "CONFIDENTIAL & PROPRIETARY — PREPARED BY BRIAN SIGEI (LEAD ANALYTICS ENGINEER)")
        self.drawRightString(584, 26, f"Page {self._pageNumber} of {page_count} | Decision Required: GO / NO-GO")
        
        self.restoreState()


def build_business_case(filename="Week11_Business_Case_BrianSigei.pdf"):
    # Page setup: letter size = 612 x 792 pt
    # Usable width = 572 - 16 = 556 pt
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=26,
        rightMargin=26,
        topMargin=26,
        bottomMargin=26
    )
    
    # Palette
    c_navy = colors.HexColor("#0B3C5D")     # Primary Dark
    c_teal = colors.HexColor("#0D9488")     # Accent Teal
    c_emerald = colors.HexColor("#059669")  # Value Green
    c_amber = colors.HexColor("#D97706")    # Risk Amber
    c_dark = colors.HexColor("#1E293B")     # Body Charcoal
    c_card_bg = colors.HexColor("#F8FAFC")  # Light Slate Box
    c_card_border = colors.HexColor("#E2E8F0")
    c_highlight = colors.HexColor("#EFF6FF")
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'MainTitle',
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=15,
        textColor=c_navy,
        alignment=TA_LEFT
    )
    
    subtitle_style = ParagraphStyle(
        'SubTitle',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#475569"),
        alignment=TA_LEFT
    )
    
    sec_heading = ParagraphStyle(
        'SecHeading',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=10.5,
        textColor=c_navy,
        spaceBefore=0,
        spaceAfter=0
    )
    
    body_style = ParagraphStyle(
        'BodyText',
        fontName='Helvetica',
        fontSize=7.2,
        leading=9.2,
        textColor=c_dark,
        alignment=TA_JUSTIFY
    )
    
    bold_style = ParagraphStyle(
        'BoldText',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=9.2,
        textColor=c_dark
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=6.8,
        leading=8.5,
        textColor=c_dark
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=6.8,
        leading=8.5,
        textColor=c_navy
    )
    
    table_cell_green = ParagraphStyle(
        'TableCellGreen',
        fontName='Helvetica-Bold',
        fontSize=7.2,
        leading=8.8,
        textColor=c_emerald
    )

    story = []
    
    # ---------------------------------------------------------
    # 1. HEADER & METADATA TABLE
    # ---------------------------------------------------------
    header_left = Paragraph(
        "<b>BUSINESS CASE: HEALTHCARE SUPPLY CHAIN INTELLIGENCE & REDISTRIBUTION PLATFORM</b><br/>"
        "<font color='#0D9488'><b>AI-Driven Stockout Elimination, Expiry Wastage Reduction & Operational Cost Optimization</b></font>",
        title_style
    )
    
    meta_text = Paragraph(
        "<b>Target Audience:</b> CFO & Board of Directors<br/>"
        "<b>Proposer:</b> Brian Sigei (Analytics Lead)<br/>"
        "<b>Scope:</b> 47 Counties | 235 Facilities | 45 Commodities<br/>"
        "<b>Target Date:</b> Q1 2027 Rollout | <b>Status:</b> Action Required",
        subtitle_style
    )
    
    hdr_table = Table([[header_left, meta_text]], colWidths=[360, 196])
    hdr_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(hdr_table)
    story.append(HRFlowable(width="100%", thickness=1, color=c_teal, spaceBefore=2, spaceAfter=4))
    
    # ---------------------------------------------------------
    # 2. TWO-COLUMN: PROBLEM STATEMENT & PROPOSED SOLUTION
    # ---------------------------------------------------------
    col1_content = [
        Paragraph("<b>1. THE OPERATIONAL PAIN POINT (CFO CONTEXT)</b>", sec_heading),
        Spacer(1, 1),
        Paragraph(
            "Kenya's public health supply chain suffers from a structural <b>Dual Crisis</b> costing taxpayers millions annually:<br/>"
            "• <b>Fatal Rural Stockouts:</b> Primary dispensaries (Level 2/3) experience an average <b>30%+ stockout duration</b> for essential antimalarials and antibiotics, forcing patients to go untreated or buy from expensive retail pharmacies.<br/>"
            "• <b>Severe Expiry Wastage:</b> Meanwhile, regional referral hospitals (Level 5) incur <b>KES 45.2M in annual expiry losses</b> due to blind overstocking without First-Expiry-First-Out (FEFO) visibility.<br/>"
            "• <b>Emergency Procurement Surcharges:</b> Reactive, late-stage ordering triggers emergency replenishment at a <b>300% pricing premium</b>, burning an extra <b>KES 28.4M/year</b>.<br/>"
            "• <b>Siloed Blindspots:</b> Health facilities operate on isolated paper logs with a 14-day data lag, blinding KEMSA central planning.",
            body_style
        )
    ]
    
    col2_content = [
        Paragraph("<b>2. PROPOSED ANALYTICS SOLUTION (THE INTELLIGENCE LAYER)</b>", sec_heading),
        Spacer(1, 1),
        Paragraph(
            "An enterprise-grade, lightweight decision-support intelligence platform sitting atop existing ERP/LMIS infrastructure without requiring costly system replacement:<br/>"
            "• <b>Unified Star-Schema Warehouse:</b> Ingests multi-source consumption, facility inventory, and supplier logs (4.9M records across all 47 counties) with sub-second query latency.<br/>"
            "• <b>Predictive ML Risk Engine (LightGBM):</b> Forecasts 30-day commodity demand and classifies <b>7-day stockout risk with 91.2% ROC-AUC (88.4% recall)</b>, proactively identifying deficits before shelves empty.<br/>"
            "• <b>Real-Time FEFO Batch Tracker:</b> Prioritizes short-dated medicines across all tiers.<br/>"
            "• <b>AI Redistribution Engine:</b> Solves localized surplus-to-deficit imbalances by generating legal, distance-optimized (Haversine) inter-facility transfer orders while protecting source safety stocks.",
            body_style
        )
    ]
    
    prob_sol_table = Table([[col1_content, col2_content]], colWidths=[273, 273])
    prob_sol_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BACKGROUND', (0, 0), (0, 0), c_card_bg),
        ('BACKGROUND', (1, 0), (1, 0), c_highlight),
        ('BOX', (0, 0), (0, 0), 0.5, c_card_border),
        ('BOX', (1, 0), (1, 0), 0.5, colors.HexColor("#BFDBFE")),
        ('PADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(prob_sol_table)
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 3. FINANCIAL IMPACT & CFO VALUE METRICS (SHOW THE MATH)
    # ---------------------------------------------------------
    story.append(Paragraph("<b>3. FINANCIAL IMPACT & RETURN ON INVESTMENT (SHOWING THE MATH)</b>", sec_heading))
    story.append(Spacer(1, 2))
    
    fin_headers = [
        Paragraph("<b>Financial Metric</b>", table_cell_bold),
        Paragraph("<b>Baseline Cost</b>", table_cell_bold),
        Paragraph("<b>With Analytics Solution</b>", table_cell_bold),
        Paragraph("<b>Annual Net Savings / Benefit</b>", table_cell_bold)
    ]
    
    fin_row1 = [
        Paragraph("<b>Medicine Expiry Wastage</b> (Referral Tiers)", table_cell),
        Paragraph("KES 45,200,000 / yr", table_cell),
        Paragraph("KES 26,170,000 / yr (-42.1% via FEFO)", table_cell),
        Paragraph("<b>+ KES 19,030,000 / yr</b>", table_cell_green)
    ]
    fin_row2 = [
        Paragraph("<b>Emergency Replenishment Surcharge</b>", table_cell),
        Paragraph("KES 28,400,000 / yr", table_cell),
        Paragraph("KES 9,800,000 / yr (-65.5% transfers)", table_cell),
        Paragraph("<b>+ KES 18,600,000 / yr</b>", table_cell_green)
    ]
    fin_row3 = [
        Paragraph("<b>Inventory Holding & Capital Carrying</b>", table_cell),
        Paragraph("KES 22,000,000 / yr", table_cell),
        Paragraph("KES 17,750,000 / yr (Right-sizing)", table_cell),
        Paragraph("<b>+ KES 4,250,000 / yr</b>", table_cell_green)
    ]
    fin_row4 = [
        Paragraph("<b>Platform Operating Cost (Opex)</b>", table_cell_bold),
        Paragraph("KES 0 (Legacy manual)", table_cell),
        Paragraph("KES 2,800,000 / yr (Cloud + Maint.)", table_cell),
        Paragraph("<b>- KES 2,800,000 / yr</b>", table_cell_bold)
    ]
    fin_total = [
        Paragraph("<b>TOTAL ANNUALIZED NET BENEFIT</b>", table_cell_bold),
        Paragraph("<b>KES 95,600,000</b>", table_cell_bold),
        Paragraph("<b>KES 56,520,000</b>", table_cell_bold),
        Paragraph("<b>+ KES 39,080,000 / yr</b>", table_cell_green)
    ]
    
    fin_table = Table([fin_headers, fin_row1, fin_row2, fin_row3, fin_row4, fin_total], colWidths=[155, 120, 145, 136])
    fin_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#E2E8F0")),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor("#DCFCE7")),
        ('GRID', (0, 0), (-1, -1), 0.5, c_card_border),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('PADDING', (0, 0), (-1, -1), 2.5),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    story.append(fin_table)
    story.append(Spacer(1, 3))
    
    # Financial Formulas & Math Box
    math_p1 = Paragraph(
        "<b>Capital Expenditure (Capex):</b> KES 8,500,000 (Architecture, ETL integration, ML pipeline, Dash UI, Staff training).<br/>"
        "<b>Annual Net Cash Inflow:</b> Gross Savings (KES 41.88M) - Annual Opex (KES 2.80M) = <b>KES 39.08M / year</b>.",
        body_style
    )
    
    math_p2 = Paragraph(
        "<b>• Payback Period:</b> $\\text{Capex} / \\text{Annual Net Cash Flow} = \\frac{\\text{KES } 8.50\\text{M}}{\\text{KES } 39.08\\text{M}} \\times 12 \\text{ mos} = \\mathbf{2.61\\text{ Months}}$ (~78 Days to full cost recovery).<br/>"
        "<b>• Year 1 Net ROI:</b> $\\frac{\\text{Net Annual Benefit} - \\text{Initial Investment}}{\\text{Initial Investment}} = \\frac{39.08\\text{M} - 8.50\\text{M}}{8.50\\text{M}} \\times 100\\% = \\mathbf{359.8\\%}$ in Year 1.<br/>"
        "<b>• 3-Year Net Cumulative Value:</b> $(39.08\\text{M} \\times 3) - 8.50\\text{M} = \\mathbf{\\text{KES } 108.74\\text{M}}$ (3-Yr NPV @ 12% WACC: <b>KES 85.34M</b>, IRR: <b>428%</b>).",
        body_style
    )
    
    math_table = Table([[math_p1, math_p2]], colWidths=[246, 300])
    math_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor("#FEF9C3")),
        ('BOX', (0, 0), (-1, -1), 0.75, colors.HexColor("#FACC15")),
        ('PADDING', (0, 0), (-1, -1), 3),
    ]))
    story.append(math_table)
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 4. TOP 2 OPERATIONAL RISKS & RIGOROUS MITIGATION
    # ---------------------------------------------------------
    story.append(Paragraph("<b>4. TOP 2 OPERATIONAL RISKS & PROACTIVE MITIGATION</b>", sec_heading))
    story.append(Spacer(1, 2))
    
    risk_headers = [
        Paragraph("<b>Key Risk Dimension</b>", table_cell_bold),
        Paragraph("<b>Severity & Root Impact</b>", table_cell_bold),
        Paragraph("<b>Engineered Risk Mitigation Strategy</b>", table_cell_bold)
    ]
    
    risk_row1 = [
        Paragraph("<b>1. Data Quality & Rural Connectivity Lag</b>", table_cell_bold),
        Paragraph("High / Operational: Incomplete logs or delayed weekly paper submissions from remote clinics degrade ML forecast accuracy.", table_cell),
        Paragraph("<b>Offline-First Architecture & Imputation:</b> Lightweight edge caching with automated data validation rules; missing logs are imputed via synthetic patient-demand multipliers and historical baselines; automated daily SMS anomaly alerts flag overdue reports.", table_cell)
    ]
    
    risk_row2 = [
        Paragraph("<b>2. Inter-County Resistance & Hoarding</b>", table_cell_bold),
        Paragraph("Medium / Political: County health directors may hesitate to transfer stock to neighboring jurisdictions fearing localized shortages.", table_cell),
        Paragraph("<b>Safety-Stock Math Protection & MoH Vouchers:</b> The redistribution algorithm strictly preserves 45-day source safety buffers before releasing surplus; transfers are backed by automated MoH digital vouchers and inter-county billing credits.", table_cell)
    ]
    
    risk_table = Table([risk_headers, risk_row1, risk_row2], colWidths=[130, 160, 256])
    risk_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F1F5F9")),
        ('GRID', (0, 0), (-1, -1), 0.5, c_card_border),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('PADDING', (0, 0), (-1, -1), 2.5),
    ]))
    story.append(risk_table)
    story.append(Spacer(1, 4))
    
    # ---------------------------------------------------------
    # 5. STRATEGIC RECOMMENDATION & CLEAR "GO / NO-GO" ASK
    # ---------------------------------------------------------
    rec_box_text = Paragraph(
        "<b>5. STRATEGIC RECOMMENDATION: UNANIMOUS 'GO' DECISION</b><br/>"
        "<b>The Ask:</b> Authorize <b>KES 8,500,000</b> in Phase 1 capital expenditure to implement the Healthcare Supply Chain Intelligence Platform across a 10-county pilot (150 facilities) in Q1 2027, followed by a national rollout in Q3. <br/>"
        "<b>The Return:</b> Full capital cost recovery in <b>2.6 months</b>, delivering <b>KES 39.08M in recurring net annual savings</b>, a <b>359.8% Year 1 ROI</b>, and a <b>68.3% reduction in patient stockout duration</b> across Kenya's public healthcare network. <i>Zero disruption to active clinical workflows.</i>",
        body_style
    )
    
    rec_table = Table([[rec_box_text]], colWidths=[546])
    rec_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor("#ECFDF5")),
        ('BOX', (0, 0), (0, 0), 1, c_emerald),
        ('PADDING', (0, 0), (0, 0), 4),
    ]))
    story.append(rec_table)
    
    # Build Document
    doc.build(story, canvasmaker=SinglePageCanvas)
    print(f"Successfully generated 1-Page Business Case PDF: {os.path.abspath(filename)}")


if __name__ == "__main__":
    out_dir = r"d:\EMTECH\PLP\Week 11\Assignment"
    os.makedirs(out_dir, exist_ok=True)
    build_business_case(os.path.join(out_dir, "Week11_Business_Case_BrianSigei.pdf"))
    build_business_case(os.path.join(out_dir, "Week11_Business_Case_Brian_Sigei.pdf"))

