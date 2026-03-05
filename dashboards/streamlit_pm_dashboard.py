
import streamlit as st
from code.roi_calculator import calculate_ai_roi

st.title("Enterprise AI PM Control Tower")

investment = st.number_input("Investment",500000)
savings = st.number_input("Annual Cost Savings",200000)
revenue = st.number_input("Annual Revenue Increase",350000)
months = st.number_input("Implementation Months",8)

if st.button("Calculate ROI"):
    result = calculate_ai_roi(investment,savings,revenue,months)
    st.write(result)
