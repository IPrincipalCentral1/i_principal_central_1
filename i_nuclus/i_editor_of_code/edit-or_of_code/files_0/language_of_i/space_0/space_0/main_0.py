













def find_in_0(str_0, str_1):
    
    
    len_str_0 = len(str_0)
    
    len_str_1 = len(str_1)
    
    counter_0 = 0
    
    counter_1 = 0
    
    while (counter_1 < len_str_1):
    
        
        counter_2 = counter_1
        
        counter_0 = 0
        
        while ((counter_0 < len_str_0) and (counter_2 < len_str_1) and (str_0[counter_0] == str_1[counter_2])):
            
            counter_0 += 1
            
            counter_2 += 1
        
        
        if (counter_0 == len_str_0):
        
            break
        
        
        counter_1 += 1
        
        
    
    if (counter_0 == len_str_0):
        
        return True
        
    else:
        
        return False
        
        
    







result = find_in_0(str_0="i_0", str_1="i_0")

print(f"result = {result} .")






