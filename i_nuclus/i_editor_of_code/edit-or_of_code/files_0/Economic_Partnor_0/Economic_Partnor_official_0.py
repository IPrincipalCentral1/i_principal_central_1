





















list_of_liberary_to_install = [

                            ["psutil"] ,

                            

]










import os



import sys

import subprocess

import platform

import traceback



counter_0 = 0


while (counter_0 < len(list_of_liberary_to_install)):

        
    try:
    
    
        print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
    
        #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
    
        
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
    
    
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
    
    
    counter_0 += 1
    



def compile_0():
    
    
    
    
    file_1 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_10.c")
    
    
    with open(file_1, "r") as f_:
    
        content = f_.read(os.path.getsize(file_1))
    
    
    
    
    content = content.replace("___number_of_chunk___", "10")
    
    
    content = content.replace("___i_macro_of_number_of_digite_maximum_after_the_floating_point___", i_macro_of_number_of_digite_maximum_after_the_floating_point)
    
    
    content = content.replace("___postion_of_max_range___", str(10))
    
    
    
    file_2 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_10_0.c")
    
    
    with open(file_2, "w") as f_:
    
        f_.write(content)
    
    
    
    
    os.system("gcc Economic_Partner_official_produced_mixer_10_0.c -o E_P_o_p_mixer_10_0")
    
    
    
    open_popup_terminal(command="./E_P_o_p_mixer_10_0")
    
    
    


'''





create_account

delete_account

add_unity

delete_unity

add_amount_in_a_specific_unity

substruct_amount_in_a_specific_unity












'''








#i_macro_of_number_of_digite_maximum_after_the_floating_point = 1000




#compile_0()





import psutil

# الحصول على معلومات الذاكرة

memory = psutil.virtual_memory()

# طباعة القيم

print(f"إجمالي الذاكرة (Total): {memory.total / (1024 ** 3):.2f} GB")


print(f"الذاكرة المتاحة (Available): {memory.available / (1024 ** 3):.2f} GB")



print("-" * 10)


print("-" * 10)


print("-" * 10)


os.system("free -h")












