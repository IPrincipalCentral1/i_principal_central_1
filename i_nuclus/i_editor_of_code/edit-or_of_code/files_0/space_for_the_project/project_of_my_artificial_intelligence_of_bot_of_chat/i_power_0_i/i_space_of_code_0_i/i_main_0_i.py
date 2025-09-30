










'''

this is a space for the code .


'''












list_of_liberary_to_install = [
                            
                            ["playwright"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess


cwd = os.path.dirname(os.path.abspath(__file__))



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







i_path_0_i = os.path.dirname(cwd)


sys.path.append(i_path_0_i)


sys.path.append(os.path.join(i_path_0_i, "i_tool_0_i"))


sys.path.append(os.path.join(i_path_0_i, "i_memory_0_i"))


























