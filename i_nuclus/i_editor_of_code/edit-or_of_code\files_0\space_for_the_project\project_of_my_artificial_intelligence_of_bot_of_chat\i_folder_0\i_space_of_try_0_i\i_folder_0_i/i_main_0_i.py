













'''







Example :
    
    
    
    input :    
        
        
        [0, 1, 2]
        
    
    output :
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < 3):
            
            
            i_counter_0_i += 1
            
        
        
        it will return [3, 4, 5]
        
        
        
    
    
        
        
        
        
    
    
    
    
    






link :
    
    
/media/iprincipalcentrali/0058B82F5DED5DF5/i_space_0_i/i_folder_0_i
    
    
    


'''









import os


import sys







cwd = os.path.dirname(os.path.abspath(__file__))








i_path_0_i = os.path.dirname(cwd)


i_path_0_i = os.path.dirname(i_path_0_i)


i_path_0_i = os.path.dirname(i_path_0_i)



print(f"i_path_0_i = {i_path_0_i} .")


sys.path.append(i_path_0_i)



import i_tester_of_arithmetic_expretion_0_i










i_list_of_variables_0_i = [" i_v_0_i ", " i_v_1_i ", " i_v_2_i "]






i_operation_0_i = " i_v_0_i  +  i_v_0_i "




i_content_of_import_0_i = r"""





"""




i_init_of_variables_0_i = r"""



i_v_0_i = 1


i_v_1_i = 1


i_v_2_i = 1



"""















i_v_0_i = i_tester_of_arithmetic_expretion_0_i.i_main_0_i(i_list_of_variables_0_i=i_list_of_variables_0_i, i_operation_0_i=i_operation_0_i, i_content_of_import_0_i=i_content_of_import_0_i, i_init_of_variables_0_i=i_init_of_variables_0_i)



print(f"i_v_0_i = {i_v_0_i} .")





















