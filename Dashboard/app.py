import streamlit as st
import pandas as pd
import plotly.express as px 
import io

st.set_page_config(page_title="F1 Pit Stop Analysis", page_icon="🏎️", layout="wide")

st.markdown("""
    <style>
    /* 1. Fondo de Fibra de Carbono para el Sidebar */
    [data-testid="stSidebar"] {
        background-color: #151515;
        background-image: 
            linear-gradient(30deg, #111 12%, transparent 12.5%, transparent 87%, #111 87.5%, #111),
            linear-gradient(150deg, #111 12%, transparent 12.5%, transparent 87%, #111 87.5%, #111),
            linear-gradient(30deg, #111 12%, transparent 12.5%, transparent 87%, #111 87.5%, #111),
            linear-gradient(150deg, #111 12%, transparent 12.5%, transparent 87%, #111 87.5%, #111),
            linear-gradient(60deg, #1d1d1d 25%, transparent 25.5%, transparent 75%, #1d1d1d 75%, #1d1d1d),
            linear-gradient(60deg, #1d1d1d 25%, transparent 25.5%, transparent 75%, #1d1d1d 75%, #1d1d1d);
        background-size: 20px 35px;
        background-position: 0 0, 0 0, 10px 18px, 10px 18px, 0 0, 10px 18px;
    }

    /* 2. Fondo Principal con Humo/Gradiente */
    .stApp {
        background: radial-gradient(circle at center, #1a0000 0%, #000000 100%);
    }

    /* Estilo para los títulos */
    h1, h2, h3 {
        color: white !important;
        font-family: 'Arial Black', sans-serif;
        text-transform: uppercase;
    }
    
    /* Estilo para las métricas */
    [data-testid="stMetricValue"] {
        font-size: 40px;
        color: #E4FDE1 !important;
    }
    </style>
    """, unsafe_allow_html=True)


def formato_espanol(valor):
    if isinstance(valor, (int, float)):
        return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return valor

@st.cache_data
def cargar_datos():
    df = pd.read_csv("Dashboard/formula 1.csv")

    df.columns = df.columns.str.strip()

    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df['Time'] = pd.to_numeric(df['Time'], errors='coerce')

    df = df.dropna(subset=['Time', 'Year', 'Car'])

    df['Stops'] = df['Stops'].astype(str).str.replace('.0', '', regex=False) 
    df['Car'] = df['Car'].astype(str)
    return df

df = cargar_datos()

st.sidebar.image("Dashboard/F1_logo.png", width=150)
st.sidebar.title("⚙️ Filtros de Análisis")
year_range = st.sidebar.slider("Selecciona el rango de años",int(df['Year'].min()), int(df['Year'].max()), (1994, 1996))

lista_escuderias = df['Car'].unique().tolist()
selected_teams = st.sidebar.multiselect("Seleccionar Escuderías", lista_escuderias, default=lista_escuderias[:8])

df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
if selected_teams:
    df_filtered = df_filtered[df_filtered['Car'].isin(selected_teams)]

st.image("Dashboard/F1_logo.png", width=200)
st.title("Eficiencia Operativa en Boxes 🏎️")
st.markdown("### Análisis Estadístico de Pit Stops en F1 (1994-1996)")
st.markdown("📊 Resumen General")

if not df_filtered.empty:
    
    total_paradas = df_filtered.shape[0]
    promedio_gen = df_filtered['Time'].mean()
    equipo_rapido = df_filtered.groupby('Car')['Time'].mean().idxmin()
    fastest_stop_time = df_filtered['Time'].min()

    m_col1, m_col2 = st.columns(2)
    m_col3, m_col4 = st.columns(2)

    with m_col1:
        st.metric("Total de Paradas", total_paradas)

    with m_col2:
        st.metric("Tiempo Promedio General", f"{formato_espanol(promedio_gen)} seg")
    with m_col3:
        st.metric("Equipo Más Rápido (Promedio)", equipo_rapido)
        
    with m_col4:
        st.metric("Parada Más Rápida (Registrada)", f"{formato_espanol(fastest_stop_time)} seg")

