




















'''






this is a program of artificial intelligence .






you should insert your text into this file : text_0.txt

and than run the program .



this program take :

    minimum_value_0

and :

    number_of_calcule_minimum



this is for creating new words from the letters on the text . 



this one bring all letters possible from the text of input .








you should adjust this one : 

    list_to_organize_0

    
to contain the words that you have .

for example :

    list_to_organize_0 = [
                            "get_power", "move", "produce_power", 
        ]



you will get some answers . maybe it will help .



you should make the most valubale thing on the beginning . like "get_power", so the less valubale from him after that like "move", and so on .


and you should put your target in the first . like "get_power" .

so the result will start and end with that .



if your things are not supported by this language . than you can do the same as in my mixer .


{

"0" : word_0

"1" : word_1

"2" : word_2


}


and so on .

so the list here will be like :

    ["0", "1", "2"]

and after the end you translate to your words that you have .



you can go deeper and do :

    ["move_0", "move_1", "move_2"]


and "move_0" is related to : ["dream", "eat", "take_a_sit"] 

and "move_1" is related to : ["drive_a_vehicle", "get_food", "enjoy"] 

and so on .

and after that translate the moves by there equivalant .

of course do not do repetition like :

    ["move_0", "move_0"]

each move have her own identificator like :

    ["move_0", "move_1"]


and maybe you can calcule faster .




if you want to initialize the mixer to vierge do : _____init_____ = "init" .

if you want to start from a point do : _____init_____ = "_" .






if you want to know about all the languages that exist , you should do :
    
    
    
    display_all_the_language = True
    




if you want to translate from a language to another , you should do :
    
    
        
    the_language_to_translate_from = "code_0"
    
    the_language_to_translate_to = "code_1"
    
    
    
    


if you do not want to translate from a language to another , you should do :
    
    
    the_language_to_translate_from = ""
    
    the_language_to_translate_to = ""
    
    
    
    
    
    










'''






import os

import traceback

import importlib

from pathlib import Path




cwd = os.path.dirname(os.path.abspath(__file__))










# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 








i_number_of_mixer_0_i = _____i_number_of_mixer_0_i_____






# i_maximum_time_2_i shloud be a number double . if (i_maximum_time_2_i > 0) : it will make the maximum time . else :  it will not make the maximum time .

i_maximum_time_2_i = _____i_maximum_time_2_i_____










i_semaphore_of_get_the_first_successful_number_0_i = _____i_semaphore_of_get_the_first_successful_number_0_i_____





minimum_value_0 = "_____minimum_value_0_____"








encoding_0 = "_____encoding_0_____"






file_of_text_0 = os.path.join(cwd, "text_0.txt")

with open(file_of_text_0, "r", encoding=encoding_0) as f_:
    
    text = f_.read(os.path.getsize(file_of_text_0))
    
    





not_counted_words = _____not_counted_words_____


















# number_of_digit_after_the_floating_point should be int . like : 2 or 20 .

number_of_digit_after_the_floating_point = _____number_of_digit_after_the_floating_point_0_____


# porcent_of_gain should be : 0.0 <= porcent_of_gain < 1.0

porcent_of_gain = "_____porcent_of_gain_0_____"




# number_of_calcule_minimum should be int . like : 10_000 or 1_000_000 .

number_of_calcule_minimum = "_____number_of_calcule_minimum_0_____"





_____init_____ = "__________init_____0_____"






latest_type_of_int = "_____latest_type_of_int_0_____"



# the_length_of_1_complete_number_of_your_int should be an int . like : 18 or 36 .

the_length_of_1_complete_number_of_your_int = "_____the_length_of_1_complete_number_of_your_int_0_____"





i_caractere_separator_of_words_0_i = _____i_caractere_separator_of_words_0_i_____


i_caractere_separator_of_words_1_i = _____i_caractere_separator_of_words_1_i_____





i_length_maximum_of_mix_0_i = _____i_length_maximum_of_mix_0__i_____











i_semaphore_of_print_0_i = _____i_semaphore_of_print_0_i_____



i_semaphore_of_enable_pip_install_0_i = _____i_semaphore_of_enable_pip_install_0_i_____












# end_section_of_parameter 



# ---------------------------------------------------------------------------

