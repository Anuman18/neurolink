import cv2

for i in range(3):  # Try indexes 0, 1, 2
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ Camera index {i} is working!")
        cap.release()
    else:
        print(f"❌ Camera index {i} not working")
