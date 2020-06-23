# Flower-image-classifier

This is the firsts project  of the the AI Programming with Python Nanodegree from [https://www.udacity.com/] to classify dog breed images using pretrained CNN (Alexnet, vgg, resnet) and evaluate the efficiency in terms of accuracy and time, the project is based on scripts provided by Udacity.

The project is broken down into multiple steps:

- Generate the image labels
- Classify the images using the differente CNN models
- Compare and print the results
- Evaluate which model fits better

# Dataset

A 40 images including dogs and cats images, in addition 5 random images including dog, objects and other animals.

# Pre trained CNN Models used:

- AlexNet 
- Vgg16   
- ResNet18 


# Files in the repository

- **adjust_results4.py**               : Porgram to djusts the results dictionary   
- **calculates_results_stats.py**      : Program that calculates the statistics of the results    
- **check_images.py**                  : Program that check the images using classifier.py 
- **classifier.py**                    : Program to classify pet images using a pretrained CNN model
- **dognames.txt**                     : File with the dognames labes of the images
- **get_input_args.py**                : Utility to get the args form command line
- **get_pet_labels.py**                : Program to get the pet labels
- **print_functions_for_lab_checks.py** :Support scripts to check the results
- **print_results.py**                 : Program to format and print the results
- **imagenet1000_clsid_to_human.txt** : File with the different classes

# Install
Clone the repository to the local machine

`$ git clone https://github.com/rafaelmata357/Dog-breed-classifier.git`

# Running

The app is called using **check_images.py ** 

```python check_images.py --dir <directory with images> --arch <model>  --dogfile <file that contains dognames> ```

The following options are the arguments:

     1. Directory with images                     --dir with default value 'flowers'
     2. Model                                     --arch with default value current directory
     3. Dog file that containes dogname           --dogfile

Example:

```$ python check_images.py --dir pet_images --arch vgg --dofile dognames.txt````

In addition to get help execute:

`$ python check_images.py -h `

Ouput example:

![Example](https://github.com/rafaelmata357/Dog-breed-classifier/blob/master/output.png)

# Python version:
This app uses **Python 3.8.1**

# License:

The code follows this license: https://creativecommons.org/licenses/by/3.0/us/
