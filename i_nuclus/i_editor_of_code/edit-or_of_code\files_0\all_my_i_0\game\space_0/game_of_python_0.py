
















list_of_liberary_to_install = [
                            
                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            
                            
                            ["pillow"] ,


                          




]










import os


cwd = os.path.dirname(os.path.abspath(__file__))



import traceback

import sys


import subprocess





try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            #subprocess.check_call([sys.executable, "-m", "pip", "uninstall", f"{list_of_liberary_to_install[counter_0][0]}"])
            
            
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




width, height = 400, 200

# إنشاء صورة جديدة بلون خلفية أحمر (RGB)


img = Image.new("RGB", (width, height), color=(255, 255, 255))


img.save(os.path.join(cwd, "space_0", "photo", "white.png"))










