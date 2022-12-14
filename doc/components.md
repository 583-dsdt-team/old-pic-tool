## Components

### Preprocesser (preprocess/face_crop.py)

This module takes photos of people and returns the photos cropped, and grayscale if requested. 

_Inputs_
* file path of image
* to_gray, a boolean indicating whether image should be converted to grayscale in the processing process
* gaussian_blur, a boolean indicating whether image should be blurred

_Outputs_
* photo as array

### Colorizer (colorizer/colorize_image.py)

The colorizer takes photos and runs them through a colorizing algorithm, returning a colorized photo. 

_Inputs_
* file path of image

_Outputs_
* photo as array

### Detector (detector/complexion_detection.py)

This module detects the composition of each photo by bins on the Monk Scale. It can detect either color or grayscale versions of the Monk Scale. In future iterations of the tool, users will be able to set their own colors to detect in a photo. 

_Inputs_
* image file path (string)
* rounding_places, an integer indicating how precise the output shoul dbe
* grayscale, a boolean indicating whether to detect based on the color or grayscale Monk Scale

_Outputs_
* dataframe with photo file path linked to the composition of the photo according to the Monk Scale 

### Compare predicted color distribution to true distribution

Three modules produce different results that illustrate how well a given predicted color composition matches a true color distribution. 

#### conf_matrix.py

This module takes as inputs two dataframes, one representing the "true" color distribution of an image and another representing a predicted version using the grayscale photo. The module calculates the most prominent color bin from the Monk Scale in each image in both the true and predicted data and returns a confusion matrix showing how well the method did at deriving color from the black and white image.

_Inputs_
* true and pred, pandas dataframes representing the true distribution of Monk Scale colors in a photo and predicted values using a given prediction method, respectively. Both pandas dataframes include a column called "picid" which is a unique identifier of each image (and can be used to link across dataframes) and ten columns numbered from 0 to 9 which index the bins. 

_Outputs_
* confusion matrix object which can be plotted or saved

#### pcp.py

This module takes the same inputs as conf_matrix and calculates the percent correctly predicted by comparing the color bin making up the largest share of the image in the true data vs. the predicted data. It returns the share of images for which the prediction method accurately predicted the most prominent color in the image.

_Inputs_
* true and pred, pandas dataframes representing the true distribution of Monk Scale colors in a photo and predicted values using a given prediction method, respectively. Both pandas dataframes include a column called "picid" which is a unique identifier of each image (and can be used to link across dataframes) and ten columns numbered from 0 to 9 which index the bins. 

_Outputs_
* single float representing the proportion correctly predicted

#### mse.py

This module again takes the same inputs as conf_matrix, as well as a boolean indicating whether to return the overall mean squared error of the prediction method, or a data frame which indicates the error for each color bin. 
_Inputs_
* true and pred, pandas dataframes representing the true distribution of Monk Scale colors in a photo and predicted values using a given prediction method, respectively. Both pandas dataframes include a column called "picid" which is a unique identifier of each image (and can be used to link across dataframes) and ten columns numbered from 0 to 9 which index the bins. 
* bybin is a boolean; when True the function returns a MSE value for each color bin; when False the function returns returns a single MSE for the entire set of bins 

_Outputs_
* if bybin == True: pandas dataframe showing the MSE separately for each bin 
* if bybin == False: single float number representing the total MSE
