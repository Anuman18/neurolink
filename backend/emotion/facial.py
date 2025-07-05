# backend/emotion/facial.py

import cv2
import numpy as np
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from backend.utils.db import log_emotion

# Load ViT model
model_name = "mo-thecreator/vit-Facial-Expression-Recognition"
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(model_name)
model.eval()

# Label map
labels = list(model.config.id2label.values())

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_emotion(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = frame[y : y + h, x : x + w]
        img = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))

        inputs = processor(images=img, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
            probs = torch.softmax(logits, dim=1)[0]
            confidence, pred = torch.max(probs, dim=0)
            emotion = labels[pred]

        # Optional filter for low confidence
        if confidence < 0.5:
            emotion = "Uncertain"

        log_emotion("face", emotion)
        return emotion

    return "No Face"
