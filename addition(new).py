import numpy as np
import pandas as pd
import streamlit as st

def welcome():
    return "Welcome"

def main():
  st.title("Addition")
  
  num1 = st.number_input("Number 1")
  num2 = st.number_input("Number 2")
  result = num1 + num2
  
  st.success('The result is {}'.format(result))
 
if __name__=='__main__':
  main()
