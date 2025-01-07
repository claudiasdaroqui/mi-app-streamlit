# app.py
import moviepy.editor as mp
from PIL import Image
import streamlit as st

# Función para cargar un video y extraer su primer fotograma
def extract_frame(video_path):
    video = mp.VideoFileClip(video_path)
    frame = video.get_frame(1)  # Extrae el primer fotograma (segundo 1)
    image = Image.fromarray(frame)
    return image

# Función para cargar el video y mostrarlo
def display_video(video_path):
    video = mp.VideoFileClip(video_path)
    st.video(video_path)

# Título de la app
st.title("Sistema de Etiquetado Automático de Videos")

# Subir un video para procesar
uploaded_video = st.file_uploader("Sube un video", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Mostrar el video
    st.header("Video Cargado:")
    display_video(uploaded_video)

    # Extraer y mostrar el primer fotograma
    st.header("Primer fotograma del video:")
    frame_image = extract_frame(uploaded_video)
    st.image(frame_image, caption="Primer fotograma extraído", use_column_width=True)
