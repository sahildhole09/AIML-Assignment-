import streamlit as st

st.set_page_config(
    page_title = "Addition",
    layout = "centered"
)

st.divider()

st.title("Marvellous Infosystems Addition Dashboard")

st.header("Addition of Two Numbers")

st.caption("By Sahil Ashok Dhole | Student of Marvellous Infosystems")

st.divider()

st.subheader("Enter Two Numbers : ")

No1 = st.number_input("Enter First Number",value = 1, min_value = 0, step = 1)

No2 = st.number_input("Enter Second Number",value = 1, min_value = 0, step = 1)

if st.button("Addition", use_container_width=True):
    Add = No1 + No2
    st.subheader(f"Addition of {No1} and {No2} is : {Add}")

st.divider()