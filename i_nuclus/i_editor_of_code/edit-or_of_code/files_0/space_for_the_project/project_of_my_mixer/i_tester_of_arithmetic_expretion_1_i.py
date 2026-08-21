
















'''




you should put the list of all your variables here :
    
    
    i_list_of_variables_0_i
    
    
    
and than you should put your expretion here :
    
    
    i_operation_0_i
    
    
    



you should make the variables in between 2 spaces :
    
    
    i_list_of_variables_0_i = [" i_v_0_i ", " i_v_1_i ", " i_v_2_i "]
    
    
    



the arithmetic expretion use just :
    
    
    [" + ", " - ", " * ", " / ", " // ", " ** ", " % " , " if ", " else ", " == ", " >= ", " <= ", " > ", " < ", " != ", " ( ", " ) "]
    
    
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    
    
    add your operators and put it between 2 spaces
    
    
    and your variables
    




when you use it after the mix . you should include this range of mix in the mixer before :
    
    
    
    
    [" + ", " - ", " * ", " / ", " // ", " ** ", " % " , " if ", " else ", " == ", " >= ", " <= ", " > ", " < ", " != ", " ( ", " ) "]
    
    
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    
    
    add your operators and put it between 2 spaces
    
    
    and your variables
    


    
    







'''




















import ast


import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))







# start section of parameter 

# ------------------------------------------------------------------------------

# start_section_of_parameter 







i_list_of_variables_0_i = ______i_list_of_variables_0_i______






i_operation_0_i = ______i_operation_0_i______




i_content_of_import_0_i = r"""


__________i_content_of_import_0_i__________




"""




i_init_of_variables_0_i = r"""



__________i_init_of_variables_0_i__________



"""







# end_section_of_parameter 

# -----------------------------------------------------------------------------

# end section of parameter 







i_file_0_i = os.path.join(cwd, "i_main_of_test_2_i.py")


i_file_1_i = os.path.join(cwd, "i_main_of_test_2_0_i.py")


i_file_4_i = os.path.join(cwd, "i_file_of_semaphore_of_error_compilation_0_i.txt")




i_content_of_testing_0_i = r"""













_____i_section_of_import_0_i_____






import os



cwd = os.path.dirname(os.path.abspath(__file__))







i_var_of_result_0_i = False






_____i_variables_0_i_____




_____i_init_of_variables_1_i_____





if ((_____i_expretion_0_i_____) >= 10):
    
    
    
    i_var_of_result_0_i = True
    
    
else:
    
    
    
    
    i_var_of_result_0_i = True
    
    
    



i_file_4_i = os.path.join(cwd, "i_file_of_semaphore_of_error_compilation_0_i.txt")





with open(i_file_4_i, "w") as f_:
    
    
    f_.write("False")
    









"""











def i_main_0_i():
    
    
    
    
    i_content_0_i = i_content_of_testing_0_i
    
    
        
        
        
    
    
    
    
    
    
    
    i_content_of_variables_0_i = "\n\n"
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < len(i_list_of_variables_0_i)):
        
        
        
        
        i_var_0_i = i_list_of_variables_0_i[i_counter_0_i]
        
        
        i_counter_1_i = 0
        
        
        while ((i_counter_1_i < len(i_var_0_i)) and (i_var_0_i[i_counter_1_i] == " ")):
            
            
            i_counter_1_i += 1
            
            
            
        
        i_var_0_i = i_var_0_i[i_counter_1_i:]
        
        
        i_content_of_variables_0_i += i_var_0_i + " = 1\n\n"
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
    
    
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_section_of_import_0_i_____", i_content_of_import_0_i)
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_variables_0_i_____", i_content_of_variables_0_i)
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_expretion_0_i_____", i_operation_0_i)
    
    
    
    
    
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
        
        
        
    
    
    
    
    return i_var_of_error_compilation_0_i










if __name__ == "__main__":
    
    
    
    
    i_var_of_error_compilation_0_i = i_main_0_i()
    
    
    print(f"i_var_of_error_compilation_0_i = {i_var_of_error_compilation_0_i}")
    
    
    


















