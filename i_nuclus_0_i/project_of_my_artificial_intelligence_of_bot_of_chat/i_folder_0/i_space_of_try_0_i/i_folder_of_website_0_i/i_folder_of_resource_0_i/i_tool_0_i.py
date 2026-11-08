




































import os

import traceback

from pathlib import Path

import time




cwd = os.path.dirname(os.path.abspath(__file__))









# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 






i_list_of_expretion_0_i = ["بحث"]












# end_section_of_parameter 

# ---------------------------------------------------------------------------

# end of section of parameter











def i_find_0_i(i_content_0_i, i_list_of_expretion_0_i):
    
    
    i_list_of_result_0_i = []
    
    i_semaphore_of_find_0_i = False
    
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_of_expretion_0_i)):
        
        if (i_list_of_expretion_0_i[i_counter_0_i] != ""):
            
            i_v_0_i = i_content_0_i.split(i_list_of_expretion_0_i[i_counter_0_i])
            
            
            i_list_of_result_0_i.append([len(i_v_0_i) - 1, i_list_of_expretion_0_i[i_counter_0_i]])
            
            
            
            if (len(i_v_0_i) - 1 > 0):
                
                i_semaphore_of_find_0_i = True
                
            
        
        
        
        i_counter_0_i += 1
        
    
    
    
    return [i_list_of_result_0_i, i_semaphore_of_find_0_i]
    
    
    






def i_find_an_expretion_in_a_folder_0_i(i_folder_of_source_0_i, i_list_of_expretion_0_i, i_semaphore_of_print_0_i):
    
    
    
    
    
    
    i_list_of_files_containing_the_expretion_0_i = []
    
    
    
    i_counter_2_i = 0
    
    
    i_t_0_i = time.time() 
    
    
    srcs = [""]
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(srcs)):
    
        
        
        dirs_ = []
        
        
        i_files_0_i = []
        
        
        for root, dirs_, i_files_0_i in os.walk(os.path.join(i_folder_of_source_0_i, srcs[i_counter_0_i])):
    
            break
    
        
    
        i_counter_1_i = 0
    
        while (i_counter_1_i < len(dirs_)):
            
            srcs.append(os.path.join(srcs[i_counter_0_i], dirs_[i_counter_1_i]))
            
            i_counter_1_i += 1
        
        
        
        
        src_ = os.path.join(i_folder_of_source_0_i, srcs[i_counter_0_i])
        
        
    
        i_counter_1_i = 0
    
        while (i_counter_1_i < len(i_files_0_i)):
            
            
            
            try:
                
                
                
                i_file_0_i = os.path.join(src_, i_files_0_i[i_counter_1_i])
                
                
                i_d_0_i = Path(i_file_0_i)
                
                i_content_0_i = i_d_0_i.read_text()
                
                i_v_0_i = i_find_0_i(i_content_0_i=i_content_0_i, i_list_of_expretion_0_i=i_list_of_expretion_0_i)
                
                if (i_v_0_i[1] == True):
                    
                    
                    i_t_1_i = time.time() 
                    
                    i_list_of_files_containing_the_expretion_0_i.append([i_v_0_i[0], i_file_0_i])
                    
                    if (i_semaphore_of_print_0_i == True):
                        
                        print(f"element_( {i_counter_2_i} ) = {i_file_0_i} . time = {i_t_1_i - i_t_0_i} second .")
                        
                    
                    i_counter_2_i += 1
                    
                    
    
            except:
                
                
                
                
                error = traceback.format_exc()
                
                i_semaphore_0_i = True
                
                #print(f"Erreur : {str(error)}")
    
    
    
            
            i_counter_1_i += 1
    
    
        i_counter_0_i += 1
    
    
    i_t_2_i = time.time() 
    
    
    if (i_semaphore_of_print_0_i == True):
        
        print(f"total_time = {i_t_2_i - i_t_0_i} second .")
        
    
    
    
    
    return i_list_of_files_containing_the_expretion_0_i
    
    
    




def i_search_expretion_0_i(i_list_of_expretion_0_i):
    
    
    
    i_folder_to_find_in_0_i = os.path.join(cwd, "templates", "i_space_of_work_0_i")
    
    
    i_folder_to_find_in_1_i = os.path.join(cwd, "static")
    
    
    
    
    
    i_semaphore_of_print_0_i = False
    
    
    
    
    i_v_0_i = i_find_an_expretion_in_a_folder_0_i(i_folder_of_source_0_i=i_folder_to_find_in_0_i, i_list_of_expretion_0_i=i_list_of_expretion_0_i, i_semaphore_of_print_0_i=i_semaphore_of_print_0_i)
    
    
    i_v_0_i.extend(i_find_an_expretion_in_a_folder_0_i(i_folder_of_source_0_i=i_folder_to_find_in_1_i, i_list_of_expretion_0_i=i_list_of_expretion_0_i, i_semaphore_of_print_0_i=i_semaphore_of_print_0_i))
    
    
    #print(f"i_v_0_i = {i_v_0_i} .")
    
    return i_v_0_i
    


if __name__ == "__main__":
    
    
    i_search_expretion_0_i()
    
    

























'''


file:///F:/i_/i_directory/new_0/i_folder_8_i/i_space_of_work_0_i/space_for_the_project/project_of_my_artificial_intelligence_of_bot_of_chat/i_folder_0/i_space_of_try_0_i/i_folder_of_website_0_i/i_folder_of_resource_0_i/templates/i_research_0_i.html

'''










