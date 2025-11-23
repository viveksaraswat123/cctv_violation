# 🚦 AI-Based Traffic Violation Detection (FastAPI + YOLO)

This project detects basic traffic violations like **no-helmet** and **triple-riding** using YOLO and FastAPI.  
You can upload an image, and the API returns:

- Detected objects (person, bike, etc.)
- Violation type (if found)
- Bounding box details
- Confidence scores

The goal is to create a simple, easy-to-understand backend that connects machine learning models with a real API system.

---

## 🧠 Features

- Upload an image and run YOLO detection  
- Detect simple violations (no-helmet, triple-riding)  
- FastAPI backend with a clean and modular structure  
- Lightweight ML pipeline in separate folder  
- Easy to extend (OCR, database, video stream, dashboard, etc.)

---

## 🏗️ Project Structure

cctv_violation/
│
├── app/
│ ├── main.py
│ ├── routers/
│ │ ├── detect.py
│ ├── schemas/
│ │ ├── detect.py
│ ├── ml/
│ ├── model.py
│ ├── logic.py
│
└── requirements.txt

yaml
Copy code

---

## 🚀 How to Run

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Start the backend server
bash
Copy code
uvicorn app.main:app --reload
4. Open API docs
Visit:

arduino
Copy code
http://127.0.0.1:8000/docs
Use the /detect endpoint and upload an image to test.

📦 API Endpoints
POST /detect
Uploads an image → returns:

json
Copy code
{
  "violations": ["no_helmet"],
  "detections": [
    {
      "class_name": "person",
      "confidence": 0.89,
      "bbox": [x1, y1, x2, y2]
    }
  ]
}