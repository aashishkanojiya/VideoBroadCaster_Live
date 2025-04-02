import cv2

print("🔍 Checking available cameras...")

for i in range(10):  # Try 10 possible camera indices
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cap.isOpened():
        print(f"✅ Camera found at index {i}")
        cap.release()
    else:
        print(f"❌ No camera at index {i}")
