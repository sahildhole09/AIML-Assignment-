import streamlit as st

st.set_page_config(
    page_title = "Simple Interest Calculator",
    layout = "wide"
)

st.title("Marvellous Infosystems Simple Interest Calculator Dashboard")

st.header("Calculation of Simple Interest using Principal Amount, Rate of Interest & Time Period")

st.caption("By Sahil Ashok Dhole | Student of Marvellous Infosystems")

st.divider()

amount = st.number_input("Enter Principal Amount", min_value = 0, value = 0)

rate = st.number_input("Enter Rate of Interest in Percentage", min_value = 0, value = 0)

time = st.number_input("Enter Time Period in Years",min_value = 0, value = 0)

if st.button("Simple Interest"):
    SI = (amount * rate * time) / 100
    st.subheader(f"Simple Interest : {SI}")

st.divider()