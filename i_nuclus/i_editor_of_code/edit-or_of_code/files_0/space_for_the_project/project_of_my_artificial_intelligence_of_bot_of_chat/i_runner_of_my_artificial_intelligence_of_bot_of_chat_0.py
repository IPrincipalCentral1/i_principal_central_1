













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








'''












# start of section of parameter 

# ---------------------------------------------------------------------------






list_to_organize_0 = [
                        
                        
                        "EUR", "USD", "DZD",
                        
                        
                        ]




number_of_digit_after_the_floating_point = 2


porcent_of_gain = "0.0"






number_of_calcule = "10_000"







# ---------------------------------------------------------------------------

# end of section of parameter












number_of_chunk_0 = str(int(( len(list_to_organize_0) // (10 ** 18) ) + 2))






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
    
    
    
    
    with open(file_of_i_calculater_of_way_to_money_1_0, "w", encoding="utf-8") as f_:
        
        
        f_.write(content_of_i_calculater_of_way_to_money_1)
        
        
        
    
    
    
    import i_calculater_of_way_to_money_1_0
    
    
    max_0 = i_calculater_of_way_to_money_1_0.main(argv_1="init")
    
    
    
    result_max_0 = max_0
    
    
    
    
    print(f"    result_max_0 = {result_max_0} .\n\n\n")
    
    
    return result_max_0






    
if __name__ == "__main__":
    
    
    
    result_max_0 = main()
    
    
    






 














