import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.write("Elzy Tabel Coding")
df = pd.DataFrame({
    'No' : [1, 2, 3, 4, 5, 6],
    'Nama' : ['Nurul', 'Nadia', 'Vino', 'Zahwa'],
    'Tinggi' : [98, 90, 83, 92]
})

df