# end of section of parameter
















import i_reformater_1

importlib.reload(i_reformater_1)







list_to_organize_0 = i_reformater_1.extract_list_3(text=text, not_counted_words=not_counted_words)






if (i_semaphore_of_print_0_i == True):
    
    print(f"\n\n\n    list_to_organize_0 = {list_to_organize_0} .\n\n\n")
    
    



list_to_organize_2 = list_to_organize_0[1:]


list_to_organize_0 = list_to_organize_0[0]


number_of_digit_after_the_floating_point += len(list_to_organize_0)






if (i_semaphore_of_print_0_i == True):
    
    
    print(f"\n\n\n    finaly :    list_to_organize_0 = {list_to_organize_0} .\n\n\n")
    
        
    
    
    
    









number_of_chunk_0 = str(int(( len(list_to_organize_0) * 2 ) + 2))








def transform_from_list_to_string_0(list_0):
    
    
    i_counter_0 = 0
    
    i_content_0 = ""
    
    
        
    if (i_counter_0 < len(list_0)):
        
        i_content_0 += list_0[i_counter_0]
        
        i_counter_0 += 1
    
    
    while (i_counter_0 < len(list_0)):
        
        i_content_0 += i_caractere_separator_of_words_1_i + list_0[i_counter_0]
        
        i_counter_0 += 1
        
        
    
    
    return i_content_0
    
    
    






def transform_from_list_to_string_1(list_0):
    
    
    i_counter_0 = 0
    
    i_content_0 = ""
    
    
        
    if (i_counter_0 < len(list_0)):
        
        i_content_0 += list_0[i_counter_0]
        
        i_counter_0 += 1
    
    
    while (i_counter_0 < len(list_0)):
        
        i_content_0 += list_0[i_counter_0]
        
        i_counter_0 += 1
        
        
    
    
    return i_content_0
    
    
    



def transform_from_list_to_string_2(list_0):
    
    
    i_counter_0 = 0
    
    i_content_0 = ""
    
    
        
    if (i_counter_0 < len(list_0)):
        
        i_content_0 += transform_from_list_to_string_0(list_0=list_0[i_counter_0][1])
        
        i_counter_0 += 1
    
    
    while (i_counter_0 < len(list_0)):
        
        i_content_0 += i_caractere_separator_of_words_0_i + transform_from_list_to_string_0(list_0=list_0[i_counter_0][1])
        
        i_counter_0 += 1
        
        
    
    
    return i_content_0
    
    
    





def transform_from_list_to_string_3(list_0):
    
    
    i_counter_0 = 0
    
    i_content_0 = ""
    
    
        
    if (i_counter_0 < len(list_0)):
        
        i_content_0 += transform_from_list_to_string_1(list_0=list_0[i_counter_0][1])
        
        i_counter_0 += 1
    
    
    while (i_counter_0 < len(list_0)):
        
        i_content_0 += i_caractere_separator_of_words_0_i + transform_from_list_to_string_1(list_0=list_0[i_counter_0][1])
        
        i_counter_0 += 1
        
        
    
    
    return i_content_0
    
    
    



def i_check_if_all_word_finded_0_i(i_list_to_organize_1_i):
    
    
    
    # check if all the words are found :
    
    i_semaphore_of_continue_0_i = True
    
    
    i_counter_3_i = 0
    
    while ((i_counter_3_i < len(i_list_to_organize_1_i)) and (i_list_to_organize_1_i[i_counter_3_i][1] == 1)):
                    
        i_counter_3_i += 1
        
    
    
    if (i_counter_3_i == len(i_list_to_organize_1_i)):
        
        
        i_semaphore_of_continue_0_i = False
        
        
    
    return i_semaphore_of_continue_0_i
    
    





file_of_i_calculater_of_way_to_money_8 = os.path.join(cwd, "i_calculater_of_way_to_money_8.py")


file_of_i_calculater_of_way_to_money_8_0 = os.path.join(cwd, "i_calculater_of_way_to_money_8_0.py")





file_of_i_organize_official_3 = os.path.join(cwd, "i_organize_official_3.py")


file_of_i_organize_official_3_0 = os.path.join(cwd, "i_organize_official_3_0.py")




