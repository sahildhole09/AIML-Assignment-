import streamlit as st

st.set_page_config(
    page_title = "Student Result Calculator",
    layout = "wide"
)

st.title("Marvellous Infosystems Student Result Dashboard")

st.header("Student Result Calculation using its 3 Subjects Marks")

st.caption("By Sahil Ashok Dhole | Student of Marvellous Infosystems")

st.divider()

Name = st.text_input("Enter Your Name")

Subject1 = st.number_input("Enter First Subject Marks", value = 0, min_value = 0, max_value = 100)
Subject2 = st.number_input("Enter Second Subject Marks", value = 0, min_value = 0, max_value = 100)
Subject3 = st.number_input("Enter Third Subject Marks", value = 0, min_value = 0, max_value = 100)

Total = 300

percentage = Subject1 + Subject2 + Subject3 / Total

if st.button("Result"):
    percentage = (Subject1 + Subject2 + Subject3) / Total * 100 

    if Subject1 >= 40 and Subject2 >= 40 and Subject3 >= 40:
        st.subheader(f"Result : Passed & Percentage : {percentage} %")
    else:
        st.subheader(f"Result : Failed")

st.divider()