else:
    st.warning("Selecciona al menos una escudería para ver los datos.")

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(["⏱️ 1ra Parada vs 2da Parada", "🏆 2. Eficiencia por Escudería", "🧠 3. Estrategias", "📄 4. Explorador de Datos" ])

COLOR_PRIMARIO = "#C1121F"

# OBJETIVO 1
with tab1:
    st.subheader("1. Comparación de Tiempos: 1ra Parada vs 2da Parada")
    st.info("En este periodo, la segunda parada tiende a ser consistentemente más rápida. Esto se debe a la regla de repostaje, " \
    "ya que en el segundo *pit stop* se inyectaba menos combustible para cubrir únicamente el tramo final de la carrera.")
    df_paradas_1_2 = df_filtered[df_filtered['Stops'].isin(['1', '2'])]

    if not df_paradas_1_2.empty:
        fig1 = px.box(df_paradas_1_2, x='Stops', y='Time',
                      title="1ra Parada vs 2da Parada (Boxplot)",
                      labels={'Stops': 'Número de Parada', 'Time': 'Tiempo (Segundos)'},
                      color_discrete_sequence=[COLOR_PRIMARIO])
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
                      color_discrete_sequence=[COLOR_PRIMARIO])
        fig2.update_layout(yaxis={'categoryorder':'total descending'}) 
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.warning("No hay datos de escuderías para esta selección.")

# OBJETIVO 3
with tab3:
    st.subheader("3. Estrategias de Carrera (Frecuencias)")
    st.info("El gráfico de embudo ilustra la reducción progresiva en el volumen de casos a medida que aumenta el número de paradas. " \
    "Permite visualizar claramente cómo la base estratégica se concentra en una detención, filtrando drásticamente a la minoría que optó por tres o más ingresos al pit lane.")
    df_stops_freq = df_filtered['Stops'].value_counts().reset_index()
    df_stops_freq.columns = ['Stops', 'Count']
    df_stops_freq = df_stops_freq.sort_values('Stops')

    if not df_stops_freq.empty:
        fig3 = px.funnel(df_stops_freq, x='Count', y='Stops', 
                      title="Embudo Estratégico de Paradas",
                      labels={'Count': 'Frecuencia Absoluta', 'Stops': 'N° de Paradas realizadas'},
                      color_discrete_sequence= [COLOR_PRIMARIO])
        st.plotly_chart(fig3, use_container_width=True)
    else:
        st.warning("No hay datos suficientes para mostrar estrategias.")

with tab4:
    st.subheader("4. Explorador de Datos Crudos")
    st.info(" Esta tabla muestra los registros exactos que están alimentando los gráficos anteriores, ajustándose dinámicamente a los filtros del menú lateral.")
    
    if not df_filtered.empty:
        # st.dataframe crea la tabla interactiva bonita
        st.dataframe(df_filtered, use_container_width=True, hide_index=True)
    else:
        st.warning("No hay datos para mostrar.")
    st.markdown("---")

    st.markdown("### 💾 Exportar Datos")

    formato = st.radio("Selecciona el formato de descarga:", ("Descargar archivo en Excel", "Descargar archivo en CSV"))

    if formato == "Descargar archivo en CSV":
       csv = df_filtered.to_csv(index=False).encode('utf-8')
       st.download_button(
           label="Descargar archivo",
           data=csv,
           file_name="F1_PitStops_Datos.csv",
           mime="text/csv"
        )
    else:
        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
             df_filtered.to_excel(writer, index=False, sheet_name='Datos Filtrados')
        
        st.download_button(
            label="Descargar archivo",
            data=buffer.getvalue(),
            file_name="F1_PitStops_Datos.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

st.markdown("---")
st.caption(f"🏁 Datos procesados con los filtros actuales: **{df_filtered.shape[0]} registros**.")
