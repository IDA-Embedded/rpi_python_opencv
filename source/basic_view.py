import cv2

from source.ImageAnalysis_Utility import ImageAnalysis_Utility
from source.Image_Loader import Image_Loader
PATH_TO_IMG = "/home/pi/node_red/images/esp32Img.png"
class Basic_View:   

    def view_image():
        m_loader = Image_Loader(PATH_TO_IMG)

        while True:
            (res,img) = m_loader.getImage()
            if(res):
                ImageAnalysis_Utility.viewSimple(img,"raw")
           


