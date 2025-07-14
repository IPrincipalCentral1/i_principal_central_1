













import os









list_of_what_i_have = [
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["detail", "Huawei"], ["number_of_phone", "+213 561577437"]],
                    
                    
                    [["name_of_thing", "water"], ["amount", ""]],
                    
                    
                    [["name_of_thing", "electricity"], ["amount", ""]],
                    
                    
                    
                    ]










file_0 = os.path.join(os.getcwd(), "all_what_i_have_0.txt")





with open(file_0, "w") as f_:
    
    
    f_.write("\n" * 10)
    
    
    f_.write("i have : \n")
    
    counter_3 = 1
    
    
    f_.write("\n" * counter_3)

    counter_0 = 0
    
    while (counter_0 < len(list_of_what_i_have)):
        
        
        counter_1 = 0
        
        
        
        f_.write(f"    {list_of_what_i_have[counter_0][counter_1][0]} : \"{list_of_what_i_have[counter_0][counter_1][1]}\" \n")
        
        f_.write("\n" * counter_3)
        
        
        counter_1 += 1
        
        
        while (counter_1 < len(list_of_what_i_have[counter_0])):
        
                        
            f_.write(f"        {list_of_what_i_have[counter_0][counter_1][0]} : \"{list_of_what_i_have[counter_0][counter_1][1]}\" \n")
            
            f_.write("\n" * counter_3)
            
            
            counter_1 += 1
        
        
        counter_0 += 1
    











