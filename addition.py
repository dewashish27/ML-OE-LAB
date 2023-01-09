import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome"

def main():
  st.title("Addition")
  html_temp = """
  <div style="background-color:red;padding:10px">
  <h2 style="color:black;text-align:center;">Addition of 2 numbers using Streamlit</h2>
  </div>
  """
  st.markdown(html_temp,unsafe_allow_html=True)
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  result = num1 + num2
  st.success('The result is {}'.format(result))
  if st.button("Made By"):
      st.text("Bishal Banerjee")
      st.text("21f2000514")

if __name__=='__main__':
  main()
