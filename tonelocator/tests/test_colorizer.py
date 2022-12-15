"""
Module for testing the colorizer function
"""

import os.path
import tempfile
import unittest

import tonelocator.colorizer.colorizer as colorizer

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
        smoke_image_path = os.path.join(os.path.dirname(__name__), r'tonelocator/colorizer/input/bw_photo_8.jpeg') 
        colorizer.colorize_image(smoke_image_path)
    
    def test_no_picture(self):
        """
        One shot test for wrong filetype
        Calls the colorizer on file that is not jpeg
        Test is successful if error is caught 
        """
        test_no_image = os.path.join(os.path.dirname(__name__), r'tonelocator/data/test/test.txt') 
        with self.assertRaises(ValueError):
            colorizer.colorize_image(test_no_image)
        return

    def test_empty_folder(self):
        """
        One shot test for empty folder
        Calls the colorize folder function on an empty folder
        Test is successful if error is caught
        """
        test_empty_folder = os.path.join(os.path.dirname(__name__), r'tonelocator/data/test/empty_test_folder') 
        with self.assertRaises(ValueError):
            colorizer.colorize_folder(input_folder=test_empty_folder)
        return

"""
test_empty_folder = tempfile.TemporaryDirectory()

with tempfile.TemporaryDirectory() as tmpdirname:
     print('created temporary directory', tmpdirname)


tmpdir = tempfile.mktemp()
os.rmdir(tmpdir)

tmpdir = tempfile.TemporaryDirectory()

"""