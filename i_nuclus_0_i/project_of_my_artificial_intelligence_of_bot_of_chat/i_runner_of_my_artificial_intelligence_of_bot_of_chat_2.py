













'''




this is a program of artificial intelligence .






you should insert your text into this file : text_0.txt

and than run the program .















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


cwd = os.path.dirname(os.path.abspath(__file__))










# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 





encoding_0 = "utf-8"







file_of_text_0 = os.path.join(cwd, "text_0.txt")

with open(file_of_text_0, "r", encoding=encoding_0) as f_:
    
    text = f_.read(os.path.getsize(file_of_text_0))
    
    





separater_of_words = [" ", "\n", "."]


not_counted_words = [""]











display_all_the_language = False


the_language_to_translate_from = ""

the_language_to_translate_to = ""






number_of_digit_after_the_floating_point = 20


porcent_of_gain = "0.0"







number_of_calcule = "10_000"





_____init_____ = "init"






latest_type_of_int = "int64_t"



the_length_of_1_complete_number_of_your_int = "18"







# end_section_of_parameter 



# ---------------------------------------------------------------------------

# end of section of parameter









import i_reformater_1






list_to_organize_0 = i_reformater_1.extract_list_0(text=text, separater_of_words=separater_of_words, not_counted_words=not_counted_words)



print(f"\n\n\n    list_to_organize_0 = {list_to_organize_0} .\n\n\n")




if (display_all_the_language == True):
    
    
    list_of_langage_0 = i_reformater_1.i_displayer_of_language_0()
    
    
    
    



if ((the_language_to_translate_from != "") and (the_language_to_translate_to != "")):
    
    
    
    
    try:
        
        
        
        list_to_organize_0 = i_reformater_1.i_translate_list_0(list_0=list_to_organize_0, language_from=the_language_to_translate_from, language_to=the_language_to_translate_to)
        
        
        
        
        
    except:
        
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
    




print(f"\n\n\n    finaly :    list_to_organize_0 = {list_to_organize_0} .\n\n\n")

    
    
    
    
    







number_of_chunk_0 = str(int(( len(list_to_organize_0) * 2 ) + 2))








def transform_from_list_to_string_0(list_0):
    
    
    i_counter_0 = 0
    
    i_content_0 = ""
    
    
        
    if (i_counter_0 < len(list_0)):
        
        i_content_0 += list_0[i_counter_0]
        
        i_counter_0 += 1
    
    
    while (i_counter_0 < len(list_0)):
        
        i_content_0 += " " + list_0[i_counter_0]
        
        i_counter_0 += 1
        
        
    
    
    return i_content_0
    
    
    






def transform_from_list_to_string_2(list_0):
    
    
    i_counter_0 = 0
    
    i_content_0 = ""
    
    
        
    if (i_counter_0 < len(list_0)):
        
        i_content_0 += transform_from_list_to_string_0(list_0=list_0[i_counter_0][1])
        
        i_counter_0 += 1
    
    
    while (i_counter_0 < len(list_0)):
        
        i_content_0 += " . " + transform_from_list_to_string_0(list_0=list_0[i_counter_0][1])
        
        i_counter_0 += 1
        
        
    
    
    return i_content_0
    
    
    








file_of_i_calculater_of_way_to_money_1 = os.path.join(cwd, "i_calculater_of_way_to_money_1.py")


file_of_i_calculater_of_way_to_money_1_0 = os.path.join(cwd, "i_calculater_of_way_to_money_1_0.py")





file_of_i_organize_official_1 = os.path.join(cwd, "i_organize_official_1.py")


file_of_i_organize_official_1_0 = os.path.join(cwd, "i_organize_official_1_0.py")





file_of_result_text_1 = os.path.join(cwd, "text_1.txt")



def main():



    
    content_of_i_organize_official_1 = ""
    
    
    
    with open(file_of_i_organize_official_1, "r", encoding="utf-8") as f_:
        
        
        content_of_i_organize_official_1 = f_.read(os.path.getsize(file_of_i_organize_official_1))
        
        
        
    
    
    content_of_i_organize_official_1 = content_of_i_organize_official_1.replace("_____number_of_digit_after_the_floating_point_____", str(number_of_digit_after_the_floating_point))
    
    
    
    content_of_i_organize_official_1 = content_of_i_organize_official_1.replace("_____porcent_of_gain_____", porcent_of_gain)
    
    
    
    content_of_i_organize_official_1 = content_of_i_organize_official_1.replace("_____list_to_organize_____", str(list_to_organize_0))
    
    
    
    
    with open(file_of_i_organize_official_1_0, "w", encoding="utf-8") as f_:
        
        
        f_.write(content_of_i_organize_official_1)
        
        
        
    
    
    
    import i_organize_official_1_0
    
    
    
    string_of_list_organized = i_organize_official_1_0.main()
    
        
        
    
    #print(f"string_of_list_organized = {string_of_list_organized} .")
    
    
    
    
    
    content_of_i_calculater_of_way_to_money_1 = ""
    
    
    with open(file_of_i_calculater_of_way_to_money_1, "r", encoding="utf-8") as f_:
        
        content_of_i_calculater_of_way_to_money_1 = f_.read(os.path.getsize(file_of_i_calculater_of_way_to_money_1))
        
        
        
    
    
    
    
    
    
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("_____number_of_calcule_____", number_of_calcule)
    
    
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("_____supported_currencies_____", str(list_to_organize_0))
    
    
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("_____list_of_result_____", string_of_list_organized)
    
    
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("_____number_of_digit_after_the_floating_point_____", str(number_of_digit_after_the_floating_point))
    
    
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("___number_of_chunk_0___", number_of_chunk_0)
    
    
        
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("_____latest_type_of_int_____", latest_type_of_int)
    
    
    
    content_of_i_calculater_of_way_to_money_1 = content_of_i_calculater_of_way_to_money_1.replace("_____the_length_of_1_complete_number_of_your_int_____", f"{the_length_of_1_complete_number_of_your_int}")
    
    
    
    
    
    
    with open(file_of_i_calculater_of_way_to_money_1_0, "w", encoding="utf-8") as f_:
        
        
        f_.write(content_of_i_calculater_of_way_to_money_1)
        
        
        
    
    
    
    import i_calculater_of_way_to_money_1_0
    
    
    max_1 = i_calculater_of_way_to_money_1_0.main(argv_1=_____init_____)
    
    
    
    result_max_0 = max_1[0]
    
    
    
    result_max_1 = max_1
    
    
    
    
    print(f"    result_max_0 = {result_max_0} .\n\n\n")
    
    
    
    
        
    
    i_content_0 = transform_from_list_to_string_0(list_0=result_max_1[0][1])
    
    
    print(f"    i_content_0 = \"{i_content_0}\" .\n\n")
    
    
    
    i_content_1 = transform_from_list_to_string_2(list_0=result_max_1[1])
    
    
        
    
    with open(file_of_result_text_1, "w", encoding="utf-8") as f_:
        
        f_.write(i_content_1)
        
        
    
    #print(f"    i_content_1 = \"{i_content_1}\" .\n\n")
    
    
     
        
    
    # return [ max_1, content, all_content_combine ]
    
    
    return [max_1, i_content_0, i_content_1]
    
    




    
if __name__ == "__main__":
    
    
    
    result_max_1 = main()
    












