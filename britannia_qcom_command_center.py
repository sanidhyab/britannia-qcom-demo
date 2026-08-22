import streamlit as st
import pandas as pd
import numpy as np
import json
import time
import matplotlib.pyplot as plt

# Define Color Palette and Styles
PRIMARY_COLOR = "#1B4332"  # Forest Green
ACCENT_COLOR = "#D97706"   # Ochre Gold
BG_COLOR = "#FAF8F5"       # Warm Cream
CARD_BG = "#FFFFFF"

# Page Configurations
st.set_page_config(
    page_title="Britannia Q-Com Smart Replenishment Command Center",
    page_icon="🍪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject Custom CSS for Premium Look
st.markdown(f"""
<style>
    .reportview-container {{
        background-color: {BG_COLOR};
        color: {PRIMARY_COLOR};
    }}
    h1, h2, h3, h4 {{
        font-family: 'Georgia', serif;
        color: {PRIMARY_COLOR} !important;
        font-weight: bold;
    }}
    .metric-card {{
        background-color: {CARD_BG};
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid {ACCENT_COLOR};
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }}
    .api-box {{
        background-color: #1E1E1E;
        color: #A9FF54;
        font-family: 'Courier New', Courier, monospace;
        padding: 15px;
        border-radius: 8px;
        font-size: 13px;
        overflow-x: auto;
    }}
    .stButton>button {{
        background-color: {PRIMARY_COLOR};
        color: white;
        border-radius: 6px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: {ACCENT_COLOR};
        color: white;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar Branding & Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/e/e4/Globe_icon_2.svg", width=50) # Generic clean anchor logo
st.sidebar.markdown(f"<h2 style='text-align: center; color: {PRIMARY_COLOR};'>BRITANNIA</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; font-style: italic; font-size: 13px;'>Quick Commerce Replenishment Operations</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navigation Console",
    ["Executive Dashboard", "Real-Time B2B API Simulator", "Dynamic Routing Engine", "Feasibility & P&L Calculator"]
)

# ----------------- DATA PREPARATION -----------------
@st.cache_data
def load_mock_data():
    dark_stores = pd.DataFrame({
        'Dark Store ID': [f'DS-{100+i}' for i in range(8)],
        'Platform': ['Blinkit', 'Zepto', 'Swiggy Instamart', 'Blinkit', 'Zepto', 'Instamart', 'Blinkit', 'Zepto'],
        'Zone': ['Delhi South', 'Delhi East', 'Noida Sec 62', 'Gurgaon Ph 3', 'Delhi West', 'Noida Sec 15', 'Gurgaon Sec 45', 'Delhi South-2'],
        'Demand Rate (Cases/Day)': [45, 30, 25, 60, 40, 20, 55, 35],
        'Current Stock (Days)': [1.2, 0.5, 2.1, 0.4, 1.8, 0.9, 0.6, 2.5]
    })
    return dark_stores

dark_stores_df = load_mock_data()

# ----------------- PAGE 1: EXECUTIVE DASHBOARD -----------------
if menu == "Executive Dashboard":
    st.markdown("# 🍪 Britannia Q-Com Smart Replenishment Command Center")
    st.markdown("### *Operational Overview of Localized 3PL Micro-Fulfillment Operations*")
    st.markdown("---")
    
    # Hero Metric Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <span style="font-size:14px; color:#6B7280; font-weight:600;">CHANNEL SCALE (FY25)</span><br>
            <span style="font-size:28px; font-weight:bold; color:{PRIMARY_COLOR};">₹675.0 Cr</span>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <span style="font-size:14px; color:#6B7280; font-weight:600;">ACTIVE SYSTEM FILL RATE</span><br>
            <span style="font-size:28px; font-weight:bold; color:#10B981;">99.6%</span><br>
            <span style="font-size:12px; color:#10B981;">▲ +11.6% vs Legacy Depot</span>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <span style="font-size:14px; color:#6B7280; font-weight:600;">AVG REPLENISHMENT SLA</span><br>
            <span style="font-size:28px; font-weight:bold; color:{PRIMARY_COLOR};">4.8 Hours</span><br>
            <span style="font-size:12px; color:#10B981;">▼ Compressed from 36h</span>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <span style="font-size:14px; color:#6B7280; font-weight:600;">GATE DISCREPANCY RATE</span><br>
            <span style="font-size:28px; font-weight:bold; color:#10B981;">0.15%</span><br>
            <span style="font-size:12px; color:#10B981;">▼ Resolved at Gate</span>
        </div>
        """, unsafe_allow_html=True)

    # Main Grid Layout
    left_col, right_col = st.columns([2, 1])
    
    with left_col:
        st.markdown("### 🏬 Real-Time Dark Store Inventory Alert Panel")
        # Highlights critical inventory alerts
        alert_df = dark_stores_df.copy()
        def highlight_stock(val):
            color = '#FEE2E2' if val < 1.0 else '#ECFDF5'
            text_color = '#991B1B' if val < 1.0 else '#065F46'
            return f'background-color: {color}; color: {text_color}; font-weight: bold;'
        
        st.dataframe(alert_df.style.applymap(highlight_stock, subset=['Current Stock (Days)']), use_container_width=True)
        st.markdown("<p style='font-size: 12px; color: #6B7280;'>*Alert trigger threshold is set to <1.0 days of safety stock. System automatically fires API dispatch protocols for flagged nodes.</p>", unsafe_allow_html=True)

    with right_col:
        st.markdown("### 🏆 National Champion Frameworks Used")
        st.markdown(f"""
        *   **SCOR 12.0 Model Alignment:** Physically decoupling 'Deliver' and 'Source' networks to insulate factory schedules from quick commerce demand spikes.
        *   **Geospatial Siting Analytics:** Locating city-side 3PL MFC nodes using a **Weighted K-Means** and **Greenfield Optimization Model** based on dark store cluster density.
        *   **Voronoi Load Rebalancing:** Dynamic load shifting to avoid node congestion.
        *   **Portfolio Premiumization:** Strategic shift to high-margin indulgence SKUs to absorb quick commerce delivery SLA overheads.
        """)

# ----------------- PAGE 2: B2B API SIMULATOR -----------------
elif menu == "Real-Time B2B API Simulator":
    st.markdown("# 🔌 Real-Time B2B API Middleware Console")
    st.markdown("### *Simulating the Automated Order-to-Cash Lifecycle Connecting Platforms to Britannia's OMS*")
    st.markdown("---")

    st.markdown("Select an operational event to trigger our custom-designed REST APIs and view real-time request-response JSON logs:")
    
    api_selection = st.selectbox(
        "Select Supply Chain Trigger Event:",
        [
            "1. Platform cuts PO (Instant Order Retrieval API)",
            "2. Dispatch Fleet Leaves MFC (Dynamic Slot Scheduling API)",
            "3. Gate-Level Shortage Resolved (Goods Discrepancy Note API)"
        ]
    )
    
    trigger_btn = st.button("🔌 Fire API REST Call")
    
    if trigger_btn:
        st.info("Sending encrypted REST API payload to middleware...")
        time.sleep(0.4)
        
        if "1." in api_selection:
            st.success("API Transaction Successful! (HTTP 201 Created)")
            req_json = {
                "header": {"auth_token": "bearer_brit_qcom_991823x", "content_type": "application/json"},
                "endpoint": "GET /v1/supply-orders",
                "parameters": {"status": "OPEN", "limit": 100}
            }
            res_json = {
                "status": "success",
                "retrieved_orders": [
                    {
                        "order_id": "PO-BLINK-9902",
                        "platform": "Blinkit",
                        "dark_store_id": "DS-103",
                        "order_timestamp": "2026-08-22T07:18:22Z",
                        "po_validity_remaining_minutes": 180,
                        "line_items": [
                            {"sku": "Good Day Choco Chip 120g", "units_ordered": 240, "allocated": True},
                            {"sku": "Bourbon Premium 150g", "units_ordered": 120, "allocated": True}
                        ]
                    }
                ],
                "oms_reconciliation": {
                    "auto_allocated_at": "2026-08-22T07:19:10Z",
                    "status": "LOCKED"
                }
            }
        elif "2." in api_selection:
            st.success("API Transaction Successful! (HTTP 200 OK)")
            req_json = {
                "endpoint": "PATCH /v1/supply-orders/PO-BLINK-9902/status",
                "payload": {
                    "status": "DISPATCHED",
                    "vehicle_id": "DL-1L-Y-9011",
                    "driver_contact": "+919876543210",
                    "current_gps": {"lat": 28.5355, "lng": 77.2410},
                    "estimated_arrival": "2026-08-22T08:15:00Z"
                }
            }
            res_json = {
                "status": "success",
                "appointment_slot": {
                    "scheduled_gate": "Gate 3 - Inbound",
                    "allocated_window": "08:15 AM - 08:30 AM",
                    "sla_breach_threshold": "08:45 AM",
                    "dynamic_dock_assignment_id": "DOCK-12"
                }
            }
        else:
            st.success("API Transaction Successful! (HTTP 200 OK)")
            req_json = {
                "endpoint": "POST /v1/supply-orders/PO-BLINK-9902/discrepancy",
                "payload": {
                    "gate_arrival_timestamp": "2026-08-22T08:14:12Z",
                    "physical_count": {
                        "Good Day Choco Chip 120g": {"delivered": 240, "damaged": 2},
                        "Bourbon Premium 150g": {"delivered": 118, "damaged": 0}
                    },
                    "logged_by": "Gate_Officer_DS-103"
                }
            }
            res_json = {
                "status": "reconciled",
                "action_taken": "Digital Invoice Adjusted Instantly",
                "original_bill_value": "₹34,200.00",
                "reconciled_bill_value": "₹33,840.00",
                "single_grn_status": "COMPLIANT_AND_CLOSED",
                "settlement_horizon": "T+7 (Eligible for automated sweep)"
            }
            
        col_req, col_res = st.columns(2)
        with col_req:
            st.markdown("#### **API Request Body (OMS -> Platform)**")
            st.code(json.dumps(req_json, indent=2), language="json")
        with col_res:
            st.markdown("#### **API Response Body (Platform -> OMS)**")
            st.code(json.dumps(res_json, indent=2), language="json")

# ----------------- PAGE 3: ROUTING ENGINE -----------------
elif menu == "Dynamic Routing Engine":
    st.markdown("# 🗺️ Machine Learning Dynamic Routing & Siting Engine")
    st.markdown("### *Simulating Greenfield Siting Sourcing Decision Models*")
    st.markdown("---")

    st.markdown("""
    When an automated alert fires, Britannia's ERP determines whether to fulfill the order via the specialized **city-side MFC** (high-speed milk-runs) or a **Regional central DC** (higher volume replenishment), utilizing Greenfield Siting coordinates.
    """)
    
    col_input, col_viz = st.columns([1, 1.5])
    
    with col_input:
        st.markdown("### **Fulfillment Decision Variables**")
        ds_select = st.selectbox("Select Targeting Dark Store Node:", dark_stores_df['Dark Store ID'].tolist())
        target_store = dark_stores_df[dark_stores_df['Dark Store ID'] == ds_select].iloc[0]
        
        st.info(f"Targeting Store Parameters:\n- Platform: {target_store['Platform']}\n- Zone: {target_store['Zone']}\n- Current Stock: {target_store['Current Stock (Days)']} Days")
        
        distance = st.slider("Distance from Local MFC (km):", 1.0, 30.0, 8.5, step=0.5)
        mfc_stock = st.slider("Current MFC SKU Stock Level (Cases):", 0, 500, 150, step=10)
        urgency = st.radio("Order Priority Horizon:", ["CRITICAL (SLA Breach Risk <3h)", "STANDARD (Restocking Cycle)"])
        
        calc_btn = st.button("🧠 Run Routing Optimization Model")
        
    with col_viz:
        st.markdown("### **Geospatial Fulfillment Siting Decision Model**")
        
        if calc_btn:
            # Simple decision model logic based on variables
            is_mfc = True
            reasons = []
            
            if distance > 15.0:
                is_mfc = False
                reasons.append("Distance exceeds 15km suburban threshold (MFC service limits)")
            if mfc_stock < 50:
                is_mfc = False
                reasons.append("MFC safety stock under replenishment threshold (<50 cases)")
            if urgency == "STANDARD (Restocking Cycle)" and distance > 12.0:
                is_mfc = False
                reasons.append("Standard restocking routed to central Mother DC to minimize 3PL secondary costs")
                
            if is_mfc:
                st.success("🎯 DECISION: Route through LOCAL CITY-SIDE 3PL MFC")
                st.markdown(f"""
                **Reasoning Matrix:**
                *   Distance ({distance} km) falls within the **under-15km dynamic Voronoi boundary**.
                *   MFC Stock ({mfc_stock} cases) is robustly above threshold.
                *   Replenishment Lead Time: **<3.5 Hours** (Guaranteed SLA compliance).
                """)
            else:
                st.warning("🚛 DECISION: Route through MOTHER DC / REGIONAL DEPOT")
                st.markdown(f"""
                **Reasoning Matrix:**
                *   **Friction triggers:** {', '.join(reasons)}.
                *   Replenishment Lead Time: **24–36 Hours**.
                *   System auto-updates delivery appointment window to next scheduled platform bulk slot.
                """)
                
            # Render a clean conceptual matplot map of the nodes
            fig, ax = plt.subplots(figsize=(6, 4))
            fig.patch.set_facecolor('#FAF8F5')
            ax.set_facecolor('#FFFFFF')
            
            # Nodes coordinates (mocking spatial layout)
            # Central DC (0,0), MFC (4,4), DS (based on distance)
            ax.plot(0, 0, marker='H', color='#1B4332', markersize=15, label='Central Mother DC', linestyle='None')
            ax.plot(4, 4, marker='s', color='#D97706', markersize=12, label='3PL City MFC', linestyle='None')
            
            # Target Store Position
            theta = np.radians(45)
            ds_x = 4 + distance * np.cos(theta) * 0.4
            ds_y = 4 + distance * np.sin(theta) * 0.4
            ax.plot(ds_x, ds_y, marker='o', color='#EF4444', markersize=10, label=f'Target {ds_select}', linestyle='None')
            
            # Draw line for route
            if is_mfc:
                ax.plot([4, ds_x], [4, ds_y], color='#D97706', linestyle='--', label='Agile Delivery Route')
            else:
                ax.plot([0, ds_x], [0, ds_y], color='#1B4332', linestyle=':', label='Bulk Secondary Route')
                
            ax.grid(True, linestyle=':', alpha=0.6)
            ax.legend(facecolor='#FAF8F5', edgecolor='#E5E7EB')
            ax.set_title("Operational Geospatial Layout Projection", fontsize=10, fontweight='bold', color='#1B4332')
            st.pyplot(fig)
        else:
            st.info("Set variables and click button to run simulation model.")

# ----------------- PAGE 4: P&L CALCULATOR -----------------
# ----------------- PAGE 4: P&L CALCULATOR -----------------
elif menu == "Feasibility & P&L Calculator":
    st.markdown("# 📊 Executive Boardroom P&L Feasibility Calculator")
    st.markdown("### *Simulating the Pilot P&L and Payback Horizons*")
    st.markdown("---")

    st.markdown("""
    FMCG executives challenge quick commerce solutions on logistics costs. Use this simulator to prove to the board how **Portfolio Premiumization** and **Stockout Recovery** completely offset the operational costs of city-side 3PL MFC operations.
    
    This model utilizes validated, grounded industry benchmarks for FMCG brands (including actual ₹675 Cr Britannia Q-Com scale) to test financial feasibility under conservative and rigorous operational constraints.
    """)

    col_slide, col_chart = st.columns([1.2, 1.5])
    
    with col_slide:
        st.markdown("### **1. Scope & Scale Configurations**")
        qcom_revenue = st.slider(
            "Britannia Q-Com National Sales Baseline (₹ Cr):", 
            200, 1500, 675, step=25,
            help="Grounded in FY25 actuals, representing ~4% of Britannia's domestic revenue."
        )
        
        pilot_scope = st.radio(
            "Fulfillment Implementation Scope:",
            [
                "Regional Pilot (Delhi NCR + Mumbai) - 40% of National Base",
                "National Rollout (Top 10 Metros) - 100% of National Base"
            ],
            help="Metros like Delhi and Mumbai account for ~40% of India's Q-Com sales. Rollout covers full scale."
        )
        
        recovery_rate = st.slider(
            "Sales Recovery Rate (% of Addressable Sales Base):",
            2.0, 15.0, 6.0, step=0.5,
            help="Conserving a 12% stockout rate. A realistic sales recovery rate (6% to 8%) represents actual returned purchase capture."
        )
        
        st.markdown("---")
        st.markdown("### **2. Assortment Strategy**")
        assortment_strategy = st.radio(
            "Product Assortment Portfolio Strategy:",
            [
                "Traditional GT Biscuit Mix (Marie Gold, Tiger)",
                "Q-Com Premium Assortment (Good Day Chunkies, Cheese, Gifting)"
            ],
            help="Traditional Trade biscuits carry low gross margins (25-30%) and cannot support Q-Com costs. Premiumization shifts gross margins to 45-50%."
        )
        
        if assortment_strategy == "Q-Com Premium Assortment (Good Day Chunkies, Cheese, Gifting)":
            premium_gross_margin = st.slider("Premium SKU Gross Margin (%):", 40.0, 55.0, 48.0, step=1.0)
            is_premium = True
        else:
            gross_margin = 28.0
            is_premium = False
            st.warning("Traditional biscuits are locked at a low Gross Margin of 28.0%.")
            
        st.markdown("---")
        with st.expander("🛠️ Advanced Platform & Logistics Costs"):
            base_commission = st.slider("Negotiated Base Platform Commission (% of Sales):", 10.0, 25.0, 18.0, step=0.5)
            ads_spending = st.slider("Dedicated In-App Performance Ads Spend (% of Sales):", 2.0, 15.0, 6.0, step=0.5)
            promos_funding = st.slider("Promotional Co-Funding & Invoice Discrepancies (% of Sales):", 2.0, 15.0, 6.0, step=0.5)
            logistics_cost = st.slider("3PL Local MFC & Daily Milk-Run Fleet Operations (% of Sales):", 2.0, 15.0, 6.0, step=0.5)

        st.markdown("---")
        st.markdown("### **3. Investment Requirements**")
        mfc_capex = st.slider("Upfront Setup CapEx (₹ Cr):", 1.0, 15.0, 4.0, step=0.5, help="Includes REST API middleware licensing, sorting automation, and local facility setup.")
        mfc_opex = st.slider("Annual Pilot Operations OpEx (₹ Cr/year):", 0.5, 5.0, 1.0, step=0.1, help="Covers localized 3PL transit fleets, operations, and overheads.")
        
    with col_chart:
        st.markdown("### **Feasibility & EBITDA Summary Output**")
        
        # Calculations
        # 1. Determine addressable revenue base
        if "Regional Pilot" in pilot_scope:
            addressable_base = qcom_revenue * 0.40
            st.info(f"📍 Addressable regional sales base for pilot: ₹{addressable_base:.1f} Cr (40% of national scale)")
        else:
            addressable_base = qcom_revenue
            st.info(f"🌐 Addressable national sales base for rollout: ₹{addressable_base:.1f} Cr (100% of national scale)")
            
        # 2. Recovered Sales
        recovered_sales = addressable_base * (recovery_rate / 100.0)
        
        # 3. Margins
        total_platform_cost = base_commission + ads_spending + promos_funding
        
        if is_premium:
            gross_margin = premium_gross_margin
            net_margin = gross_margin - total_platform_cost - logistics_cost
        else:
            gross_margin = 28.0
            net_margin = gross_margin - total_platform_cost - logistics_cost
            
        # 4. Cash Flows
        incremental_ebitda = recovered_sales * (net_margin / 100.0)
        net_cash_flow = incremental_ebitda - mfc_opex
        
        if net_cash_flow > 0:
            payback_years = mfc_capex / net_cash_flow
            payback_months = payback_years * 12.0
            roi = (net_cash_flow / mfc_capex) * 100.0
        else:
            payback_months = 999.0
            roi = (net_cash_flow / mfc_capex) * 100.0 if mfc_capex > 0 else 0.0

        col_out1, col_out2 = st.columns(2)
        with col_out1:
            st.metric(
                label="Recovered Revenue (Yr 1)",
                value=f"₹{recovered_sales:.2f} Cr",
                delta=f"{recovery_rate:.1f}% Sales Captured"
            )
            
            # Highlight EBITDA in green if positive, red if negative
            if incremental_ebitda >= 0:
                st.metric(
                    label="Incremental EBITDA (Yr 1)",
                    value=f"₹{incremental_ebitda:.2f} Cr",
                    delta=f"Net Channel Margin: {net_margin:.1f}%",
                    delta_color="normal"
                )
            else:
                st.metric(
                    label="Incremental EBITDA (Yr 1)",
                    value=f"₹{incremental_ebitda:.2f} Cr",
                    delta=f"Net Channel Margin: {net_margin:.1f}%",
                    delta_color="inverse"
                )
        with col_out2:
            if payback_months < 999 and payback_months > 0:
                st.metric(
                    label="Investment Payback Period",
                    value=f"{payback_months:.1f} Months",
                    delta="COMPLETE BREAKEVEN",
                    delta_color="normal"
                )
            else:
                st.metric(
                    label="Investment Payback",
                    value="Infinite",
                    delta="OpEx Exceeds EBITDA",
                    delta_color="inverse"
                )
                
            if roi >= 0:
                st.metric(
                    label="First Year ROI (%)",
                    value=f"{roi:.1f}%",
                    delta="Positive Net Return",
                    delta_color="normal"
                )
            else:
                st.metric(
                    label="First Year ROI (%)",
                    value=f"{roi:.1f}%",
                    delta="Negative Cash Flow",
                    delta_color="inverse"
                )
            
        st.markdown("---")
        st.markdown("#### **Channel Margin Portfolio Comparison**")
        
        # Plot margin comparison bar chart
        fig2, ax2 = plt.subplots(figsize=(6, 3.2))
        fig2.patch.set_facecolor('#FAF8F5')
        ax2.set_facecolor('#FFFFFF')
        
        # Comparative data
        labels = ['Traditional (GT/MT)', 'Q-Com Core SKU', 'Q-Com Premium Assortment']
        gross_margins = [28.0, 28.0, premium_gross_margin if is_premium else 28.0]
        net_margins = [12.0, 28.0 - total_platform_cost - logistics_cost, net_margin if is_premium else -8.0]
        
        x = np.arange(len(labels))
        width = 0.35
        
        rects1 = ax2.bar(x - width/2, gross_margins, width, label='Gross Margin (%)', color='#1B4332')
        rects2 = ax2.bar(x + width/2, net_margins, width, label='Net Contribution Margin (%)', color='#D97706')
        
        # Add a baseline grid and line at 0% margin
        ax2.axhline(0, color='black', linewidth=0.8, linestyle='--')
        
        ax2.set_xticks(x)
        ax2.set_xticklabels(labels, fontsize=8)
        ax2.set_ylabel('Percentage (%)', fontsize=8)
        ax2.legend(fontsize=8, facecolor='#FAF8F5', edgecolor='#E5E7EB')
        ax2.grid(True, axis='y', linestyle=':', alpha=0.6)
        ax2.set_ylim(-20, 60)
        
        # Label values on bars for high-impact visual representation
        for rect in rects1:
            height = rect.get_height()
            ax2.annotate(f'{height:.0f}%',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 2 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=7)
                        
        for rect in rects2:
            height = rect.get_height()
            # If negative margin, position text slightly below the bar
            va_pos = 'top' if height < 0 else 'bottom'
            xy_off = -10 if height < 0 else 2
            ax2.annotate(f'{height:.1f}%',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, xy_off),  # vertical offset
                        textcoords="offset points",
                        ha='center', va=va_pos, fontsize=7, fontweight='bold')
        
        st.pyplot(fig2)
        st.markdown("<p style='font-size: 11px; text-align: center; color: #6B7280;'>*Standard Q-Com SKUs yield a negative contribution margin (approx. -8%) under traditional cost structures. Premiumizing our Q-Com assortment (inducing 48% Gross Margin) easily absorbs the 30% platform take-rate and 6% logistics cost to deliver a highly viable 12% net channel contribution.</p>", unsafe_allow_html=True)
