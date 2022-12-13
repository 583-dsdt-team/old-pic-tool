## Use Cases 

We envision four primary use cases for these tools:

1: **Pre-process an image of a face.** In this use case, a user is interested in pre-processing a set of images, in order to crop the photos to faces so that skin complexion can be detected. This use case is a pre-processing component of the skin tone detection process, but could also be used on its own. 
* Input: Set of image files depicting people with a unique identifier per file
* Output: Set of image files cropped to faces with a unique identifier for each face, file pair

2: **Detect prevalence of Monk scale bins in color image.** In this use case, a user is interested in detecting the share of a photo that falls within each of the color bins in the Monk scale. The user has a set of color images and wishes to return a dataframe that indicates what proportion of the image matches each bin of the Monk scale. 
* User loads set of color photos
* Tool returns dataframe linked to image identifier, with ten columns reporting composition of photo across ten-bin Monk scale

3: **Detect prevalence of Monk scale bins in B&W image.** In this case, a user is interested in detecing the share of a photo that falls within each of the color bins in the Monk scale, but only has a set of black & white images. The user wishes to assess what share of each image matches the grayscale version of each bin of the Monk scale. 
* User loads set of black & white photos
* Tool returns dataframe of estimated composition across color Monk scale

4: **Test the effectiveness of different methods of colorizing.** In this case, a user is interested in assessing different methods of determining Monk Scale bin prevalence in black & white photos. The research team (Breon, David, and Lizzy) applied this use case -- we were interested in testing our two methods, as described on our poster and below. This use case could also apply to those who develop their own method of colorizing old photos and want to compare across methods.
* User loads set of true and predicted Monk scale composition values
* Tool returns confusion matrix, percent correctly predicted, and overall MSE and MSE by bin

