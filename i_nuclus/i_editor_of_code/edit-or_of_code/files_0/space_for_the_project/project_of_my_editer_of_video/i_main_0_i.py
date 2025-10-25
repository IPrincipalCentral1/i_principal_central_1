




















































































































list_of_liberary_to_install = [
                            
                            
                            ["pillow"] ,
                            
                            
                            ["manim"] ,
                            
                            
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






global i_content_0_i



i_content_0_i = r"""











list_of_liberary_to_install = [
                            
                            
                            ["pillow"] ,
                            
                            
                            ["manim"] ,
                            
                            
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







'''

the part of the code .


'''




from manim import *



class _____name_of_class_0_____(Scene):
    
    
    
    def construct(self):
        
        
        i_text_0_i = "i_hello_i"
        
        text = Text(i_text_0_i)
        
        self.play(Write(text))
        
        self.wait(0.2)
        
        




"""





def i_main_0_i():
    
    
    
    global i_content_0_i
    
    
    
    i_name_of_project_0_i = "HelloManim"
    
    
    i_content_0_i = i_content_0_i.replace("_____name_of_class_0_____", i_name_of_project_0_i)
    
    
    
    
    i_name_of_file_0_i = "i_main_0_0_i.py"
    
    i_file_0_i = os.path.join(cwd, i_name_of_file_0_i)
    
    with open(i_file_0_i, "w") as f_:
        
        f_.write(i_content_0_i)
        
    
    
    os.system(f"{sys.executable} -m manim -pql {i_name_of_file_0_i} {i_name_of_project_0_i}")
    
    
    
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    
    
    



























