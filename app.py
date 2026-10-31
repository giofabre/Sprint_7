import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Dashboard de Vehículos Usados",
    page_icon="🚗",
    layout="wide"
)

# -----------------------------------------------------------------------------
# 1. CARGA DE DATOS
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    # Cargar el dataset desde la ruta especificada
    df = pd.read_csv('./data/vehicles_us.csv')
    
    # Tratamiento básico de tipos de datos para filtros
    if 'model_year' in df.columns:
        df['model_year'] = df['model_year'].fillna(0).astype(int)
    
    return df

# Cargar los datos
data = load_data()

# -----------------------------------------------------------------------------
# 2. TÍTULO Y SUBTÍTULO LLAMATIVOS
# -----------------------------------------------------------------------------
st.title("🚗⚡ ¡Super Panel Interactivo de Vehículos en EE.UU.! 🚘💨")
st.markdown("### 📊 *Explora, filtra y analiza el mercado de autos usados en tiempo real* 🔍✨")
st.divider()

# -----------------------------------------------------------------------------
# 4. BARRA LATERAL (FILTROS EN ESTILO DROPDOWN Y CHECKBOX)
# -----------------------------------------------------------------------------
st.sidebar.header("⚙️ Filtros de Selección")

# Filtro Dropdown: Condición del vehículo
all_conditions = ["Todas"] + sorted(data['condition'].dropna().unique().tolist())
selected_condition = st.sidebar.selectbox("Selecciona la condición:", all_conditions)

# Filtro Dropdown: Tipo de combustible
all_fuels = ["Todos"] + sorted(data['fuel'].dropna().unique().tolist())
selected_fuel = st.sidebar.selectbox("Selecciona el tipo de combustible:", all_fuels)

# Filtro Checkbox: Solo vehículos 4WD
filter_4wd = st.sidebar.checkbox("Mostrar solo vehículos 4WD (Tracción 4x4) 🚜")

# Aplicación de los filtros al DataFrame
filtered_df = data.copy()

if selected_condition != "Todas":
    filtered_df = filtered_df[filtered_df['condition'] == selected_condition]

if selected_fuel != "Todos":
    filtered_df = filtered_df[filtered_df['fuel'] == selected_fuel]

if filter_4wd:
    filtered_df = filtered_df[filtered_df['is_4wd'] == 1.0]

# -----------------------------------------------------------------------------
# 3. CHECKBOX PARA VISTA PREVIA DEL DATAFRAME
# -----------------------------------------------------------------------------
show_preview = st.checkbox("👀 Mostrar vista previa del conjunto de datos filtrado")

if show_preview:
    st.subheader("📋 Vista Previa de los Datos (Primeras 10 filas)")
    st.dataframe(filtered_df.head(10), use_container_width=True)
    st.write(f"*Total de registros encontrados con los filtros actuales:* **{len(filtered_df)}**")
    st.divider()

# Validar que haya datos tras aplicar los filtros
if filtered_df.empty:
    st.warning("⚠️ No hay vehículos que coincidan con los filtros seleccionados.")
else:
    # -----------------------------------------------------------------------------
    # 5 & 6. GRÁFICOS INTERACTIVOS CON PLOTLY EXPRESS
    # -----------------------------------------------------------------------------
    
    # Fila 1: Gráfico 1 (Barras) y Gráfico 2 (Pie/Donut)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Tipo de Vehículo vs. Precio Promedio")
        
        # Agrupación para el gráfico de barras
        avg_price_type = (
            filtered_df.groupby('type', as_index=False)['price']
            .mean()
            .sort_values(by='price', ascending=True)
        )
        
        fig_bar = px.bar(
            avg_price_type,
            x='price',
            y='type',
            orientation='h',
            labels={'price': 'Precio Promedio ($)', 'type': 'Tipo de Vehículo'},
            color='price',
            color_continuous_scale='Viridis',
            template='plotly_white'
        )
        fig_bar.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        
        # Renderizado ancho completo
        st.plotly_chart(fig_bar, use_container_width=True)

    with col2:
        st.subheader("🍕 Distribución por Tipo de Transmisión")
        
        fig_pie = px.pie(
            filtered_df,
            names='transmission',
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            template='plotly_white'
        )
        fig_pie.update_traces(textinfo='percent+label')
        fig_pie.update_layout(margin=dict(l=20, r=20, t=30, b=20))
        
        # Renderizado ancho completo
        st.plotly_chart(fig_pie, use_container_width=True)

    st.divider()

    # Fila 2: Gráfico 3 (Histograma a ancho completo)
    st.subheader("📈 Historial y Distribución de Precios")
    
    fig_hist = px.histogram(
        filtered_df,
        x='price',
        nbins=40,
        labels={'price': 'Precio ($)', 'count': 'Frecuencia'},
        color_discrete_sequence=['#636EFA'],
        template='plotly_white',
        marginal="rug"
    )
    fig_hist.update_layout(
        xaxis_title="Precio ($)",
        yaxis_title="Cantidad de Vehículos",
        margin=dict(l=20, r=20, t=30, b=20)
    )
    
    # Renderizado ancho completo
    st.plotly_chart(fig_hist, use_container_width=True)