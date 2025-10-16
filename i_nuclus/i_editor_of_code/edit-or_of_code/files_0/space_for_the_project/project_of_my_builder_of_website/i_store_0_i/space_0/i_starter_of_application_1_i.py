












import os

import threading

import time

import importlib.util



cwd = os.path.dirname(os.path.abspath(__file__))





i_file_of_transmission_0_i = os.path.join(cwd, "i_transmission_0_i.txt")



i_encoding_0_i = "utf-8"


i_list_of_program_0_i = []


def load_module(path):

    """تحميل الملف كـ module"""

    spec = importlib.util.spec_from_file_location("file_selected", path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module



def i_runner_of_thread_0_i(module, flag_list, idx):
    

    """يشغل main داخل Thread ويراقب flag"""

    i_p_0_i = threading.Thread(target=module.main, daemon=True).start()

    
    i_run_0_i = flag_list[idx][1]
    
    
    while (i_run_0_i == True):
        
        
        i_run_0_i = flag_list[idx][1]
        
    




def i_main_0_i():
    
    
    
    
    i_content_0_i = ""
    
    i_run_1_i = True
    
    
    while (i_run_1_i == True):
        
        
        
        with open(i_file_of_transmission_0_i, "r", encoding=i_encoding_0_i) as f_:
            
            
            i_content_0_i = f_.read(os.path.getsize(i_file_of_transmission_0_i))
            
            
            
        
        print(f"i_hello_4_i . i_content_0_i = \"{i_content_0_i}\" .")
        
        if (i_content_0_i == "Stop"):
            
            
            print(f"i_hello_3_i .")
            
            i_run_1_i = False
            
            
            
        elif (i_content_0_i != ""):
            
            
            print(f"i_hello_0_i .")
            
            i_v_0_i = i_content_0_i.split(";")
            
            if (i_v_0_i[1] == "True"):
                
                
                
                i_counter_0_i = 0
                
                while ((i_counter_0_i < len(i_list_of_program_0_i)) and (i_list_of_program_0_i[i_counter_0_i][1] != i_v_0_i[0])):
                    
                    
                    i_counter_0_i += 1
                    
                    
                    
                    
                
                
                if (i_counter_0_i >= len(i_list_of_program_0_i)):
                        
                    
                    i_list_of_program_0_i.append([i_v_0_i[0], True])
                    
                     
                
                
                print(f"i_hello_1_i .")
                
                module = load_module(path=i_v_0_i[0])
                
                
                i_p_0_i = threading.Thread(target=i_runner_of_thread_0_i, args=(module, i_list_of_program_0_i, i_counter_0_i, ), daemon=True).start()
                
            
            elif (i_v_0_i[1] == "False"):
                
                
                i_counter_0_i = 0
                
                while ((i_counter_0_i < len(i_list_of_program_0_i)) and (i_list_of_program_0_i[i_counter_0_i][0] != i_v_0_i[0])):
                    
                    
                    i_counter_0_i += 1
                    
                    
                    
                    
                
                
                if (i_counter_0_i < len(i_list_of_program_0_i)):
                    
                    i_list_of_program_0_i[i_counter_0_i][1] = False
                    
                    
                    
                print(f"i_hello_2_i .")
                
                
                
            
            
            
        # wait 
        
        time.sleep(2)
        
        
        with open(i_file_of_transmission_0_i, "w", encoding=i_encoding_0_i) as f_:
            
            f_.write("")
            
        
        
        
        
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    







