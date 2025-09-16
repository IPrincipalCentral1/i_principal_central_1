


















import os 

import platform


list_of_file_to_execute = [


                        r"downloader_from_UniversalDependencies_0.py",
                        
                        
                        r"organize_from_file_of_conllu_0.py",
                        
                        
                        r"extracter_of_list_of_word_0.py",
                        
                        
                        r"get_definition_of_word_0.py",
                        
                        
                        r"get_hypernyms_of_word_0.py",
                        
                        
                        ]



 
system = platform.system()


if system == "Windows":


    counter_0 = 0
    
    while (counter_0 < len(list_of_file_to_execute)):
    
        command = f"python {list_of_file_to_execute[counter_0]}"
    
        print(f"command = '{command}'")
    
        os.system(command)
    
        counter_0 += 1

elif system == "Linux":


    counter_0 = 0
    
    while (counter_0 < len(list_of_file_to_execute)):
        
        command = f"python3 {list_of_file_to_execute[counter_0]}"
        
        print(f"command = '{command}'")
        
        os.system(command)
        
        counter_0 += 1
    

elif system == "Darwin":
    
    
        
    counter_0 = 0
    
    while (counter_0 < len(list_of_file_to_execute)):
    
        command = f"python3 {list_of_file_to_execute[counter_0]}"
    
        print(f"command = '{command}'")
        
        os.system(command)
    
        counter_0 += 1
    
    







































