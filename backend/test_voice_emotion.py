from emotion.voice import predict_voice_emotion

if __name__ == "__main__":
    emotion = predict_voice_emotion()
    print("Detected Emotion (Voice):", emotion)
