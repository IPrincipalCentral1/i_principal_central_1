
















list_of_liberary_to_install = [

                            ["googletrans"] ,
                            
                            
                            
                            



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
    
    
    




# تثبيت: pip install googletrans==4.0.0-rc1

from googletrans import LANGUAGES

# LANGUAGES هو dict فيه كل الأكواد كـ key واللغة بالإنجليزية كـ value


for code, name in LANGUAGES.items():

    print(code, ":", name)
    













