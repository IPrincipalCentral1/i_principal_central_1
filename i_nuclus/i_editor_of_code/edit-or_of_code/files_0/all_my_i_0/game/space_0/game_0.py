









'''


this should be my first game right here .

---------------------------------------------------------


i want to make game of i .


this game work with pixel-s .

it is on 2 Dimenssion ( 2D ) .


the pixel can have 2 color-s : 

    ( white , black )



it is work-ing on a layer of ( 3 x 3 ) .


if the pixel transform to white . it means that it is alive .


if the pixel transform to black . it means that it is a chance .




the rule-s :

    0 - if the pixel have less then 2 other pixel-s white touch-ing it . it will be black . { ( number_of_pixel_in_touch < 2 ) ===> will be black ( make a chance )  }

    1 - if the pixel is black and the pixel have exactly 3 pixel-s white touch-ing it . it will be white . { ( number_of_pixel_in_touch == 3 ) ===> will be white ( be alive ) }

    2 - if the pixel is white and have 2 other pixel-s white touch-ing it . it will be stay white . { ( ( 2 <= number_of_pixel_in_touch <= 3 ) and (color is white) ) ===> will be stay white ( stay alive ) }
    
    0 - if the pixel have more then 3 other pixel-s white touch-ing it . it will be black . { ( number_of_pixel_in_touch > 3 ) ===> will be black ( make a chance )  }





i want to build a computer use-ing this game . 

so there is an input and output in this game . like when i use the computer to do some task so it will have input and output .

it can be multiple simulation at the same time .

For Example : 
    
    1 simulation for the processor .
    
    1 simulation for the memory RAM .
    
    1 simulation for the memory Disk .
    
    etc...



and they can exchange information-s between each other ( those simulation-s ) .











'''









list_of_liberary_to_install = [
                            
                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            
                            
                            ["pillow"] ,
                            
                            
                            ["opencv-python-headless"] ,


                            #["opencv-python"] ,


                            #["opencv-contrib-python"] ,




]










import os


import traceback

import sys


import subprocess





try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
        
            
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
        
        
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
        
        
        counter_0 += 1
        
        
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    
    


print("\n" * 10)






from PIL import Image









































