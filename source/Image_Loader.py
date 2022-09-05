#!/usr/bin/env python3
import time
import os

import cv2
import numpy as np


#####
# class to simplify recieving an image from a local storage.
# the class is expecting an absolute path to the image + the image name as input
# and also the expected image format : color ? grayscale ect
#
# The public function getImage() returns a cv2.mat object when a new image has been aquired
# however this is a blocking function, meaning we are waiting forever untill a new image has arrived.
#
# @code {.py}
# # instatiate class: path+img_name , format
# m_loader = Image_Loader.Image_Loader('some-path/img.png',cv2.IMREAD_GRAYSCALE)
# while(1):
#  try:
#	mat = m_loader.getImage()
#  except:
#	print("an error occured, ignore image")
#  ... do image analysis ....
# @endcode
#
#####
class Image_Loader:
    ''' Class to load in an image based on a file change'''

    def __init__(self, path_to_image, image_format=cv2.IMREAD_COLOR):
        ''' initialize the loader '''
        self._cached_stamp = 0
        self.filename = path_to_image  # define the input file/image/whatever
        self.image_format = image_format
        print("[Image_Loader]::[__init__] local image path and name is: ",
              self.filename)

    def __is_input_ready__(self):
        '''  private function to poll a filechange '''
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            print(
                "[Image_Loader]::[__is_input_ready__] an image has been accuired"
            )
            return True
        return False
        # Execute the model, parse the input along
    def getImage(self):
        ''' 
        return a image if we are ready. 
        Check errorcode for result : if true -> we recieved an image
                                     if false -> ignore image
        '''
        if self.__is_input_ready__():
            return (True, cv2.imread(self.filename, self.image_format))
        else:
            cv2.waitKey(100)
            return (False, None)
