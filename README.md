**📌 Project Overview**
This project implements a License Plate Detection System using Deep Learning.
The model is trained to detect vehicle license plates from images and video streams using a YOLO-based object detection approach.
**🧠 Model Details**
Model Type: YOLO (You Only Look Once)
Framework: PyTorch
Task: Object Detection
Detected Object: Vehicle License Plate
Input: Images / Video frames
Output: Bounding box coordinates with confidence score
**⚙️ Installation**
**1️⃣ Clone the Repository**
     -git clone <repository-url>
      cd license-plate-detectio
**  2️⃣ Create Virtual Environment (Optional but Recommended)**
          python -m venv venv
          source venv/bin/activate
**3️⃣ Install Dependencies**
pip install -r requirements.txt
**▶️ How to Run**
🔹 Detect License Plate in an Image
python detect.py --model "license_plate_detector (1).pt" --source image.jpg
🔹 Detect License Plate in a Video
python detect.py --model "license_plate_detector (1).pt" --source video.mp4
🔹 Use Webcam
python detect.py --model "license_plate_detector (1).pt" --source 0
