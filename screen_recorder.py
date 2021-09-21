
import numpy as np
from PIL import ImageGrab
import time

# SAVE JUST A BOX
#box = (1106,657,1166,679) #Upper left and lower right corners
#ImageGrab.grab(box).save('box.png') 


box = (0,0,1920,1080) 

sleeping_time = 2 # in seconds

images_taken=1

while True:
           
           ImageGrab.grab(box).save('images/screenshot {0}.png'.format(time.asctime())) # SAVE FULLSCREEN
           
           time.sleep( sleeping_time ) 
           
           print(images_taken)
          
           images_taken+=1
                      
