










































































































'''







if you want to do the dupliquor of list of folders . you should add at your table :
    
    
    
    ( i_simbole_of_empty_file_0_i == n + 1 ) : for the file that are empty . and chose just the mixs that are with 1 ( n + 1 ) in the file .
    
    
    





when you mix . you should impliment this in your table of mix :
    
    
    
    ["[", "]", ","]
    
    
    and you can add the numbers in between 2 spaces . like that :
        
        
        [" 0 ", " 1 ", ...]
        
        
    
    
    and you add :
        
        ( i_simbole_of_empty_file_0_i == n + 1 ) : n is the length of your table of mix .
        
    






'''






import os

import copy

import sys

import importlib







cwd = os.path.dirname(os.path.abspath(__file__))







# start of parametter :

# -----------------------------------------------------------------------------------






# end of parametter .

# -----------------------------------------------------------------------------------








i_name_standard_of_file_0_i = "file"



i_name_standard_of_folder_0_i = "folder"







def i_filter_of_if__int_xor_list__0_i(i_list_0_i):
    
    
    
    
    i_semaphore_of_pass_0_i = False
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (type(i_list_0_i[i_counter_0_i]) == list)):
        
        
        i_counter_0_i += 1
        
        
        
        
    
    if (i_counter_0_i > 0):
        
        
        if (i_counter_0_i < len(i_list_0_i)):
            
            
            i_semaphore_of_pass_0_i = False
            
            
        else:
            
            
            i_semaphore_of_pass_0_i = True
            
            
            
        
    else:
        
        
        
        
        
        i_counter_0_i = 0
        
        
        while ((i_counter_0_i < len(i_list_0_i)) and (type(i_list_0_i[i_counter_0_i]) == int)):
            
            
            i_counter_0_i += 1
            
            
            
        
        
        
        
        if (i_counter_0_i > 0):
            
            
            if (i_counter_0_i < len(i_list_0_i)):
                
                
                i_semaphore_of_pass_0_i = False
                
                
            else:
                
                
                i_semaphore_of_pass_0_i = True
                
                
        
        
        
    
    
    return i_semaphore_of_pass_0_i
    
    
    




def i_filter_of_if__int_xor_list__1_i(i_list_0_i):
    
    
    
    
    i_semaphore_of_pass_0_i = False
    
    
    i_semaphore_of_type_0_i = ""
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (type(i_list_0_i[i_counter_0_i]) == list)):
        
        
        i_counter_0_i += 1
        
        
        
    
    
    if (i_counter_0_i > 0):
        
        
        if (i_counter_0_i < len(i_list_0_i)):
            
            
            i_semaphore_of_pass_0_i = False
            
            
        else:
            
            
            i_semaphore_of_pass_0_i = True
            
            
            i_semaphore_of_type_0_i = i_name_standard_of_folder_0_i
            
            
            
        
    else:
        
        
        
        
        
        i_counter_0_i = 0
        
        
        while ((i_counter_0_i < len(i_list_0_i)) and (type(i_list_0_i[i_counter_0_i]) == int)):
            
            
            i_counter_0_i += 1
            
            
            
        
        
        
        
        if (i_counter_0_i > 0):
            
            
            if (i_counter_0_i < len(i_list_0_i)):
                
                
                i_semaphore_of_pass_0_i = False
                
                
            else:
                
                
                i_semaphore_of_pass_0_i = True
                
                
                i_semaphore_of_type_0_i = i_name_standard_of_file_0_i
                
                
                
            
            
        else:
            
            
            
            i_semaphore_of_pass_0_i = True
            
            
            i_semaphore_of_type_0_i = i_name_standard_of_folder_0_i
            
            
            
        
    
    
    
    
    
    return [i_semaphore_of_pass_0_i, i_semaphore_of_type_0_i]
    
    
    






