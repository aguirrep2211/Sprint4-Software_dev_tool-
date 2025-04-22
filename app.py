# app.py

import pandas as pd
import plotly.express as px
import streamlit as st
import panel as pn

# Título de la app
st.title("Análisis de Datos de Vehículos Usados")

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")  # Assumes the CSV is in the same directory

df = load_data()

# Separar brand y model_01
df[['brand', 'model_01']] = df['model'].str.split(' ', n=1, expand=True)

# Eliminar la original
df.drop(columns='model', inplace=True)

# Reordenar columnas para que brand y model_01 estén juntos después de 'price'
cols = list(df.columns)
insert_index = cols.index('price') + 1
new_order = cols[:insert_index] + ['brand', 'model_01'] + [col for col in cols[insert_index:] if col not in ['brand', 'model_01']]
df = df[new_order]


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

#pannel 

def resumen_por_marca(marca):
    df_filtrado = df[df['brand'] == marca]
    if df_filtrado.empty:
        return "No hay datos para esta marca."

    # Modelo más frecuente (más vendido)
    modelo_top = df_filtrado['model_01'].mode().iloc[0]
    df_modelo = df_filtrado[df_filtrado['model_01'] == modelo_top]

    tipo = df_modelo['type'].mode().iloc[0] if not df_modelo['type'].isna().all() else 'Desconocido'
    promedio_days_listed = df_modelo['days_listed'].mean()

    return pn.pane.Markdown(f"""
    ## Resumen by **{marca}**
    - Most sold model: **{modelo_top}**
    - Type: **{tipo}**
    - Average number of days listed: **{promedio_days_listed:.2f}**
    """)

# Widget brand selection 
marcas = sorted(vehicles_df['brand'].dropna().unique())
selector_marca = pn.widgets.Select(name='Marca', options=marcas)

# Interactive pannel 
panel_interactivo = pn.Column(
    selector_marca,
    pn.bind(resumen_por_marca, selector_marca)
)

panel_interactivo.servable()