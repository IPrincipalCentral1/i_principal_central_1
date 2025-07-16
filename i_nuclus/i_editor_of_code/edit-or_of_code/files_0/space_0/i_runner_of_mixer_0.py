











import os

import platform






number_of_element_minus_1 = "_____number_of_element_minus_1_____"

















test_0 = int(number_of_element_minus_1)







def refresher_0():

        
    os.system("python3 refresher_0.py")
    
    
    
    
    list_of_file = []
    
    
    counter_0 = 0
    
    
    while (counter_0 < 1):
    
    
    
        str_number_0 = int_to_str_0(number_0=counter_0)
    
        file_0 = os.path.join(os.getcwd(), "space_for_mix", f"file_part_{str_number_0}.mixer")
    
    
        with open(file_0, "w") as f_:
    
            f_.write("0")
    
        counter_0 += 1
    




def open_popup_terminal(command):
    
    
    system = platform.system()

    if system == "Windows":

        subprocess.run(["cmd", "/c", f"{command}"])

    elif system == "Linux":

        subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command}; exit"])

    elif system == "Darwin":

        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command}; exit"'])











refresher_0()




file_1 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_9.c")


with open(file_1, "r") as f_:

    content = f_.read(os.path.getsize(file_1))




content = content.replace("___number_of_chunk___", "100")



content = content.replace("___postion_of_max_range___", number_of_element_minus_1)



file_2 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_9_0.c")


with open(file_2, "w") as f_:

    f_.write(content)




os.system("gcc Economic_Partner_official_produced_mixer_9_0.c -o E_P_o_p_mixer_9_0")



open_popup_terminal(command="./E_P_o_p_mixer_9_0")

















