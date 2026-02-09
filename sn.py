import streamlit as st
import math

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="AASHTO 1993 - Structural Number Calculator",
    page_icon="🛣️",
    layout="wide"
)

# หัวเรื่อง
st.title("🛣️ AASHTO 1993 Pavement Design")
st.header("Structural Number (SN) Calculator")
st.markdown("---")

# คำอธิบาย
with st.expander("ℹ️ เกี่ยวกับ Structural Number (SN)"):
    st.write("""
    **Structural Number (SN)** คือดัชนีที่แสดงถึงความแข็งแรงโครงสร้างของผิวทางลาดยาง
    
    **สูตรการคำนวณ:**
    ```
    SN = a₁D₁ + a₂D₂m₂ + a₃D₃m₃
    ```
    
    โดยที่:
    - **a₁, a₂, a₃** = ค่าสัมประสิทธิ์โครงสร้างของชั้นทาง (Structural Layer Coefficient)
    - **D₁, D₂, D₃** = ความหนาของชั้นทาง (นิ้ว)
    - **m₂, m₃** = ค่าสัมประสิทธิ์การระบายน้ำ (Drainage Coefficient)
    """)

# สร้าง 2 คอลัมน์
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 ข้อมูลชั้นทาง")
    
    # ชั้นที่ 1 - ผิวจราจร (Surface Course)
    st.markdown("**ชั้นที่ 1: ผิวจราจร (Surface Course - Asphalt Concrete)**")
    a1 = st.number_input(
        "ค่าสัมประสิทธิ์ a₁",
        min_value=0.0,
        max_value=1.0,
        value=0.44,
        step=0.01,
        help="ค่าทั่วไป: 0.35-0.44 สำหรับ AC"
    )
    D1 = st.number_input(
        "ความหนา D₁ (นิ้ว)",
        min_value=0.0,
        value=4.0,
        step=0.5
    )
    
    st.markdown("---")
    
    # ชั้นที่ 2 - ชั้นรอง (Base Course)
    st.markdown("**ชั้นที่ 2: ชั้นรอง (Base Course)**")
    a2 = st.number_input(
        "ค่าสัมประสิทธิ์ a₂",
        min_value=0.0,
        max_value=1.0,
        value=0.14,
        step=0.01,
        help="ค่าทั่วไป: 0.10-0.14 สำหรับ Crushed Stone"
    )
    D2 = st.number_input(
        "ความหนา D₂ (นิ้ว)",
        min_value=0.0,
        value=6.0,
        step=0.5
    )
    m2 = st.number_input(
        "ค่าการระบายน้ำ m₂",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.05,
        help="ค่าทั่วไป: 0.80-1.20 ขึ้นอยู่กับคุณภาพการระบายน้ำ"
    )
    
    st.markdown("---")
    
    # ชั้นที่ 3 - ชั้นรองพื้น (Subbase Course)
    st.markdown("**ชั้นที่ 3: ชั้นรองพื้น (Subbase Course)**")
    a3 = st.number_input(
        "ค่าสัมประสิทธิ์ a₃",
        min_value=0.0,
        max_value=1.0,
        value=0.11,
        step=0.01,
        help="ค่าทั่วไป: 0.08-0.14 สำหรับ Granular Material"
    )
    D3 = st.number_input(
        "ความหนา D₃ (นิ้ว)",
        min_value=0.0,
        value=8.0,
        step=0.5
    )
    m3 = st.number_input(
        "ค่าการระบายน้ำ m₃",
        min_value=0.0,
        max_value=2.0,
        value=1.0,
        step=0.05,
        help="ค่าทั่วไป: 0.80-1.20 ขึ้นอยู่กับคุณภาพการระบายน้ำ"
    )

with col2:
    st.subheader("🧮 ผลการคำนวณ")
    
    # คำนวณ SN
    SN_layer1 = a1 * D1
    SN_layer2 = a2 * D2 * m2
    SN_layer3 = a3 * D3 * m3
    SN_total = SN_layer1 + SN_layer2 + SN_layer3
    
    # แสดงผลแบบ Card
    st.markdown(f"""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #4169e1;">
        <h2 style="color: #4169e1; margin-top: 0;">Structural Number (SN)</h2>
        <h1 style="color: #1e3a8a; font-size: 48px; margin: 10px 0;">{SN_total:.3f}</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # รายละเอียดการคำนวณ
    st.markdown("**รายละเอียดการคำนวณ:**")
    
    st.write(f"**ชั้นที่ 1 (Surface):**")
    st.latex(f"SN_1 = a_1 \\times D_1 = {a1:.2f} \\times {D1:.1f} = {SN_layer1:.3f}")
    
    st.write(f"**ชั้นที่ 2 (Base):**")
    st.latex(f"SN_2 = a_2 \\times D_2 \\times m_2 = {a2:.2f} \\times {D2:.1f} \\times {m2:.2f} = {SN_layer2:.3f}")
    
    st.write(f"**ชั้นที่ 3 (Subbase):**")
    st.latex(f"SN_3 = a_3 \\times D_3 \\times m_3 = {a3:.2f} \\times {D3:.1f} \\times {m3:.2f} = {SN_layer3:.3f}")
    
    st.markdown("---")
    st.write(f"**SN รวม:**")
    st.latex(f"SN_{{total}} = {SN_layer1:.3f} + {SN_layer2:.3f} + {SN_layer3:.3f} = {SN_total:.3f}")
    
    # ความหนารวม
    total_thickness = D1 + D2 + D3
    st.info(f"📏 **ความหนารวมทั้งหมด:** {total_thickness:.1f} นิ้ว ({total_thickness * 2.54:.1f} ซม.)")
    
    # คำแนะนำ
    st.markdown("---")
    st.markdown("**💡 คำแนะนำ:**")
    if SN_total < 3:
        st.warning("⚠️ SN ค่อนข้างต่ำ - เหมาะสำหรับจราจรเบา")
    elif SN_total < 5:
        st.success("✅ SN ในระดับปานกลาง - เหมาะสำหรับจราจรปานกลาง")
    else:
        st.success("✅ SN ในระดับสูง - เหมาะสำหรับจราจรหนัก")

# ตารางค่าอ้างอิง
st.markdown("---")
with st.expander("📋 ตารางค่าอ้างอิงตาม AASHTO 1993"):
    col_ref1, col_ref2 = st.columns(2)
    
    with col_ref1:
        st.markdown("**ค่าสัมประสิทธิ์โครงสร้าง (Layer Coefficient)**")
        st.markdown("""
        | วัสดุ | ค่า a |
        |-------|-------|
        | Asphalt Concrete | 0.35 - 0.44 |
        | Crushed Stone Base | 0.10 - 0.14 |
        | Cement Treated Base | 0.15 - 0.30 |
        | Granular Subbase | 0.08 - 0.14 |
        | Sand-Gravel | 0.05 - 0.10 |
        """)
    
    with col_ref2:
        st.markdown("**ค่าสัมประสิทธิ์การระบายน้ำ (Drainage Coefficient)**")
        st.markdown("""
        | คุณภาพการระบายน้ำ | ค่า m |
        |-------------------|-------|
        | ดีเยี่ยม | 1.20 - 1.35 |
        | ดี | 1.00 - 1.20 |
        | ปานกลาง | 0.80 - 1.00 |
        | แย่ | 0.60 - 0.80 |
        | แย่มาก | 0.40 - 0.60 |
        """)

# Footer
st.markdown("---")
st.caption("📚 Based on AASHTO Guide for Design of Pavement Structures, 1993")
