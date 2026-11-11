


















'''




this is a good example of how to use my mixer





Suppose we want to mix, for example: (water, stone, air).

We must arrange these objects in sequential order. For example:



{

"water" : 0

"stone" : 1

"air"   : 2

}


Then we create a range from 0 to 2 .


Then we place only the number 2 in position i_number_of_element__minus_1__0_i .



and then we have many mix :
    
    
    [] : nothing 
    
    [0] : ["water"]
    
    [1] : ["stone"]
    
    [2] : ["air"]
    
    [0, 0] : ["water", "water"]
    
    [1, 0] : ["stone", "water"]
    
    
    ...
    
    and so on 
    
    



we allways start from : 
    
    
    [] : nothing 
    
    




if you want to use it do like this :
    
    
    
    
    import i_my_mixer_1_i
    
    
    
    i_list_0_i = []
    
    
    i_number_of_element__minus_1__0_i = 2
    
    
    
    i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    









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
    
    
    
    i_max_number_0_i = 1
    
    
    i_list_0_i = []
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = []
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    print(f"i_hello_0_i . i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < 15):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_1_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_2_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        i_list_3_i = i_next_step_3_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        print(f"i_hello_1_i . i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    '''
    
    
    
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
    
    '''
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    

















