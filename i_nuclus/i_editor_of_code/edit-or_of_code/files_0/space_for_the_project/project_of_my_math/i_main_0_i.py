











































































































import sys

import os

import platform

import subprocess






cwd = os.path.dirname(os.path.abspath(__file__))







# start section of parametter :

# ------------------------------------------------------------------





number_of_chunk_0 = "10"




latest_type_of_int = "int64_t"


number_of_bit = 64


the_length_of_1_complete_number_of_your_int = "18"






# end section of parametter :

# ------------------------------------------------------------------






i_v_0_i = i_get_the_length_of_1_complete_number_of_your_int_0_i(i_number_of_bit_0_i=number_of_bit)


print(f"i_v_0_i = {i_v_0_i} .")





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









def i_main_0_i(argv_1):



    if (argv_1 == "init"):

        refresher_0()




    file_1 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_11.c")


    with open(file_1, "r") as f_:

        content = f_.read(os.path.getsize(file_1))




    content = content.replace("___number_of_chunk___", number_of_chunk_0)



    content = content.replace("___postion_of_max_range___", "1")
    
    
            
    content = content.replace("int64_t", latest_type_of_int)
    
    
    
    content = content.replace("#define i_Number_of_digits_max 18", f"#define i_Number_of_digits_max {the_length_of_1_complete_number_of_your_int}")
    
    


    file_2 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_11_0.c")


    with open(file_2, "w") as f_:

        f_.write(content)




    os.system("gcc Economic_Partner_official_produced_mixer_11_0.c -o E_P_o_p_mixer_11_0")


    os.system("./E_P_o_p_mixer_11_0")
    

    #open_popup_terminal(command="./E_P_o_p_mixer_11_0")





if __name__ == "__main__":
    
    
    i_main_0_i(argv_1="init")
    
    
    
    









