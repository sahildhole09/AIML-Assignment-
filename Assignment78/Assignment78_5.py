import streamlit as st

st.set_page_config(
    page_title = "Celsius to Fahrenheit Converter",
    layout = "wide"
)

st.title("Marvellous Infosystems Celsius to Fahrenheit Converter Dashboard")

st.header("Converting the Temperature from Celsius to Fahrenheit")

st.caption("By Sahil Ashok Dhole | Student of Marvellous Infosystems")

st.divider()

TempCelsius = st.number_input("Enter Temperature in Celsius", value = 0)

if st.button("Fahrenheit"):
    Fahrenheit = (9 / 5) * TempCelsius + 32
    st.subheader(f"Temperature in Fahrenheit : {Fahrenheit}")

st.divider()