# SRIFFS
SRIFFS - Synthesizing Realistic Images From Facial Sketches
## Introduction
Understanding images is still a challenging problem in computer vision, nevertheless going in the opposite direction to generate a realistic image. Especially in this project in which we are working across two domains, sketches, and images, it is difficult to completely rely on the computer for the entire image synthesis process.
we aimed our own dataset consisting of sketches generated from real world images from different origins, sources, websites and manually taken images for making it as accurate as possible and giving the machine a versatile set of images to train upon and give accurate outputs with an increased accuracy of the model.

### Objective

* The goal of sketch-based image synthesis is to generate some image resembling to reality derived from a sketch, given the constraint of a sketched object/person.
*  Create an Indian -oriented dataset of sketch-image pairs and hence designing a deep learning model using GAN (Generative Adversarial Network) to synthesize realistic images. 
* Pipeline the flow of project to provide easy optimization.



## Installations required

**

**

## Dataset collection

The dataset was taken from various multiple sources and named according to a specific naming convention.
Sources of the data is mentioned below :
1.  Indian People Dataset ( Kaggle)
[https://www.kaggle.com/sinhayush29/indian-people/](https://www.kaggle.com/sinhayush29/indian-people/)

2.  Indian Faces Dataset ( IEEE)
   [https://ieee-dataport.org/keywords/indian-face-database](https://ieee-dataport.org/keywords/indian-face-database)

3. Free usable images from websites like unsplash.com and stock free images 

| Source |No of Images  |
|--|--|
| IEEE Faces Dataset |  201|
| Indian Faces Dataset |186  |
| Other Sources |67  |

Total Images : 454

  Link to the dataset: https://github.com/DependerKumarSoni/SRIFFS/tree/main/data  
Original_Images folder contains the coloured facial images and Converted_Sketches folder contains the corresponding facial sketches.



## Dataset Creation

Our dataset consists of Image- Sketch pairs that will be used to train and test our model. The data collected from various sources was raw and needs to be pre-processed before feeding it to the model. Various pre-processing steps taken are mentioned below :
1. Renaming all the images according to the naming convention
    Code: https://github.com/DependerKumarSoni/SRIFFS/blob/main/scripts/ImgRename.py
2.  Resizing all the images into (512 x 512 ) pixels format 
Code: https://github.com/DependerKumarSoni/SRIFFS/blob/main/scripts/ImgResizer.py 
3. Converting Images into sketches to create respective image - sketch pairs
Code: https://github.com/DependerKumarSoni/SRIFFS/blob/main/scripts/Img2Sketch.py




## **Image Augmentation**

**




## Model Development

Code : https://github.com/DependerKumarSoni/SRIFFS/blob/main/notebooks/Sketch2color_image.ipynb







## Model Training

**






## Model Evaluation


**

