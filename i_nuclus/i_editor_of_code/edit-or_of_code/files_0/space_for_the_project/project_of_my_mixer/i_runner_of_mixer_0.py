












'''




this is a program to run a new project with my mixer . 

you sould replace _____number_of_element_minus_1_____ by (number_of_element - 1) .

and than run the program .


when you insert 'true' at this file i_run_mixer_2.txt my mixer will stop .


when you insert 'true' at this file i_run_mixer_1.txt my mixer will make the next step .






if you want to initialize the mixer to certain stat . for example :
    
    file_000000000000000000.txt ==> 10
    
    file_000000000000000001.txt ==> 0
    
    file_000000000000000002.txt ==> 3
    
    


you should put those files into the same folder and let there containt like what you want and do this :


    initialize_0 = True


so the mixer will not start from the beginning . but will start from the current stat .

and if there is a mistake in the files . it will start from the beginning .


if you do not want to initialize my mixer you should do this :


    initialize_0 = False





now you should put latest type of int . for example :


    latest_type_of_int = "int64_t"



and the length of the latest number with [ my 10 ] ( 10 ** n ) . for example : 


    the_length_of_1_complete_number_of_your_int = "18"


because int64_t <==> ( 2 ** 64 ) > 10 ** 18 .

the biggest number that can be gotten from 10 to the power is : 10 ** 18 .


this 18 you should put it on here the_length_of_1_complete_number_of_your_int .



( 2 ** ( 64 - 1 ) ) ==  9 223 372 036 854 775 808

( 10 ** 18 )        ==  1 000 000 000 000 000 000


you should do the number that are with : 10 ** n . but he is less then : 2 ** 64 .


i am speaking about 64 because i have a computer with 64 bit in the processor . 




'''

















import os

import platform

import subprocess





cwd = os.path.dirname(os.path.abspath(__file__))




number_of_element_minus_1 = "_____number_of_element_minus_1_____"



latest_type_of_int = "_____latest_type_of_int_____"



the_length_of_1_complete_number_of_your_int = "_____the_length_of_1_complete_number_of_your_int_____"




initialize_0 = False











test_0 = int(number_of_element_minus_1)


number_of_chunk_0 = str(int(( len(number_of_element_minus_1) // (10 ** 18) ) + 2))






def main():
    
    
    
    
    
    def refresher_0():
        
            
        os.system("python3 refresher_0.py")
        
        
        
    
    
    
    
    def open_popup_terminal(command):
        
        
        system = platform.system()
    
        if system == "Windows":
    
            subprocess.run(["cmd", "/c", f"{command}"])
    
        elif system == "Linux":
    
            subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command}; exit"])
    
        elif system == "Darwin":
    
            subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command}; exit"'])
    
    
    
    
    
    
    
    
    
    if (initialize_0 == False):
        
        refresher_0()
        
    
    
    
    file_1 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_9.c")
    
    
    with open(file_1, "r") as f_:
    
        content = f_.read(os.path.getsize(file_1))
    
    
    
    
    content = content.replace("___number_of_chunk___", number_of_chunk_0)
    
    
    
    content = content.replace("___postion_of_max_range___", number_of_element_minus_1)
    
    
    
    content = content.replace("int64_t", latest_type_of_int)
    
    
    
    content = content.replace("#define i_Number_of_digits_max 18", f"#define i_Number_of_digits_max {the_length_of_1_complete_number_of_your_int}")
    
    
    
    file_2 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_9_0.c")
    
    
    with open(file_2, "w") as f_:
    
        f_.write(content)
    
    
    
    
    os.system("gcc Economic_Partner_official_produced_mixer_9_0.c -o E_P_o_p_mixer_9_0")
    
    
    
    open_popup_terminal(command="./E_P_o_p_mixer_9_0")
    
    
    
    
    
    



    
if __name__ == "__main__":
    
    
    
    main()
    
    
    











