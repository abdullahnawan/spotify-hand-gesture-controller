<div align="center">

# 🎵 Spotify Hand Gesture Controller

Control your Spotify playback using simple **hand gestures** — no mouse or keyboard needed!

Built with **Python**, **MediaPipe**, **OpenCV**, and **Spotify’s Web API**, this project detects real-time hand movements through your webcam to play, pause, skip, or adjust volume on Spotify.

---

### 🧠 Powered By

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-009688?style=for-the-badge&logo=google&logoColor=white)
![Spotify](https://img.shields.io/badge/Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![TensorFlowLite](https://img.shields.io/badge/TensorFlow_Lite-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

---

### 🌐 Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdullahnawan)
[![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abdullahnawan)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:1abdullah0awan1@gmail.com)

</div>

---

## 🪄 Overview

Control Spotify hands-free with **real-time hand gesture recognition**.  
With gestures like palm, swipe, or raise, you can play/pause, skip tracks, or adjust volume — powered by **computer vision** and the **Spotify API**.

It even includes an **accuracy testing mode** to measure performance live.

---

## 🧩 Features

✅ Real-time hand gesture recognition  
✅ Gesture-to-Spotify command mapping  
✅ Accuracy testing mode  
✅ Works with Spotify Desktop or Web Player  
✅ Built with clean, modular Python code

---

## 🎮 Gesture Controls

|    Gesture     | Action         |
| :------------: | :------------- |
|    ✋ Palm     | Play / Pause   |
| 👉 Swipe Right | Next Track     |
| 👈 Swipe Left  | Previous Track |
|  👆 Swipe Up   | Volume Up      |
| 👇 Swipe Down  | Volume Down    |

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abdullahnawan/spotify-hand-gesture-controller.git
cd spotify-hand-gesture-controller
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Spotify Developer App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create a new app.
3. Set **Redirect URI** to `http://localhost:8888/callback`.
4. Copy your **Client ID** and **Client Secret**.

### 5️⃣ Add Your Credentials

Create a file called `.env` in the project folder:

```bash
SPOTIPY_CLIENT_ID=your_client_id_here
SPOTIPY_CLIENT_SECRET=your_client_secret_here
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

### 6️⃣ Run the Project

```bash
python hand_gesture_spotify.py
```

---

## 🧠 How It Works

1. **MediaPipe** detects hand landmarks via your webcam.
2. **OpenCV** processes and visualizes the frame.
3. The gesture is recognized from landmark motion.
4. **Spotipy** communicates with Spotify’s API for control.

💡 _Tip: Start playing a song on Spotify before launching this script._

---

## 🧰 Tech Stack

| Category             | Tools                 |
| -------------------- | --------------------- |
| **Language**         | Python                |
| **Computer Vision**  | OpenCV, MediaPipe     |
| **Machine Learning** | TensorFlow Lite       |
| **API Integration**  | Spotipy (Spotify API) |
| **Environment**      | Python Virtual Env    |

---

## 🧪 Example Console Output

```
Gesture Control Active | Press 1=palm, 2=right, 3=left, 4=up, 5=down, 0=none
Expected: palm, Detected: palm, Accuracy: 5/6 (83.3%)
```

---

## 🛠️ Future Plans

- Gesture calibration for custom sensitivity
- Multi-hand and multi-user support
- On-screen gesture overlay UI
- Voice + gesture hybrid control

---

## 🛡️ License

This project is open source under the **MIT License**.  
⭐ _If you like this project, consider giving it a star on GitHub!_ ⭐
