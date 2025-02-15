import streamlit as st
from PIL import Image
import base64

# Configure the page layout
st.set_page_config(layout="wide")

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'inicio'

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0;
    }
    .stButton button {
        background-color:rgb(20, 17, 189);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .title-text {   
        font-size: 48px;
        font-weight: bold;
        margin-bottom: 0;
    }
    .green-text {
        color: rgb(20, 17, 189);
    }
    .subtitle-text {
        color: white;
        font-size: 20px;
        margin-bottom: 20px;
    }
    .nav-link {
        cursor: pointer;
        text-decoration: none;
        color: black;
    }
    .nav-link:hover {
        color: rgb(20, 17, 189);
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation bar
col1, col2, col3, col4, col5, = st.columns([2,2,2,2,2])
with col1:
    st.image("https://i.ibb.co/qLxTvHvW/logo.png", width=80)
with col2:
    if st.button("Inicio"):
        st.session_state.current_page = 'inicio'
with col3:
    if st.button("Características"):
        st.session_state.current_page = 'caracteristicas'
with col4:
    if st.button("Servicios"):
        st.session_state.current_page = 'servicios'
with col5:
    if st.button("Sobre Nosotros"):
        st.session_state.current_page = 'sobre_nosotros'

# Content based on current page
if st.session_state.current_page == 'inicio':
    st.markdown("""
        <div style="position: relative; text-align: center; color: white; padding: 100px 0; 
                    background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                    url('https://images.unsplash.com/photo-1486312338219-ce68d2c6f44d?w=1000') center/cover;">
            <h1 class="title-text">
                <span class="green-text">SIGCO</span> SYSTEMS
            </h1>
            <p class="subtitle-text">
                Desarrollo de software de Gestión a medida con facturación electrónica
            </p>
            <button class="stButton">Saber Más</button>
        </div>
        """, unsafe_allow_html=True)

elif st.session_state.current_page == 'caracteristicas':
    st.header("Características")
    st.write("""
    ### Nuestras Características Principales
    - Desarrollo a medida
    - Interfaz intuitiva
    - Soporte 24/7
    - Actualizaciones continuas
    - Seguridad avanzada
    """)

elif st.session_state.current_page == 'servicios':
    st.header("Servicios")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Desarrollo Web")
        st.write("Creamos soluciones web personalizadas")
    with col2:
        st.subheader("Software Empresarial")
        st.write("Sistemas de gestión empresarial a medida")
    with col3:
        st.subheader("Consultoría IT")
        st.write("Asesoramiento tecnológico especializado")

elif st.session_state.current_page == 'sobre_nosotros':
    st.header("Sobre Nosotros")
    st.write("""
    ### Nuestra Historia
    SIGCO SYSTEMS es una empresa líder en desarrollo de software con más de 10 años de experiencia
    en el mercado. Nos especializamos en crear soluciones tecnológicas que impulsan el crecimiento
    de nuestros clientes.
    
    ### Nuestra Misión
    Proporcionar soluciones tecnológicas innovadoras que transformen y mejoren los procesos
    empresariales de nuestros clientes.
    """)

# Add navigation arrows (only visible in home page)
if st.session_state.current_page == 'inicio':
    col_left, col_center, col_right = st.columns([1,10,1])
    with col_left:
        st.markdown("""
            <div style="color: white; font-size: 24px; cursor: pointer;">←</div>
        """, unsafe_allow_html=True)
    with col_right:
        st.markdown("""
            <div style="color: white; font-size: 24px; cursor: pointer;">→</div>
        """, unsafe_allow_html=True)