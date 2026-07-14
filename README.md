# AI Virtual Painter — Real Finger Tracking (MediaPipe + OpenCV)

Koi colored marker/cap nahi chahiye — apni **khaali ungli** se hawa mein
draw karo. Camera aapke haath ke 21 landmarks real-time detect karta hai
aur finger gestures se decide karta hai ke aap **draw**, **color select**,
ya **erase** (hand wave) kar rahi hain.

## 1. Setup

```bash
pip install opencv-python mediapipe numpy
python ai_virtual_painter.py
```

Pehli baar run karne pe browser/OS webcam permission maang sakta hai —
**Allow** kar dein.

## 2. Gestures (ye hi interface hai — koi keyboard click nahi chahiye)

| Gesture | Mode | Kya hota hai |
|---|---|---|
| ☝️ Sirf **index finger** khuli | **DRAW** | Jahan ungli move karo, wahan line banti hai |
| ✌️ **Index + middle** dono khuli | **SELECT** | Top palette ke color box pe ~0.7 sec ruko — color select ho jata hai |
| 🖐 **4 fingers khuli** (khula haath) | **ERASE** | Haath jahan bhi "wave" karo, wahan ki drawing mit jati hai |
| ✊ Mutthi band | **IDLE** | Kuch nahi hota — pen "uthi hui" hai |

Screen ke top-right corner mein hamesha current mode ka colored badge
dikhta rahega (Green=Draw, Orange=Select, Red=Erase, Gray=Idle) — taake
aap bina soche confirm kar sakein ke system kya samajh raha hai.

## 3. Keyboard (extra, optional)

| Key | Action |
|---|---|
| `c` | Pura canvas clear |
| `+` / `-` | Brush aur eraser size badhao/kam karo |
| `h` | Hand-skeleton overlay on/off (dikhane ke liye ke landmarks kaise kaam kar rahe hain) |
| `s` | Drawing ko `paintings/` folder mein PNG save karo |
| `q` / `Esc` | Band karo |

## 4. Troubleshooting

- **Camera nahi khul rahi:** file mein `CAM_INDEX = 0` ko `1` kar dein.
- **Haath detect nahi ho raha:** achi lighting rakhein, haath camera se
  ~30-50cm door rakhein, poora haath frame ke andar hona chahiye.
- **Draw mode "flicker" karta hai:** thoda dheeme move karein — fast
  motion mein MediaPipe kabhi landmark miss kar deta hai (`min_tracking_confidence`
  ko file mein 0.6 se 0.5 kar ke bhi try kar sakti hain).

## 5. Viva / Portfolio ke liye Concepts

1. **Real-time landmark detection** — MediaPipe Hands ek pre-trained
   lightweight CNN model use karta hai jo har frame mein haath ke 21
   keypoints (wrist, knuckles, fingertips) predict karta hai — ye
   syllabus ke "Object Detection & Recognition (Deep Learning models)"
   wale part ko cover karta hai, bina khud model train kiye.
2. **Geometric gesture logic** — Har finger ka "up/down" state uske
   fingertip aur PIP joint ke y-coordinate compare kar ke nikala jata
   hai (`landmarks[tip].y < landmarks[pip].y`). Ye simple lekin
   effective feature-engineering hai.
3. **State machine UI** — Gesture combinations (kitni fingers khuli
   hain) ek chhoti state machine banati hain: Draw / Select / Erase /
   Idle — bina kisi button ke, sirf hand pose se.
4. **Image compositing** — Har frame mein persistent drawing canvas ko
   binary mask (`cv2.threshold` + `bitwise_and`/`bitwise_or`) se live
   video ke upar merge kiya jata hai — image processing ka core concept.

## 6. Extend Karne Ke Ideas (extra marks ke liye)

- Thumb-index pinch distance se brush size control karna (real-time).
- Two-hand support: ek haath draw, dusra haath color palette control.
- Shape recognition: agar drawn stroke roughly circle/rectangle jaisa
  ho to auto-perfect shape mein snap kar dena.
- Recording: har stroke ko timestamp ke sath save kar ke "replay"
  feature banana.

## 7. Files

- `ai_virtual_painter.py` — main program (real finger tracking version)
- `virtual_painter.py` — pehla version (colored marker + HSV tracking) —
  agar aap dono approaches side-by-side dikhana chahein (marker-based
  vs. landmark-based) to ye comparison portfolio mein aur bhi strong
  lagega.
- `paintings/` — saved drawings (auto-created)
