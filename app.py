import streamlit as st
from itinerary_generator import generate_itinerary
import os

st.set_page_config(page_title="AI Travel Itinerary Generator", layout="centered")

st.title("🌍 AI Travel Itinerary Generator")
st.write("Plan your next trip with AI! Just enter your details below:")

os.environ["OPENAI_API_KEY"] = ""  # or set via environment variable

with st.form("itinerary_form"):
    location = st.text_input("🌆 Destination", placeholder="e.g., Manali, Goa, Paris")
    budget = st.number_input("💰 Budget (in INR)", min_value=1000, value=15000, step=500)
    days = st.number_input("📅 Number of Days", min_value=1, value=5, step=1)
    interests = st.text_area("🎯 Interests (comma separated)", placeholder="e.g., beaches, hiking, local food")
    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    with st.spinner("Planning your dream trip..."):
        itinerary = generate_itinerary(location, budget, days, interests)
        st.success("Here's your itinerary!")
        st.markdown("### 🗺️ Your Travel Plan")
        st.markdown(itinerary)