def i_walk_0_i(i_list_0_i, i_rooty_path_0_i):
    
    
    
    
    i_semaphore_of_error_0_i = False
    
    
    i_list_of_folders_0_i = []
    
    
    i_list_of_files_0_i = []
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_error_0_i == False)):
        
        
        
        i_item_0_i = i_filter_of_if__int_xor_list__1_i(i_list_0_i=i_list_0_i[i_counter_0_i])
        
        
        
        if (i_item_0_i[0] == True):
            
            
            if (i_item_0_i[1] == i_name_standard_of_folder_0_i):
                
                
                i_list_of_folders_0_i.append([i_list_0_i[i_counter_0_i], i_counter_0_i, f"{i_rooty_path_0_i}_{i_counter_0_i}"])
                
                
                
            elif (i_item_0_i[1] == i_name_standard_of_file_0_i):
                
                
                i_list_of_files_0_i.append([i_list_0_i[i_counter_0_i], i_counter_0_i, f"{i_rooty_path_0_i}_{i_counter_0_i}"])
                
                
                
                
            
            
            
        else:
            
            
            
            i_semaphore_of_error_0_i = True
            
            
            
            
        
        i_counter_0_i += 1
        
        
        
    
    
    return [i_semaphore_of_error_0_i, i_list_0_i, i_list_of_folders_0_i, i_list_of_files_0_i]
    
    
    
    
    



def i_walk_1_i(i_list_0_i, i_rooty_path_0_i):
    
    
    
    
    i_semaphore_of_error_0_i = False
    
    
    i_list_of_folders_0_i = []
    
    
    i_list_of_items_0_i = []
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_error_0_i == False)):
        
        
        
        i_item_0_i = i_list_0_i[i_counter_0_i]
        
        
        if (type(i_item_0_i) == list):
            
            
            i_list_of_folders_0_i.append([i_list_0_i[i_counter_0_i], i_counter_0_i, f"{i_rooty_path_0_i}_{i_counter_0_i}"])
            
            
            
        else:
            
            
            i_list_of_items_0_i.append([i_list_0_i[i_counter_0_i], i_counter_0_i, f"{i_rooty_path_0_i}_{i_counter_0_i}"])
            
            
            
            
            
            
            
            
            
            
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    return [i_list_0_i, i_list_of_folders_0_i, i_list_of_items_0_i]
    
    
    
    
    





def i_go_to_in_list_0_i(i_list_0_i, i_path_0_i):
    
    
    
    i_list_1_i = i_list_0_i
    
    
    if (len(i_path_0_i) > 0):
    
        
        i_v_2_i = i_path_0_i.split("_")
        
        
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_v_2_i)):
            
            
            if (i_v_2_i[i_counter_0_i] != ""):
                
                i_list_1_i = i_list_1_i[int(i_v_2_i[i_counter_0_i])]
                
            
            
            i_counter_0_i += 1
            
            
    
    
    
    
    return i_list_1_i
    
    
    
    
    




