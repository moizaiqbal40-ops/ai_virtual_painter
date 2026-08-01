"""Lightweight particle system used for the drawing glow/sparkle effect."""

import random
import cv2


class Particles:
    def __init__(self, max_particles: int = 180):
        self.items = []
        self.max_particles = max_particles

    def spawn(self, pos, color):
        if len(self.items) >= self.max_particles:
            return
        for _ in range(2):
            jitter = (random.randint(-6, 6), random.randint(-6, 6))
            self.items.append({
                "pos": (pos[0] + jitter[0], pos[1] + jitter[1]),
                "color": color,
                "life": random.randint(10, 18),
                "max_life": 18,
                "radius": random.randint(2, 4),
            })

    def update_and_draw(self, frame):
        alive = []
        for p in self.items:
            p["life"] -= 1
            if p["life"] > 0:
                fade = p["life"] / p["max_life"]
                overlay = frame.copy()
                cv2.circle(overlay, p["pos"], p["radius"], p["color"], -1, cv2.LINE_AA)
                cv2.addWeighted(overlay, fade * 0.6, frame, 1 - fade * 0.6, 0, dst=frame)
                alive.append(p)
        self.items = alive
