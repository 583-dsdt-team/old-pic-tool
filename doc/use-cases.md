## Functional design: use cases


**Use case 1:** Crop picture to face

This use case is a pre-processing component of the skin tone detection process, but could also be used on its own. 
* Input: Set of image files depicting people with a unique identifier per file
* Output: Set of image files cropped to faces with a unique identifier for each face, file pair

**Use case 2:** Estimate skin tone bin

In this use case, users upload black and white photos and receive a single modal skin tone bin per photo. 
* Input: Set of image files depicting people with a unique identifier per file
* Output: Data frame with image ID's linked to skin tone bin identifier according to Monk scale: 

![Monk scale of skin tones](monkscale.png)

**Use case 3:** Produce probability distribution of skin tones 

In this use case, users upload black and white photos and receive a data frame with a probability distribution of likely skin tones for each photo. 
* Input: Set of image files depicting people with a unique identifier per file
* Output: Data frame with image ID's linked to probability for each skin tone
