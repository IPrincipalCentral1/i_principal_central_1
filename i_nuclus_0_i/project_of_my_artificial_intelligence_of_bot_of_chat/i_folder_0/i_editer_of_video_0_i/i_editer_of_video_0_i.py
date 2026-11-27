


















list_of_liberary_to_install = [
                            
                            

]










import os


import traceback

import sys


import subprocess





print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])




try:

    counter_0 = 0


    while (counter_0 < len(list_of_liberary_to_install)):



        try:


            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")

            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", f"{list_of_liberary_to_install[counter_0][0]}"])



        except:



            traceback.print_exc()

            error = traceback.format_exc()

            semaphore = True

            print(f"Erreur : {str(error)}")



        counter_0 += 1



except:



    traceback.print_exc()

    error = traceback.format_exc()

    semaphore = True

    print(f"Erreur : {str(error)}")




print("\n" * 10)







class i_editer_of_video_0_i():
    
    def i_get_list_of_description_0_i(self):
        
        
        i_list_of_result_0_i = []
        
        
        i_functions_0_i = self.i_get_all_functions_0_i()
        
        
        for i_name_0_i, i_function_0_i in i_functions_0_i:
            
            print(f"i_name_0_i = {i_name_0_i} .")
            
            
            i_code_source_0_i = inspect.getsource(i_function_0_i)
            
            
            print(f"i_code_source_0_i = \n{i_code_source_0_i} .")
            
            
            
            i_line_0_i = inspect.getsourcelines(i_function_0_i)[1]
            
            
            print(f"i_line_0_i = {i_line_0_i} .")
            
            
            
            i_list_of_result_0_i.append([i_name_0_i, i_code_source_0_i, i_line_0_i])
            
            
        
        
        return i_list_of_result_0_i
        
    
    
    def i_get_all_functions_0_i(self):
        
        
        i_functions_0_i = inspect.getmembers(
                    
                    self.__class__,
                    
                    predicate=inspect.isfunction
                    
                )
                
                
        
        return i_functions_0_i 
         





import inspect

class i_test_0_i:
    def i_sum_0_i(self, a, b):
        return a + b

    def i_sub_0_i(self, a, b):
        return a - b

    def i_print_0_i(self):
        print("Hello")
    
    
    def i_function_0_i(self):
        
        
        i_functions_0_i = inspect.getmembers(
                    self.__class__,
                    predicate=inspect.isfunction
                )
        
        return i_functions_0_i 
        
    
    

'''

i_functions_0_i = inspect.getmembers(
    i_test_0_i,
    predicate=inspect.isfunction
)

'''

i_v_0_i = i_test_0_i()

i_functions_0_i = i_v_0_i.i_function_0_i() 


for i_name_0_i, i_function_0_i in i_functions_0_i:
    
    print(f"i_name_0_i = {i_name_0_i} .")
    
    
    i_code_source_0_i = inspect.getsource(i_function_0_i)
    
    
    print(f"i_code_source_0_i = \n{i_code_source_0_i} .")
    
    
    
    i_line_0_i = inspect.getsourcelines(i_function_0_i)[1]
    
    
    print(f"i_line_0_i = {i_line_0_i} .")
    
    
    
    
    
    
    
    
    









