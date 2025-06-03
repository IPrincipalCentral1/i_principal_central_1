












# i_hello








# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
     
     
 


  
   
# hello 























    
    
    
    
    





# section of ai 






import traceback


import subprocess

import platform


import os




if __name__ == "__main__":



        
    
    
    list_of_liberary_to_install = [
    
                                ["PyQt5"] ,
                                
                                
                                ["psutil"] ,
                                
                                
                                ["requests"] ,
    
    
    ]
    
    
    
    

        
            
    command_1 = ""
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    
        command_1 += f"pip install {list_of_liberary_to_install[counter_0][0]};"
    
        counter_0 += 1
    
    

        
    system = platform.system()

    path_of_file = os.path.join(os.getcwd(), "edit-or_of_code", "files_0", "editor_of_code_0.py")
    
    
    
    
    
    
    
    if system == "Windows":
    
    
                
        command_1 = ""
        
        counter_0 = 0
        
        
        while (counter_0 < len(list_of_liberary_to_install)):
        
            command_1 += f"pip install {list_of_liberary_to_install[counter_0][0]} && "
        
            counter_0 += 1
        
        
    
        subprocess.run(["cmd", "/c", f"{command_1} python {path_of_file}"])
    
    elif system == "Linux":
    
        
        subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command_1} ; python3 {path_of_file}; exit"])
    
    elif system == "Darwin":
    
        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command_1} ;python3 {path_of_file}; exit"'])
    
    








# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


# my code 













