"""
Module for testing the colorizer function
"""

import unittest

from colorizer import colorizer

class TestDetection(unittest.TestCase):
    """
    Test class for colorizer: colorizer.colorizer
    """

    def test_smoke(self):
        """
        Smoke test for functionality
        Calls the colorizer on known picture in practice_set folder
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
        detection.complexion_detection(test_no_picture_image_path)