import streamlit as st
st.write("Hello!")

categories =['a', 'b', 'c']
st.multiselect("Pick an option!", categories)
st.button("Click me!")
if st.checkbox("Select me!"):
  st.write("you selected the checkbox!")
st.write("Hello")
