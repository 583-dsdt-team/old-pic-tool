"""
Module defines the color detection function
"""

import cv2
import numpy
import pandas


rgb_df = pandas.read_csv('https://raw.githubusercontent.com/583-dsdt-team/old-picture-complexion-detection/main/detection/monk_scales_rgb.csv')
bw_df = pandas.read_csv('https://raw.githubusercontent.com/583-dsdt-team/old-picture-complexion-detection/main/detection/monk_scales_bw.csv')

def complexion_detection(image_path, rounding_places=2, grayscale=False):
    """
    Uses the inRange function in opencv
    Detects % of colors from ellis monk scale in image
    """
    filler = []
    temp_image = cv2.imread(image_path)
    


    if grayscale == False:
        for index in range(rgb_df.shape[0]):
            upper = numpy.uint8([rgb_df['upper_b'][index], rgb_df['upper_g'][index], rgb_df['upper_r'][index]])
            lower = numpy.uint8([rgb_df['lower_b'][index], rgb_df['lower_g'][index], rgb_df['lower_r'][index]])
            mask = cv2.inRange(temp_image, lower, upper)
            cur_val = (mask > 0).mean()
            rounded_val = round(cur_val, rounding_places)
            filler.append(rounded_val)
    elif grayscale == True:
        for index in range(bw_df.shape[0]):
            upper = numpy.uint8([bw_df['upper_b'][index], bw_df['upper_g'][index], bw_df['upper_r'][index]])
            lower = numpy.uint8([bw_df['lower_b'][index], bw_df['lower_g'][index], bw_df['lower_r'][index]])
            mask = cv2.inRange(temp_image, lower, upper)
            cur_val = (mask > 0).mean()
            rounded_val = round(cur_val, rounding_places)
            filler.append(rounded_val)
    return(filler)
