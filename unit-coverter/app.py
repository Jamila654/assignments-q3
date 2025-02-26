#type: ignore
import streamlit as st
import pandas as pd
import json
import os
from datetime import datetime

conversions = {
    "Length": {
        "Meter (m)": 1,
        "Kilometer (km)": 0.001,
        "Centimeter (cm)": 100,
        "Millimeter (mm)": 1000,
        "Inch (in)": 39.3701,
        "Foot (ft)": 3.28084,
        "Yard (yd)": 1.09361,
        "Mile (mi)": 0.000621371
    },
    "Weight": {
        "Kilogram (kg)": 1,
        "Gram (g)": 1000,
        "Milligram (mg)": 1000000,
        "Pound (lb)": 2.20462,
        "Ounce (oz)": 35.274,
        "Ton (t)": 0.001
    },
    "Temperature": {
        "Celsius (°C)": lambda x: x,
        "Fahrenheit (°F)": lambda x: (x * 9/5) + 32,
        "Kelvin (K)": lambda x: x + 273.15
    },
    "Volume": {
        "Liter (L)": 1,
        "Milliliter (mL)": 1000,
        "Cubic Meter (m³)": 0.001,
        "Gallon (gal)": 0.264172,
        "Quart (qt)": 1.05669,
        "Pint (pt)": 2.11338
    },
    "Area": {
        "Square Meter (m²)": 1,
        "Square Kilometer (km²)": 0.000001,
        "Square Centimeter (cm²)": 10000,
        "Square Inch (in²)": 1550,
        "Square Foot (ft²)": 10.7639,
        "Acre": 0.000247105
    },
    "Speed": {
        "Meter per Second (m/s)": 1,
        "Kilometer per Hour (km/h)": 3.6,
        "Mile per Hour (mph)": 2.23694,
        "Knot (kn)": 1.94384
    },
    "Time": {
        "Second (s)": 1,
        "Minute (min)": 1/60,
        "Hour (h)": 1/3600,
        "Day (d)": 1/86400
    },
    "Energy": {
        "Joule (J)": 1,
        "Kilojoule (kJ)": 0.001,
        "Calorie (cal)": 0.2388459,
        "Kilocalorie (kcal)": 0.0002388459,
        "Watt-hour (Wh)": 0.000277778
    }
}


st.set_page_config(page_title="Unit Converter Elite", layout="wide", initial_sidebar_state="expanded", menu_items={
    'Get Help': None,
    'Report a bug': None,
    'About': None
})


st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #74ebd5, #acb6e5);
        font-family: 'Segoe UI', sans-serif;
    }
    .main {
        background: rgba(255, 255, 255, 0.9);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.1);
        max-width: 900px;
        margin: 0 auto;
    }
    .title {
        font-size: 42px;
        font-weight: 700;
        color: #2c3e50;
        text-align: center;
        background: -webkit-linear-gradient(#3498db, #8e44ad);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        font-size: 18px;
        color: #34495e;
        text-align: center;
        margin-bottom: 30px;
        font-style: italic;
    }
    .history-box {
        background: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        margin-top: 25px;
    }
    .stButton>button {
        background: linear-gradient(90deg, #3498db, #2980b9);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #2980b9, #1f618d);
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 18px;
        padding: 12px 25px;
        color: #2c3e50;
        font-weight: 600;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background-color: #ecf0f1;
        border-radius: 10px;
    }
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 8px;
    }
    .result-container {
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

HISTORY_FILE = "history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)

if 'history' not in st.session_state:
    st.session_state.history = load_history()

def convert_units(value, from_unit, to_unit, category):
    try:
        value = float(value)
        if category == "Temperature":
            if from_unit == "Celsius (°C)":
                result = conversions[category][to_unit](value)
            elif from_unit == "Fahrenheit (°F)":
                celsius = (value - 32) * 5/9
                result = conversions[category][to_unit](celsius)
            else:
                celsius = value - 273.15
                result = conversions[category][to_unit](celsius)
        else:
            base_value = value / conversions[category][from_unit]
            result = base_value * conversions[category][to_unit]
        return result
    except ValueError:
        return "Invalid input! Please enter a numeric value."

def main():
    with st.sidebar:
        st.header("Options", divider="blue")
        precision = st.slider("Decimal Precision", 2, 6, 4, help="Set decimal places for results")
        show_preview = st.checkbox("Real-time Preview", value=True, help="See results as you type")
        st.info("History is saved locally and persists across sessions!")
        
    st.markdown('<div class="title">Unit Converter Elite</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your ultimate conversion companion</div>', unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Converter", "History"])

    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            category = st.selectbox("Category", list(conversions.keys()), help="Choose a conversion type")
            units = list(conversions[category].keys())
            from_unit = st.selectbox("From Unit", units, help="Unit to convert from")
            to_unit = st.selectbox("To Unit", units, index=1, help="Unit to convert to")

            value = st.text_input("Value", "1.0", help="Enter a number")
            if show_preview:
                result = convert_units(value, from_unit, to_unit, category)
                if isinstance(result, str):
                    st.warning(result)
                else:
                    st.info(f"Preview: {value} {from_unit} = {result:.{precision}f} {to_unit}")

            result_container = st.empty()
            if st.button("Convert"):
                result = convert_units(value, from_unit, to_unit, category)
                with result_container.container():
                    st.markdown('<div class="result-container" id="result">', unsafe_allow_html=True)
                    if isinstance(result, str):
                        st.error(result)
                    else:
                        st.success(f"{value} {from_unit} = {result:.{precision}f} {to_unit}")
                        history_entry = {
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "value": value,
                            "from_unit": from_unit,
                            "to_unit": to_unit,
                            "result": f"{result:.{precision}f}",
                            "category": category
                        }
                        st.session_state.history.append(history_entry)
                        save_history(st.session_state.history)
                    st.markdown('</div>', unsafe_allow_html=True)

                st.markdown("""
                    <script>
                    document.getElementById('result').scrollIntoView({behavior: 'smooth'});
                    </script>
                """, unsafe_allow_html=True)

        with col2:
            st.subheader("Tips", divider="blue")
            st.write("- Use decimals for precision.")
            st.write("- Preview updates instantly.")
            st.write("- History tracks all conversions.")

    with tab2:
        if st.session_state.history:
            st.markdown('<div class="history-box">', unsafe_allow_html=True)
            st.subheader("Conversion History", divider="blue")
            history_df = pd.DataFrame(st.session_state.history)
            st.dataframe(history_df, use_container_width=True)

            csv = history_df.to_csv(index=False)
            st.download_button("Download History", csv, "conversion_history.csv", "text/csv")

            if st.button("Clear History"):
                st.session_state.history = []
                clear_history()
                st.rerun()

            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.write("No history yet!")

    st.markdown('</div>', unsafe_allow_html=True)

main()