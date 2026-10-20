



















'''


i am i .

this file will find an expretion inside any file in a folder .






'''






import os

import traceback

from pathlib import Path

import time




cwd = os.path.dirname(os.path.abspath(__file__))









# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 






i_expretion_0_i = r""





i_folder_to_find_in_0_i = r""





i_semaphore_of_print_0_i = True










# end_section_of_parameter 

# ---------------------------------------------------------------------------

# end of section of parameter













def i_find_an_expretion_in_a_folder_0_i(i_folder_of_source_0_i, i_expretion_0_i):
    
    
    
    
    
    
    i_list_of_files_containing_the_expretion_0_i = []
    
    
    
    i_counter_2_i = 0
    
    
    i_t_0_i = time.time() 
    
    
    srcs = [""]
    
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(srcs)):
    
        for root, dirs_, i_files_0_i in os.walk(os.path.join(i_folder_of_source_0_i, srcs[i_counter_0])):
    
            break
    
    
    
        i_counter_1 = 0
    
        while (i_counter_1 < len(dirs_)):
            
            srcs.append(os.path.join(srcs[i_counter_0], dirs_[i_counter_1]))
            
            i_counter_1 += 1
        
        
        
        
        src_ = os.path.join(i_folder_of_source_0_i, srcs[i_counter_0])
        
        
    
        i_counter_1 = 0
    
        while (i_counter_1 < len(i_files_0_i)):
            
            
            
            try:
                
                
                
                i_file_0_i = os.path.join(src_, i_files_0_i[i_counter_1])
                
                
                i_d_0_i = Path(i_file_0_i)
                
                i_content_0_i = i_d_0_i.read_text()
                
                i_v_0_i = i_content_0_i.split(i_expretion_0_i)
                
                if (len(i_v_0_i) > 1):
                    
                    
                    i_t_1_i = time.time() 
                    
                    i_list_of_files_containing_the_expretion_0_i.append(i_file_0_i)
                    
                    if (i_semaphore_of_print_0_i == True):
                        
                        print(f"element_( {i_counter_2_i} ) = {i_file_0_i} . time = {i_t_1_i - i_t_0_i} second .")
                        
                    
                    i_counter_2_i += 1
                    
                    
    
            except:
                
                
                
                
                error = traceback.format_exc()
                
                i_semaphore_0_i = True
                
                #print(f"Erreur : {str(error)}")
    
    
    
            
            i_counter_1 += 1
    
    
        i_counter_0 += 1
    
    
    i_t_2_i = time.time() 
    
    
    if (i_semaphore_of_print_0_i == True):
        
        print(f"total_time = {i_t_2_i - i_t_0_i} second .")
        
    
    
    
    
    return i_list_of_files_containing_the_expretion_0_i
    
    
    




def i_main_0_i():
    
    
    i_list_of_files_containing_the_expretion_0_i = i_find_an_expretion_in_a_folder_0_i(i_folder_of_source_0_i=i_folder_to_find_in_0_i, i_expretion_0_i=i_expretion_0_i)
    
    
    


if __name__ == "__main__":
    
    
    i_main_0_i()
    
    























