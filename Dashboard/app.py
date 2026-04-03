import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="F1 Pit Stop Analysis", layout="wide")

@st.cache_data
def cargar_datos():
    df = pd.read_csv("formula 1.csv")

    df.columns = df.columns.str.strip()

    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Time'] = pd.to_numeric(df['Time'], errors='coerce')

    df = df.dropna(subset=['Time', 'Year', 'Car'])

    df['Stops'] = df['Stops'].astype(str).str.replace('.0', '', regex=False) 
    df['Car'] = df['Car'].astype(str)
    return df

df = cargar_datos()

# Títulos
st.title("Análisis Estadístico de Pit Stops en F1")
st.markdown("Trabajo de Investigación - Computación I")
st.markdown("---")

st.sidebar.header("Filtros de Análisis")
year_range = st.sidebar.slider("Selecciona el rango de años",int(df['Year'].min()), int(df['Year'].max()), (1994, 1996))

lista_escuderias = df['Car'].unique().tolist()
selected_teams = st.sidebar.multiselect("Seleccionar Escuderías", lista_escuderias, default=lista_escuderias[:8])

df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
if selected_teams:
    df_filtered = df_filtered[df_filtered['Car'].isin(selected_teams)]

col1, col2 = st.columns(2)

# OBJETIVO 1
st.subheader("1. Comparación de Tiempos: 1ra Parada vs 2da Parada")
df_paradas_1_2 = df_filtered[df_filtered['Stops'].isin(['1', '2'])]

if not df_paradas_1_2.empty:
        fig1 = px.box(df_paradas_1_2, x='Stops', y='Time', color='Stops',
                      title="1ra Parada vs 2da Parada (Boxplot)",
                      labels={'Stops': 'Número de Parada', 'Time': 'Tiempo (Segundos)'},
                      color_discrete_map={'1': 'blue', '2': 'orange'})
        st.plotly_chart(fig1, use_container_width=True)

else:
        st.warning("No hay suficientes datos de paradas 1 y 2 para esta selección.")

