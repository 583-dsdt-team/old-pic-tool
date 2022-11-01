## User Stories

> In class assignment from 11-01-22

* Who is the user
* What do they want to do with the tool
* What needs and desires do they want for the tool
* What is their skill level

**User 1: Peter**

Peter is a professor in the social sciences. He wants to use this tool to probabilistically derive skin tone from old photographs for research. Peter needs the tool to output a dataframe that is clearly documented and easy to interpret. Peter is a skilled researcher who can add images and receive output but not troubleshoot technical issues with the code.

**User 2: Technical researcher**

This user is looking for a place to start in identifying skin tone from old photos, but will go on to build their own method. This user will use our tool to produce a set of priors about their own set of photos, but will go on to build their own model. They will need to feed their own pictures in and receive a basic guess about each person's skin tone, which will inform their own work moving forward. This person will likely be looking at the code comprising specific components of the tool. They are a highly skilled programmer and will be adapting or using our code moving forward.

**User 3: Basic researcher**

This user is looking for a place to start in identifying skin tone from old photos - the easiest, out-of-the-box method. This user will use our tool to produce a set of priors about their own set of photos and will use that in their research. They will need to feed their own pictures in and receive a basic guess about each person's skin tone or a data frame with a distribution of probabilities.  They are a skilled researcher but not necessarily a skilled programmer. 


**Use cases** - initial thoughts
* Crop picture to face - pre-processing
* Produce single guess of skin tone bin
* Produce probability distribution

