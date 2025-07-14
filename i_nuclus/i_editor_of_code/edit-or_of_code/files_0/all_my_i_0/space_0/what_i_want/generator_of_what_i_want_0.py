













import os









list_of_what_i_have = [
                    
                    
                    
                    [["name_of_thing", "money"], ["detail", "i want a payment for i of '1_000_000 DZD' each '1 month' wich is the equivalent of : '1_000_000 second' . in my account eccp ."]],
                    
                    
                    [["name_of_thing", "house"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "i want a house for i in my country 'Algeria' with '2 level' . build with cement and brick . and i own it with the ground ."]],
                    
                    
                    [["name_of_thing", "house"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "i want a house for i in my country 'Algeria' with '2 level' . build with cement and brick . and i own it with the ground . and this house is for my restaurant for i ."]],
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "Apple"]],
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "NVIDIA"]],
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "LENOVO"]],
                    
                    
                    [["name_of_thing", "Hard Disk"], ["amount", "2.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["size_of_storage", "more than 2 tera Byte"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "Huawei"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "LG"], ["number_of_phone", "+213 561577437"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "IPhone"]],
                    
                    
                    [["name_of_thing", "water to drink"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    [["name_of_thing", "water to clean"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    [["name_of_thing", "electricity"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    
                    ]










file_0 = os.path.join(os.getcwd(), "what_i_want_0.txt")





with open(file_0, "w") as f_:
    
    
    f_.write("\n" * 10)
    
    
    f_.write("i want : \n")
    
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
    











