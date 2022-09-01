


#from source.ImageAnalysis_FindObject import ImageAnalysis_FindObject
import time
from source.basic_view import Basic_View
from source.detect_object import DetectObject
from source.ML_AquireDataset import ML_AquireDataset
from source.detect_object import DetectObject
class main_:
    def __init__(self):
        ''' initialize the class '''
  
    # Defining main function
    def main_loop(self):      
        print("hey there")
        while 1:
            print("hey there in loop")
            time.sleep(1)

        return
        
# __name__
if __name__=="__main__":
    print("Running main file")
   # ML_AquireDataset.AquireFromRaspistill("/home/pi/Capture/",100)

    m_detector = DetectObject()
    m_detector.simple_detect()


