













import os

















def upload_the_content(list_0, counter_0):


    result_0 = list_0[counter_0][0] + "\n"

    counter_1 = 0
    
    while (counter_1 < len(list_0[counter_0][1])):
        
        result_0 += list_0[counter_0][1][counter_1] + "\n"
        
        counter_1 += 1
    
    
    
    return result_0
    
    
     
    





def finder_0(element_0, element_1):
    
    
    counter_0 = 0
    
    
    while ((counter_0 < len(element_0)) and (counter_0 < len(element_1)) and (element_0[counter_0] == element_1[counter_0])):
        
        
        counter_0 += 1
        
    
    if (counter_0 == len(element_0)):
    
        return True
        
    else:
    
        return False
        
        
    

def finder_1(element_0, list_0):
    
    
    
    
    content_0 = ""
    
    counter_0 = 0
    
    
    
    while (counter_0 < len(list_0)):
        
        
                
        
        if (finder_0(element_0=element_0, element_1=list_0[counter_0][0]) == True):
          
             
            content_0 += upload_the_content(list_0, counter_0)
        
        
        

            
            
        counter_0 += 1
    
    
    
    return content_0
    
    
    


















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
            
            list_of_element.append([v_0[counter_0], []])
            
            
            counter_0 += 1
            
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
    

    #print(f"{list_of_element[counter_0][0]}")
    
    counter_1 = 0
    
    while ((counter_1 < len(list_of_element[counter_0][1]))):
        
        
        
        
        #print(f"{list_of_element[counter_0][1][counter_1]}")
        
        
        counter_1 += 1
        
        
    counter_0 += 1








content_2 = "name_of_thing : \"com"






content_0 = finder_1(element_0=content_2, list_0=list_of_element)






file_0 = os.path.join(os.getcwd(), "content_0.txt")


with open(file_0, "w") as f_:

    f_.write(content_0)

































