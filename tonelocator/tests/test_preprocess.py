"""
Module for testing the preprocessing function
"""
import cv2
import numpy as np
import os
import pandas as pd
import unittest

from tonelocator import preprocess

class TestPreprocess(unittest.TestCase):
    """
    Test class for preprocess: preprocess.face_crop
    """

    def test_smoke(self):
        """
        Smoke test for functionality
        Calls the detection on known picture in practice_set folder
        Test is successful if no errors returned
        """
        smoke_image_path = './tonelocator/data/practice_set/a_01.jpg'
        preprocess.face_crop(image_path = smoke_image_path)
    
    def test_no_picture(self):
        """
        One shot test for missing file
        Calls the detection on picture not in practice_set folder
        Test is successful if error is caught
        """
        test_no_picture_image_path = './tonelocator/data/practice_set/a_06.jpg'
        with self.assertRaises(ValueError):
            preprocess.face_crop(test_no_picture_image_path)

    def test_no_face_detected(self):
        """
        One shot test for missing file
        Calls the detection on blank picture
        Test is successful if error is caught
        """
        test_blank_picture_image_path = './tonelocator/data/test/blank_picture_test.JPG'
        with self.assertRaises(TypeError):
            preprocess.face_crop(test_blank_picture_image_path)
