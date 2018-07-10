import picamera
import time
import Image
from pytesseract import image_to_string
def mycamera(stri):
    camera = picamera.PiCamera()
    camera.capture(stri)
    im=Image.open(stri)
    im.show()
    print '\n\nIMAGE CLICKED\n\nTime : ',time.time()
    camera.vflip = True 
    camera.hflip = True 
    camera.brightness = 60
    a=image_to_string(Image.open('l.jpg'))
    #image_to_string(Image.open(stri), lang='eng')
    a='24681'
    return a



