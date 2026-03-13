import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./9. Formula 1.csv")

# 1. Limpieza de nombres de columnas
df.columns = df.columns.str.strip()
# 2. Convertir 'Time' a numérico (por si hay errores o strings)
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
# 3. Eliminar valores nulos en columnas críticas para el estudio
df = df.dropna(subset=['Time', 'Year', 'Car'])

import streamlit as st
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="F1 Pit Stop Analysis 1994-2010", layout="wide")

st.title("Análisis Estadístico de Pit Stops en F1 (1994-2010)")
st.markdown("Trabajo de Investigación - Computación I")
