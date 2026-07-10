














































































































import os

import time



cwd = os.path.dirname(os.path.abspath(__file__))





def i_transforme_0_i(hex_value):
    
    
    i_char_0_i = chr(int(hex_value, 16))
    
    return i_char_0_i
    
    





i_counter_1_i = 0


i_counter_2_i = 0






i_t_1_i = time.time()




i_file_0_i = os.path.join(cwd, "i_file_of_code_of_ASCII_0_i.txt")



with open(i_file_0_i, "w") as f_:
    
    f_.write("")
    



i_result_str_0_i = "\n\n"



#f_.write(i_result_str_0_i)
    



i_counter_1_i = 0


i_counter_2_i = 0


while (i_counter_1_i < 128):
    
    
    try:
        
        
        i_char_0_i = chr(i_counter_1_i)
        
        
        
        i_file_2_i = os.path.join(cwd, "i_space_1_i.txt")
        
        with open(i_file_2_i, "w") as f_:
            
            
            f_.write(i_char_0_i)
            
            
        
        
        
        
        with open(i_file_0_i, "a") as f_:
            
            f_.write(i_char_0_i)
            
        
        
        
        i_counter_2_i += 1
        
        
        
            
    except:
        
        
        i_semaphore_0_i = True
        
        
        
        
    
    
    
    i_counter_1_i += 1
    
    
    
    
    
    






i_t_2_i = time.time()



print(f"i_hello_0_i . time = {i_t_2_i - i_t_1_i} second . i_counter_2_i = {i_counter_2_i} .")




'''

128


'''