file_of_result_text_1 = os.path.join(cwd, "text_1.txt")








def main():



    
    content_of_i_organize_official_3 = ""
    
    
    i_d_0_i = Path(file_of_i_organize_official_3)
    
    
    content_of_i_organize_official_3 = i_d_0_i.read_text()
    
    
    
    #with open(file_of_i_organize_official_3, "r", encoding=encoding_0) as f_:


        #content_of_i_organize_official_3 = f_.read(os.path.getsize(file_of_i_organize_official_3))

        
        
    
    
    content_of_i_organize_official_3 = content_of_i_organize_official_3.replace("_____number_of_digit_after_the_floating_point_____", str(number_of_digit_after_the_floating_point))
    
    
    
    content_of_i_organize_official_3 = content_of_i_organize_official_3.replace("_____porcent_of_gain_____", porcent_of_gain)
    
    
    
    content_of_i_organize_official_3 = content_of_i_organize_official_3.replace("_____list_to_organize_____", str(list_to_organize_0))
    
    
    
    content_of_i_organize_official_3 = content_of_i_organize_official_3.replace("_____i_semaphore_of_print_0__i_____", str(i_semaphore_of_print_0_i))
    
    
    
    
    
    i_d_0_i = Path(file_of_i_organize_official_3_0)
    
    
    i_d_0_i.write_text(content_of_i_organize_official_3)
    


    #with open(file_of_i_organize_official_3_0, "w", encoding=encoding_0) as f_:


        #f_.write(content_of_i_organize_official_3)

        
        
    
    
    
    import i_organize_official_3_0
    
    
    importlib.reload(i_organize_official_3_0)
    
    
    string_of_list_organized = i_organize_official_3_0.main()
    
        
        
    
    #print(f"string_of_list_organized = {string_of_list_organized} .")
    
    
    
    
    
    content_of_i_calculater_of_way_to_money_8 = ""
    
    
    
    
    i_d_0_i = Path(file_of_i_calculater_of_way_to_money_8)
    
    
    content_of_i_calculater_of_way_to_money_8 = i_d_0_i.read_text()
    
    
    

    #with open(file_of_i_calculater_of_way_to_money_8, "r", encoding=encoding_0) as f_:

        #content_of_i_calculater_of_way_to_money_8 = f_.read(os.path.getsize(file_of_i_calculater_of_way_to_money_8))


        
    
    
    
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____i_maximum_time_0_i_____", f"{i_maximum_time_2_i}")
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____number_of_calcule_____", number_of_calcule_minimum)
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____supported_currencies_____", str(list_to_organize_0))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____list_of_result_____", string_of_list_organized)
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____number_of_digit_after_the_floating_point_____", str(number_of_digit_after_the_floating_point))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("___number_of_chunk_0___", number_of_chunk_0)
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____latest_type_of_int_____", latest_type_of_int)
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____the_length_of_1_complete_number_of_your_int_____", f"{the_length_of_1_complete_number_of_your_int}")
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____minimum_value_1_____", minimum_value_0)
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____type_of_encoding_0_____", encoding_0)
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____number_of_element_minus_1_____", str(len(list_to_organize_0) - 1))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____i_length_maximum_of_mix_0_i_____", str(i_length_maximum_of_mix_0_i))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____i_semaphore_of_get_the_first_successful_number_0__i_____", str(i_semaphore_of_get_the_first_successful_number_0_i))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____i_semaphore_of_print_0__i_____", str(i_semaphore_of_print_0_i))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____i_semaphore_of_enable_pip_install_0__i_____", str(i_semaphore_of_enable_pip_install_0_i))
    
    
    
    content_of_i_calculater_of_way_to_money_8 = content_of_i_calculater_of_way_to_money_8.replace("_____i_number_of_mixer_0___i_____", str(i_number_of_mixer_0_i))
    
    
    
    
    
    
    
    
    
    i_d_0_i = Path(file_of_i_calculater_of_way_to_money_8_0)
    
    
    i_d_0_i.write_text(content_of_i_calculater_of_way_to_money_8)
    


    #with open(file_of_i_calculater_of_way_to_money_8_0, "w", encoding=encoding_0) as f_:


        #f_.write(content_of_i_calculater_of_way_to_money_8)


        
    
    
    
    import i_calculater_of_way_to_money_8_0
    
    
    importlib.reload(i_calculater_of_way_to_money_8_0)
    
    
    
    max_1 = i_calculater_of_way_to_money_8_0.main(argv_1=_____init_____)
    
    
    
    result_max_0 = max_1[0]
    
    
    
    result_max_1 = max_1
    
    
    
    
    if (i_semaphore_of_print_0_i == True):
        
        print(f"    result_max_0 = {result_max_0} .\n\n\n")
        
        
    
    
        
    
    i_content_0 = transform_from_list_to_string_1(list_0=result_max_1[0][1])
    
    
    
    if (i_semaphore_of_print_0_i == True):
        
        print(f"    i_content_0 = \"{i_content_0}\" .\n\n")
        
    
    
    i_content_1 = transform_from_list_to_string_3(list_0=result_max_1[1])
    
    
    
    
    with open(file_of_result_text_1, "w", encoding=encoding_0) as f_:
        
        f_.write(i_content_1)
        
        
        
        
    
    
    #print(f"    i_content_1 = \"{i_content_1}\" .\n\n")
    
    
    
    
    i_list_to_organize_1_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(list_to_organize_0)):
        
        
        i_list_to_organize_1_i.append([list_to_organize_0[i_counter_0_i], 0])
        
        i_counter_0_i += 1
        
        
        
    
    
    
    
    i_list_of_list_of_word_0_i = max_1[1]
    
    
    
    i_list_combine_all_word_0_i = []
    
    
    i_semaphore_of_continue_0_i = True
    
    
    
    
    
    
    i_counter_of_word_finded_0_i = 0
    
    
    i_counter_0_i = len(i_list_of_list_of_word_0_i) - 1
    
    while ((0 <= i_counter_0_i) and (i_semaphore_of_continue_0_i == True)):
        
        
        i_element_0_i = i_list_of_list_of_word_0_i[i_counter_0_i][1]
        
        
        
        i_counter_2_i = 0
        
        
        while (i_counter_2_i < len(i_element_0_i)):
            
            
            
            i_counter_1_i = 0
            
            while (i_counter_1_i < len(i_list_to_organize_1_i)):
                
                
                if (i_list_to_organize_1_i[i_counter_1_i][0] == i_element_0_i[i_counter_2_i]):
                    
                    i_list_to_organize_1_i[i_counter_1_i][1] = 1
                    
                    
                
                i_counter_1_i += 1
                
                
                
            
            
            i_counter_2_i += 1
            
            
        
        
        
        
        # check if all the words are found 
        
        
        i_semaphore_of_continue_0_i = i_check_if_all_word_finded_0_i(i_list_to_organize_1_i=i_list_to_organize_1_i)
            
        
        
        if (i_semaphore_of_continue_0_i == True):
            
            i_counter_0_i -= 1
            
        
    
    
    
    
    
    if (i_counter_0_i < 0):
        
        i_counter_0_i = 0
    
    
    
    
    
    
    
    i_list_result_with_all_word_possible_0_i = max_1[1][i_counter_0_i:]
    
    
    
    i_string_result_with_all_word_possible_0_i = transform_from_list_to_string_3(list_0=i_list_result_with_all_word_possible_0_i)
    
    
    
    
    if (i_semaphore_of_print_0_i == True):
        
        
        print(f"\n\n\n    i_counter_0_i = {i_counter_0_i} . i_string_result_with_all_word_possible_0_i = \"{i_string_result_with_all_word_possible_0_i}\" .\n\n\n")
        
    
    
    '''    
        
        return [ max_1 , content , all_content_combine , i_string_result_with_all_word_possible_0_i , the_counter_of_the_first_element 
                
                    i_list_result_with_all_word_possible_0_i , list_to_organize_0 , list_to_organize_2
                
                ]
        
    '''
    
    return [max_1, i_content_0, i_content_1, i_string_result_with_all_word_possible_0_i, i_counter_0_i, 
            
            
            i_list_result_with_all_word_possible_0_i , list_to_organize_0 , list_to_organize_2
            
            
            ]
    
    
    
    
    
    



    
if __name__ == "__main__":
    
    
    
    result_max_1 = main()
    

    
    












