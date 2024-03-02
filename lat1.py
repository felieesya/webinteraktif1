import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.write("List Sahabat")
df = pd.DataFrame({
    'No' : [1, 2, 3, 4,],
    'Nama' : ['KK', 'UU', 'OO', 'II'],
    'Rating' : [8, 9, 5, 6]
})

df