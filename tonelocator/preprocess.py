"""
A function for implementing facial recognition
- Options for cropping
- Options for changing colorscale
- Options for blur
"""
import cv2
import numpy as np
import os
import pandas as pd


face_cascade = cv2.CascadeClassifier("./tonelocator/data/haarcascades/haarcascade_frontalface_default.xml")
    
def face_crop(image_path, to_gray=False, gaussian_blur=False):
    """
    Preprocessing of images for skin tone detection:
    a face detector and crop
    Returns image as an array
    """
    temp_picture = cv2.imread(image_path)
    face_detected = face_cascade.detectMultiScale(temp_picture, 1.1, 4)
    for (x, y, w, h) in face_detected:
        cv2.rectangle(face_detected, (x, y), (x+w, y+h), (0, 0, 255), 2)
        face = temp_picture[y:y+15 + h, x+15:x +w]
        
    if to_gray is True:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    else:
        pass

    if gaussian_blur is True:
        face = cv2.blur(face, (5,5))
    else:
        pass
    return face
