#!/usr/bin/env python
# coding: utf-8

# # Program to rename image and store in different location

#importing the libraries
import cv2
import os

def imgRename(source, destin):
    
    input_list = os.listdir(source)

    os.system('cls')
    
    for i in range(len(input_list)):

        # name of original image
        img_name = input_list[i]

        # input file path
        ip_file_path = os.path.join(source, img_name)

        image = cv2.imread(ip_file_path)

#######################################################################
        # Output file path
        ## Here you can change how image should be renamed.
        op_file_path = os.path.join(destin, "D_"+str(i+1)+".jpg")
#######################################################################

        # write images
        cv2.imwrite(op_file_path, image)

        # terminal message
        print(op_file_path + " -> Created")

    os.system('cls')
    print("Conversion Successful")


if __name__ == "__main__":
    Ans = 'n'
    while (Ans == 'n' or Ans == 'N'):
        os.system('cls')
        print("This is a program to rename images in given folder")
        print("``````````````````````````````````````````````````")
        source = input("Source Folder Location: ")
        destin = input("Destination Folder Location: ")
        imgRename(source, destin)
        Ans = input("\nWant to Exit? (y/n): ")
