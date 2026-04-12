import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="F1 Pit Stop Analysis", page_icon="🏎️", layout="wide")

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

st.sidebar.header("Filtros de Análisis")
year_range = st.sidebar.slider("Selecciona el rango de años",int(df['Year'].min()), int(df['Year'].max()), (1994, 1996))

lista_escuderias = df['Car'].unique().tolist()
selected_teams = st.sidebar.multiselect("Seleccionar Escuderías", lista_escuderias, default=lista_escuderias[:8])

df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
if selected_teams:
    df_filtered = df_filtered[df_filtered['Car'].isin(selected_teams)]

st.title("Eficiencia Operativa en Boxes 🏎️")
st.markdown("Análisis Estadístico de Pit Stops en F1 (1994-1996)")
st.markdown("📊 Resumen General")

if not df_filtered.empty:
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total de Paradas", len(df_filtered))
    col_b.metric("Tiempo Promedio General", f"{df_filtered['Time'].mean():.2f} seg")
    col_c.metric("Equipo Más Rápido (Promedio)", df_filtered.groupby('Car')['Time'].mean().idxmin())
else:
    st.warning("Selecciona al menos una escudería para ver los datos.")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["⏱️ 1ra Parada vs 2da Parada", "🏆 2. Eficiencia por Escudería", "🧠 3. Estrategias", "📄 4. Explorador de Datos" ])

# OBJETIVO 1
with tab1:
    st.subheader("1. Comparación de Tiempos: 1ra Parada vs 2da Parada")
    st.info("En este periodo, la segunda parada tiende a ser consistentemente más rápida. Esto se debe a la regla de repostaje, " \
    "ya que en el segundo *pit stop* se inyectaba menos combustible para cubrir únicamente el tramo final de la carrera.")
    df_paradas_1_2 = df_filtered[df_filtered['Stops'].isin(['1', '2'])]

    if not df_paradas_1_2.empty:
        fig1 = px.box(df_paradas_1_2, x='Stops', y='Time', color='Stops',
                      title="1ra Parada vs 2da Parada (Boxplot)",
                      labels={'Stops': 'Número de Parada', 'Time': 'Tiempo (Segundos)'},
                      color_discrete_map={'1': 'blue', '2': 'orange'})
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.warning("No hay suficientes datos de paradas 1 y 2 para esta selección.")

# OBJETIVO 2 
with tab2:
    st.subheader("2. Eficiencia por Escudería")
    st.info("Este ranking mide la eficiencia mecánica y el trabajo en equipo en el pit lane. " \
    "Las escuderías en la parte superior lograron los promedios de tiempo más bajos (más rápidos) al atender a sus monoplazas.")
    df_teams = df_filtered.groupby('Car')['Time'].mean().reset_index().sort_values('Time').head(10)
    
    if not df_teams.empty:
        fig2 = px.bar(df_teams, x='Time', y='Car', orientation='h',
                      title="Top 10 Escuderías más rápidas (Promedio)",
                      labels={'Time': 'Tiempo Promedio (Segundos)', 'Car': 'Escudería'},
                      color='Time', color_continuous_scale='Viridis')
        fig2.update_layout(yaxis={'categoryorder':'total descending'}) 
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("No hay datos de escuderías para esta selección.")

st.markdown("---")

# --- OBJETIVO 3: Estrategias (Número de Paradas) ---
st.subheader("3. Estrategias de Carrera (Frecuencias)")

df_stops_freq = df_filtered['Stops'].value_counts().reset_index()
df_stops_freq.columns = ['Stops', 'Count']
df_stops_freq = df_stops_freq.sort_values('Stops')

if not df_stops_freq.empty:
    fig3 = px.bar(df_stops_freq, x='Stops', y='Count', text_auto=True,
                  title="Frecuencia del Número de Paradas por Estrategia",
                  labels={'Count': 'Frecuencia Absoluta', 'Stops': 'N° de Paradas realizadas'},
                  color='Stops', color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig3, use_container_width=True)

else:
    st.warning("No hay datos suficientes para mostrar estrategias.")

st.markdown("---")
st.caption(f"🏁 Datos procesados con los filtros actuales: **{df_filtered.shape[0]} registros**.")
