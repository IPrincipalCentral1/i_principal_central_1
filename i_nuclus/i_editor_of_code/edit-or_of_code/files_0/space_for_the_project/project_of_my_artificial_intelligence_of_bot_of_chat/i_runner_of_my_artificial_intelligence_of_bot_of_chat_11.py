















import time 

import os

import importlib 


cwd = os.path.dirname(os.path.abspath(__file__))








i_file_of_artificial_intelligence_7_i_0 = os.path.join(cwd, "i_runner_of_my_artificial_intelligence_of_bot_of_chat_7.py")


i_file_of_artificial_intelligence_7_0_i_0 = os.path.join(cwd, "i_runner_of_my_artificial_intelligence_of_bot_of_chat_7_0.py")






i_file_of_artificial_intelligence_9_i_0 = os.path.join(cwd, "i_runner_of_my_artificial_intelligence_of_bot_of_chat_9.py")


i_file_of_artificial_intelligence_9_0_i_0 = os.path.join(cwd, "i_runner_of_my_artificial_intelligence_of_bot_of_chat_9_0.py")




file_of_text_0 = os.path.join(cwd, "text_0.txt")

with open(file_of_text_0, "r", encoding="utf-8") as f_:
    
    text = f_.read(os.path.getsize(file_of_text_0))
    




i_name_of_file_of_text_i_0 = "text_2.txt"


i_file_of_text_i_2 = os.path.join(cwd, i_name_of_file_of_text_i_0)

with open(i_file_of_text_i_2, "w", encoding="utf-8") as f_:
    
    f_.write(text)
    







def i_add_into_file_i_0(i_v_i_0):
        
    
    
    i_content_of_file_of_text_i_2 = ""
    
    
    with open(i_file_of_text_i_2, "r", encoding="utf-8") as f_:
        
        i_content_of_file_of_text_i_2 = f_.read(os.path.getsize(i_file_of_text_i_2))
        
    
    
    i_content_i_0 = i_v_i_0[1]
    
    
    
    print(f"i_hello_i_0 . i_content_i_0 = {i_content_i_0} .")
    
    
    
    i_content_of_file_of_text_i_2 += "\n\n" + i_content_i_0 + " .\n\n"
    
        
        
    
    with open(i_file_of_text_i_2, "w", encoding="utf-8") as f_:
        
        f_.write(i_content_of_file_of_text_i_2)
        
    
    
    



def i_add_into_file_i_1(i_v_i_0):
        
    
    
    i_content_of_file_of_text_i_2 = ""
    
    
    with open(i_file_of_text_i_2, "r", encoding="utf-8") as f_:
        
        i_content_of_file_of_text_i_2 = f_.read(os.path.getsize(i_file_of_text_i_2))
        
    
    
    i_content_i_0 = i_v_i_0[1]
    
    
    print(f"i_hello_i_0 . i_content_i_0 = {i_content_i_0} .")
    
    
    
    i_content_of_file_of_text_i_2 += "\n\n" + i_content_i_0 + " .\n\n"
    
        
        
    
    with open(i_file_of_text_i_2, "w", encoding="utf-8") as f_:
        
        f_.write(i_content_of_file_of_text_i_2)
        
    
    
    
    
    
    


def i_wait_and_check_content_of_file_i_0(i_file_i_0, i_content_i_0, i_encoding_i_0):
    
    
    i_content_i_1 = ""
    
    with open(i_file_i_0, "r", encoding=i_encoding_i_0) as f_:
        
        i_content_i_1 = f_.read(os.path.getsize(i_file_i_0))
        
        
    
    
    while (i_content_i_1 != i_content_i_0):
        
        
                
        with open(i_file_i_0, "r", encoding=i_encoding_i_0) as f_:
            
            i_content_i_1 = f_.read(os.path.getsize(i_file_i_0))
            
            
        
        
        
        
        
    
    
    
    
    
    
    








# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 











i_number_of_times_i_0 = _____i_number_of_times_i_0_____






minimum_value_0 = "_____minimum_value_1_____"






encoding_0 = "____encoding_1_____"









separater_of_words = _____separater_of_words_0_____


not_counted_words_0 = _____not_counted_words_0_____


    



not_counted_words_1 = _____not_counted_words_1_____












display_all_the_language = _____display_all_the_language_0_____


the_language_to_translate_from = "_____the_language_to_translate_from_0_____"

the_language_to_translate_to = "_____the_language_to_translate_to_0_____"





# number_of_digit_after_the_floating_point should be int . like : 2 or 20 .

number_of_digit_after_the_floating_point = _____number_of_digit_after_the_floating_point_____



# porcent_of_gain should be : 0.0 <= porcent_of_gain < 1.0

porcent_of_gain = "____porcent_of_gain_____"




# number_of_calcule_minimum should be int . like : 10_000 or 1_000_000 .

number_of_calcule_minimum = "_____number_of_calcule_minimum_____"





_____init_____ = "__________init______0_____"






latest_type_of_int = "_____latest_type_of_int_____"



# the_length_of_1_complete_number_of_your_int should be an int . like : 18 or 36 .

