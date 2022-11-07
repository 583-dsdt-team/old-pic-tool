## Functional design: use cases

* Inputs
* Outputs

**Use case 1:** Crop picture to face

This use case is a pre-processing component of the skin tone detection process, but could also be used on its own. 
* Input: Set of image files
* Output: Set of image files cropped to face

**Use case 2:** Guess skin tone bin

In this use case, users upload black and white photos and receive a single "most probable" skin tone bin per photo. 
* Input: Set of image files
* Output: Data frame with image ID's linked to skin tone bin identifier according to Monk scale: 

![Monk scale of skin tones](monkscale.png)

**Use case 3:** Produce probability distribution of skin tones 

In this use case, users upload black and white photos and receive a data frame with a probability distribution of likely skin tones for each photo. 
* Input: Set of image files
* Output: Data frame with image ID's linked to probability for each skin tone