def i_get_list_of_folder_0_i(i_list_0_i, i_simbole_of_empty_file_0_i):
    
    
    
    
    
    i_list_of_all_files_0_i = []
    
    
    i_list_of_all_folders_0_i = []
    
    
    i_semaphore_of_error_0_i = False
    
    
    
    
    i_v_0_i = i_filter_of_if__int_xor_list__1_i(i_list_0_i=i_list_0_i)
    
    
    
    
    
    if (i_v_0_i[1] == i_name_standard_of_file_0_i):
    
        
        
        i_list_of_all_files_0_i.extend([i_source_1_i])
        
        
        
        
        
    else:
        
        
        
        i_dirs_0_i = []
        
        
        i_path_of_dirs_0_i = [""]
        
        
        
        
        i_counter_1_i = 0
        
        
        while ((i_counter_1_i < len(i_path_of_dirs_0_i)) and (i_semaphore_of_error_0_i == False)):
            
        
            
            
            
            
            
            i_list_1_i = i_go_to_in_list_0_i(i_list_0_i=i_list_0_i, i_path_0_i=i_path_of_dirs_0_i[i_counter_1_i])
            
            
            
            
            i_v_1_i = i_walk_0_i(i_list_0_i=i_list_1_i, i_rooty_path_0_i=i_path_of_dirs_0_i[i_counter_1_i])
            
            
            
            
            if (i_v_1_i[0] == False):
            
                
                
                
                i_root_0_i = i_v_1_i[1]
                
                
                i_dirs_1_i = i_v_1_i[2]
                
                
                i_files_0_i = i_v_1_i[3]
                
                
                
        
            
                i_counter_0_i = 0
            
                while (i_counter_0_i < len(i_dirs_1_i)):
                    
                    
                    
                    i_path_of_dirs_0_i.append(f"{i_path_of_dirs_0_i[i_counter_1_i]}_{i_dirs_1_i[i_counter_0_i][1]}")
                    
                    
                    i_dirs_0_i.append(i_dirs_1_i[i_counter_0_i])
                    
                    
                    
                    i_counter_0_i += 1
                    
                
                
                
                
                
                i_counter_2_i = 0
                
                
                
                while ((i_counter_2_i < len(i_files_0_i)) and (i_semaphore_of_error_0_i == False)):
                    
                    
                    if ((1 < len(i_files_0_i[i_counter_2_i][0])) and (i_simbole_of_empty_file_0_i in i_files_0_i[i_counter_2_i][0])):
                        
                        
                        i_semaphore_of_error_0_i = True
                        
                        
                        
                    
                    
                    i_list_of_all_files_0_i.append(i_files_0_i[i_counter_2_i])
                    
                    
                    
                    
                    i_counter_2_i += 1
                    
                    
                    
                
                
                
                
                
                
                
                i_counter_1_i += 1
                
                
                
            else:
                
                
                i_semaphore_of_error_0_i = True
                
                
                
                
            
            
        
        
        
    
    
    
    
    
    i_list_of_all_folders_0_i = i_dirs_0_i
    
    
    
    return [i_list_0_i, i_list_of_all_folders_0_i, i_list_of_all_files_0_i, i_semaphore_of_error_0_i]
    
    






def i_dupliquor_of_list_1_i(i_list_0_i, i_semaphore_of_dupliquation_0_i):
    
    
    
    
    i_list_of_resulted_dupliquation_0_i = []
    
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_of_all_folders_0_i = []
    
    
    
    i_v_0_i = i_filter_of_if__int_xor_list__1_i(i_list_0_i=i_list_0_i)
    
    
    
    
    
    if (i_v_0_i[1] == i_name_standard_of_file_0_i):
    
        
        
        i_list_of_all_files_0_i.extend([i_source_1_i])
        
        
        
        
        
    else:
        
        
        
        i_dirs_0_i = []
        
        
        i_path_of_dirs_0_i = [""]
        
        
        
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_path_of_dirs_0_i)):
            
        
            
            
            
            
            
            i_list_1_i = i_go_to_in_list_0_i(i_list_0_i=i_list_0_i, i_path_0_i=i_path_of_dirs_0_i[i_counter_1_i])
            
            
            
            
            i_v_1_i = i_walk_1_i(i_list_0_i=i_list_1_i, i_rooty_path_0_i=i_path_of_dirs_0_i[i_counter_1_i])
            
        
            
            i_root_0_i = i_v_1_i[0]
            
            
            i_dirs_1_i = i_v_1_i[1]
            
            
            i_items_0_i = i_v_1_i[2]
            
            
            
            
    
        
            i_counter_0_i = 0
        
            while (i_counter_0_i < len(i_dirs_1_i)):
                
                
                
                i_path_of_dirs_0_i.append(f"{i_path_of_dirs_0_i[i_counter_1_i]}_{i_dirs_1_i[i_counter_0_i][1]}")
                
                
                i_dirs_0_i.append(i_dirs_1_i[i_counter_0_i])
                
                
                
                i_list_2_i = i_go_to_in_list_0_i(i_list_0_i=i_list_of_resulted_dupliquation_0_i, i_path_0_i=i_path_of_dirs_0_i[i_counter_1_i]) 
                
                
                
                i_list_2_i.append([])
                
                
                
                
                
                
                i_counter_0_i += 1
                
            
            
            
            
            
            
            
            
            
            
            
            i_list_of_all_items_0_i.extend(i_items_0_i)
            
            
            
         
        
            
            
            i_counter_1_i += 1
            
            
                
            
            
        
        
        
        
        
        # section of dupliquation 
        
        
        if (i_semaphore_of_dupliquation_0_i == True):
            
            
            
            i_counter_0_i = 0
            
            
            while (i_counter_0_i < len(i_list_of_all_items_0_i)):
                
                
                
                
                
                i_path_1_i = i_list_of_all_items_0_i[i_counter_0_i][2]
                
                
                i_path_1_i = i_path_1_i[:-2]
                
                
                
                
                i_list_2_i = i_go_to_in_list_0_i(i_list_0_i=i_list_of_resulted_dupliquation_0_i, i_path_0_i=i_path_1_i) 
                
                
                
                i_list_2_i.append(i_list_of_all_items_0_i[i_counter_0_i][0])
                
                
                i_counter_0_i += 1
                
                
                
            
            
            
            
        
        
        
        
    
    i_list_of_all_folders_0_i = i_dirs_0_i
    
    
    
    return [i_list_0_i, i_list_of_all_folders_0_i, i_list_of_all_items_0_i, i_list_of_resulted_dupliquation_0_i]
    
    












