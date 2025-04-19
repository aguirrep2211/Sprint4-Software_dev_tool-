
# Save the notebook with visualizations

import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("../vehicles_us.csv")

# Histograma del precio
fig_price_hist = px.histogram(df, x="price", nbins=100, title="Distribución de Precios")
fig_price_hist.show()

# Histograma del kilometraje
fig_odometer_hist = px.histogram(df, x="odometer", nbins=100, title="Distribución del Kilometraje")
fig_odometer_hist.show()

# Scatterplot: precio vs año del modelo
fig_price_model_year = px.scatter(df, x="model_year", y="price", title="Precio vs Año del Modelo", opacity=0.5)
fig_price_model_year.show()

# Scatterplot: precio vs kilometraje
fig_price_odometer = px.scatter(df, x="odometer", y="price", title="Precio vs Kilometraje", opacity=0.5)
fig_price_odometer.show()

notebook_path = f"{notebook_dir}/EDA.ipynb"