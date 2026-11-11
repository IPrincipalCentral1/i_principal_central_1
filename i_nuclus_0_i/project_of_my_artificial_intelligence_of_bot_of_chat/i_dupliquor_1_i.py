























import os    

from pathlib import Path

import traceback

import sys









# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 









i_source_1_i = r"_____i_source_1_i_____"



i_duplication_place_0_i = r"_____i_duplication_place_0_i_____"



i_semaphore_of_dupliquating_0_i = _____i_semaphore_of_dupliquating_0_i_____









# end_section_of_parameter 

# ---------------------------------------------------------------------------

# end of section of parameter














def i_dupliquor_0_i(i_source_1_i, i_duplication_place_0_i, i_semaphore_of_dupliquating_0_i):
    
    
    
    
    
    i_list_of_all_files_0_i = []
    
    
    i_list_of_all_folders_0_i = []
    
    
    i_list_of_errors_0_i = []
    
    
    
    if (os.path.isfile(i_source_1_i) == True):
    
                
        
        
        try:
            
            
            
            i_list_of_all_files_0_i.extend([i_source_1_i])
            
            
            if (i_semaphore_of_dupliquating_0_i == True):
                    
                
                d = Path(i_source_1_i)
                
                d_ = Path(i_duplication_place_0_i)
                
                
                d_.write_bytes(d.read_bytes())
                
                
            
        except:
            
            
            
            traceback.print_exc()
            
            i_error_0_i = traceback.format_exc()
            
            i_semaphore_of_error_0_i = True
            
            #print(f"Erreur : {str(i_error_0_i)}")
            
            i_list_of_errors_0_i.append(str(i_error_0_i))
            
            
            
        
        
    else:
        
        
        
        i_dirs_0_i = [""]
        
        i_sources_0_i = [""]
        
        
        
        
        i_counter_1_i = 0
        
        while (i_counter_1_i < len(i_dirs_0_i)):
            
            
            try:
                
                
                i_files_0_i = []
                
                
                i_dirs_1_i = []
            
            
                for i_root_0_i, i_dirs_1_i, i_files_0_i in os.walk(os.path.join(i_source_1_i, i_dirs_0_i[i_counter_1_i])):
            
                    break
            
        
            
                i_counter_0_i = 0
            
                while (i_counter_0_i < len(i_dirs_1_i)):
                    
                    i_dirs_0_i.append(os.path.join(i_dirs_0_i[i_counter_1_i], i_dirs_1_i[i_counter_0_i]))
                    
                    i_sources_0_i.append(os.path.join(i_sources_0_i[i_counter_1_i], i_dirs_1_i[i_counter_0_i]))
                    
                    i_counter_0_i += 1
                    
                
                
                
                    
                i_source_2_i = os.path.join(i_source_1_i, i_sources_0_i[i_counter_1_i])
                
                i_source_3_i = os.path.join(i_sources_0_i[i_counter_1_i])
                
                i_distination_0_i = os.path.join(i_duplication_place_0_i, i_dirs_0_i[i_counter_1_i])
                
                
                if (i_semaphore_of_dupliquating_0_i == True):
                    
                    
                    if (not (os.path.exists(i_distination_0_i))):
                        
                        os.makedirs(i_distination_0_i, exist_ok=True)
                        
                    
                    
                    
                
                
                
                i_counter_0_i = 0
                
                while (i_counter_0_i < len(i_files_0_i)):
                    
                    
                    
                    
                    try:
                        
                        
                        
                        i_list_of_all_files_0_i.append(os.path.join(i_source_3_i, i_files_0_i[i_counter_0_i]))
                        
                        
                        
                        
                        
                        if (i_semaphore_of_dupliquating_0_i == True):
                                
                            
                            d = Path(os.path.join(i_source_2_i, i_files_0_i[i_counter_0_i]))
                            
                            d_ = Path(os.path.join(i_distination_0_i, i_files_0_i[i_counter_0_i]))
                            
                            
                            
                            d_.write_bytes(d.read_bytes())
                            
                            
                        
                        
                            
                    except:
                        
                        
                        
                        traceback.print_exc()
                        
                        i_error_0_i = traceback.format_exc()
                        
                        i_semaphore_of_error_0_i = True
                        
                        #print(f"Erreur : {str(i_error_0_i)}")
                        
                        i_list_of_errors_0_i.append(str(i_error_0_i))
                        
                        
                        
                    
                    
                    
                    
                    i_counter_0_i += 1
                
                
                
            except:
                
                
                
                
                
                traceback.print_exc()
                
                i_error_0_i = traceback.format_exc()
                
                i_semaphore_of_error_0_i = True
                
                #print(f"Erreur : {str(i_error_0_i)}")
                
                i_list_of_errors_0_i.append(str(i_error_0_i))
                
                
                
                
                
            
            
            
            i_counter_1_i += 1
            
            
            
            
        
        
        
    
    
    i_sources_0_i.pop(0)
    
    
    i_list_of_all_folders_0_i = i_sources_0_i
    
    
    return [i_source_1_i, i_list_of_all_folders_0_i, i_list_of_all_files_0_i, i_list_of_errors_0_i]
    
    















