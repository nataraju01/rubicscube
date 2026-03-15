
import cv2
import numpy as np

def detect_color(bgr):

    b, g, r = bgr

    if r > 150 and g < 80 and b < 80:
        return "R"
    elif g > 150 and r < 100:
        return "G"
    elif b > 150 and r < 100:
        return "B"
    elif r > 150 and g > 150 and b < 80:
        return "Y"
    elif r > 150 and g > 150 and b > 150:
        return "W"
    else:
        return "O"


def extract_colors(frame):

    h, w, _ = frame.shape
    step = 50

    colors = []

    for i in range(3):
        for j in range(3):

            x = int(w/2 - 75 + j*step)
            y = int(h/2 - 75 + i*step)

            region = frame[y:y+30, x:x+30]
            avg = region.mean(axis=0).mean(axis=0)

            colors.append(detect_color(avg))

    return colors
