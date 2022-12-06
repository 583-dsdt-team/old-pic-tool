"""
This script will use the colorizer from colorizer.py in this folder to colorize images in batches

You will need to define your input folder with black and white photos, and your output folder 
which will include the processed color images.
"""

import os.path
from colorizer import *


# get list of files in input folder
input_folder = [f for f in os.listdir("./colorizer/input") if not f.startswith('.')]

# Colorize each file in loop in input folder and save in output folder
for photo in input_folder:
    img = "./colorizer/input/" + photo
    output = "./colorizer/output/" + photo.rsplit('.', 1)[0] + "_colorized." + photo.rsplit('.', 1)[1]
    image, colorized = colorize_image(img)
    data=cv2.imencode('.png', colorized)[1].tobytes()
    cv2.imwrite(output, colorized)


["./colorizer/input/" + s for s in input_folder]g

input_folder[0]

output = "./colorizer/output/" + input_folder[0].split('.', 1)[0] + "_colorized" + photo.split('.', 1)[1]

image, colorized = colorize_image("./colorizer/input/gray_Aaron_Sorkin_0002.jpg")
data=cv2.imencode('.png', colorized)[1].tobytes()
cv2.imwrite("./colorizer/output/gray_Aaron_Sorkin_0002_colorized.jpg", colorized)
