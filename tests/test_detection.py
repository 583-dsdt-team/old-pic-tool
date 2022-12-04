"""
Module for testing the complexion detection function
"""
import cv2
import numpy
import os
import pandas
import unittest

from src import detection

class TestDetection(unittest.TestCase):
    """
    Test class for complexion detection: detection.detection
    """
    def test_smoke(self):
        """
        Smoke test for functionality
        Calls the detection on known picture in example folder
        Test is successful if no errors returned
        """
        
        detection.detection()