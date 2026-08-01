"""All OpenCV UI-drawing helpers (topbar, sidebar, badges, skeleton overlay)."""

import cv2

from config import FRAME_W, FRAME_H, TOPBAR_H, SIDEBAR_W, PALETTE, HAND_CONNECTIONS


def draw_topbar(frame, fps):
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (FRAME_W, TOPBAR_H), (25, 25, 25), -1)
    cv2.addWeighted(overlay, 0.85, frame, 0.15, 0, dst=frame)
    cv2.putText(frame, "AI VIRTUAL PAINTER", (16, 30), cv2.FONT_HERSHEY_DUPLEX,
                0.62, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, f"FPS: {int(fps)}", (FRAME_W - 110, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (200, 200, 200), 1, cv2.LINE_AA)
    cv2.putText(frame, "1 finger=draw  2=pick color  pinch=resize  open palm=erase",
                (250, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (170, 170, 170), 1, cv2.LINE_AA)


def sidebar_box_height():
    usable_h = FRAME_H - TOPBAR_H
    n_boxes = len(PALETTE) + 1
    return usable_h // n_boxes


def draw_sidebar(frame, hand_states):
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, TOPBAR_H), (SIDEBAR_W, FRAME_H), (25, 25, 25), -1)
    cv2.addWeighted(overlay, 0.85, frame, 0.15, 0, dst=frame)

    box_h = sidebar_box_height()
    for i, item in enumerate(PALETTE):
        y1 = TOPBAR_H + i * box_h
        y2 = y1 + box_h - 6
        cv2.rectangle(frame, (10, y1 + 3), (SIDEBAR_W - 10, y2), item["bgr"], -1, cv2.LINE_AA)
        for label, st in hand_states.items():
            if st["color_idx"] == i:
                ring_color = (255, 255, 255) if label == "Right" else (0, 255, 255)
                cv2.rectangle(frame, (10, y1 + 3), (SIDEBAR_W - 10, y2), ring_color, 2, cv2.LINE_AA)

    y1 = TOPBAR_H + len(PALETTE) * box_h
    y2 = y1 + box_h - 6
    cv2.rectangle(frame, (10, y1 + 3), (SIDEBAR_W - 10, y2), (40, 40, 40), -1, cv2.LINE_AA)
    cv2.putText(frame, "CLEAR", (18, (y1 + y2) // 2 + 5), cv2.FONT_HERSHEY_SIMPLEX,
                0.42, (255, 255, 255), 1, cv2.LINE_AA)

    return box_h


def sidebar_index_for_y(y, box_h):
    if y < TOPBAR_H:
        return -1
    idx = (y - TOPBAR_H) // box_h
    if 0 <= idx <= len(PALETTE):
        return int(idx)
    return -1


def draw_hand_badge(frame, label, pos, mode, color):
    text = f"{label}: {mode}"
    x, y = pos[0] - 40, max(pos[1] - 26, TOPBAR_H + 14)
    (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    cv2.rectangle(frame, (x - 6, y - th - 6), (x + tw + 6, y + 6), (20, 20, 20), -1, cv2.LINE_AA)
    cv2.rectangle(frame, (x - 6, y - th - 6), (x + tw + 6, y + 6), color, 1, cv2.LINE_AA)
    cv2.putText(frame, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)


def draw_skeleton(frame, landmarks_px, tint):
    for a, b in HAND_CONNECTIONS:
        cv2.line(frame, landmarks_px[a], landmarks_px[b], tint, 2, cv2.LINE_AA)
    for pt in landmarks_px:
        cv2.circle(frame, pt, 3, (255, 255, 255), -1, cv2.LINE_AA)
