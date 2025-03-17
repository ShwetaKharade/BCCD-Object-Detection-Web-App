# 🧬 BCCD Blood Cell Detector (YOLOv10 + Streamlit)

This web app detects **WBCs, RBCs, and Platelets** in microscopic blood images using a YOLOv10 model fine-tuned on the [BCCD Dataset](https://github.com/Shenggan/BCCD_Dataset).

## 🚀 Try the Live App
👉 [Hugging Face Space Link](https://huggingface.co/spaces/ShwetaKh/bccd-streamlit-detector)

## 🔧 Tech Stack
- YOLOv10 (Ultralytics)
- Streamlit (Web Interface)
- Hugging Face Spaces (Deployment)

## 📂 Files
- `app.py` – Streamlit app interface
- `yolov10_best.pt` – Fine-tuned model on BCCD dataset
- `requirements.txt` – Python dependencies

## 📊 Model Details
- Model: YOLOv10s
- Trained for 50 epochs on BCCD dataset
- Classes: WBC, RBC, Platelets

## 📸 Sample Image
Use [this image](https://github.com/Shenggan/BCCD_Dataset/blob/master/BCCD/JPEGImages/BloodImage_00006.jpg) or [this image](https://www.google.com/url?sa=i&url=https%3A%2F%2Fquizlet.com%2F272599408%2Fblood-cells-under-the-microscope-diagram%2F&psig=AOvVaw3pHJrYIRd8WU2kClgjBZR_&ust=1742285743035000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNCqwbDWkIwDFQAAAAAdAAAAABAE)for testing.


---
> Made for Artigence Healthcare Internship Assignment
