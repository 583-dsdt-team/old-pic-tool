"""
This script will import black and white photos,
add color to them, and save the colorized image.

Colorization based on the Zhang Image Colorization Deep Learning Algorithm
This header to remain with this code.

Code was based on code for the PySimpleGUI colorizer:
    https://github.com/PySimpleGUI/PySimpleGUI-Photo-Colorizer

The implementation of the colorization algorithm is from PyImageSearch
You can learn how the algorithm works and the details of this implementation here:
https://www.pyimagesearch.com/2019/02/25/black-and-white-image-colorization-with-opencv-and-deep-learning/

You will need to download the pre-trained data from this location and place in the model folder:
https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1

"""

import cv2
import imghdr
import numpy as np
import os.path
import sys

VERSION = '1 December 2022'

# DMC - added 'colorizer' to path name
PROTOTXT = r'tonelocator/colorizer/model/colorization_deploy_v2.prototxt'
MODEL = r'tonelocator/colorizer/model/colorization_release_v2.caffemodel'
POINTS = r'tonelocator/colorizer/model/pts_in_hull.npy'
PROTOTXT = os.path.join(os.path.dirname(__name__), PROTOTXT)
MODEL = os.path.join(os.path.dirname(__name__), MODEL)
POINTS = os.path.join(os.path.dirname(__name__), POINTS)

if not os.path.isfile(MODEL):
    raise ValueError('You are missing the file "colorization_release_v2.caffemodel"',
        'Download it and place into your "model" folder',
        'You can download this file from this location:\n',
        r'https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1')
else:
    pass

net = cv2.dnn.readNetFromCaffe(PROTOTXT, MODEL)     # load model from disk
pts = np.load(POINTS)

# add the cluster centers as 1x1 convolutions to the model
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]


def colorize_image(image_filename=None):
    """
    This sets up the colorizer.
    """
    # Making sure image is in jpeg format
    if imghdr.what(image_filename) != 'jpeg':
        raise ValueError("Image not in jpeg format")
    # load the input image from disk, scale the pixel intensities to the range [0, 1],
    #   and then convert the image from the BGR to Lab color space
    image = cv2.imread(image_filename)
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    # resize the Lab image to 224x224 (the dimensions the colorization network accepts),
    #   split channels, extract the 'L' channel, and then perform mean centering
    resized = cv2.resize(lab, (224, 224))
    lchan = cv2.split(resized)[0]
    lchan -= 50

    # pass the L channel through the network which will *predict* the 'a' and 'b' channel values
    net.setInput(cv2.dnn.blobFromImage(lchan))
    abchan = net.forward()[0, :, :, :].transpose((1, 2, 0))

    # resize the predicted 'ab' volume to the same dimensions as our input image
    abchan = cv2.resize(abchan, (image.shape[1], image.shape[0]))

    # grab the 'L' channel from the *original* input image (not the resized one)
    #   and concatenate the original 'L' channel with the predicted 'ab' channels
    lchan = cv2.split(lab)[0]
    colorized = np.concatenate((lchan[:, :, np.newaxis], abchan), axis=2)

    # convert the output image from the Lab color space to RGB,
    #   then clip any values that fall outside the range [0, 1]
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)

    # the current colorized image is represented as a floating point data type in the range [0, 1],
    #   let's convert to an unsigned 8-bit integer representation in the range [0, 255]
    colorized = (255 * colorized).astype("uint8")
    return image, colorized


# Setting up file paths for input and output folders
INPUT_DIR = r'tonelocator/colorizer/input/'
INPUT_DIR = os.path.join(os.path.dirname(__name__), INPUT_DIR)
OUTPUT_DIR = r'tonelocator/colorizer/output/'
OUTPUT_DIR = os.path.join(os.path.dirname(__name__), OUTPUT_DIR)


# Colorize each file in loop in input folder and save in output folder
def colorize_folder(input_folder=INPUT_DIR, output_folder=OUTPUT_DIR):
    """
    Will colorize all photos in input folder. By default, uses input folder from
    colorizer folder and pushes to output folder. User can change these by including
    two arguments (input folder path, output folder path). All photos must be in jpeg format.
    """
    # get list of files in input folder
    bw_images = [f for f in os.listdir(input_folder) if not f.startswith('.')]
    if len(bw_images) == 0:
        raise ValueError("No images in input folder")
    # loop to colorize each file in input folder and save in output folder
    for photo in bw_images:
        #Loop that will run through every file in the input folder, colorize them,
        # and save the colorized image to the output folder.
        img = input_folder + photo
        output = output_folder + photo.rsplit('.', 1)[0] + "_colorized." + photo.rsplit('.', 1)[1]
        image, colorized = colorize_image(img)
        data=cv2.imencode('.png', colorized)[1].tobytes()
        cv2.imwrite(output, colorized)

# colorizing images in input folder
colorize_folder()