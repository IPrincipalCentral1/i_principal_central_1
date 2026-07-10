














import i_my_mixer_1_i


import ast


import os


import time




cwd = os.path.dirname(os.path.abspath(__file__))












def i_calculate_the_general_of_numbers_0_i(i_list_0_i):
    
    
    i_result_0_i = 0
    
    
    i_counter_0_i = 0
    
    
    
    
    
    
    while (i_counter_0_i < len(i_list_0_i)):
        
        
        i_result_0_i += i_list_0_i[i_counter_0_i]
        
        
        i_counter_0_i += 1
        
        
        
    
    
    i_result_0_i = int( i_result_0_i / len(i_list_0_i) )
    
    
    
    return i_result_0_i
    






def i_main_0_i():
    
    
    
    i_max_number_0_i = 3
    
    
    i_list_0_i = []
    
    
    
    i_name_of_file_0_i = os.path.join(cwd, "i_file_of_sauvgard_of_stat_0_i.txt")
    
    
    i_t_0_i = 0.0
    
    
    i_t_1_i = 0.0
    
    
    i_number_of_operation_per_second_0_i = 0
    
    
    i_max_0_i = 0
    
    
    i_min_0_i = 100_000_000
    
    
    i_list_of_general_0_i = []
    
    
    i_limit_of_list_0_i = 1_000
    
    
    i_number_of_general_0_i = 0
    
    
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} .")
    
    
    
    
    i_semaphore_of_continue_0_i = True    
    
    
    while (i_semaphore_of_continue_0_i == True):
        
        
        i_t_0_i = time.time()
        
        
        i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        i_t_1_i = time.time()
        
        
        if (i_t_0_i != i_t_1_i):
            
            i_number_of_operation_per_second_0_i = int(1 / (i_t_1_i - i_t_0_i))
            
        else:
            
            i_number_of_operation_per_second_0_i = -1
            
            
        
        
        if (i_max_0_i < i_number_of_operation_per_second_0_i):
            
            
            i_max_0_i = i_number_of_operation_per_second_0_i
            
            
        
        if (i_min_0_i > i_number_of_operation_per_second_0_i):
            
            
            i_min_0_i = i_number_of_operation_per_second_0_i
            
            
        
        
        i_list_of_general_0_i.append(i_number_of_operation_per_second_0_i)
        
        
        if (len(i_list_of_general_0_i) > i_limit_of_list_0_i):
            
            
            i_list_of_general_0_i.pop(0)
            
            
            
        
        i_number_of_general_0_i = i_calculate_the_general_of_numbers_0_i(i_list_0_i=i_list_of_general_0_i)
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} .\n i_number_of_operation_per_second_0_i = {i_number_of_operation_per_second_0_i} operation . i_max_0_i = {i_max_0_i} operation . i_min_0_i = {i_min_0_i} operation . i_number_of_general_0_i = {i_number_of_general_0_i} operation .")
        
        
        
        
        
        
        
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    







