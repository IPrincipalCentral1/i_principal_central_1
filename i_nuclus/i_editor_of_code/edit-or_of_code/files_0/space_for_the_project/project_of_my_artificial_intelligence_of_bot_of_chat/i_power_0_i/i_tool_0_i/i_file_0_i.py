


















list_of_liberary_to_install = [
                            
                            ["playwright"] ,
                            
                            



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

















def i_function_0_i(i_text_0_i):
    
    
    '''
    
    this function print a message or a text on the terminal .
    
    
    '''
    
    
    print(f"{i_text_0_i}")
    
    
    
    
    
    





def i_function_1_i(i_number_0_i, i_number_1_i):
    
    
    '''
    
    this function count a number to anohter number . from i_number_0_i to i_number_1_i .
    
    
    '''
    
    
    
    
    if (i_number_0_i <= i_number_1_i):
        
        
        
        i_counter_0_i = i_number_0_i
        
        while (i_counter_0_i <= i_number_1_i):
            
            
            
            print(f"{i_counter_0_i}")
            
            
            i_counter_0_i += 1
            
            
        
    else:
        
        
        
        i_counter_0_i = i_number_1_i
        
        while (i_counter_0_i <= i_number_0_i):
            
            
            
            print(f"{i_counter_0_i}")
            
            
            i_counter_0_i += 1
            
        
        
        
        
        
    
    
    



























