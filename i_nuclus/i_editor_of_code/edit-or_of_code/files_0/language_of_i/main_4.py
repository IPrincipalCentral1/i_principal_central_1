















import os







def find_word_in_folder(word):


    
    list_of_result = []
    
    
    folder_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_1")
    
    
    list_of_file = []
    
    
    for root, dir_, list_of_file in os.walk(folder_0):
    
        break
        
        
        
    
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_file)):
    
        file_0 = os.path.join(folder_0, list_of_file[counter_0])
    
        content = ""
    
        with open(file_0, "r") as f_:
        
            content = f_.read(os.path.getsize(file_0))
    
    
    
        number_of_line = 0
        
        
        v_0 = content.split(word)
        
        
        if (len(v_0) > 1):
        
        
            counter_1 = 0
            
            while (counter_1 < len(v_0)):
            
                n_0 = len(v_0[counter_1].split("\n"))
                
                
                number_of_line += n_0
                
                list_of_result.append([counter_1, os.path.getsize(file_0), list_of_file[counter_0], number_of_line])
                
                
            
                counter_1 += 1
    
    
    
    
    
        counter_0 += 1
    
    
    
    return list_of_result








list_of_result = find_word_in_folder(word="what")



counter_0 = 0


while (counter_0 < len(list_of_result)):

    print(f"counter_0 = {counter_0} . list_of_result[counter_0] = {list_of_result[counter_0]} .")
    
    counter_0 += 1












