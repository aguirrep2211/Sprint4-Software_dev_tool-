# app.py

import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Análisis de Datos de Vehículos Usados")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")  # Assumes the CSV is in the same directory

df = load_data()

# Mostrar tabla de datos
st.subheader("Vista previa de los datos")
st.dataframe(df.head())

# Histograma del precio
st.subheader("Distribución de Precios")
fig_price_hist = px.histogram(df, x="price", nbins=100)
st.plotly_chart(fig_price_hist)

# Histograma del kilometraje
st.subheader("Distribución del Kilometraje")
fig_odometer_hist = px.histogram(df, x="odometer", nbins=100)
st.plotly_chart(fig_odometer_hist)

# Scatterplot: precio vs año del modelo
st.subheader("Precio vs Año del Modelo")
fig_price_model_year = px.scatter(df, x="model_year", y="price", opacity=0.5)
st.plotly_chart(fig_price_model_year)

# Scatterplot: precio vs kilometraje
st.subheader("Precio vs Kilometraje")
fig_price_odometer = px.scatter(df, x="odometer", y="price", opacity=0.5)
st.plotly_chart(fig_price_odometer)