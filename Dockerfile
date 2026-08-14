# Folosim o imagine de bază Python
FROM python:3.9-slim

WORKDIR /app

# Instalăm dependențele necesare
RUN pip install streamlit xarray netCDF4 matplotlib copernicusmarine numpy dask

# Copiem tot codul sursă în container
COPY . /app

# Expunem portul pentru interfața web Streamlit
EXPOSE 8501

# Comanda de start pentru aplicație
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]