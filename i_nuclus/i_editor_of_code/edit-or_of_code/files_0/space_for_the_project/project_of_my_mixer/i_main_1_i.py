













































































































def i_next_step_0_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    
    i_counter_0_i = 0
    
    
    if (i_counter_0_i < len(i_list_0_i)):
        
        
        i_list_0_i[i_counter_0_i] += 1
        
        
        i_semaphore_of_add_0_i = True
        
        
        while (((i_counter_0_i < len(i_list_0_i))) and (i_semaphore_of_add_0_i == True)):
            
            
            print(f"                                                    i_list_0_i[i_counter_0_i] = {i_list_0_i[i_counter_0_i]} . i_list_0_i = {i_list_0_i} .")
            
            
            if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
                
                
                i_list_0_i[i_counter_0_i] = 0
                
                
                i_counter_0_i += 1
                
                
                i_semaphore_of_add_0_i = True
                
                
            else:
                
                
                print(f"i_hello_3_i . i_list_0_i[i_counter_0_i] = {i_list_0_i[i_counter_0_i]} .")
                
                i_list_0_i[i_counter_0_i] += 1
                
                print(f"i_hello_4_i . i_list_0_i[i_counter_0_i] = {i_list_0_i[i_counter_0_i]} .")
                
                if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                    
                    
                    i_semaphore_of_add_0_i = False
                    
                    
                
            
            
            print(f"    i_hello_2_i . i_counter_0_i = {i_counter_0_i} . i_semaphore_of_add_0_i = {i_semaphore_of_add_0_i} .")
                        
            
                
        
        if (i_semaphore_of_add_0_i == True):
            
            
            
            i_list_0_i.append(0)
            
            
        
            
        
    else:
        
        
        
        i_list_0_i.append(0)
        
        
        
        
    
    return i_list_0_i




i_max_number_0_i = 3


i_list_0_i = [3, 2, 3]



print(f"i_hello_0_i . i_list_0_i = {i_list_0_i} .")


i_list_0_i = i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)





print(f"i_hello_1_i . i_list_0_i = {i_list_0_i} .")






















