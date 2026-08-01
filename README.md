````markdown
# 🎨 AI Virtual Painter

A real-time **hand gesture-based virtual drawing application** built with **Python, OpenCV, and MediaPipe**. The application enables users to draw in the air using natural hand gestures without requiring gloves, colored markers, or external hardware.

By leveraging MediaPipe's 21-hand-landmark detection, the system recognizes different gestures for drawing, color selection, brush resizing, erasing, and canvas interaction in real time.

---

## ✨ Features

- 🖐️ Real-time hand tracking using MediaPipe
- ✍️ Draw naturally with your index finger
- 👋 Simultaneous drawing with **both hands**
- 🎨 Interactive left-side color palette
- 🤏 Pinch gesture to resize the brush dynamically
- 🧽 Hand gesture eraser
- ✨ Glow trail and particle effects
- 💾 Save drawings as PNG images
- 🦴 Toggle hand landmark visualization
- ⚡ Smooth drawing using exponential moving average (EMA)

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- MediaPipe Tasks API
- NumPy

---

## 📂 Project Structure

```text
AI-Virtual-Painter/
│
├── ai_virtual_painter.py
├── hand_landmarker.task
├── README.md
├── paintings/
└── assets/
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Virtual-Painter.git
cd AI-Virtual-Painter
```

### 2. Install dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 3. Download the MediaPipe model

Download the **hand_landmarker.task** model from the official MediaPipe repository and place it in the project directory.

> The application automatically checks whether the model exists before launching.

### 4. Run the project

```bash
python ai_virtual_painter.py
```

---

## 🎮 Gesture Controls

| Gesture                  | Action       |
| ------------------------ | ------------ |
| ☝️ Index Finger          | Draw         |
| ✌️ Index + Middle Finger | Select Color |
| 🤏 Thumb + Index Pinch   | Resize Brush |
| 🖐️ Open Palm             | Erase        |
| ✊ Fist                  | Idle         |

---

## ⌨️ Keyboard Shortcuts

| Key         | Function                       |
| ----------- | ------------------------------ |
| `C`         | Clear Canvas                   |
| `G`         | Toggle Glow & Particle Effects |
| `H`         | Toggle Hand Skeleton           |
| `S`         | Save Current Drawing           |
| `Q` / `ESC` | Exit Application               |

---

## 📸 Screenshots

> Add screenshots or a GIF inside the **assets/** directory.

```text
assets/
├── demo.gif
├── drawing.png
├── sidebar.png
├── resize.png
└── erase.png
```

Example:

```markdown
![Demo](assets/demo.gif)
```

---

## ⚙️ How It Works

1. The webcam captures live video frames.
2. MediaPipe detects 21 hand landmarks in real time.
3. Finger positions are analyzed using geometric rules.
4. Each gesture is mapped to a specific application state.
5. Drawing is rendered on a persistent canvas with smoothing.
6. Glow effects and particles enhance the visual experience.

---

## 📈 Future Improvements

- Shape recognition (Circle, Rectangle, Line)
- Undo / Redo support
- Multi-layer canvas
- Stroke recording and replay
- Export to SVG/PDF
- Gesture customization
- AI-based gesture classification

---

## 💡 Computer Vision Concepts

This project demonstrates several important computer vision concepts:

- Real-time Hand Landmark Detection
- Gesture Recognition
- Feature Engineering
- Image Compositing
- Human-Computer Interaction (HCI)
- State Machine Design
- Motion Smoothing
- Real-Time Graphics Rendering

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Moeeza Iqbal**

Computer Science Student | Python Developer | Computer Vision Enthusiast

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN

---

⭐ If you found this project helpful, consider giving it a star.
````
