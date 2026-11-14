





























































































































import os

import importlib




cwd = os.path.dirname(os.path.abspath(__file__))




i_file_of_runner_of_mixer_0_i = os.path.join(cwd, "i_runner_of_mixer_0.py")



i_file_of_runner_of_mixer_0_0_i = os.path.join(cwd, "i_runner_of_mixer_0_0_i.py")



i_file_of_get_list_of_dimenssion_0_i = os.path.join(cwd, "i_get_list_of_dimenssion_0_i.py")



i_file_of_get_list_of_dimenssion_0_0_i = os.path.join(cwd, "i_get_list_of_dimenssion_0_0_i.py")




'''





number_of_element_minus_1 = "_____number_of_element_minus_1_____"



latest_type_of_int = "_____latest_type_of_int_____"



number_of_bit_max_of_the_processor = _____number_of_bit_max_of_the_processor_____




'''



def i_main_0_i():
    
    
    
    
    
    i_content_of_runner_of_mixer_0_i = ""
    
    with open(i_file_of_runner_of_mixer_0_i, "r") as f_:
        
        
        i_content_of_runner_of_mixer_0_i = f_.read(os.path.getsize(i_file_of_runner_of_mixer_0_i))
        
        
    
    
    
    
    i_content_of_runner_of_mixer_0_i = i_content_of_runner_of_mixer_0_i.replace("_____number_of_element_minus_1_____", "2")
    
    
    i_content_of_runner_of_mixer_0_i = i_content_of_runner_of_mixer_0_i.replace("_____latest_type_of_int_____", "int64_t")
    
    
    i_content_of_runner_of_mixer_0_i = i_content_of_runner_of_mixer_0_i.replace("_____number_of_bit_max_of_the_processor_____", "64")
    
    
    
    i_content_of_runner_of_mixer_0_0_i = i_content_of_runner_of_mixer_0_i
    
    
    with open(i_file_of_runner_of_mixer_0_0_i, "w") as f_:
        
        
        f_.write(i_content_of_runner_of_mixer_0_0_i)
        
        
        
    
    
    
    
        
    import i_runner_of_mixer_0_0_i
    
    importlib.reload(i_runner_of_mixer_0_0_i)
    
    
    
    i_runner_of_mixer_0_0_i.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    
    
    
    
    i_main_0_i()
    
    
    






















