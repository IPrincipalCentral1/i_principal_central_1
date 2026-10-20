












'''


you start by puting this :
    
    
    number_of_calcule = 100
    


and than do the list of your items . unities :
    
    
    i_supported_currencies_0_i = [
                                
                                "DZD", "EUR", "USD"
                                
    ]
    
    



and than you give me all the ways of converssion between 2 unities :
    
    
    
    list_of_result = [
                    
                    ['DZD', "0.9", 'DZD'], ['DZD', "0.01", 'EUR'], ['DZD', "0.01", 'USD'], 
                    
                    ['EUR', "135.73", 'DZD'], ['EUR', "0.9", 'EUR'], ['EUR', "1.04", 'USD'], 
                    
                    ['USD', "116.94", 'DZD'], ['USD', "0.78", 'EUR'], ['USD', "0.9", 'USD']
                    
    ]
    
    



and than you should specify  number_of_digit_after_the_floating_point :
    
    
    number_of_digit_after_the_floating_point = 2
    



and you run the program .





'''








































































number_of_calcule = 100



i_supported_currencies_0_i = [
                            
                            "DZD", "EUR", "USD"
                            
]





list_of_result = [
                
                ['DZD', "0.9", 'DZD'], ['DZD', "0.01", 'EUR'], ['DZD', "0.01", 'USD'], 
                
                ['EUR', "135.73", 'DZD'], ['EUR', "0.9", 'EUR'], ['EUR', "1.04", 'USD'], 
                
                ['USD', "116.94", 'DZD'], ['USD', "0.78", 'EUR'], ['USD', "0.9", 'USD']
                
]









number_of_digit_after_the_floating_point = 2


































list_of_liberary_to_install = [
                                
                                
                                
                                
                                
                                
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
    



import requests

import time

from pathlib import Path

import copy



cwd = os.path.dirname(os.path.abspath(__file__))




import i_my_mixer_1_i



import i_math_i_am_i_0







def finder_0(list_0, element):

    counter_0 = 0
    
    while ((counter_0 < len(list_0)) and (list_0[counter_0][0] != element)):
    
        counter_0 += 1

    
    return counter_0


def finder_1(list_0, element_0, element_1):

    counter_0 = 0
    
    while ((counter_0 < len(list_0)) and (list_0[counter_0][0] != element_0)):
    
        counter_0 += 1

    if (counter_0 < len(list_0)):
    
                
        while ((counter_0 < len(list_0)) and (list_0[counter_0][2] != element_1)):
        
            counter_0 += 1
            
    else:
    
        counter_0 = len(list_0)
        
        
    
    return counter_0




def transformer_0(list_0, unity_0, unity_1, amount):

    counter_0 = finder_1(list_0=list_0, element_0=unity_0, element_1=unity_1)
    
    semaphore_of_error = False

    amount_of_result = "0.0"

    if ((counter_0 < len(list_0))):

        
        operation = f"{amount} * {list_0[counter_0][1]}"
        
        
        m = i_math_i_am_i_0.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
        
        if (m[0] != True):
        
            amount_of_result = m[1][0]
        
        
        
    else:
    
        semaphore_of_error = True
        
    
    return  [semaphore_of_error, amount_of_result]




def transform_and_calculate_0(list_0, amount):
    
    
    
        
    
    list_of_unity = list_0
    
    
    
    result_1 = [False, amount]
    
    
    #print(f"\n\n list_of_unity = {list_of_unity} \n\n result_1 = {result_1} \n\n")
    
    
    counter_0 = 0
    
    
    while (counter_0 + 1 < len(list_of_unity)):
    
        
        result_1 = transformer_0(list_0=list_of_result, unity_0=list_of_unity[counter_0], unity_1=list_of_unity[counter_0 + 1], amount=result_1[1])
        
        counter_0 += 1
    
    
    
    #print(f"\n\n\n new : result_1 = {result_1} \n\n\n")
    
    
    return result_1
    







def int_to_str_0(number_0):

    str_0 = str(number_0)
    
    counter_0 = len(str_0)
    


    str_result = str_0
    

    if (18 > len(str_0)):
    
    
        counter_1 = 0
    
        while (counter_1 < 18 - counter_0):
            
            str_result = "0" + str_result
            
            counter_1 += 1
        
    
    
    return str_result





def open_popup_terminal(command):
    
    
    system = platform.system()

    if system == "Windows":

        subprocess.run(["cmd", "/c", f"{command}"])

    elif system == "Linux":

        subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command}; exit"])

    elif system == "Darwin":

        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command}; exit"'])






def extract_and_calculate_0(list_of_result, amount):


        
    list_of_unity = []
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_result)):
        
        
        list_of_unity.append(i_supported_currencies_0_i[int(list_of_result[counter_0])])
        
        counter_0 += 1
    
    
    
    result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)
    
    return [result_1, list_of_unity]








print(f"\n\n\n list_of_result = {list_of_result} .\n\n")











'''

-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------



start




'''




def i_main_0_i():
    
    
    
    
    print("\n\n start :")
    
    
    
    
    
    
    t1 = time.time()
    
    
    
    amount = "1.0"
    
    
    print(f" statring from {amount} {i_supported_currencies_0_i[0]} .")
    
    
    max_0 = ["0.0", []]
    
    
    i_list_0_i = []
    
    
    i_max_number_0_i = len(i_supported_currencies_0_i) - 1
    
    
    list_of_result_0 = []
    
    
    
    counter_2 = 1
    
    
    while (counter_2 <= number_of_calcule):
        
        
        
        
        
        
        list_of_result_0.clear()
        
        
        list_of_result_0.append(0)
        
        
        list_of_result_0.extend(i_list_0_i)
        
        
        list_of_result_0.append(0)
        
        
        
        
        result = extract_and_calculate_0(list_of_result=list_of_result_0, amount=amount)
        
        
        
        
        s1 = f"{result[0][1]}"
        
        s2 = f"{max_0[0]}"
        
        
        bool_0 = i_math_i_am_i_0.my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
        
        
        
        if ((bool_0 == True)):
            
            
            max_0[0] = result[0][1]
            
            
            
            
            max_0[1].clear()
            
            max_0[1] = copy.deepcopy(result[1])
            
            
            
        
        
        
        
        i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
    
    
        counter_2 += 1
    
    
    
    
    
    
    t2 = time.time()
    
    print("-" * 30)
    
    
    print(f"\n\n max_0 = {max_0} .\n\n time = {t2 - t1} second . \n\n")
    
    
    
    
    
    
    
    
    
    
    print(f" finish .\n\n")
    
    
    return [max_0]







if __name__ == "__main__":
    
    
    i_main_0_i()
    
    
    

















