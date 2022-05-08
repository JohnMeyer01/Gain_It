import streamlit as st
import pandas as pd
import datetime

st.title("Weight Tracker")

number = st.number_input('Insert Weight')
st.write('Todays Weight ', number)

d = st.date_input(
     "Insert Date",
     datetime.date(2019, 7, 6))
st.write('Todays Date:', d)

age = st.slider('Insert Calories Consumed', 0, 4000, 25)
st.write("Calories Consumed:", age)

st.button("Plot Data")