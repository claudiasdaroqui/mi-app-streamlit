import streamlit as st
import cv2
import os
import numpy as np
from moviepy.editor import VideoFileClip

# Create a simple Streamlit dashboard
st.title("Automatic Video Tagging System")
st.write("Welcome to the automatic video tagging project! This tool processes videos and assigns tags based on their content.")

# Video upload
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    video_path = f"temp/{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.video(video_path)

    # Video processing with OpenCV
    st.write("Processing video...")

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    tags = set()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect objects using basic color detection (as a placeholder for actual ML models)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

        if np.sum(mask) > 10000:
            tags.add("Blue Object Detected")

        frame_count += 1

        if frame_count % 30 == 0:
            st.write(f"Processed {frame_count} frames...")

    cap.release()

    # Display tags
    st.write("Video processing complete! Here are the detected tags:")
    for tag in tags:
        st.write(f"- {tag}")

# Adding your CV and projects
st.sidebar.title("About Me")
st.sidebar.write("**Name:** Your Name")
st.sidebar.write("**Skills:** Python, Video Editing, Production")
st.sidebar.write("**CV:** [View my CV](#)")

st.sidebar.title("Projects")
st.sidebar.write("1. Automatic Video Tagging System")
st.sidebar.write("2. Video Editing Portfolio")
st.sidebar.write("3. Showrunner Production Course")
