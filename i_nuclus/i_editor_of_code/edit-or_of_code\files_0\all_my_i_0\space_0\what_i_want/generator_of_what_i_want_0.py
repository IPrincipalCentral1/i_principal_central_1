













import os









list_of_what_i_want = [
                    
                    
                    
                    # section of money
                    
                    
                    [["name_of_thing", "money"]],
                    
                    
                    
                    [["name_of_thing", "money"], ["detail", "i want a payment for i of '1_000_000 DZD' each '1 month' wich is the equivalent of : '1_000_000 second' . in my account eccp ."]],
                    
                    
                    
                    # section of house
                    
                    
                    [["name_of_thing", "house"]],
                    
                    
                    [["name_of_thing", "house"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "i want a house for i in my country 'Algeria' with '2 level' . build with cement and brick . and i own it with the ground ."]],
                    
                    
                    [["name_of_thing", "house"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "i want a house for i in my country 'Algeria' with '2 level' . build with cement and brick . and i own it with the ground . and this house is for my restaurant for i ."]],
                    
                    
                                        
                    # section of vehicle
                    
                    
                    [["name_of_thing", "vehicle"]],
                    
                    
                    [["name_of_thing", "vehicle"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "i own it from the beginning to the end ."]],
                    
                    
                    
                    
                    
                    # section of computer
                    
                    
                    
                    [["name_of_thing", "computer"]],
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "Apple"]],
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "NVIDIA"]],
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "LENOVO"]],
                    
                    
                    
                    [["name_of_thing", "computer"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["type", "intel"]],
                    
                    
                    
                    # section of memory
                    
                    
                    
                    [["name_of_thing", "memory"]],
                    
                    [["name_of_thing", "Hard Disk"], ["amount", "2.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["size_of_storage", "more than 2 tera Byte"]],
                    
                    
                    
                                        
                    
                    # section of connection
                    
                    
                    
                    [["name_of_thing", "connection"]],
                    
                    [["name_of_thing", "connection_to_the_internet"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail_0", "i want a debit of 1_000_000_000 Byte per second . i want to be capabel of sending and receiving in the internet with height quality ( quality = 1_000_000_000_000_000_000.0 ) ."]],
                    
                    
                    
                    # section of phone
                    
                    
                    
                    
                    
                    [["name_of_thing", "phone"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "Huawei"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "LG"], ["number_of_phone", "+213 561577437"]],
                    
                    
                    [["name_of_thing", "phone"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail", "IPhone"]],
                    
                    
                    
                    
                    # section of water
                    
                    
                    
                    [["name_of_thing", "water"]],
                    
                    
                    [["name_of_thing", "water to drink"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    [["name_of_thing", "water to clean"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    
                    
                    
                    
                    
                    # section of energy 
                    
                    
                    
                    
                    [["name_of_thing", "energy"]],
                    
                    
                    [["name_of_thing", "electricity"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    
                    
                                          
                    
                    # section of مشزي 
                    
                    
                    
                    
                    [["name_of_thing", "مشزي"]],
                    
                    
                    [["name_of_thing", "مشزي"], ["amount", "True"], ["the_quality", "1_000_000_000_000_000_000.0"]],
                    
                    
                    
                    # section of society-s
                    
                    
                    [["name_of_thing", "society"]],
                    
                    
                    [["name_of_thing", "society"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail_0", "i want 1 socity for my i as a user"],],
                    
                    
                    [["name_of_thing", "society"], ["amount", "1.0"], ["the_quality", "1_000_000_000_000_000_000.0"], ["detail_0", "i want 1 socity for my i as a producer"],],
                    
                    
                    
                    
                    ]










file_0 = os.path.join(os.getcwd(), "what_i_want_0.txt")





with open(file_0, "w") as f_:
    
    
    f_.write("\n" * 10)
    
    
    f_.write("i want : \n")
    
    counter_3 = 1
    
    
    f_.write("\n" * counter_3)

    counter_0 = 0
    
    while (counter_0 < len(list_of_what_i_want)):
        
        
        counter_1 = 0
        
        
        
        f_.write(f"    {list_of_what_i_want[counter_0][counter_1][0]} : \"{list_of_what_i_want[counter_0][counter_1][1]}\" \n")
        
        f_.write("\n" * counter_3)
        
        
        counter_1 += 1
        
        
        while (counter_1 < len(list_of_what_i_want[counter_0])):
        
                        
            f_.write(f"        {list_of_what_i_want[counter_0][counter_1][0]} : \"{list_of_what_i_want[counter_0][counter_1][1]}\" \n")
            
            f_.write("\n" * counter_3)
            
            
            counter_1 += 1
        
        
        counter_0 += 1
    











