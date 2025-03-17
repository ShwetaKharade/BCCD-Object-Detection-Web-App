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
Use [this image](https://github.com/Shenggan/BCCD_Dataset/blob/master/BCCD/JPEGImages/BloodImage_00006.jpg) for testing.

---

> Made with ❤️ for Artigence Healthcare Internship Assignment
