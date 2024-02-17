import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

st.write("Elzy Tabel Coding")
df = pd.DataFrame({
    'No' : [1, 2, 3, 4, 5, 6],
    'Nama' : ['Sowoon', 'Yuju', 'Yerin', 'Eunha', 'Sinb', 'Umji'],
    'Tinggi' : [173, 170, 168, 163, 167, 164]
})

df