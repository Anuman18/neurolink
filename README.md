# 🧠 NeuroLink – Emotion-Aware AI Assistant

NeuroLink is a full-stack AI-powered assistant that detects **real-time human emotions** using facial expressions and voice tone. Built with **Streamlit**, **OpenCV**, and **Hugging Face Transformers**, it combines AI and psychology to understand how users feel.

---

## 🎯 Features

- 🔍 **Real-time Facial Emotion Detection**  
  Uses webcam + ViT model (`mo-thecreator/vit-Facial-Expression-Recognition`) from Hugging Face

- 🔊 **Voice-Based Emotion Detection**  
  Analyzes user's tone using `Wav2Vec2` speech emotion recognition model

- 📊 **Emotion Logs Dashboard**  
  View stored emotion predictions with timestamps from both face and voice

- 💾 **SQLite Storage**  
  Session logs are stored locally with type (face/voice), emotion, and timestamp

---

## 🛠️ Tech Stack

| Frontend        | Backend            | AI Models                            | Database    |
|-----------------|--------------------|--------------------------------------|-------------|
| Streamlit       | OpenCV, Python     | HuggingFace ViT, Wav2Vec2            | SQLite      |

---

## 📸 Demo Screenshot

> ![Demo](assets/demo.png) <!-- You can replace this with a real screenshot -->

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/<your-username>/neurolink.git
cd neurolink
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run frontend/streamlit_app.py


