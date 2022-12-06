"""
This script will use the colorizer from colorizer.py in this folder to colorize images in batches

You will need to define your input folder with black and white photos, and your output folder 
which will include the processed color images.
"""

import os.path
import glob

from colorizer import *

# DMC - added 'colorizer' to path name
prototxt = r'colorizer/model/colorization_deploy_v2.prototxt'
model = r'colorizer/model/colorization_release_v2.caffemodel'
points = r'colorizer/model/pts_in_hull.npy'
points = os.path.join(os.path.dirname(__name__), points)        # DMC changing "__file__" to "__name__"
prototxt = os.path.join(os.path.dirname(__name__), prototxt)
model = os.path.join(os.path.dirname(__name__), model)


# First, get list of files in input folder
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield(f)

input_folder = listdir_nohidden("./colorizer/input")

input_folder = os.listdir("./colorizer/input")

def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))
    


input_folder = [f for f in os.listdir("./colorizer/input") if not f.startswith('.')]
for photo in input_folder:
    img = "./colorizer/input/" + photo
    output = "./colorizer/output/" + photo.rsplit('.', 1)[0] + "_colorized." + photo.rsplit('.', 1)[1]
    image, colorized = colorize_image(img)
    data=cv2.imencode('.png', colorized)[1].tobytes()
    cv2.imwrite(output, colorized)


["./colorizer/input/" + s for s in input_folder]

input_folder[0]

output = "./colorizer/output/" + input_folder[0].split('.', 1)[0] + "_colorized" + photo.split('.', 1)[1]

image, colorized = colorize_image("./colorizer/input/gray_Aaron_Sorkin_0002.jpg")
data=cv2.imencode('.png', colorized)[1].tobytes()
cv2.imwrite("./colorizer/output/gray_Aaron_Sorkin_0002_colorized.jpg", colorized)
