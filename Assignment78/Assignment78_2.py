import streamlit as st

st.set_page_config(
    page_title = "Even Odd Checker",
    layout = "centered"
)

st.divider()

st.title("Marvellous Infosystems Even Odd Checker Dashboard")

st.header("Checking Weather a Number is Even or Odd")

st.caption("By Sahil Ashok Dhole | Student of Marvellous Infosystems")

st.divider()

Num = st.number_input("Enter the number", value = 0, min_value = 0)

if st.button("EvenOddChecker"):

    if Num % 2 == 0:
        st.subheader("Given number is Even Number")
    else:
        st.subheader("Given number is Odd Number")

st.divider()