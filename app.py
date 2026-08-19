#varianta asta e cea imbunatatia de chat gpt, a plecat de la app.py
import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Secchi Depth – Black Sea",
    layout="wide"
)

st.title("Secchi Depth – Black Sea")

st.write(
    "Secchi Depth estimated from Copernicus Marine remote-sensing "
    "reflectance using the Lee et al. methodology."
)


@st.cache_resource
def load_data():
    return xr.open_dataset(
        "data/output/zsd_black_sea_today.nc"
    )


ds = load_data()

zsd = ds["ZSD"].squeeze()

fig, ax = plt.subplots(figsize=(12, 7))

zsd.plot(
    ax=ax,
    cmap="viridis",
    vmin=0,
    vmax=20,
    cbar_kwargs={"label": "Secchi Depth (m)"}
)

ax.set_title("Secchi Depth – Black Sea")
ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")

st.pyplot(fig, use_container_width=True)