the_length_of_1_complete_number_of_your_int = "_____the_length_of_1_complete_number_of_your_int_____"







# end_section_of_parameter 



# ---------------------------------------------------------------------------

# end of section of parameter











    
    
    
i_counter_i_0 = 0


while (i_counter_i_0 < i_number_of_times_i_0):

    
    
    
    
    
    
    
    
    
    
    
    with open(i_file_of_artificial_intelligence_7_i_0, "r", encoding="utf-8") as f_:
        
        i_content_of_artificial_intelligence_7_i_0 = f_.read(os.path.getsize(i_file_of_artificial_intelligence_7_i_0))
        
        
    
    
    
    
    
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("text_0.txt", i_name_of_file_of_text_i_0)
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____minimum_value_0_____", minimum_value_0)
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____encoding_0_____", encoding_0)
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____separater_of_words_____", f"{separater_of_words}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____not_counted_words_____", f"{not_counted_words_0}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____display_all_the_language_____", f"{display_all_the_language}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____the_language_to_translate_from_____", f"{the_language_to_translate_from}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____the_language_to_translate_to____", f"{the_language_to_translate_to}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____number_of_digit_after_the_floating_point_0_____", f"{number_of_digit_after_the_floating_point}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____porcent_of_gain_0_____", f"{porcent_of_gain}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____number_of_calcule_minimum_0_____", f"{number_of_calcule_minimum}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("__________init_____0_____", f"{_____init_____}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____latest_type_of_int_0_____", f"{latest_type_of_int}")
    
    
    i_content_of_artificial_intelligence_7_i_0 = i_content_of_artificial_intelligence_7_i_0.replace("_____the_length_of_1_complete_number_of_your_int_0_____", f"{the_length_of_1_complete_number_of_your_int}")
    
    
    
    
    
    
    with open(i_file_of_artificial_intelligence_7_0_i_0, "w", encoding="utf-8") as f_:
        
        f_.write(i_content_of_artificial_intelligence_7_i_0)
        
        
    
    
    
    i_wait_and_check_content_of_file_i_0(i_file_i_0=i_file_of_artificial_intelligence_7_0_i_0, i_content_i_0=i_content_of_artificial_intelligence_7_i_0, i_encoding_i_0="utf-8")
    
    
    
    
    
    
    import i_runner_of_my_artificial_intelligence_of_bot_of_chat_7_0
    
    importlib.reload(i_runner_of_my_artificial_intelligence_of_bot_of_chat_7_0)
    
    
    i_v_i_0 = i_runner_of_my_artificial_intelligence_of_bot_of_chat_7_0.main()
    
    
    
    i_add_into_file_i_0(i_v_i_0=i_v_i_0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    with open(i_file_of_artificial_intelligence_9_i_0, "r", encoding="utf-8") as f_:
        
        i_content_of_artificial_intelligence_9_i_0 = f_.read(os.path.getsize(i_file_of_artificial_intelligence_9_i_0))
        
        
    
    
    
    
    
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("text_0.txt", i_name_of_file_of_text_i_0)
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____minimum_value_0_____", minimum_value_0)
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____encoding_0_____", encoding_0)
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____not_counted_words_____", f"{not_counted_words_1}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____display_all_the_language_____", f"{display_all_the_language}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____the_language_to_translate_from_____", f"{the_language_to_translate_from}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____the_language_to_translate_to____", f"{the_language_to_translate_to}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____number_of_digit_after_the_floating_point_0_____", f"{number_of_digit_after_the_floating_point}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____porcent_of_gain_0_____", f"{porcent_of_gain}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____number_of_calcule_minimum_0_____", f"{number_of_calcule_minimum}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("__________init_____0_____", f"{_____init_____}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____latest_type_of_int_0_____", f"{latest_type_of_int}")
    
    
    i_content_of_artificial_intelligence_9_i_0 = i_content_of_artificial_intelligence_9_i_0.replace("_____the_length_of_1_complete_number_of_your_int_0_____", f"{the_length_of_1_complete_number_of_your_int}")
    
    
    
    
    
    
    with open(i_file_of_artificial_intelligence_9_0_i_0, "w", encoding="utf-8") as f_:
        
        f_.write(i_content_of_artificial_intelligence_9_i_0)
        
        
    
    
    
    i_wait_and_check_content_of_file_i_0(i_file_i_0=i_file_of_artificial_intelligence_9_0_i_0, i_content_i_0=i_content_of_artificial_intelligence_9_i_0, i_encoding_i_0="utf-8")
    
    
    
    import i_runner_of_my_artificial_intelligence_of_bot_of_chat_9_0
    
    
    importlib.reload(i_runner_of_my_artificial_intelligence_of_bot_of_chat_9_0)
    
    
    
    i_v_i_0 = i_runner_of_my_artificial_intelligence_of_bot_of_chat_9_0.main()
    
    
    
    i_add_into_file_i_1(i_v_i_0=i_v_i_0)
    
    
    
    
    
    
    
    
    
    
    i_counter_i_0 += 1 














