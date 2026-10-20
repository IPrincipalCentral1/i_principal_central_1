


















list_of_liberary_to_install = [
                            
                            

]










import os


import traceback

import sys


import subprocess





print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])




try:

    counter_0 = 0


    while (counter_0 < len(list_of_liberary_to_install)):



        try:


            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")

            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", f"{list_of_liberary_to_install[counter_0][0]}"])



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












class i_editer_of_video_0_i():
    
    def i_get_file_of_description_0_i():
        
        pass
        
        
    














