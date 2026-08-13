# app.py
import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt

st.title("Monitorizarea Adâncimii Secchi - Marea Neagră")
st.write("Aplicație bazată pe modelul ZhongPing Lee (2015) folosind date CMEMS.")

# Încărcăm datele procesate
@st.cache_data
def load_data():
    return xr.open_dataset("data/output/zsd_black_sea_today.nc")

ds = load_data()

# Crearea graficului cu matplotlib
fig, ax = plt.subplots(figsize=(10, 6))
# Selectăm harta 2D folosind squeeze pentru a elimina dimensiunea timpului
plot = ds['Secchi_Depth_m'].squeeze().plot(ax=ax, cmap='viridis', vmin=0, vmax=20)
plt.title("Adâncimea Secchi (m)")

# Afișăm graficul în pagina de Streamlit
st.pyplot(fig)