import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# App title
st.title("🧍 YOLOv8 Person Counter with Bounding Boxes")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Cache the model so it doesn't reload on every run
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")  # Automatically downloads the model if not present

model = load_model()

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert PIL image to numpy array (BGR for OpenCV)
    image_np = np.array(image)

    # Detect with spinner
    with st.spinner("Detecting persons..."):
        results = model.predict(image_np, conf=0.3)[0]

    person_count = 0
    names = model.names

    # Draw bounding boxes
    for box in results.boxes:
        cls_id = int(box.cls[0])
        conf = float(box.conf[0])
        if names[cls_id] == "person":
            person_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image_np, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"person {conf:.2f}"
            cv2.putText(image_np, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    st.success(f"🧍 Persons Detected: {person_count}")

    # Convert back to PIL for Streamlit display
    result_image = Image.fromarray(image_np)
    st.image(result_image, caption="Detections", use_container_width=True)
