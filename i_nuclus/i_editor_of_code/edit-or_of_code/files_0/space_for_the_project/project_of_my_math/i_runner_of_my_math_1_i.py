











































































































import sys

import os

import platform

import subprocess






cwd = os.path.dirname(os.path.abspath(__file__))







# start section of parametter :

# ------------------------------------------------------------------





number_of_digit_after_the_floating_point = _____number_of_digit_after_the_floating_point_____



latest_type_of_int = "_____latest_type_of_int_____"



number_of_bit_max_of_the_processor = _____number_of_bit_max_of_the_processor____






# end section of parametter :

# ------------------------------------------------------------------











i_file_of_a_0_i = os.path.join(cwd, "i_space_of_calcul_0_i", "i_file_of_a_0_i.txt")

i_file_of_b_0_i = os.path.join(cwd, "i_space_of_calcul_0_i", "i_file_of_b_0_i.txt")




def i_get_the_length_of_1_complete_number_of_your_int_0_i(i_number_of_bit_0_i):
    
    
    
    
    
    i_limit_0_i = ( ( 2 ** ( i_number_of_bit_0_i - 1 ) ) - 1 )
    
    
    i_q_0_i = 1
    
    i_counter_0_i = 0
    
    while (i_q_0_i < i_limit_0_i):
        
        
        i_q_0_i *= 10
        
        i_counter_0_i += 1
        
    
    
    
    if (i_q_0_i > i_limit_0_i):
        
        i_counter_0_i -= 1
        
    
    if (i_counter_0_i % 2 == 1):
        
        
        i_counter_0_i -= 1
        
    
    
    
    return i_counter_0_i
    






def refresher_0():
    
        
    os.system(f"{sys.executable} refresher_0.py")
    





def open_popup_terminal(command):
    
    
    system = platform.system()

    if system == "Windows":

        subprocess.run(["cmd", "/c", f"{command}"])

    elif system == "Linux":

        subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command}; exit"])

    elif system == "Darwin":

        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command}; exit"'])







def i_max_0_i(i_v_a_0, i_v_b_0):
    
    
    if (i_v_a_0 > i_v_b_0):
        
        return i_v_a_0
        
    else:
        
        return i_v_b_0
        
        
        
    
    
    
    
    




def i_main_0_i():    


        
    i_v_0_i = i_get_the_length_of_1_complete_number_of_your_int_0_i(i_number_of_bit_0_i=number_of_bit_max_of_the_processor)
    
    the_length_of_1_complete_number_of_your_int = str(i_v_0_i)
    



    i_length_of_a_0_i = 0
    
    
    i_length_of_b_0_i = 0
    
    
    with open(i_file_of_a_0_i, "r") as f_:
        
        
        i_length_of_a_0_i = len(f_.read(os.path.getsize(i_file_of_a_0_i)))
        
        
    
    with open(i_file_of_b_0_i, "r") as f_:
        
        
        i_length_of_b_0_i = len(f_.read(os.path.getsize(i_file_of_b_0_i)))
        
        
        
    
    
    
    i_macro_of_maximum_length_of_the_content_of_the_files_1_i = i_max_0_i(i_v_a_0=i_length_of_a_0_i, i_v_b_0=i_length_of_b_0_i) * 2
    
    
    
    i_length_of_the_numbers_0_i = (( ( i_macro_of_maximum_length_of_the_content_of_the_files_1_i + number_of_digit_after_the_floating_point ) // ( i_v_0_i ) ) + 2)
    
    
    
    
    number_of_chunk_0 = str(i_length_of_the_numbers_0_i)
    
    
    
    print(f"i_hello_0_i . number_of_chunk_0 = {number_of_chunk_0} .")
    
    
    
    file_1 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_11.c")
    

    with open(file_1, "r") as f_:

        content = f_.read(os.path.getsize(file_1))




    content = content.replace("___number_of_chunk___", number_of_chunk_0)



    content = content.replace("___postion_of_max_range___", "1")
    
    
            
    content = content.replace("int64_t", latest_type_of_int)
    
    
    
    content = content.replace("#define i_Number_of_digits_max 18", f"#define i_Number_of_digits_max {the_length_of_1_complete_number_of_your_int}")
    
    
    
    content = content.replace("#define i_macro_of_number_of_digite_maximum_after_the_floating_point 0", f"#define i_macro_of_number_of_digite_maximum_after_the_floating_point {number_of_digit_after_the_floating_point}")
    
    
    
    
    content = content.replace("_____i_macro_of_length_of_char_pointer_1_i_____", f"{i_macro_of_maximum_length_of_the_content_of_the_files_1_i}")
    
    
    


    file_2 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_11_0.c")


    with open(file_2, "w") as f_:

        f_.write(content)
    
    

    
    
    os.chdir(cwd)
    
    
    
    os.system("gcc Economic_Partner_official_produced_mixer_11_0.c -o E_P_o_p_mixer_11_0")
    
    

    os.system("./E_P_o_p_mixer_11_0")
    





if __name__ == "__main__":
    
    
    i_main_0_i()
    
    
    
    













