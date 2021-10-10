#!/usr/bin/env python
# coding: utf-8

# # Program to convert image to sketch

#importing the libraries
import cv2
import os

def converter(image, kernel):
    # Get the image location
    img = cv2.imread(image)

    # convert image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # invert the image
    inverted_gray_image = 255 - gray_image

    # blur the image by gaussian blur
    blurred_img = cv2.GaussianBlur(inverted_gray_image, kernel, 0)

    # invert the blurred image
    inverted_blur_image = 255 - blurred_img

    # the pencil sketch image
    sketch = cv2.divide(gray_image, inverted_blur_image, scale=256.0)

    # return the sketch
    return sketch

def multiConverter(source, destin):

    kernel = (0,0)
    
    input_list = os.listdir(source)

    os.system('cls')
    
    for img_name in input_list:

        if("D" in img_name):
            kernel = (5,5)
        elif("N" in img_name):
            kernel = (11,11)
        elif("T" in img_name):
            kernel = (15,15)
            
        # input file path
        ip_file_path = os.path.join(source, img_name)

        sketch = converter(ip_file_path, kernel)

        # Output file path
        op_file_path = os.path.join(destin, img_name)

        # write images
        cv2.imwrite(op_file_path, sketch)

        # terminal message
        print(op_file_path + " -> Created")

    os.system('cls')
    print("Conversion Successful")



if __name__ == "__main__":
    
    ANS = 'n'
    while(ANS == 'n'):
        os.system('cls')
        print("Please choose one of the options below")
        print("1. Test Kernel on single image.")
        print("2. Convert multiple files.")
        option = int(input("Option Number: "))

        os.system('cls')

        if(option == 1):
            os.system('cls')
            source = input("Please enter the location of image (with extension): ")
            kernel = tuple(list(map(int, input("Please enter Kernel values (x,y) seperated by space (odd values only): ").split())))
            Image = converter(source, kernel)

            cv2.imshow("Original Image", cv2.imread(source))
            cv2.imshow("Sketch based on kernel", Image)
            cv2.waitKey(0)
            os.system('cls')
            print("Images Displayed")
            

        elif(option == 2):
            os.system('cls')
            # Input
            source = input("Please enter the 'Source Folder' location: ")
            destin = input("Please enter the 'Destination Folder' location: ")
            ## Kerner Size
            ##kernel = tuple(list(map(int, input("Please enter Kernel values (x,y) seperated by space (odd values only): ").split())))
            multiConverter(source, destin)

        else:
            os.system('cls')
            print("Wrong Input..!")
        ANS = input("\nWant to Exit? (y/n): ")
    
    os.system('cls')
