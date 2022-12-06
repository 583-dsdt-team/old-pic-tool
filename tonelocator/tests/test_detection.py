"""
Module for testing the complexion detection function
"""
import cv2
import numpy
import os
import pandas
import unittest

import detection

class TestDetection(unittest.TestCase):
    """
    Test class for complexion detection: detection.detection
    """

    def test_smoke(self):
        """
        Smoke test for functionality
        Calls the detection on known picture in practice_set folder
        Test is successful if no errors returned
        """
        smoke_image_path = './data/practice_set/a_01.jpg'
        detection.complexion_detection(image_path = smoke_image_path)

    def test_no_picture(self):
        """
        One shot test for missing file
        Calls the detection on picture not in practice_set folder
        Test is successful if error is caught
        """
        test_no_picture_image_path = './data/practice_set/a_06.jpg'
        with self.assertRaises(ValueError):
            detection.complexion_detection(test_no_picture_image_path)
