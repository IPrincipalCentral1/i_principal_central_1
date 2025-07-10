















list_to_organize = [
                        
                        
                    0, 1, 2, 3, 4, 5,
                    
                    ]









organized_list = []



counter_2 = 0

counter_0 = 0


while (counter_0 < len(list_to_organize)):

    counter_1 = 0
    
    
    while (counter_1 < len(list_to_organize)):
        
        organized_list.append([list_to_organize[counter_0], counter_1 + 1, list_to_organize[counter_1]])
        
                
        print(f"organized_list[{counter_2}] = {organized_list[counter_2]} .")
        
        
        counter_2 += 1
        
        counter_1 += 1
        
        
    
    counter_0 += 1
















