













'''

this file should be executed before . if you want to launch a new mix from the beginning



'''



import os

folder_0 = os.path.join(os.getcwd(), "space_for_mix")


if (os.path.exists(folder_0)):
    
    
    
    
    
    


    
    dirs = [""]
    
    srcs = [""]
    
    
    counter_1 = 0
    
    while (counter_1 < len(dirs)):
    
    
        files = []
        
        
        dirs_ = []
    
    
        for root, dirs_, files in os.walk(os.path.join(folder_0, dirs[counter_1])):
    
            break
    
    
    
        counter_0 = 0
    
        while (counter_0 < len(dirs_)):


            srcs.append(os.path.join(srcs[counter_1], dirs_[counter_0]))
    
            counter_0 += 1
    
    
                    
        
    
            
        src_ = os.path.join(folder_0, srcs[counter_1])
        

    
    
    
        
    
        counter_0 = 0
    
        while (counter_0 < len(files)):
    
            try:


                os.remove(os.path.join(src_, files[counter_0]))

    
            except:
    
                            
                traceback.print_exc()
                
                error = traceback.format_exc()
                
                semaphore = True
    
                print(f"Erreur : {str(error)}")
    
    
    
    
    
            
            counter_0 += 1
    
        counter_1 += 1
    
    
    
    
    
    
else:


    os.makedirs(dist_, exist_ok=True)














