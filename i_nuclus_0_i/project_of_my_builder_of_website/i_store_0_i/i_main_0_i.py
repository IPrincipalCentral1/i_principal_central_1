












import threading

import time


i_t_1_i = time.time()




def processus_1():
    
    
    
    while (True):
        
        print(f"i_hello_0_i . time = {time.time() - i_t_1_i} second .")
        
    





def processus_0():
    
    
    
    
    i_p_1_i = threading.Thread(target=processus_1, daemon=True).start()
    
    i_counter_0_i = 0
    
    while (True):
        
        
        i_counter_0_i += 1
        
        
        
    
    
    






i_p_0_i = threading.Thread(target=processus_0, daemon=True).start()






while (True):
    
    pass
    
    
    







