"""
This script will import black and white photos,
add color to them, and save the colorized image.

Code was based on code for the PySimpleGUI colorizer: 
    https://github.com/PySimpleGUI/PySimpleGUI-Photo-Colorizer

Colorization based on the Zhang Image Colorization Deep Learning Algorithm
This header to remain with this code.

The implementation of the colorization algorithm is from PyImageSearch
You can learn how the algorithm works and the details of this implementation here:
https://www.pyimagesearch.com/2019/02/25/black-and-white-image-colorization-with-opencv-and-deep-learning/

You will need to download the pre-trained data from this location and place in the model folder:
https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1

"""

import numpy as np
import cv2
import os.path

version = '1 December 2022'

# DMC - added 'colorizer' to path name
prototxt = r'colorizer/model/colorization_deploy_v2.prototxt'
model = r'colorizer/model/colorization_release_v2.caffemodel'
points = r'colorizer/model/pts_in_hull.npy'
points = os.path.join(os.path.dirname(__name__), points)        # DMC changing "__file__" to "__name__"
prototxt = os.path.join(os.path.dirname(__name__), prototxt)
model = os.path.join(os.path.dirname(__name__), model)


if not os.path.isfile(model):    # DMC - this is for the GUI - need to figure out how to add warning if not using GUI
    sg.popup_scrolled('Missing model file', 'You are missing the file "colorization_release_v2.caffemodel"',
                      'Download it and place into your "model" folder', 'You can download this file from this location:\n', r'https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1')
    exit()
    
net = cv2.dnn.readNetFromCaffe(prototxt, model)     # load model from disk
pts = np.load(points)

# add the cluster centers as 1x1 convolutions to the model
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

def colorize_image(image_filename=None, cv2_frame=None):
    # DMC - do we need the cv2_frame bit. This seems to colorize from a webcam, which we likely don't need for this project
    """
    Where all the magic happens.  Colorizes the image provided. Can colorize either
    a filename OR a cv2 frame (read from a web cam most likely)
    :param image_filename: (str) full filename to colorize
    :param cv2_frame: (cv2 frame)
    :return: Tuple[cv2 frame, cv2 frame] both non-colorized and colorized images in cv2 format as a tuple
    """
    # load the input image from disk, scale the pixel intensities to the range [0, 1], and then convert the image from the BGR to Lab color space
    image = cv2.imread(image_filename) if image_filename else cv2_frame
    scaled = image.astype("float32") / 255.0
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

    # resize the Lab image to 224x224 (the dimensions the colorization network accepts), split channels, extract the 'L' channel, and then perform mean centering
    resized = cv2.resize(lab, (224, 224))
    L = cv2.split(resized)[0]
    L -= 50

    # pass the L channel through the network which will *predict* the 'a' and 'b' channel values
    'print("[INFO] colorizing image...")'
    net.setInput(cv2.dnn.blobFromImage(L))
    ab = net.forward()[0, :, :, :].transpose((1, 2, 0))

    # resize the predicted 'ab' volume to the same dimensions as our input image
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))

    # grab the 'L' channel from the *original* input image (not the resized one) and concatenate the original 'L' channel with the predicted 'ab' channels
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)

    # convert the output image from the Lab color space to RGB, then clip any values that fall outside the range [0, 1]
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)

    # the current colorized image is represented as a floating point data type in the range [0, 1] -- let's convert to an unsigned 8-bit integer representation in the range [0, 255]
    colorized = (255 * colorized).astype("uint8")
    return image, colorized

# DMC - this code will select an image and colorize it
#image, colorized = colorize_image("./colorizer/input/gray_Aaron_Sorkin_0002.jpg")
#data=cv2.imencode('.png', colorized)[1].tobytes()
#cv2.imwrite("./colorizer/output/gray_Aaron_Sorkin_0002_colorized.jpg", colorized)

# get list of files in input folder
input_folder = [f for f in os.listdir("./colorizer/input") if not f.startswith('.')]

# Colorize each file in loop in input folder and save in output folder
for photo in input_folder:
    img = "./colorizer/input/" + photo
    output = "./colorizer/output/" + photo.rsplit('.', 1)[0] + "_colorized." + photo.rsplit('.', 1)[1]
    image, colorized = colorize_image(img)
    data=cv2.imencode('.png', colorized)[1].tobytes()
    cv2.imwrite(output, colorized)
