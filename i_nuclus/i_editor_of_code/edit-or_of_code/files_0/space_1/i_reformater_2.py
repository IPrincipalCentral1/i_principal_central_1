
















list_of_liberary_to_install = [
                            
                            ["psutil"] ,
                            
                            


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







import psutil



def bytes_to_gb(b):

    return b / (1024**3)


vm = psutil.virtual_memory()


print(f"Total RAM:     {bytes_to_gb(vm.total):.2f} GB")

print(f"Available RAM: {bytes_to_gb(vm.available):.2f} GB")

print(f"Used RAM:      {bytes_to_gb(vm.used):.2f} GB")

print(f"Free RAM:      {bytes_to_gb(vm.free):.2f} GB")

print(f"Usage percent: {vm.percent}%")
















