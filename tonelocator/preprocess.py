"""
A function for implementing facial recognition
- Options for cropping
- Options for changing colorscale
- Options for blur
"""

face_cascade = cv2.CascadeClassifier("/mnt/c/Users/breha/Documents/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml")
    
def face_detection(origin_path, destination_path, keep_colors = True, gaussian_blur = False):
    """
    Preprocessing of images for skin tone detection.
    """
    temp_picture = cv2.imread(image_path)
    face_detected = face_cascade.detectMultiScale(example_picture, 1.1, 4)
    for (x, y, w, h) in face_detected:
        cv2.rectangle(face_detected, (x, y), (x+w, y+h), (0, 0, 255), 2)
        face = example_picture[y:y+15 + h, x+15:x +w]
        cv2.imwrite(destination_path, face)

