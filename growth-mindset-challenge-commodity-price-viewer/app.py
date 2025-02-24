#type: ignore
import streamlit as st
import requests
import plotly.express as px
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="Commodity Price Viewer", layout="centered")


st.title("Commodity Price Viewer")
st.subheader("Select a commodity to see its current price and trend!")

API_KEY = "lKtqOcitXKlPdf5kvf1ysg==AguhIHwYblypgdyF"  # Your API key
API_URL = "https://api.api-ninjas.com/v1/commodityprice"

COMMODITIES = [
    "gold", "platinum", "lean_hogs", "oat", "aluminum", "soybean_meal",
    "lumber", "micro_gold", "feeder_cattle", "rough_rice", "palladium"
]


UNITS = {
    "gold": "USD/oz", "platinum": "USD/oz", "lean_hogs": "USD/lb", "oat": "USD/bushel",
    "aluminum": "USD/ton", "soybean_meal": "USD/ton", "lumber": "USD/1000bf",
    "micro_gold": "USD/oz", "feeder_cattle": "USD/lb", "rough_rice": "USD/cwt",
    "palladium": "USD/oz"
}


def fetch_commodity_price(commodity):
    
    try:
        response = requests.get(
            API_URL,
            headers={"X-Api-Key": API_KEY},
            params={"name": commodity},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        price = data.get("price", "N/A")
        unit = UNITS.get(commodity, "N/A")
        return price, unit
    except requests.RequestException as e:
        st.error(f"Failed to fetch price for {commodity}: {e}")
        return "N/A", "N/A"

def generate_mock_historical_data(current_price, days=30):
    if current_price == "N/A" or not isinstance(current_price, (int, float)):
        current_price = 100.0
    dates = [datetime.now() - timedelta(days=x) for x in range(days)]
    prices = [current_price * (1 + random.uniform(-0.05, 0.05)) for _ in range(days)]
    return pd.DataFrame({"Date": dates, "Price": prices})

selected_commodity = st.selectbox("Choose a commodity:", COMMODITIES)

if st.button("Get Price"):
    with st.spinner(f"Fetching price for {selected_commodity}..."):
        price, unit = fetch_commodity_price(selected_commodity)
        st.write(f"### Current Price of {selected_commodity.capitalize()}:")
        if price != "N/A":
            st.success(f"${price} {unit}")
        else:
            st.warning("Price data unavailable for this commodity.")
        df = generate_mock_historical_data(price)
        fig = px.line(df, x="Date", y="Price", title=f"{selected_commodity.capitalize()} Price Trend (Mock Data)")
        fig.update_layout(yaxis_title=f"Price ({unit})")
        st.plotly_chart(fig)
        
st.sidebar.header("About")
st.sidebar.markdown(
    "This app fetches real-time commodity prices using the API-Ninjas API and shows a mock trend chart. "
    "Made with ❤️ by Jam."
)