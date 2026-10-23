"""
Live webcam to ASCII art
Author: Huerte (https://github.com/huerte)
"""

import cv2
import numpy as np
import sys
import os
import time
import shutil
import ctypes

# Clean, monotonic ramp (dark -> bright) for dark terminals.
# Same characters as constants.py, reversed.
RAMP = np.array(list(" .:-=+*#%@"))
GAMMA = 0.8  # <1 brightens midtones so they spread across the ramp
LUT = np.array([255 * (i / 255) ** GAMMA for i in range(256)], dtype=np.uint8)
IDX_LUT = (LUT.astype(np.uint32) * (len(RAMP) - 1) // 255).astype(np.uint8)

if os.name == "nt":
    try:
        k32 = ctypes.windll.kernel32
        k32.SetConsoleMode(k32.GetStdHandle(-11), 7)
    except Exception:
        pass

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No webcam found.")
    sys.exit(1)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

sys.stdout.reconfigure(encoding="utf-8")
os.system("cls" if os.name == "nt" else "clear")
sys.stdout.write("\033[?25l")
sys.stdout.flush()

saved = (0, 0)
fw = fh = 1

try:
    while True:
        ok, frame = cap.read()
        if not ok:
            break

        frame = cv2.flip(frame, 1)

        cols, rows = shutil.get_terminal_size()
        if (cols, rows) != saved:
            saved = (cols, rows)
            h, w = frame.shape[:2]
            # fit inside terminal while keeping aspect ratio (no stretching)
            scale = min((cols - 1) / w, (rows - 2) / (h * 0.55))
            fw = max(1, int(w * scale))
            fh = max(1, int(h * scale * 0.55))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = clahe.apply(gray)
        small = cv2.resize(gray, (fw, fh), interpolation=cv2.INTER_AREA)

        picked = RAMP[IDX_LUT[small]]

        sys.stdout.write("\033[H" + "\n".join("".join(r) for r in picked))
        sys.stdout.flush()
        time.sleep(1 / 15)

except KeyboardInterrupt:
    pass
finally:
    sys.stdout.write("\033[?25h")
    os.system("cls" if os.name == "nt" else "clear")
    print("Done.")
    cap.release()