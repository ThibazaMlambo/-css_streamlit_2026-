

import streamlit as st

st.write("CSS 2026")

st.title("Title heading")

st.write("My first Streamlit App")

st.header("Number selection")

number = st.slider("Pick a number", 1, 200)
st.write(f"You picked: {number}")

st.markdown("Add an addtional text here")