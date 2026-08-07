













'''




this is a program of artificial intelligence .


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















'''












# start of section of parameter 



# ---------------------------------------------------------------------------

# beging_section_of_parameter 





list_to_organize_0 = _____list_to_organize_0_____



number_of_digit_after_the_floating_point = _____number_of_digit_after_the_floating_point_0_____



porcent_of_gain = "_____porcent_of_gain_0_____"






number_of_calcule = "_____number_of_calcule_0_____"





_____init_____ = "__________init_____0_____"






latest_type_of_int = "_____latest_type_of_int_0_____"



the_length_of_1_complete_number_of_your_int = "_____the_length_of_1_complete_number_of_your_int_0_____"







# end_section_of_parameter 



# ---------------------------------------------------------------------------

# end of section of parameter











number_of_chunk_0 = str(int(( len(list_to_organize_0) * 2 ) + 2))






import os



cwd = os.path.dirname(os.path.abspath(__file__))












file_of_i_calculater_of_way_to_money_1 = os.path.join(cwd, "i_calculater_of_way_to_money_1.py")


file_of_i_calculater_of_way_to_money_1_0 = os.path.join(cwd, "i_calculater_of_way_to_money_1_0.py")





file_of_i_organize_official_1 = os.path.join(cwd, "i_organize_official_1.py")


file_of_i_organize_official_1_0 = os.path.join(cwd, "i_organize_official_1_0.py")



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
    
    
    
    
    print(f"    result_max_0 = {result_max_0} .\n\n\n")
    
    
    return max_1






    
if __name__ == "__main__":
    
    
    
    result_max_1 = main()
    
    
    






 
















