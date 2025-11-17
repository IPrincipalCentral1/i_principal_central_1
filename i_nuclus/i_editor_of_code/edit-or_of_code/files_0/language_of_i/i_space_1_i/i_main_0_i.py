











































































































list_of_liberary_to_install = [
                            
                            
                            ["pillow"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess




cwd = os.path.dirname(os.path.abspath(__file__))



print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])



try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
            
            
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

# حجم الصورة (العرض، الارتفاع)
width, height = 1200, 700

# إنشاء صورة بيضاء
img = Image.new("RGB", (width, height), color="white")



i_file_0_i = os.path.join(cwd, "i_image_0_i.png")

# حفظ الصورة

img.save(i_file_0_i)

































