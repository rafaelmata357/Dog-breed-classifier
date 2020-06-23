#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Rafael Mata M.
# DATE CREATED: 13 April 2020                                 
# REVISED DATE: 15 April 2020
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
  
    
    results_dic = {}
    #Retrieve  the filenames from folder pet_images/
    filename_list = listdir(image_dir)
       
    for dogs_file in filename_list:
        
        #Format the pet name
        pet_image = dogs_file
        low_pet_image = pet_image.lower()
        word_list_pet_image = low_pet_image.split("_")
        pet_name = ""
        for word in word_list_pet_image:
            if word.isalpha():
                pet_name += word + " "
        pet_name = pet_name.strip()
        
        if (dogs_file not in results_dic) and (not dogs_file.startswith('.')):  #Ignore if file starts with '.' hidden file
            results_dic[dogs_file] = [pet_name]
        else:
            print('Warning {} already exist in dictionary!! with pet name {}'.format(dogs_file,pet_name))
    

    return results_dic


