import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import cv2
import tempfile
import os
from backend.emotion.facial import detect_emotion
from backend.emotion.voice import predict_voice_emotion
from backend.utils.db import get_emotion_logs
import streamlit as st
import cv2
import tempfile
import os
from backend.emotion.facial import detect_emotion
from backend.emotion.voice import predict_voice_emotion
from backend.utils.db import get_emotion_logs

st.set_page_config(page_title="NeuroLink - Emotion Aware AI", layout="wide")
st.title("🧠 NeuroLink - Emotion-Aware AI Assistant")

# ───────────────────────────── Tabs ─────────────────────────────
home, face_tab, voice_tab, logs_tab = st.tabs([
    "🏠 Home",
    "😀 Face Emotion",
    "🎙️ Voice Emotion",
    "📊 Logs"
])

# ──────────────────────── HOME TAB ────────────────────────
with home:
    st.markdown("""
    ### Welcome to NeuroLink
    NeuroLink is an AI-powered assistant that detects emotions from **facial expressions** and **voice tone** in real-time.

    🔍 Use the tabs to:
    - Detect facial emotion from webcam
    - Upload voice recordings for emotional analysis
    - View emotion logs and trends
    """)

# ─────────────── FACE EMOTION DETECTION TAB ───────────────
with face_tab:
    st.header("😀 Real-time Face Emotion Detection")

    run_face = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.image([])

    if run_face:
        cap = cv2.VideoCapture(0)
        st.info("Press the checkbox again to stop webcam.")

        while run_face:
            ret, frame = cap.read()
            if not ret:
                st.error("Failed to grab frame.")
                break

            emotion = detect_emotion(frame)

            # Draw emotion on frame
            cv2.putText(frame, emotion, (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            FRAME_WINDOW.image(frame)

        cap.release()
        cv2.destroyAllWindows()

# ─────────────── VOICE EMOTION DETECTION TAB ───────────────
with voice_tab:
    st.header("🎙️ Voice Emotion Detection")
    uploaded_audio = st.file_uploader("Upload a `.wav` audio file", type=["wav"])

    if uploaded_audio is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_file.write(uploaded_audio.read())
            tmp_path = tmp_file.name

        st.audio(tmp_path, format="audio/wav")
        with st.spinner("Analyzing voice emotion..."):
            emotion = predict_voice_emotion(tmp_path)

        st.success(f"Predicted Emotion: **{emotion.upper()}**")

# ─────────────── EMOTION LOGS TAB ───────────────
with logs_tab:
    st.header("📊 Emotion Logs")

    logs = get_emotion_logs()

    if logs and len(logs) > 0:
        st.table(logs)
    else:
        st.info("No emotion logs found yet.")
