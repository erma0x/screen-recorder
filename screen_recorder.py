import numpy as np
from PIL import ImageGrab
import time
import os
import datetime

 #Upper left and lower right corners
#box = (1106,657,1166,679)
box = (0,0,1920,1080) 
sleeping_time = 2 # in seconds
images_taken = 0

LOGO = """                                                                       _            
                                                                      | |            
  ___  ____  ____ _____ _____ ____      ____ _____  ____ ___   ____ __| |_____  ____ 
 /___)/ ___)/ ___) ___ | ___ |  _ \    / ___) ___ |/ ___) _ \ / ___) _  | ___ |/ ___)
|___ ( (___| |   | ____| ____| | | |  | |   | ____( (__| |_| | |  ( (_| | ____| |    
(___/ \____)_|   |_____)_____)_| |_|  |_|   |_____)\____)___/|_|   \____|_____)_|    
                                                                                     
                                                                                    
"""
if __name__ == '__main__':
    while True:
        ImageGrab.grab(box).save('images/screenshot {0}.png'.format(time.asctime())) # SAVE FULLSCREEN
        time.sleep( sleeping_time ) 
        os.system('clear')
        images_taken+=1
        print(LOGO)
        print('\n\t'+str(time.asctime()))
        print(f'\n\tnumber images taken: [{images_taken}]')
                      