def i_from_string_to_list_0_i(i_string_of_list_0_i):
    
    
    
    
    
    
    
    
    i_list_of_result_0_i = []
    
    
    i_var_of_error_compilation_0_i = True
    
    
    i_init_of_variables_0_i = i_string_of_list_0_i
    
    
    
    
    if ((len(i_init_of_variables_0_i) >= 2) and (i_init_of_variables_0_i[0] == "[") and (i_init_of_variables_0_i[-1] == "]")):
    
        
        
        
        
        
        i_file_1_i = os.path.join(cwd, "i_main_of_test_2_0_i.py")
        
        
        i_file_4_i = os.path.join(cwd, "i_file_of_semaphore_of_error_compilation_0_i.txt")
        
        
        
        
        i_content_of_testing_0_i = r"""
    
    














import os



cwd = os.path.dirname(os.path.abspath(__file__))




def i_main_0_i():
    
    
    
    
    
    
    
    i_v_0_i = _____i_init_of_variables_1_i_____
    
    
    
    
    
    
    
    
    
    i_file_4_i = os.path.join(cwd, "i_file_of_semaphore_of_error_compilation_0_i.txt")
    
    
    
    
    if (type(i_v_0_i) == list):
        
        
        
        with open(i_file_4_i, "w") as f_:
            
            
            f_.write("False")
            
        
        
    else:
        
        
        
        with open(i_file_4_i, "w") as f_:
            
            
            f_.write("True")
            
        
        
        
    
    
    
    return i_v_0_i
    



i_v_0_i = i_main_0_i()


    
    
        
        
        """
        
        
        
        
        
    
    
    
        
        
    
        
        
        i_content_0_i = i_content_of_testing_0_i
        
        
            
            
            
        
        
        
        
        
        
        
        
        i_content_0_i = i_content_0_i.replace("_____i_init_of_variables_1_i_____", i_init_of_variables_0_i)
        
        
        
        
        
        
        
        
        with open(i_file_1_i, "w") as f_:
            
            
            f_.write(i_content_0_i)
            
            
            
            
            
        
        
        
        
        
        
        with open(i_file_4_i, "w") as f_:
            
            
            f_.write("True")
            
            
        
        
        
        
        os.system(f"{sys.executable} {i_file_1_i}")
        
        
        
        
        
        
        
        
        i_content_1_i = ""
        
        
        with open(i_file_4_i, "r") as f_:
            
            
            i_content_1_i = f_.read(os.path.getsize(i_file_4_i))
            
            
        
        
        
        
        
        #print(f"i_content_1_i = {i_content_1_i} .") 
        
        
        
        if (i_content_1_i == "True"):
            
            
            i_var_of_error_compilation_0_i = True
            
            
        elif (i_content_1_i == "False"):
            
            
            i_var_of_error_compilation_0_i = False
            
            
            
        
        
        if (i_var_of_error_compilation_0_i == False):
            
            
            
            
            import i_main_of_test_2_0_i
            
            
            importlib.reload(i_main_of_test_2_0_i)
            
            
            
            
            i_list_of_result_0_i = i_main_of_test_2_0_i.i_main_0_i()
            
            
            
            
            
        
        
    
    
    
    
    
    return [i_var_of_error_compilation_0_i, i_list_of_result_0_i]


    
    
    
    
    
    
    

















