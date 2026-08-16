

















'''


the 'base of information' should have this syntax :

element_0
    content_0
    content_1
    content_2
element_1    
    content_0
    content_1
    content_2   


and so on .



you should put the list of link of the 'base of infomration' that you want to find the element in it . and place it here in this file :

    ___the_links_to_the_base_of_information___.txt
    
    for example  :
    
        link_to_the_base_0
        link_to_the_base_1
        link_to_the_base_2
    
    and so on .
        
    

and you should put the element that you want to find in the list right here in this file :

     
    file_of_content_to_search_0.txt
    
    
    

you after that make :


    if (length_of(___the_element_in_the_list_that_are_found___) != 0):

        pourcentage_of_similarity = length_of(___the_element___) / length_of(___the_element_in_the_list_that_are_found___)
    


    
    
    







'''












import os


import traceback




try:


    
    cwd = os.path.dirname(os.path.abspath(__file__))
    
    
    
    
    list_of_link = []
    
    
    
    
    content_of_file_of_links = ""
    
    
    
    try:
        
        file_of_the_links_to_the_base_of_information_0 = os.path.join(cwd, "___the_links_to_the_base_of_information___.txt")
        
        if (os.path.exists(file_of_the_links_to_the_base_of_information_0) == True):
            
            
            with open(file_of_the_links_to_the_base_of_information_0, "r") as f_:
                
                content_of_file_of_links = f_.read(os.path.getsize(file_of_the_links_to_the_base_of_information_0))
                
            
            
            list_of_link = content_of_file_of_links.split("\n")
            
            
            
            
        else:
            
            massage = "this file should have the links to the base of information ."
            
            with open(file_of_the_links_to_the_base_of_information_0, "w") as f_:
            
                f_.write(massage)
        
        
    except:
    
        semaphore = True
    
    
    
    
    
    
    
    
    content_2 = ""
    
    
    
    
    
    
    
    try:
        
        file_of_content_to_search_0 = os.path.join(cwd, "file_of_content_to_search_0.txt")
        
        if (os.path.exists(file_of_content_to_search_0) == True):
            
            
            with open(file_of_content_to_search_0, "r") as f_:
                
                content_2 = f_.read(os.path.getsize(file_of_content_to_search_0))
                
            
        else:
            
            massage = "this file should have the content to search for ."
            
            with open(file_of_content_to_search_0, "w") as f_:
            
                f_.write(massage)
        
        
    except:
    
        semaphore = True
    
    
    
    
    
    
    
    
    
    file_0 = os.path.join(cwd, "result_0.txt")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    content_0 = ""
    
    
    list_of_element = []
    
    
    
    counter_5 = 0
    
    
    while (counter_5 < len(list_of_link)):
        
        
        with open(list_of_link[counter_5], "r") as f_:
        
            content_0 = f_.read(os.path.getsize(list_of_link[counter_5]))
            
        
        
        
        
        
        content_1 = ""
        
        
        v_0 = content_0.split("\n")
        
        
        
        
        list_of_element.append([])
        
        
        
        pass_0 = False
        
        counter_0 = 0
        
        while (counter_0 < len(v_0)):
                    
            if (v_0[counter_0] != ""):
                    
                    
                    content_1 += v_0[counter_0] + "\n"
                    
                    list_of_element[-1].append([v_0[counter_0], []])
                    
                    
                    counter_0 += 1
                    
                    while ((counter_0 < len(v_0)) and (v_0[counter_0][:4] == "    ")):
                        
                        
                        content_1 += v_0[counter_0] + "\n"
                        
                        
                        list_of_element[-1][-1][1].append(v_0[counter_0])
                        
                        
                        counter_0 += 1
                        
                        
                        pass_0 = True
                        
                        
                        
                        
            if (pass_0 == False):
                
                counter_0 += 1
                
            else:
                
                pass_0 = False
        
        
        
        
        counter_5 += 1
        
        
        
        
        
        
        
    
    
    
    
    # section of finder
        
        
    content_0 = ""
        
        
        
        
    
    counter_5 = 0
        
    
    while (counter_5 < len(list_of_element)):
        
        
        content_0 += finder_1(element_0=content_2, list_0=list_of_element[counter_5])
        
    
        counter_5 += 1
        
    
    
    with open(file_0, "w") as f_:
    
        f_.write(content_0)
    



        
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    

    
    
    
    
    
    
    
    
    
    
    




















