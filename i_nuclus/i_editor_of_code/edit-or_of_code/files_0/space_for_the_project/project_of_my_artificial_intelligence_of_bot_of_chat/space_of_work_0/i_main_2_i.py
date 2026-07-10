














































































































import os

import time



cwd = os.path.dirname(os.path.abspath(__file__))





def i_transforme_0_i(hex_value):
    
    
    i_char_0_i = chr(int(hex_value, 16))
    
    return i_char_0_i
    
    









i_t_1_i = time.time()



hex_value = "004A"

char = chr(int(hex_value, 16))

print(char)   # J





i_file_0_i = os.path.join(cwd, "unicode-characters.csv")

with open(i_file_0_i, "r") as f_:
    
    i_content_0_i = f_.read(os.path.getsize(i_file_0_i))
    
    



i_v_1_i = i_content_0_i.split("\n")



i_str_result_0_i = ""




i_counter_1_i = 1


while (i_counter_1_i < len(i_v_1_i)):
    
    
    try:
        
        #i_string_0_i = "004A,LATIN CAPITAL LETTER J,Lu,0,L,,,,,N,,,,006A,"
        
        
        
        
        i_string_0_i = i_v_1_i[i_counter_1_i]
        
        
        i_v_0_i = i_string_0_i.split(",")
        
        
        i_char_0_i = i_transforme_0_i(hex_value=i_v_0_i[0])
        
        
        
        i_file_2_i = os.path.join(cwd, "i_space_1_i.txt")
        
        with open(i_file_2_i, "w") as f_:
            
            
            f_.write(i_char_0_i)
            
            
        
        
        
        i_str_result_0_i += f"\n{i_char_0_i} : "
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_v_0_i)):
            
            
            if (i_v_0_i[i_counter_0_i] != ""):
                
                i_str_result_0_i += f" {i_v_0_i[i_counter_0_i]} , "
                
                
            
            
            i_counter_0_i += 1
            
            
            
    except:
        
        
        i_semaphore_0_i = True
        
        
        
        
    
    
    
    
    i_counter_1_i += 1
    
    




i_file_1_i = os.path.join(cwd, "i_unicode_characters_1_i.csv")

with open(i_file_1_i, "w") as f_:
    
    
    f_.write(i_str_result_0_i)
    
    





i_t_2_i = time.time()



print(f"time = {i_t_2_i - i_t_1_i} second .")











