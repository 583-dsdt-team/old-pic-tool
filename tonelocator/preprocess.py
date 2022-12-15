"""
A function for implementing facial recognition
- Options for cropping
- Options for changing colorscale
- Options for blur
"""
import os
import cv2
import numpy as np


cascade = cv2.CascadeClassifier("./tonelocator/data/haarcascade_frontalface_default.xml")

def face_crop(image_path, to_gray=False, gaussian_blur=False):
    """
    Preprocessing of images for skin tone detection:
    a face detector and image crop to detected face
    Returns image as an array per cv2
    """
    # Check file path
    path_check = os.path.isfile(image_path)

    # Error for path check
    if path_check is False:
        raise ValueError('File does not exist at this location')

    # Load image when file path exists
    temp_image = cv2.imread(image_path)

    # Check if image loaded
    if temp_image is None:
        raise ValueError('Image file not read.')

    # Detect a face in the loaded image
    face_detected = cascade.detectMultiScale(temp_image, 1.1, 4)

    # opencv loads images as an array:
    if isinstance(face_detected, np.ndarray):
        for (x_dim, y_dim, width, height) in face_detected:
            cv2.rectangle(face_detected, (x_dim, y_dim), (x_dim + width, y_dim + height), (0, 0, 255), 2)
            face = temp_image[y_dim:y_dim + 15 + height, x_dim + 15:x_dim + width]
    else:
        raise TypeError('Face not properly detected')

    # Boolean for converting to grayscale
    if to_gray is True:
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    else:
        pass

    # Adding some blur
    if gaussian_blur is True:
        face = cv2.blur(face, (5, 5))
    else:
        pass

    return face
