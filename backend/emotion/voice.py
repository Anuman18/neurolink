from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification
import torch
import librosa
from backend.utils.db import log_emotion

# ✅ Correct model name from HuggingFace
model_name = "ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"

try:
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name)
except Exception as e:
    print("Failed to load model:", e)
    processor = None
    model = None

labels = ['angry', 'calm', 'happy', 'fearful', 'disgust', 'surprised', 'neutral', 'sad']

def predict_voice_emotion(audio_path):
    if processor is None or model is None:
        return "Model not loaded"

    speech, sr = librosa.load(audio_path, sr=16000)
    input_values = processor(speech, return_tensors="pt", sampling_rate=16000).input_values

    with torch.no_grad():
        logits = model(input_values).logits
    predicted_class = torch.argmax(logits).item()
    emotion = labels[predicted_class]
    log_emotion("voice", emotion)
    return emotion
