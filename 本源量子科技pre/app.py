import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 页面设置
st.set_page_config(
    page_title="Origin Quantum CFO Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select a Section",
    [
        "🏠 Home",
        "💎 Application Value Potential",
        "🌍 Market Opportunity",
        "💰 Investment Strategy",
        "🔚 End"
    ]
)

# ==========================
# HOME
# ==========================

if page == "🏠 Home":

    st.markdown("""
    <h1 style='text-align:center; margin-bottom:0px;'>
    CFO Dashboard: Origin Quantum
    </h1>

    <p style='text-align:right;
            color:#666666;
            font-size:20px;
            margin-top:0px;'>
    Financial Overview and Future Growth Strategy
    </p >

    <hr>
    """, unsafe_allow_html=True)

    st.image(
        "images/wukong.jpg",
        use_container_width=True
    )
   

# ==========================
# COMPANY SNAPSHOT
# ==========================

elif page == "💎 Application Value Potential":

    st.title("💎 Application Value Potential")
    st.caption("Current commercial maturity vs future market potential")

    with st.expander("📖 what is Commercial Maturity？"):
        st.markdown("""
        **商业成熟度（Commercial Maturity）**

        用来衡量一个应用距离实际商业化和产生收入有多近。

        分数越高，说明：

        - 客户需求越明确
        - 产品越成熟
        - 更容易产生稳定收入
        - 商业模式已经得到验证

        例如：

        🎓 Research & Education

        高校、科研院所已经在使用量子计算平台，
        因此商业成熟度较高。
        """)

    with st.expander("📖 what is Market Potential？"):
        st.markdown("""
        **市场潜力（Market Potential）**

        用来衡量一个应用未来可能创造的市场价值。

        分数越高，说明：

        - 市场规模更大
        - 长期增长空间更强
        - 对公司估值贡献更高

        例如：

        🤖 AI + Quantum

        当前商业化程度有限，
        但未来市场空间巨大，
        因此市场潜力非常高。
        """)
    # 数据：课堂展示用的战略评分，不是公司真实营收
    app_data = pd.DataFrame({
        "Application": [
            "Research & Education",
            "Quantum Cloud",
            "Industrial Solutions",
            "AI + Quantum",
            "Drug Discovery",
            "Advanced Materials"
        ],
        "Commercial Maturity": [90, 75, 60, 35, 25, 45],
        "Market Potential": [45, 60, 70, 95, 85, 80],
        "Strategic Importance": [55, 65, 70, 95, 85, 80],
        "Category": [
            "Current Revenue Driver",
            "Current Revenue Driver",
            "Current Revenue Driver",
            "Future Valuation Driver",
            "Future Valuation Driver",
            "Future Valuation Driver"
        ]
    })

    fig = px.scatter(
        app_data,
        x="Commercial Maturity",
        y="Market Potential",
        size="Strategic Importance",
        color="Category",
        text="Application",
        size_max=55,
        title="Application Portfolio: Revenue Today vs Value Tomorrow"
    )

    fig.update_traces(
        textposition="top center",
        marker=dict(
            line=dict(width=1.5, color="white")
        )
    )

    fig.update_layout(
        height=620,
        xaxis=dict(
            title="Commercial Maturity",
            range=[0, 100]
        ),
        yaxis=dict(
            title="Market Potential",
            range=[0, 100]
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        margin=dict(l=40, r=40, t=90, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        **💰 Current Revenue Drivers**

        Research & Education, Quantum Cloud, and Industrial Solutions are closer to commercialization and can support near-term revenue.
        """)

    with col2:
        st.success("""
        **🚀 Future Valuation Drivers**

        AI + Quantum, Drug Discovery, and Advanced Materials have higher long-term market potential and support future valuation growth.
        """)

    st.caption(
        "Note: Scores are strategic estimates for classroom visualization, not exact financial disclosure."
    )

# ==========================
# MARKET OPPORTUNITY
# ==========================

elif page == "🌍 Market Opportunity":

    st.title("Market Opportunity")
    st.header("🌍 Market Layers")
    st.caption("Global strategic market positioning of Origin Quantum")
    with st.expander("🏛 What are SOEs?"):
        st.markdown("""
        **SOEs = State-Owned Enterprises**

        中文：国有企业

        These are companies owned or controlled by the government.

        Examples include energy, telecommunications,
        transportation, and defense enterprises.

        SOEs are important potential customers for
        quantum computing solutions due to their large-scale
        optimization and simulation needs.
        """)
        
    # ==========================
    # 1. 市场层级数据
    # ==========================

    market_data = pd.DataFrame({
        "country": [
            "China",
            "Japan",
            "South Korea",
            "Singapore",
            "Germany",
            "France",
            "United Kingdom",
            "United States"
        ],
        "market_type": [
            "Core Market",
            "Collaboration Market",
            "Collaboration Market",
            "Collaboration Market",
            "Research Market",
            "Research Market",
            "Research Market",
            "Future Opportunity"
        ],
        "reason": [
            "Government support, universities, research institutes, SOEs, quantum cloud users",
            "Active quantum research and regional cooperation",
            "Advanced semiconductor and quantum research ecosystem",
            "Strong technology hub in Southeast Asia",
            "Strong European quantum research and national programs",
            "CNRS and strong scientific research base",
            "Leading universities and quantum technology programs",
            "Largest potential market, but strongest competition"
        ]
    })

    color_map = {
        "Core Market": "#dc2626",
        "Collaboration Market": "#2563eb",
        "Research Market": "#16a34a",
        "Future Opportunity": "#f97316"
    }

    # ==========================
    # 2. 合肥总部 + 目标市场坐标
    # ==========================

    hq = {
        "name": "Hefei HQ",
        "lat": 31.8206,
        "lon": 117.2272
    }

    market_points = pd.DataFrame({
        "country": [
            "China",
            "Japan",
            "South Korea",
            "Singapore",
            "Germany",
            "France",
            "United Kingdom",
            "United States"
        ],
        "lat": [
            35.8617,
            36.2048,
            35.9078,
            1.3521,
            51.1657,
            46.2276,
            55.3781,
            37.0902
        ],
        "lon": [
            104.1954,
            138.2529,
            127.7669,
            103.8198,
            10.4515,
            2.2137,
            -3.4360,
            -95.7129
        ],
        "market_type": [
            "Core Market",
            "Collaboration Market",
            "Collaboration Market",
            "Collaboration Market",
            "Research Market",
            "Research Market",
            "Research Market",
            "Future Opportunity"
        ]
    })

    # ==========================
    # 3. 页面布局：左地图 + 右说明
    # ==========================

    left, right = st.columns([2.2, 1])

    with left:

        fig = go.Figure()

        # 国家填色 Choropleth
        fig.add_trace(go.Choropleth(
            locations=market_data["country"],
            locationmode="country names",
            z=market_data["market_type"].map({
                "Core Market": 1,
                "Collaboration Market": 2,
                "Research Market": 3,
                "Future Opportunity": 4
            }),
            text=market_data["country"],
            customdata=market_data[["market_type", "reason"]],
            colorscale=[
                [0.00, "#dc2626"],
                [0.25, "#dc2626"],
                [0.26, "#2563eb"],
                [0.50, "#2563eb"],
                [0.51, "#16a34a"],
                [0.75, "#16a34a"],
                [0.76, "#f97316"],
                [1.00, "#f97316"]
            ],
            showscale=False,
            marker_line_color="white",
            marker_line_width=0.8,
            hovertemplate=
            "<b>%{text}</b><br>" +
            "Type: %{customdata[0]}<br>" +
            "Reason: %{customdata[1]}<extra></extra>"
        ))

        # 从合肥总部到各目标市场的连接线
        for _, row in market_points.iterrows():
            line_color = color_map[row["market_type"]]

            fig.add_trace(go.Scattergeo(
                lon=[hq["lon"], row["lon"]],
                lat=[hq["lat"], row["lat"]],
                mode="lines",
                line=dict(
                    width=2.3,
                    color=line_color
                ),
                opacity=0.55,
                showlegend=False
            ))

        # 目标市场点
        for market_type in market_points["market_type"].unique():
            df = market_points[market_points["market_type"] == market_type]

            fig.add_trace(go.Scattergeo(
                lon=df["lon"],
                lat=df["lat"],
                text=df["country"],
                mode="markers+text",
                marker=dict(
                    size=12,
                    color=color_map[market_type],
                    line=dict(width=1.5, color="white")
                ),
                textposition="bottom center",
                name=market_type
            ))

        # 合肥总部点
        fig.add_trace(go.Scattergeo(
            lon=[hq["lon"]],
            lat=[hq["lat"]],
            text=["HEFEI HQ"],
            mode="markers+text",
            marker=dict(
                size=24,
                color="#7f1d1d",
                line=dict(width=2.5, color="white")
            ),
            textposition="top center",
            name="Headquarters"
        ))

        fig.update_layout(
            height=680,
            margin=dict(l=0, r=0, t=20, b=0),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.02,
                xanchor="center",
                x=0.5
            ),
            geo=dict(
                projection_type="natural earth",
                showland=True,
                landcolor="rgb(243, 246, 250)",
                showocean=True,
                oceancolor="rgb(250, 252, 255)",
                showcountries=True,
                countrycolor="white",
                coastlinecolor="white",
                bgcolor="rgba(0,0,0,0)"
            )
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        st.markdown("""
        <div style="border-left:7px solid #dc2626;
                    padding:14px;
                    margin-bottom:14px;
                    background:#fff5f5;
                    border-radius:10px;">
        <h4>🇨🇳 Core Market</h4>
        <b>China</b><br>
        Primary market with government support, universities,
        research institutes, SOEs and quantum cloud users.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="border-left:7px solid #2563eb;
                    padding:14px;
                    margin-bottom:14px;
                    background:#eff6ff;
                    border-radius:10px;">
        <h4>🇯🇵 🇰🇷 🇸🇬 Collaboration Market</h4>
        <b>Japan / South Korea / Singapore</b><br>
        Regional technology hubs with active quantum research
        and cooperation opportunities.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="border-left:7px solid #16a34a;
                    padding:14px;
                    margin-bottom:14px;
                    background:#f0fdf4;
                    border-radius:10px;">
        <h4>🇩🇪 🇫🇷 🇬🇧 Research Market</h4>
        <b>Germany / France / United Kingdom</b><br>
        Strong scientific research base and national quantum programs.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div style="border-left:7px solid #f97316;
                    padding:14px;
                    margin-bottom:14px;
                    background:#fff7ed;
                    border-radius:10px;">
        <h4>🇺🇸 Future Opportunity</h4>
        <b>United States</b><br>
        Largest potential market, but also the strongest competition.
        </div>
        """, unsafe_allow_html=True)
    st.info(
        "China remains Origin Quantum's core market. "
        "East Asia and Europe provide research and collaboration opportunities, "
        "while North America represents a long-term strategic opportunity."
    )
    st.caption(
        "Note: This map shows strategic market opportunities, not exact revenue distribution."
    )
    st.divider()

    # ==========================
    # 2. MARKET SIZE FORECAST
    # ==========================

    st.header("📈 Market Size Forecast")
    st.caption("Global quantum computing market: historical data and CAGR-based forecast")

    market_size = pd.DataFrame({
        "Year": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
        "Market Size (USD Billion)": [0.72, 0.93, 1.42, 1.72, 2.07, 2.50, 3.01, 3.63, 4.37],
        "Type": [
            "Historical", "Historical", "Historical", "Historical",
            "Historical", "Forecast", "Forecast", "Forecast", "Forecast"
        ]
    })

    market_size["Growth Index"] = (
        market_size["Market Size (USD Billion)"] 
        / market_size.loc[market_size["Year"] == 2022, "Market Size (USD Billion)"].values[0] 
        * 100
    ).round(0)

    left, right = st.columns([2.2, 1])

    with left:
        fig = go.Figure()

        # 柱状图：市场规模
        fig.add_trace(go.Bar(
            x=market_size["Year"],
            y=market_size["Market Size (USD Billion)"],
            name="Market Size",
            text=market_size["Market Size (USD Billion)"],
            textposition="outside",
            marker_color=[
                "#2563eb" if t == "Historical" else "#93c5fd"
                for t in market_size["Type"]
            ]
        ))

        # 折线图：增长指数
        fig.add_trace(go.Scatter(
            x=market_size["Year"],
            y=market_size["Growth Index"],
            name="Growth Index",
            mode="lines+markers",
            yaxis="y2",
            line=dict(
                width=4,
                color="#dc2626"
            ),
            marker=dict(size=9)
        ))

        fig.update_layout(
            title="Global Quantum Computing Market Forecast",
            height=540,
            xaxis=dict(
                title="Year",
                tickmode="array",
                tickvals=market_size["Year"]
            ),
            yaxis=dict(
                title="Market Size (USD Billion)",
                range=[0, 5],
                showgrid=True
            ),
            yaxis2=dict(
                title="Growth Index (2022 = 100)",
                overlaying="y",
                side="right",
                range=[0, 650]
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5
            ),
            margin=dict(l=40, r=40, t=90, b=40)
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:
        st.markdown("### Key Metrics")

        st.metric("2025 Market Size", "$1.72B")
        st.metric("2030 Forecast", "$4.37B")
        st.metric("Expected CAGR", "20.5%")
        with st.expander("What does CAGR mean?"):
            st.write("""
            CAGR (Compound Annual Growth Rate) is the mean annual growth rate of an investment over a specified period of time longer than one year. 
            It represents one of the most accurate ways to calculate and determine returns for anything that can rise or fall in value over time.
            """)
        st.metric("Growth Multiple", "≈2.5x")
        with st.expander("What does Growth Multiple mean?"):
            st.write("""
            Growth Multiple is the factor by which the market size is expected to increase over a specific period. 
            In this case, the market is expected to grow approximately 2.5 times from 2025 to 2030.
            """)

        st.info(
            "The market is expected to more than double by 2030, "
            "which supports long-term investment in R&D, talent and infrastructure."
        )

    st.caption(
        "Note: 2026–2030 values are calculated using a 20.5% CAGR from the 2025 estimate. "
        "This chart is for classroom visualization."
    )

# ==========================
# INVESTMENT STRATEGY
# ==========================

elif page == "💰 Investment Strategy":

    st.title("Investment Strategy")
    st.caption("Financing history, IPO plan, and valuation logic")
    with st.expander("📖 What is IPO?"):
        st.markdown("""
        **IPO (Initial Public Offering)** is the process through which a private company becomes a publicly listed company.

        **Benefits:**
        - 💰 Raise capital from public investors
        - 📈 Increase company valuation
        - 🌟 Improve brand credibility
        - 🚀 Support long-term growth

        **Origin Quantum Status:**
        - Guidance filing completed: Sep 2025
        - Current stage: Pre-IPO
        - Target: STAR Market IPO
        """)
    # ==========================
    # CSS
    # ==========================

    st.markdown("""
    <style>
    .finance-card {
        background: #1f2937;
        border-radius: 14px;
        padding: 18px;
        border-top: 5px solid #3b82f6;
        min-height: 260px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.18);
    }

    .finance-card h3 {
        color: #60a5fa;
        font-size: 24px;
        margin-bottom: 14px;
    }

    .finance-card p {
        color: #f9fafb;
        font-size: 17px;
        line-height: 1.6;
    }

    .small-card {
        background: #374151;
        border-radius: 14px;
        padding: 18px;
        min-height: 150px;
        box-shadow: 0 5px 14px rgba(0,0,0,0.15);
    }

    .small-card h3 {
        color: #60a5fa;
        font-size: 24px;
    }

    .small-card p {
        color: #f9fafb;
        font-size: 17px;
        line-height: 1.6;
    }

    .ipo-card {
        background: #1f2937;
        border-radius: 16px;
        padding: 22px;
        min-height: 260px;
        border-left: 7px solid #3b82f6;
        box-shadow: 0 6px 18px rgba(0,0,0,0.18);
    }

    .ipo-card h3 {
        color: #60a5fa;
        font-size: 26px;
    }

    .ipo-card p {
        color: #f9fafb;
        font-size: 18px;
        line-height: 1.7;
    }

    .big-number {
        font-size: 56px;
        color: #60a5fa;
        font-weight: 800;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==========================
    # PART 1: FINANCING HISTORY
    # ==========================

    st.header("💰 Financing History")
    st.caption("State-backed capital supports long-term technology development")
    with st.expander("🔬 What is CAS-related Capital?"):
        st.markdown("""
        **CAS = Chinese Academy of Sciences**
        
        (中国科学院)

        CAS-related capital refers to investment funds and institutions
        connected with the Chinese Academy of Sciences.

        For Origin Quantum, this means strong support from China's
        leading scientific research ecosystem.
        """)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown("""
        <div class="finance-card">
        <h3>Seed Round</h3>
        <p>
        <b>Date:</b> Nov 2017<br>
        <b>Amount:</b> ¥0.3M<br>
        <b>Investor:</b> Founder Team<br>
        <b>Valuation:</b> ¥0.2B
        </p >
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="finance-card">
        <h3>Angel Round</h3>
        <p>
        <b>Date:</b> Nov 2019<br>
        <b>Amount:</b> N/A<br>
        <b>Investors:</b> CAS-related Capital<br>
        <b>Purpose:</b> Technology Validation
        </p >
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="finance-card">
        <h3>Series A</h3>
        <p>
        <b>Date:</b> Jan 2021<br>
        <b>Amount:</b> N/A<br>
        <b>Investors:</b> National & Industrial Capital<br>
        <b>Purpose:</b> Product Development
        </p >
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="finance-card">
        <h3>Series B</h3>
        <p>
        <b>Date:</b> Aug 2022<br>
        <b>Amount:</b> ¥1.01B<br>
        <b>Investor:</b> CAS / Industrial Capital<br>
        <b>Valuation:</b> ~¥7B
        </p >
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="finance-card" style="border-top:5px solid #facc15;">
        <h3>Pre-IPO</h3>
        <p>
        <b>Date:</b> Jun 2026<br>
        <b>Amount:</b> ¥3.0B<br>
        <b>Lead Investor:</b> NORINCO<br>
        <b>Valuation:</b> ¥21B
        </p >
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="small-card">
        <h3>🔬 Technology Moat</h3>
        <p>
        Full-stack quantum computing capability:
        chips, operating system, cloud platform and applications.
        </p >
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="small-card">
        <h3>🏛 State-backed Capital</h3>
        <p>
        Strong support from national and industrial investors
        strengthens long-term stability.
        </p >
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="small-card">
        <h3>🛡 Independent Control</h3>
        <p>
        No major foreign control risk, supporting China's strategic
        technology security.
        </p >
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ==========================
    # PART 2: IPO PLAN & VALUATION
    # ==========================

    st.header("📈 IPO Plan & Valuation Logic")
    st.caption("Pre-IPO financing strengthens capital reserves and market confidence")
    with st.expander("🏛 What is CSRC Anhui Regulatory Bureau?"):
        st.markdown("""
        **Full Name:**
        
        China Securities Regulatory Commission Anhui Regulatory Bureau

        **Chinese Name:**
        
        中国证券监督管理委员会安徽监管局（安徽证监局）

        It is the government regulator responsible for supervising
        IPO preparation and compliance processes in Anhui Province.
        """)

    with st.expander("🏦 What is CITIC Securities?"):
        st.markdown("""
        **Full Name:**
        
        CITIC Securities Co., Ltd.

        **Chinese Name:**
        
        中信证券股份有限公司

        CITIC Securities is one of China's largest investment banks.

        In an IPO process, it acts as the sponsoring institution,
        helping companies prepare listing documents, meet regulatory
        requirements, and communicate with stock exchanges.
        """)

    left, right = st.columns([1.2, 1])

    with left:
        st.markdown("""
        <div class="ipo-card">
        <h3>🚀 IPO Status</h3>
        <p>
        In September 2025, Origin Quantum completed IPO guidance filing
        with the CSRC Anhui Regulatory Bureau, with CITIC Securities
        serving as the sponsoring institution.
        </p >
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <div class="ipo-card">
        <h3>💎 Pre-IPO Valuation</h3>
        <p>
        <span class="big-number">¥21B</span><br>
        June 2026 pre-money valuation<br><br>
        Up from ¥6.88B in Aug 2025.
        </p >
        </div>
        """, unsafe_allow_html=True)

    with right:
        r1, r2 = st.columns(2)

        with r1:
            st.markdown("""
            <div class="small-card">
            <h3>📊 Valuation Upgrade</h3>
            <p>
            ¥6.88B → ¥21B<br><br>
            About <b>+205%</b> growth within 10 months.
            </p >
            </div>
            """, unsafe_allow_html=True)

        with r2:
            st.markdown("""
            <div class="small-card">
            <h3>💰 Growth Capital</h3>
            <p>
            ¥3.0B Pre-IPO financing improves capital reserves
            before listing.
            </p >
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        r3, r4 = st.columns(2)

        with r3:
            st.markdown("""
            <div class="small-card">
            <h3>🔬 Full-stack Moat</h3>
            <p>
            Quantum chips, quantum OS, quantum cloud,
            and application ecosystem.
            </p >
            </div>
            """, unsafe_allow_html=True)

        with r4:
            st.markdown("""
            <div class="small-card">
            <h3>🏆 Market Leadership</h3>
            <p>
            Origin Wukong strengthens the company's position
            in China's quantum computing industry.
            </p >
            </div>
            """, unsafe_allow_html=True)

    st.success(
        "CFO Message: State-backed financing, rapid valuation growth and IPO preparation "
        "provide Origin Quantum with stronger capital support for long-term commercialization."
    )
elif page == "🔚 End":
    st.markdown("""
    <div style="
        height: 80vh;
        display: flex;
        justify-content: center;
        align-items: center;
    ">
        <h1 style="
            font-size: 120px;
            font-weight: 900;
            letter-spacing: 8px;
            color: #2563eb;
            text-shadow: 0px 0px 20px rgba(37,99,235,0.35);
        ">
            THANK YOU
        </h1>
    </div>
    """, unsafe_allow_html=True)
