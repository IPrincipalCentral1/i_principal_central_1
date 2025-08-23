













'''

this file should be executed before . if you want to launch a new mix from the beginning



'''



import os


cwd = os.path.dirname(os.path.abspath(__file__))


folder_0 = os.path.join(cwd, "space_for_mix")


if (os.path.exists(folder_0) == False):
    
    os.makedirs(folder_0, exist_ok=True)

else:    
    
    
    
    files = []
    
    for root, dirs, files in os.walk(folder_0):
    
        break
    
    
    
    counter_0 = 0
    
    
    while (counter_0 < len(files)):
    
        
        os.remove(os.path.join(folder_0, files[counter_0]))
    
    
        counter_0 += 1
    
    

















