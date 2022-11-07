## Component Design

* Name
* What it does
* Inputs (with type information)
* Outputs (with type information)
* How use other components

**Component 1: Crop photos to face**
* Input: set of photo image files named with a unique numeric identifier
* Output: set of cropped photo image files named with the same identifier

**Component 2: Estimate skin tone probability distribution**
* Input: set of cropped photo image files named with unique numeric identifiers
* Output: dictionary with keys representing numeric photo identifiers and values comprised of ordered lists of probabilities photo belongs to each of 10 skin tone bins
*   OR: data frame with one column representing the numeric photo identifier and ten columns each representing a skin tone bin, with probabilities that add up row-wise to one and represent the likelihood the photo belongs to each skin tone bin

**Component 3: Select most probable skin tone**
* Input: list of probabilities that add up to 1
* Output: skin tone bin identifier (integer, 1 through 10) and hex color code (six-digit string)