if __name__ == "__main__":
    
    
    
    
    
    
    i_string_0_i = "[[[0, 1], [1]], [[[]], [0]], [0, 1, 0], [0], [[]]]"
    
    
    #i_string_0_i = "[]"
    
    
    
    #i_list_0_i = ast.literal_eval(i_string_0_i)
    
    
    
    i_list_0_i = i_from_string_to_list_0_i(i_string_of_list_0_i=i_string_0_i)[1]
    
    
    print(f"\n    i_list_0_i = {i_list_0_i} .\n")
    
    
    
    
    i_string_1_i = "[[[0, 1], [1]], [[[]], [0]], [0, 1, 0, \"1.6\"], [1], [[]], 1, 1.1, \"15\"]"
    
    
    
    
    
    #i_list_1_i = ast.literal_eval(i_string_1_i)
    
    
    i_list_1_i = i_from_string_to_list_0_i(i_string_of_list_0_i=i_string_1_i)[1]
    
    
    print(f"\n    i_list_1_i = {i_list_1_i} .\n")
    
    
    
    
    i_string_2_i = "[[[0, 1], [1]], [[[]], [0]], [0, 1, 0, \"1.6\"], [1], [[]], 1, 1.1, \"15\", 2]"
    
    
    
    i_v_3_i = i_from_string_to_list_0_i(i_string_of_list_0_i=i_string_2_i)
    
    
    
    print(f"\n    i_string_2_i = {i_string_2_i} .\n    i_v_3_i = {i_v_3_i} .\n\n")
    
    
    
    
    
    
    i_v_0_i = i_walk_0_i(i_list_0_i=i_list_0_i, i_rooty_path_0_i="")
    
    
    
    print(f"\n    i_v_0_i = {i_v_0_i} .\n")
    
    
    
    print(f"\n    i_v_0_i[2] = {i_v_0_i[2]} .\n")
    
    
    
    print(f"\n    i_v_0_i[3] = {i_v_0_i[3]} .\n")
    
    
    
    
    
    
    
    i_v_1_i = i_get_list_of_folder_0_i(i_list_0_i=i_list_0_i, i_simbole_of_empty_file_0_i=2)
    
    
    
    
    
    
    print(f"\n    i_v_1_i[1] = {i_v_1_i[1]} .\n")
    
    
    
    print(f"\n    i_v_1_i[2] = {i_v_1_i[2]} .\n")
    
    
    
    print(f"\n    i_v_1_i[3] = {i_v_1_i[3]} .\n")
    
    
    
    
    
    i_v_2_i = i_dupliquor_of_list_1_i(i_list_0_i=i_list_1_i, i_semaphore_of_dupliquation_0_i=True)
    
    
    
    
    
    print(f"\n    i_v_2_i[1] = {i_v_2_i[1]} .\n")
    
    
    
    print(f"\n    i_v_2_i[2] = {i_v_2_i[2]} .\n")
    
    
    
    print(f"\n    i_v_2_i[3] = {i_v_2_i[3]} .\n")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    
    
    Example : 
        
        
        
        i_list_0_i = []
        
        
        i_string_0_i = "[[[0,1],1],[0,1,0]]"
        
        
        i_string_0_i = "[[[0, 1], [1]], [0, 1, 0]]"
        
        
        
        
        
        
        
        
    
    
    
    '''
    
    
    
    
    



