def i_deleter_0_i(i_source_of_delete_1_i, i_semaphore_of_delete_folder_source_0_i):
    
    
    
    
    
    i_semaphore_of_error_0_i = False
    
    
    
    i_list_of_errors_0_i = []
    
    
    
    
    try:
        
        
        i_v_0_i = i_dupliquor_0_i(i_source_1_i=i_source_of_delete_1_i, i_duplication_place_0_i="", i_semaphore_of_dupliquating_0_i=False)
        
        
        
        
        i_v_1_i = i_v_0_i[2]
        
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_v_1_i)):
            
            
            
            try:
                
                os.remove(os.path.join(i_source_of_delete_1_i, i_v_1_i[i_counter_0_i]))
                
            except:
                
                
                
                
                traceback.print_exc()
                
                i_error_0_i = traceback.format_exc()
                
                i_semaphore_of_error_0_i = True
                
                #print(f"Erreur : {str(i_error_0_i)}")
                
                i_list_of_errors_0_i.append(str(i_error_0_i))
                
                
                
            
            
            
            
            i_counter_0_i += 1
            
        
        
        
        i_v_1_i = i_v_0_i[1]
        
        
        i_counter_0_i = len(i_v_1_i) - 1
        
        while (i_counter_0_i >= 0):
            
            
            try:
                
                os.rmdir(os.path.join(i_source_of_delete_1_i, i_v_1_i[i_counter_0_i]))
                
                
            except:
                
                
                
                
                traceback.print_exc()
                
                i_error_0_i = traceback.format_exc()
                
                i_semaphore_of_error_0_i = True
                
                #print(f"Erreur : {str(i_error_0_i)}")
                
                i_list_of_errors_0_i.append(str(i_error_0_i))
                
                
            
            
            
            i_counter_0_i -= 1
            
        
        
        
        if (i_semaphore_of_delete_folder_source_0_i == True):
            
            
            
            try:
                
                os.rmdir(i_source_of_delete_1_i)
                
                
            except:
                
                
                
                
                
                traceback.print_exc()
                
                i_error_0_i = traceback.format_exc()
                
                i_semaphore_of_error_0_i = True
                
                #print(f"Erreur : {str(i_error_0_i)}")
                
                i_list_of_errors_0_i.append(str(i_error_0_i))
                
                
        
        
        
        
        
    except:
        
        
        
        
        traceback.print_exc()
        
        i_error_0_i = traceback.format_exc()
        
        i_semaphore_of_error_0_i = True
        
        #print(f"Erreur : {str(i_error_0_i)}")
        
        i_list_of_errors_0_i.append(str(i_error_0_i))
        
        
        
        
    
    
    
    return [i_semaphore_of_error_0_i, i_list_of_errors_0_i]
    
    






if __name__ == "__main__":
    
    
    
    
    i_v_0_i = i_dupliquor_0_i(i_source_1_i=i_source_1_i, i_duplication_place_0_i=i_duplication_place_0_i, i_semaphore_of_dupliquating_0_i=i_semaphore_of_dupliquating_0_i)
    
    
    print(f"i_v_0_i = {i_v_0_i} .")
    
    
    
    
    
    
    
       












