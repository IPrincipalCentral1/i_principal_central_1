












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


because int64_t <==> ( 2 ** ( 64 - 1 ) ) > 10 ** 18 .

the biggest number that can be gotten from 10 to the power is : 10 ** 18 .


this 18 you should put it on here the_length_of_1_complete_number_of_your_int .



( 2 ** ( 64 - 1 ) ) ==  9 223 372 036 854 775 808

( 10 ** 18 )        ==  1 000 000 000 000 000 000


you should do the number that are with : 10 ** n . but he is less then : 2 ** ( 64 - 1 ) .


i am speaking about 64 because i have a computer with 64 bit in the processor . 

the reason that i am making ( 64 - 1 ) and not ( 64 ) is that i am using the singed int and not the unsinged int . for example :
    
    'int64_t' and not 'uint64_t'
    
    
    





this is my 10 : 

{

0 : 1 - 1

1 : 1

2 : 1 + 1

3 : 1 + 1 + 1

4 : 1 + 1 + 1 + 1

5 : 1 + 1 + 1 + 1 + 1

6 : 1 + 1 + 1 + 1 + 1 + 1

7 : 1 + 1 + 1 + 1 + 1 + 1 + 1

8 : 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

9 : 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

10 : 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

}


and i build my mixer with this 10 .



now i will count from 0 to 100 with the incrementer 1 :

{

-100 , -99 , -98 , -97 , -96 , -95 , -94 , -93 , -92 , -91 , -90 , -89 , -88 , -87 , -86 , -85 , -84 , -83 , -82 , -81 , -80 , -79 , -78 , -77 , -76 , -75 , -74 , -73 , -72 , -71 , -70 , -69 , -68 , -67 , -66 , -65 , -64 , -63 , -62 , -61 , -60 , -59 , -58 , -57 , -56 , -55 , -54 , -53 , -52 , -51 , -50 , -49 , -48 , -47 , -46 , -45 , -44 , -43 , -42 , -41 , -40 , -39 , -38 , -37 , -36 , -35 , -34 , -33 , -32 , -31 , -30 , -29 , -28 , -27 , -26 , -25 , -24 , -23 , -22 , -21 , -20 , -19 , -18 , -17 , -16 , -15 , -14 , -13 , -12 , -11 , -10 , -9 , -8 , -7 , -6 , -5 , -4 , -3 , -2 , -1 , 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 , 28 , 29 , 30 , 31 , 32 , 33 , 34 , 35 , 36 , 37 , 38 , 39 , 40 , 41 , 42 , 43 , 44 , 45 , 46 , 47 , 48 , 49 , 50 , 51 , 52 , 53 , 54 , 55 , 56 , 57 , 58 , 59 , 60 , 61 , 62 , 63 , 64 , 65 , 66 , 67 , 68 , 69 , 70 , 71 , 72 , 73 , 74 , 75 , 76 , 77 , 78 , 79 , 80 , 81 , 82 , 83 , 84 , 85 , 86 , 87 , 88 , 89 , 90 , 91 , 92 , 93 , 94 , 95 , 96 , 97 , 98 , 99 , 100 , 

}



now i will count from 0 to 100 with the incrementer 0.1 :

{



}






'''

















import os

import platform

import subprocess







number_of_element_minus_1 = "_____number_of_element_minus_1_____"



latest_type_of_int = "_____latest_type_of_int_____"



the_length_of_1_complete_number_of_your_int = "_____the_length_of_1_complete_number_of_your_int_____"




initialize_0 = False













cwd = os.path.dirname(os.path.abspath(__file__))


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
    
    
    











