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

