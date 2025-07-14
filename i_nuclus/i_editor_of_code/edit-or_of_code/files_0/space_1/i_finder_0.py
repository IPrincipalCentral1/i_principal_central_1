











import os





link_to_base = "/mnt/mydisk/shared_directory_on_PC/my_link_updated/i_directory/folder_for_github/edit-or_of_code/files_0/all_my_i_0/space_0/all_what_i_have/all_what_i_have_1.txt"











with open(link_to_base, "r") as f_:

    content_0 = f_.read(os.path.getsize(link_to_base))
    


content_1 = ""


v_0 = content_0.split("\n")




list_of_element = []



pass_0 = False

counter_0 = 0

while (counter_0 < len(v_0)):
            
    if (v_0[counter_0] != ""):
            
            content_1 += v_0[counter_0] + "\n"
            
            list_of_element.append([v_0[counter_0]])
            
            
            while ((counter_0 < len(v_0)) and (v_0[counter_0][:4] == "    ")):
                
                
                content_1 += v_0[counter_0] + "\n"
                
                
                list_of_element[-1][1].append(v_0[counter_0])
                
                
                counter_0 += 1
                
                
                pass_0 = True
                
                
                
                
    if (pass_0 == False):
        
        counter_0 += 1
        
    else:
        
        pass_0 = False





pass_0 = False

counter_0 = 0

while (counter_0 < len(list_of_element)):
            
    if (v_0[counter_0] != ""):
            

            print(f"{list_of_element[counter_0][0]}")
            
            counter_1 = 0
            
            while ((counter_1 < len(list_of_element[counter_0][1]))):
                
                
                
                
                print(f"{list_of_element[counter_0][1][counter_1]}")
                
                
                counter_1 += 1
                
                
                pass_0 = True
                
                
                
                
    if (pass_0 == False):
        
        counter_0 += 1
        
    else:
        
        pass_0 = False






















#file_0 = os.path.join(os.getcwd(), "content_1.txt")


#with open(file_0, "w") as f_:

    #f_.write(content_1)

































