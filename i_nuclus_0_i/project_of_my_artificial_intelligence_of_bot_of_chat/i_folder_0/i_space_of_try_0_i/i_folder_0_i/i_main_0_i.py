













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


import importlib





cwd = os.path.dirname(os.path.abspath(__file__))








i_path_0_i = os.path.dirname(cwd)


i_path_0_i = os.path.dirname(i_path_0_i)


i_path_0_i = os.path.dirname(i_path_0_i)



print(f"i_path_0_i = {i_path_0_i} .")


sys.path.append(i_path_0_i)



import i_tester_of_arithmetic_expretion_0_i


from pathlib import Path


import time





# start section of parameter 

# ------------------------------------------------------------------------------

# start_section_of_parameter 









# end_section_of_parameter 

# -----------------------------------------------------------------------------

# end section of parameter 








def i_remove_repetition_0_i(i_list_0_i):
    
    
    i_list_1_i = []
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < len(i_list_0_i)):
        
        
        if (not (i_list_0_i[i_counter_0_i] in i_list_1_i)):
            
            i_list_1_i.append(i_list_0_i[i_counter_0_i])
            
        
        i_counter_0_i += 1
            
            
        
    
    return i_list_1_i
    
    
    







i_list_0_i = [" i_smart_word_0_i "]


i_list_0_i.extend([" + ", " - ", " * ", " / ", " // ", " ** ", " % " , " if ", " else ", " == ", " >= ", " <= ", " > ", " < ", " != ", " := ", " ( ", " ) ", " [ ", " ] ", " , ", " for ", " in "])



i_list_1_i = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

i_list_2_i = []

i_counter_0_i = 0

while (i_counter_0_i < len(i_list_1_i)):
    
    i_list_2_i.append(" " + i_list_1_i[i_counter_0_i] + " ")
    
    i_counter_0_i += 1
    
    
i_list_0_i.extend(i_list_2_i)

    
    
i_list_0_i.extend([" range ", " len "])
    


i_list_0_i.extend([" i_list_of_index_of_dimenssions_0_i ", " i_list_0_i ", " i_list_of_var_to_use_0_i "])
    





i_char_of_all_items_of_math_0_i = ""


i_counter_0_i = 0

while (i_counter_0_i < len(i_list_0_i)):
    
    
    i_char_of_all_items_of_math_0_i += i_list_0_i[i_counter_0_i]
    
    
    i_counter_0_i += 1
    
    
    


print(f"i_char_of_all_items_of_math_0_i = {i_char_of_all_items_of_math_0_i} .")



i_file_text_0__0_i = os.path.join(i_path_0_i, "text_0.txt")

print(f"i_file_text_0__0_i = {i_file_text_0__0_i} .")


i_d_0_i = Path(i_file_text_0__0_i)


i_d_0_i.write_text(i_char_of_all_items_of_math_0_i)



import i_runner_of_my_artificial_intelligence_of_bot_of_chat_fast_14



i_v_1_i = i_runner_of_my_artificial_intelligence_of_bot_of_chat_fast_14.i_main_0_i()



i_v_2_i = []

i_counter_0_i = 0


while (i_counter_0_i < len(i_v_1_i[0])):
    
    
    
    i_v_3_i = i_v_1_i[0][i_counter_0_i][0][0][1]
    
    
    
    i_counter_1_i = i_v_1_i[0][i_counter_0_i][0][0][4][-1][0]
    
    while (i_counter_1_i < len(i_v_3_i)):
        
        
        i_v_2_i.append(i_v_3_i[i_counter_1_i])
        
        
        i_counter_1_i += 1
        
    
    
    
    i_counter_0_i += 1
    





print(f"i_v_2_i = {i_v_2_i} .")


i_v_3_i = []

i_counter_0_i = 0

while (i_counter_0_i < len(i_v_2_i)):
    
    
    i_v_3_i.append(i_v_2_i[i_counter_0_i][1][1:-1])
    
    
    i_counter_0_i += 1
    
    

#print(f"i_v_3_i = {i_v_3_i} .")




i_v_4_i = []

i_counter_0_i = 0

while (i_counter_0_i < len(i_v_3_i)):
    
    
    i_content_0_i = ""
    
    i_counter_1_i = 0
    
    while (i_counter_1_i < len(i_v_3_i[i_counter_0_i])):
        
        
        i_content_1_i = i_v_3_i[i_counter_0_i][i_counter_1_i]
        
        
        if (i_content_1_i in i_list_1_i):
            
            
            i_content_0_i += i_content_1_i
            
            
        else:
            
            
            i_content_0_i += " " + i_content_1_i + " "
            
            
        
        
        i_counter_1_i += 1
        
        
    
    
    i_v_4_i.append(i_content_0_i)
    
    
    i_counter_0_i += 1
    
    




i_v_4_i = i_remove_repetition_0_i(i_list_0_i=i_v_4_i)



print(f"i_v_4_i = {i_v_4_i} .")









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





















