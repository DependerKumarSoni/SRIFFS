#!/usr/bin/env python
# coding: utf-8

# # Program to Resize Image pixel size.

#importing the libraries
import cv2
import os

def Resizer(source, dim, destin):
    
    input_list = os.listdir(source)

    os.system('cls')
    
    for img_name in input_list:

        # Remove extension from name
        new_name, _ = list(map(str, img_name.split(".")))

        # input file path
        ip_file_path = os.path.join(source, img_name)

        # Get the image
        img = cv2.imread(ip_file_path)

        # Resize image
        img_op = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        # Output file path
        op_file_path = os.path.join(destin, new_name+"_("+str(dim[0])+"px,"+str(dim[1])+"px).jpg")

        # write images
        cv2.imwrite(op_file_path, img_op)

        # terminal message
        print(op_file_path + " -> Created")

    os.system('cls')
    print("Conversion Successful")



if __name__ == "__main__":
    
    ANS = 'n'
    while(ANS == 'n'):
        os.system('cls')
        source = input("Location of Source Folder: ")
        destin = input("Location of Destination Folder: ")
        width, height = list(map(int, input("New Dimensions of Image in px (space separated): ").split()))
        dim = (width, height)
        Resizer(source, dim, destin)
        ANS = input("\nWant to Exit? (y/n): ")
    
    os.system('cls')