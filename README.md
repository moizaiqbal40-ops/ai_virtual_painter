# AI Virtual Painter

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Tasks%20API-orange)](https://developers.google.com/mediapipe)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A real-time, hand-gesture-based drawing application. Draw in the air with your index finger — no gloves, no markers, no extra hardware — using MediaPipe's 21-point hand landmark model for gesture recognition, with simultaneous dual-hand support.

<!-- Record a 10-15s GIF of yourself drawing, save as assets/demo.gif, then uncomment: -->
<!-- ![Demo](assets/demo.gif) -->

## Features

- Real-time hand tracking via MediaPipe's HandLandmarker (Tasks API)
- Draw with your index finger; both hands supported simultaneously, each with an independent color
- Live brush resizing via a pinch gesture (thumb + index), with an on-screen size preview
- Gesture-based eraser (open palm)
- Left-sidebar color palette with hover-to-select
- Exponential-moving-average smoothing for clean, non-jittery strokes
- Optional glow trail and particle effects
- Save drawings as PNG
- Toggleable hand-skeleton overlay

## Tech Stack

Python 3.9+, OpenCV, MediaPipe Tasks API, NumPy

## Installation

```bash
git clone https://github.com/moizaiqbal40-ops/ai_virtual_painter.git
cd ai_virtual_painter
pip install -r requirements.txt
python ai_virtual_painter.py
```

The hand-tracking model (`hand_landmarker.task`, ~8 MB) is **not** committed to this repository — the script checks for it on startup and, if missing, prints the exact command to fetch it:

```bash
curl -L -o hand_landmarker.task https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task
```

## Gesture Controls

| Gesture | Action |
|---|---|
| Index finger only | Draw |
| Index + middle finger | Select color (hover sidebar) |
| Thumb + index pinch | Resize brush |
| Open palm (4 fingers) | Erase |
| Fist | Idle |

## Keyboard Shortcuts

| Key | Function |
|---|---|
| `C` | Clear canvas |
| `G` | Toggle glow/particle effects |
| `H` | Toggle hand-skeleton overlay |
| `S` | Save current drawing to `paintings/` |
| `Q` / `Esc` | Quit |

## How It Works

1. Webcam frames are captured and passed to MediaPipe's `HandLandmarker`, which returns 21 landmarks per detected hand.
2. Finger states (`fingers_up`, `thumb_extended`) are derived from landmark positions using simple geometric comparisons — no ML classifier needed for gesture recognition itself.
3. Landmark geometry is mapped to one of five states (`Draw`, `Select`, `Resize`, `Erase`, `Idle`) per hand, independently.
4. Draw points are smoothed with an exponential moving average before being rendered to a persistent canvas layer, composited back onto the live frame each frame.

## Project Structure
