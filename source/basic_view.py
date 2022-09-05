
from source.ImageAnalysis_Utility import ImageAnalysis_Utility
from source.Image_Loader import Image_Loader

import cv2
import numpy as np

PATH_TO_IMG = "/home/pi/node_red/images/esp32Img.png"
class Basic_View:   

    def __do_edge_detection__(image):
        ''' function to perform simple edge detection 
            same way as in the offline-notebook-example
        '''
        # convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        norm_img = np.zeros((800,800))
        # normalize
        gray = cv2.normalize(gray,norm_img,0,255,cv2.NORM_MINMAX)
        blur = cv2.GaussianBlur(gray, (5, 5),
                            cv2.BORDER_DEFAULT)              
        canny = cv2.Canny(blur,10,100,apertureSize = 3)
        return canny
    def __do_erode_dilate__(image):
        ''' function to perfomr erode and dilate on an image '''
        # errode / dialate
        kernel1 = np.ones((10, 10), 'uint8')
        kernel2 = np.ones((5, 5), 'uint8')
        dilate_img = cv2.dilate(image, kernel1, iterations=1)
        erode_img = cv2.erode(dilate_img, kernel2, iterations=2)
        ret,erode_img= cv2.threshold(erode_img,100,255,cv2.THRESH_BINARY)
        return erode_img
    def __do_contour_detection__(raw,edge):
        ''' function to perform contour detection '''
        drawing = np.copy(raw) # raw image
        cnts = cv2.findContours(edge, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]        
        ###based on example from  http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv
        BLUE_COLOR = (0,0,255)
        THICKNESS = 15
        if len(cnts) > 0:
            for ele in cnts:
            #c = max(cnts, key=cv2.contourArea)
                cv2.drawContours(drawing, ele, -1, BLUE_COLOR, THICKNESS)
        return drawing

    def view_image():
        m_loader = Image_Loader(PATH_TO_IMG)

        while True:
            try:
                (res,img) = m_loader.getImage()
                if(res):
                    edge = Basic_View.__do_edge_detection__(img)
                    dilate_img = Basic_View.__do_erode_dilate__(edge)
                    drawing = Basic_View.__do_contour_detection__(img,dilate_img)

                    ## VIEW ##
                    ImageAnalysis_Utility.viewSimple(ImageAnalysis_Utility.scale(img,25),"raw")
                    ImageAnalysis_Utility.viewSimple(ImageAnalysis_Utility.scale(edge,25),"edge")
                    ImageAnalysis_Utility.viewSimple(ImageAnalysis_Utility.scale(dilate_img,25),"dilate_img")
                    ImageAnalysis_Utility.viewSimple(ImageAnalysis_Utility.scale(drawing,25),"drawing")

                    
            except:
                print("expection happend .... ")
                cv2.waitKey(100)

           


