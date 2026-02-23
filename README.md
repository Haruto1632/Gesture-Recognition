# 🧠 Real-Time ASL Gesture Recognition using MediaPipe

An AI-powered assistive communication system that enables real-time American Sign Language (ASL) alphabet recognition using computer vision and machine learning. This project bridges the communication gap between deaf/mute individuals and the general public by converting hand gestures into readable text.

---

## 🚀 Features

* ✋ Real-time hand tracking using MediaPipe Hands
* 🔤 ASL alphabet recognition (A–Z)
* ⚡ Lightweight GaussianNB classifier
* 🎥 Live webcam inference
* 🧩 Word formation from detected letters
* 🛡️ Stable prediction with smoothing
* 🖥️ Works on standard laptops (no special hardware)
* 🔧 Windows-friendly setup

---

## 🏗️ System Architecture

```
Webcam → MediaPipe Hands → Landmark Extraction → GaussianNB Classifier → Letter → Word Builder → Display
```

---

## 📂 Project Structure

```
Gesture-Recognition/
│
├── models/
│   ├── gesture_clf.pkl
│
├── src/
│   └── extra.py
│
├── run.py
├── README.md
└── requirements.txt
```

---

## 🧰 Tech Stack

* Python 3.10
* OpenCV
* MediaPipe
* NumPy
* Scikit-learn
* Joblib

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Haruto1632/Gesture-Recognition.git
cd Gesture-Recognition
```

---

### 2️⃣ Create virtual environment

```bash
py -3.10 -m venv .venv
.venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install mediapipe==0.10.14 opencv-python numpy scikit-learn joblib
```

---

## ▶️ Running the Project

```bash
python run.py
```

### 🎮 Controls

* **ESC** → Exit
* **Backspace** → Delete last character
* **C** → Clear word (if enabled)

---

## 🧪 How It Works

1. Webcam captures live video
2. MediaPipe detects hand landmarks
3. Landmarks converted to feature vector
4. GaussianNB model predicts ASL letter
5. Stable letters form words
6. Output displayed in real time

---

## 📈 Current Limitations

* Supports ASL alphabet only (static signs)
* Sensitive to very poor lighting
* Works best with single hand in frame
* Dynamic ASL words not yet implemented

---

## 🔮 Future Improvements

* 🔊 Text-to-speech output
* 📱 Mobile deployment
* 🧠 Deep learning classifier
* ✌️ Two-hand support
* 🗣️ Dynamic ASL gesture recognition
* 🌐 Web-based interface

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for improvements.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Haruto アビシェク**

If you found this helpful, consider ⭐ starring the repo!
