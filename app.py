import streamlit as st
import cv2
import numpy as np
import tempfile
import json
from ultralytics import YOLO

# preload object detection model
@st.cache_resource
def load_model():
    return YOLO("yolov3.pt") # pretrained weights

st.title("AIMonk Object Detection 🖼️")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded image to temp file
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())
    
    # Load with OpenCV
    img = cv2.imread(tfile.name)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Run object detection
    model = load_model()
    results = model(img_rgb)

    # Plot bounding boxes
    annotated_img = results[0].plot()
    
    # Extract structured JSON
    detections = []
    for box in results[0].boxes:
        cls_id = int(box.cls.cpu().numpy())
        label = model.names[cls_id]
        conf = float(box.conf.cpu().numpy())
        xyxy = box.xyxy.cpu().numpy().tolist()[0]  # [x1, y1, x2, y2]
        
        detections.append({
            "class_id": cls_id,
            "label": label,
            "confidence": conf,
            "bbox": {
                "x1": xyxy[0],
                "y1": xyxy[1],
                "x2": xyxy[2],
                "y2": xyxy[3]
            }
        })

    # Display results
    st.image(annotated_img, caption="Detected Objects", use_column_width=True)
    st.subheader("Detection Results (JSON)")
    st.json(detections)
