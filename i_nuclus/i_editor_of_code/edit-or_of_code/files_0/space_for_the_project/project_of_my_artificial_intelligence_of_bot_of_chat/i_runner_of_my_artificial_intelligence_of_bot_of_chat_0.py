













import os



cwd = os.path.dirname(os.path.abspath(__file__))








list_to_organize_0 = [
                        
                        
                        
                        "EUR", "USD", "DZD",
                        
                        
                        ]




number_of_digit_after_the_floating_point = 2


porcent_of_gain = "0.0"







#file_of_Economic_Partner_official_produced_mixer_9 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_9.c")


#file_of_Economic_Partner_official_produced_mixer_9_0 = os.path.join(cwd, "Economic_Partner_official_produced_mixer_9_0.c")





file_of_i_calculater_of_way_to_money_1 = os.path.join(cwd, "i_calculater_of_way_to_money_1.py")


file_of_i_calculater_of_way_to_money_1_0 = os.path.join(cwd, "i_calculater_of_way_to_money_1_0.py")





file_of_i_organize_official_1 = os.path.join(cwd, "i_organize_official_1.py")


file_of_i_organize_official_1_0 = os.path.join(cwd, "i_organize_official_1_0.py")



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

    
    

print(f"string_of_list_organized = {string_of_list_organized} .")






#content_of_i_organize_official_1 = content_of_i_organize_official_1.replace("", "")



















































