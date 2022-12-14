"""
A function for implementing facial recognition
- Options for cropping
- Options for changing colorscale
- Options for blur
"""
import os
import cv2
import numpy as np
import pandas as pd


face_cascade = cv2.CascadeClassifier("./tonelocator/data/haarcascade_frontalface_default.xml")

def face_crop(image_path, to_gray=False, gaussian_blur=False):
    """
    Preprocessing of images for skin tone detection:
    a face detector and crop
    Returns image as an array
    """
    path_check = os.path.isfile(image_path)

    if path_check is False:
        raise ValueError('File does not exist at this location')
    else:
        pass

    temp_image = cv2.imread(image_path)

    if temp_image is None:
        raise ValueError('Image file not read.')
    else:
        pass

    face_detected = face_cascade.detectMultiScale(temp_image, 1.1, 4)

    if isinstance(face_detected, np.ndarray):
        for (x_dim, y_dim, width, height) in face_detected:
            cv2.rectangle(face_detected, (x_dim, y_dim), (x_dim+width, y_dim+height), (0, 0, 255), 2)
            face = temp_image[y_dim:y_dim+15 + height, x_dim+15:x_dim +width]
    else:
        raise TypeError('Face not properly detected')

    if to_gray is True:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    else:
        pass

    if gaussian_blur is True:
        face = cv2.blur(face, (5,5))
    else:
        pass
    return face
