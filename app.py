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

# --- SIDEBAR (Filtros) ---
st.sidebar.header("Filtros de Análisis")
year_range = st.sidebar.slider("Selecciona el rango de años", 1994, 2010, (1994, 2010))
selected_teams = st.sidebar.multiselect("Seleccionar Escuderías", df['Car'].unique(), default=df['Car'].unique()[:5])

# Filtrar datos según selección
df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
if selected_teams:
    df_filtered = df_filtered[df_filtered['Car'].isin(selected_teams)]

# --- OBJETIVO 1: Evolución Temporal ---
st.subheader("1. Evolución de los tiempos de parada")
avg_time_year = df_filtered.groupby('Year')['Time'].mean().reset_index()
fig1 = px.line(avg_time_year, x='Year', y='Time', title="Promedio de tiempo en Pits por Año",
              labels={'Time': 'Segundos', 'Year': 'Año'}, markers=True)
st.plotly_chart(fig1, use_container_width=True)

# --- OBJETIVO 2: Influencia de la Escudería ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("2. Comparativa por Escudería")
    fig2 = px.box(df_filtered, x='Car', y='Time', color='Car',
                 title="Distribución de tiempos por Equipo")
    st.plotly_chart(fig2)

# --- OBJETIVO 3: Estrategias (Número de Paradas) ---
with col2:
    st.subheader("3. Estrategias de Carrera")
    # Contamos cuántos pilotos hicieron 1, 2 o 3 paradas
    fig3 = px.histogram(df_filtered, x='Stops', nbins=5, title="Frecuencia del número de paradas",
                       labels={'Stops': 'N° de Paradas', 'count': 'Frecuencia'})
    st.plotly_chart(fig3)

st.write("Datos procesados: ", df_filtered.shape[0], " registros.")