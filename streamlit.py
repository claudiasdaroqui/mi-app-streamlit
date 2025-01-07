# streamlit.py
import streamlit as st
import pandas as pd
import json

# Función para mostrar el dashboard
def show_dashboard():
    st.title("Dashboard de Proyecto: Sistema de Etiquetado de Videos")

    # Mostrar currículum y proyectos
    st.header("Currículum Vitae")
    st.write("**Nombre:** Claudia S. Daroqui")
    st.write("**Experiencia:** Showrunner, Producción Audiovisual, Editor de Video")

    # Mostrar proyectos anteriores
    st.header("Proyectos Anteriores")
    st.write("- **Sistema de Etiquetado de Videos**: Automatización en etiquetado y análisis de contenido audiovisual.")
    st.write("- **Producción de Cortometrajes**: Dirección y edición de cortometrajes para plataformas online.")

    # Mostrar las etiquetas generadas
    st.header("Etiquetas Generadas")
    example_tags = {
        "video_1.mp4": ["Comedia", "Alegría", "Personas"],
        "video_2.mp4": ["Drama", "Tristeza", "Naturaleza"]
    }
    df_tags = pd.DataFrame(example_tags)
    st.dataframe(df_tags)

# Llamar a la función de dashboard
show_dashboard()
