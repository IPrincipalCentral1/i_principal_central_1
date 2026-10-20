



































































































'''



there is a mixer type_0 


and a mixer type_1



'''










import copy








def i_next_step_0_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 0 .
    
    
    
    '''
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i += 1
            
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(0)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_1_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 1 .
    
    
    
    '''
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i -= 1
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, 0)
        
        
        
        
    
    return i_list_0_i











def i_next_step_2_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 2 .
    
    
    
    '''
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i += 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if (i_list_0_i[i_counter_0_i] >= 0):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_element__minus_1__0_i)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_3_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 3 .
    
    
    
    '''
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i -= 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if (i_list_0_i[i_counter_0_i] >= 0):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_element__minus_1__0_i)
        
        
        
        
    
    return i_list_0_i




































def i_next_step_of_type_1_mixer_0_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
   
   
   
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
   
   
   
   
   
   
    ''' 
    
    
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i += 1
            
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_first_appear_0_i)
        
        
        
        
        
    
    return i_list_0_i










def i_next_step_of_type_1_mixer_1_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    '''
    
    
        
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i -= 1
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_first_appear_0_i)
        
        
        
        
    
    return i_list_0_i











def i_next_step_of_type_1_mixer_2_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    
    '''
    
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    
    '''
    
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    i_semaphore_of_add_1_i = False
    
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True) and (i_semaphore_of_add_1_i == False)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i += 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if ((i_list_0_i[i_counter_0_i] >= 0)):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
            
            
            
            
            if ((i_list_0_i[i_counter_0_i] < i_number_of_first_appear_0_i) and (i_counter_0_i == len(i_list_0_i) - 1) and (len(i_list_0_i) > 1)):
                
                
                
                i_semaphore_of_add_1_i = True
                
                
                
                i_semaphore_of_add_0_i = True
                
                
            
            
            
        
    
    
    
    
    if (i_semaphore_of_add_1_i == True):
    
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_0_i)):
            
            
            
            i_list_0_i[i_counter_1_i] = i_number_of_element__minus_1__0_i
            
            
            
            i_counter_1_i += 1
            
            
            
    
    
    
    
    
    
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_element__minus_1__0_i)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_of_type_1_mixer_3_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    
    
    '''
    
    
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    i_semaphore_of_add_1_i = False
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True) and (i_semaphore_of_add_1_i == False)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
        
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
                
            
            
            i_counter_0_i -= 1
                
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            
            
            
            
            if ((i_list_0_i[i_counter_0_i] >= 0)):
            
                
                
                
                i_semaphore_of_add_0_i = False
                
                
                
                
                
                
                
            
            
            
            if ((i_list_0_i[i_counter_0_i] < i_number_of_first_appear_0_i) and (i_counter_0_i == 0) and (len(i_list_0_i) > 1)):
                
                
                
                i_semaphore_of_add_1_i = True
                
                
                
                i_semaphore_of_add_0_i = True
                
                
                
                
            
            
        
     
    
    
    
    if (i_semaphore_of_add_1_i == True):
    
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_0_i)):
            
            
            i_list_0_i[i_counter_1_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_1_i += 1
            
            
            
    
    
    
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_element__minus_1__0_i)
        
        
        
        
    
    return i_list_0_i




























def i_check_if_repetition_exist_0_i(i_list_0_i):
    
    
    
    i_semaphore_of_result_0_i = False
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_result_0_i == False)):
        
        
        i_counter_of_repetition_0_i = 0
        
        
        i_counter_1_i = i_counter_0_i
        
        
        while ((i_counter_1_i < len(i_list_0_i))):
            
            
            if (i_list_0_i[i_counter_1_i] == i_list_0_i[i_counter_0_i]):
                
                
                i_counter_of_repetition_0_i += 1
                
                
            
            
            i_counter_1_i += 1
            
        
        
        
        if (i_counter_of_repetition_0_i > 1):
            
            
            i_semaphore_of_result_0_i = True
            
            
        
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
    i_element_that_repeats_0_i = i_counter_0_i - 1
    
    
    
    return [i_semaphore_of_result_0_i, i_element_that_repeats_0_i]
    
    
    





def i_main_0_i():
    
    
    
    i_max_number_0_i = 9
    
    
    
    i_number_of_loop_0_i = 150
    
    
    
    i_list_0_i = []
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = []
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < i_number_of_loop_0_i):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_1_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_2_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        
        i_list_3_i = i_next_step_3_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    
    
    
    i_semaphore_of_result_0_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_0_i)
    
    
    
    i_semaphore_of_result_1_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_1_i)
    
    
    
    i_semaphore_of_result_2_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_2_i)
    
    
    
    i_semaphore_of_result_3_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_3_i)
    
    
    
    
    
    i_list_of_semaphores_of_result_0_i = [
                    
                    
                    i_semaphore_of_result_0_i,
                    
                    
                    i_semaphore_of_result_1_i,
                    
                    
                    i_semaphore_of_result_2_i,
                    
                    
                    i_semaphore_of_result_3_i,
                    
                    
                    
                    ]
    
    
    
    
    print(f"\n\n\n    i_list_of_semaphores_of_result_0_i = {i_list_of_semaphores_of_result_0_i} .\n\n\n")
    
    
    
    
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    i_number_of_first_appear_0_i = 1
    
    
    
    i_list_0_i = [0]
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = [0]
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < i_number_of_loop_0_i):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_of_type_1_mixer_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_of_type_1_mixer_1_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_of_type_1_mixer_2_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        
        i_list_3_i = i_next_step_of_type_1_mixer_3_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    
    
    
    i_semaphore_of_result_0_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_0_i)
    
    
    
    i_semaphore_of_result_1_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_1_i)
    
    
    
    i_semaphore_of_result_2_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_2_i)
    
    
    
    i_semaphore_of_result_3_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_3_i)
    
    
    
    
    i_list_of_semaphores_of_result_0_i = [
                    
                    
                    i_semaphore_of_result_0_i,
                    
                    
                    i_semaphore_of_result_1_i,
                    
                    
                    i_semaphore_of_result_2_i,
                    
                    
                    i_semaphore_of_result_3_i,
                    
                    
                    
                    ]
    
    
    
    
    print(f"\n\n\n    i_list_of_semaphores_of_result_0_i = {i_list_of_semaphores_of_result_0_i} .\n\n\n")
    
    
    
    
    
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    

















