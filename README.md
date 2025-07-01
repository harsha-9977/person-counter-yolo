https://person-counter-yolo-1625.streamlit.app/

# 🧍‍♂️ Person Counter YOLO App

This Streamlit app uses **YOLO (You Only Look Once)** from the `ultralytics` library to detect and count people in images using real-time object detection.

![Screenshot 2025-07-02 010835](https://github.com/user-attachments/assets/d4bba3a9-8957-43ca-8340-c524d44a7326)


---

## 🚀 Features

- 🧠 YOLOv8/YOLOv5-based person detection
- 📸 Upload image for analysis
- 🔢 Live count of detected persons
- 📦 Deployable on Streamlit Cloud

---

## 🛠️ Installation (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/harsha-9977/person-counter-yolo.git
cd person-counter-yolo
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Cloud

### Required Files

Make sure your repo includes:

* `app.py` (your main Streamlit app)
* `requirements.txt` (Python libraries)
* `packages.txt` (system packages like libGL)

### Example `packages.txt`

```
libgl1
```

This installs `libGL.so.1` which is needed for OpenCV to work.

---

## 📂 File Structure

```
person-counter-yolo/
├── app.py
├── requirements.txt
├── packages.txt
├── yolov8n.pt         # or your model file
└── assets/             # optional: images, test inputs
```

---

## 🧠 Model

This app uses [Ultralytics YOLOv8](https://docs.ultralytics.com/) models. You can switch to `yolov5s.pt` or `yolov8n.pt` depending on your use case.



## 👤 Author

* **Harsha** – [@your\_github](https://github.com/harsha-9977)

---


