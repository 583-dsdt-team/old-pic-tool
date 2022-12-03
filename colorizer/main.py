
import numpy as np
import cv2
import time
from os.path import splitext, basename, join
import sh

class Colorizer:
    def __init__(self, height = 480, width = 600):
        (self.height, self.width) = height, width
        self.colorModel = cv2.dnn.readNetFromCaffe("model/colorization_deploy_v2.prototext",
        caffeModel = "model/dummy.caffemodel")

        clusterCenters = np.load("model")


sh get_models.sh


