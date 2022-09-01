#!/usr/bin/env python3
import time
import os

import cv2
import matplotlib.pyplot as plt
import numpy as np
import time
import datetime
from dateutil import tz


#####
# Class to use simple image functions
#
#####
class ImageAnalysis_Utility:
    ''' Class for image analysis to use simple generic function'''

    def toGrayScale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def creatMask(width, height):
        return np.zeros((width, height))

    def toHSV(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def getROI(image, low_x, high_x, low_y, high_y):
        return image[low_y:high_y, low_x:high_x]

    def scale(frame, scale_percent):
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    def viewSimple(image, title="Pi Feed"):
        cv2.imshow(title, image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            exit(0)

    def pixel2length(pixels, distance_to_object, focal_length):
        '''
        This function converts an amount of pixels to a given length (SI)
        The length unit is defined by the unit of "distance_to_object"     

        the return is a float with 2 significan digits
        '''
        return (focal_length * pixels) / distance_to_object
        #return format(length_SI, '.2f') # only return with 2 digits
    def calculateFocalLength(distance_to_object, length_of_object,
                             pixels_length_of_object):
        '''
        This function calculates the focal length which is used for converting pixels to a SI value
        in the function "pixel2length"

        the SI unit is defined by "distance_to_object" & "length_of_object" which is expected to
        have the same unit
        '''
        return distance_to_object * (length_of_object /
                                     pixels_length_of_object)

    def viewHistogram(image):
        plt.figure(num=1, figsize=(4, 4))
        plt.title("histogram of image")
        hist = 0
        hist, bins = np.histogram(image.ravel(), 256, [0, 256])
        plt.plot(hist)
        plt.figure(num=2, figsize=(4, 4))
        print("image size is : ", image.ndim)
        if image.ndim == 2:  # at dim=2 we have a grayscaled image
            plt.imshow(image, cmap='gray', vmin=0, vmax=255)
        else:
            plt.imshow(image)
        plt.title("raw image")
        plt.axis('off')
        plt.show(block=False)
        plt.pause(1)
        return

    def draw_cross(frame, x_pos, y_pos, color, length=3):
        cv2.line(frame, (int(x_pos - length / 2), y_pos),
                 (int(x_pos + length / 2), y_pos), color, 3)  # x-axis line
        cv2.line(frame, (x_pos, int(y_pos - length / 2)),
                 (x_pos, int(y_pos + length / 2)), color, 3)  # y-axis line
        return frame

    def save_with_Timestamp(frame, title, path):
        now = datetime.datetime.now(tz=tz.tzlocal())
        date_time = now.strftime("%Y%m%d_%H%M_%S")
        filename = date_time + "_" + title + '.png'
        saved_image = path + filename
        cv2.imwrite(saved_image, frame)


if __name__ == "__main__":
    print("hello main")
