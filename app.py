import streamlit as st

# Set Page Title and Icon
st.set_page_config(page_title="Mechanical Hub", page_icon="⚙️")

# Custom CSS for the Mechanical Gear Theme and Identity
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/free-vector/mechanical-gears-background-style_23-2148318666.jpg");
        background-size: cover;
        background-attachment: fixed;
    }
    .main-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #2c3e50;
    }
    .identity-banner {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Identity Header
st.markdown(f"""
    <div class="identity-banner">
        <h1>Mechanical Engineering Hub</h1>
        <p style="font-size: 1.2rem; margin: 0;"><b>Name:</b> Aleesha Faisal</p>
        <p style="font-size: 1.2rem; margin: 0;"><b>Roll Number:</b> 25-ME-186</p>
    </div>
    """, unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Unit Converter", "Material Density Checker"])

# --- TAB 1: UNIT CONVERTER ---
with tab1:
    st.header("⚙️ Unit Converter")
    category = st.selectbox("Choose Category", ["Pressure", "Power", "Force"])
    
    val = st.number_input("Enter Value", value=1.0)
    
    if category == "Pressure":
        st.write(f"**Pascal (Pa):** {val}")
        st.write(f"**Bar:** {val / 100000:.5f}")
        st.write(f"**PSI:** {val * 0.000145038:.5f}")
        
    elif category == "Power":
        st.write(f"**Watts (W):** {val}")
        st.write(f"**Horsepower (hp):** {val / 745.7:.5f}")
        st.write(f"**Kilowatts (kW):** {val / 1000:.3f}")
        
    elif category == "Force":
        st.write(f"**Newton (N):** {val}")
        st.write(f"**Kilonewton (kN):** {val / 1000:.3f}")
        st.write(f"**Pound-force (lbf):** {val * 0.224809:.4f}")

# --- TAB 2: DENSITY CHECKER ---
with tab2:
    st.header("🔬 Material Density Checker")
    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Cast Iron": 7200,
        "Titanium": 4500,
        "Concrete": 2400
    }
    
    choice = st.selectbox("Select Material", list(materials.keys()))
    density = materials[choice]
    
    st.metric(label=f"Density of {choice}", value=f"{density} kg/m³")
    
    st.write("---")
    st.write("### Mass Calculator")
    volume = st.number_input("Enter Volume (m³)", min_value=0.0, value=1.0)
    mass = volume * density
    st.success(f"The calculated mass is: **{mass:,.2f} kg**")

# Footer
st.markdown("---")
st.caption("Developed by Aleesha Faisal (25-ME-186)")
