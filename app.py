import streamlit as st
from PIL import Image
from ultralytics import YOLO
import pandas as pd
import numpy as np
import torch

# Load fine-tuned model
@st.cache_resource
def load_model():
    model = YOLO("/content/BCCD_Dataset/bccd-streamlit-app/yolov10_best.pt")  # path to your trained model
    return model

model = load_model()
class_names = ['WBC', 'RBC', 'Platelets']

# Streamlit UI
st.set_page_config(page_title="BCCD Detector", layout="centered")
st.title("🧬 BCCD Object Detection with YOLOv10")
st.markdown("Upload a blood cell image to detect **WBCs**, **RBCs**, and **Platelets**.")

uploaded_image = st.file_uploader("📤 Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Perform inference
    results = model.predict(image)
    result = results[0]
    
    # Draw predictions
    annotated_img = result.plot()
    st.image(annotated_img, caption="Detected Cells", use_column_width=True)

    # Show predictions table
    boxes = result.boxes
    if boxes and boxes.cls is not None:
        classes = [class_names[int(cls)] for cls in boxes.cls.cpu().numpy()]
        confidences = [round(float(c), 3) for c in boxes.conf.cpu().numpy()]
        df = pd.DataFrame({"Class": classes, "Confidence": confidences})
        st.markdown("### 📊 Prediction Summary")
        st.dataframe(df)
    else:
        st.warning("No objects detected.")
