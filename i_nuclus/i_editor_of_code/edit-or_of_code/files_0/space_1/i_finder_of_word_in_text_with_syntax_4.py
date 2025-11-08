





























'''






this one should have encoding .

you should put the specific encoding right here : 

    ___type_of_encoding_0___ for the file of ___the_links_to_the_base_of_information___.txt
    
    
    ___type_of_encoding_1___ for the file of file_of_content_to_search_0.txt
    
    
    ___type_of_encoding_2___ for the file of result_0.txt
    
    
    ___type_of_encoding_3___ for the file of for the content of the base of information 
    
    



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


this program will chack if the content to research exist on the content_n .





it is possible to make something like "artificial intelligence" . like the way that neural network remember things . 

this program can remember things . so instead of using neural network . you can use this program .





you can use the functions from i_reformater_0.py :
    
    
    shift_0()
    
    unshift_0()
    


to make the format like this shaep . shaep of 'base of information' .


    







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
    


    
    
    



this is how this program work . and it should work in a threading .


there is a file called : research_0.txt


that should contain 'True' to search .



there is a file called : runner_1.txt


that should contain 'True' to stop the program .






there is a file called : runner_2.txt


that should contain 'True' to reset into the memory .


( it means that if you have a new bases of information you 

reset it into this finder so this finder will look just inside those bases )





this one is much safer because it use try and except .











'''












import os


import traceback



    

cwd = os.path.dirname(os.path.abspath(__file__))





type_of_encoding_0 = r"""_____type_of_encoding_0_____"""


type_of_encoding_1 = r"""_____type_of_encoding_1_____"""


type_of_encoding_2 = r"""_____type_of_encoding_2_____"""


type_of_encoding_3 = r"""_____type_of_encoding_3_____"""






def main():


        
    
    
    
    
    list_of_link = []
    
    
    
    
    content_of_file_of_links = ""
    
    
    
    try:
        
        file_of_the_links_to_the_base_of_information_0 = os.path.join(cwd, "___the_links_to_the_base_of_information___.txt")
        
        if (os.path.exists(file_of_the_links_to_the_base_of_information_0) == True):
            
            
            with open(file_of_the_links_to_the_base_of_information_0, "r", encoding=type_of_encoding_0) as f_:
                
                content_of_file_of_links = f_.read(os.path.getsize(file_of_the_links_to_the_base_of_information_0))
                
            
            
            list_of_link = content_of_file_of_links.split("\n")
            
            
            
            
        else:
            
            message = "this file should have the links to the base of information ."
            
            with open(file_of_the_links_to_the_base_of_information_0, "w", encoding=type_of_encoding_0) as f_:
            
                f_.write(message)
        
        
    except:
    
        semaphore = True
    
    
    
    
    
    
    
    
    content_2 = ""
    
    
    
    
    
    
    
    
    
    try:
        
        file_of_content_to_search_0 = os.path.join(cwd, "file_of_content_to_search_0.txt")
        
        if (os.path.exists(file_of_content_to_search_0) == True):
            
            
            with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                
                content_2 = f_.read(os.path.getsize(file_of_content_to_search_0))
                
            
        else:
            
            message = "this file should have the content to search for ."
            
            with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
            
                f_.write(message)
        
        
    except:
    
        semaphore = True
    
    
    
    
    
    
    
    def upload_the_content(list_0, counter_0):
        
        
        v_0 = list_0[counter_0][0].split("\n")
        
        
        result_0 = v_0[0]
        
        
        i_counter_2 = 1
        
        while (i_counter_2 < len(v_0)):
            
            
            result_0 += "\n    " + v_0[i_counter_2]
            
            i_counter_2 += 1
            
            
        
        result_0 += "\n"
        
        
        return result_0
        
        
         
        
    
    
    
    
    
    def finder_0(element_0, element_1):
        
        
        counter_0 = 0
        
        
        while ((counter_0 < len(element_0)) and (counter_0 < len(element_1)) and (element_0[counter_0] == element_1[counter_0])):
            
            
            counter_0 += 1
            
            
        if (counter_0 == len(element_0)):
            
            return True
            
        else:
            
            return False
            
            
    
        
        
    
    def finder_2(element_0, element_1):
        
        
                
        counter_1 = 0
        
        
        if (len(element_0) > 0):
            
            
            
            counter_0 = 0
            
            
            
            while (counter_0 < len(element_1)):
            
            
            
                counter_2 = 0
                
            
                #print(f"i_hello_0 . counter_0 = {counter_0} . len(element_0) = {len(element_0)} . (counter_1 * len(element_0)) = {(counter_1 * len(element_0))} .")
                
                
                while ((counter_2 < len(element_0)) and (counter_0 < len(element_1)) and (element_0[counter_2] == element_1[counter_0])):
                    
    
                    counter_0 += 1
                    
                    counter_2 += 1
                    
                
                
                
                if (counter_2 == len(element_0)):
                    
                    counter_1 += 1
                    
                else:
                
                    
                    counter_0 += 1
            
        else:
            
            counter_1 = -1
            
            
        return counter_1
    
    
    
    
        
    
        
    
    def finder_3(element_0, element_1):
        
        
                
        i_counter_1 = 0
        
        
        #i_list_of_result_0 = []
        
        
        if (len(element_0) > 0):
            
            
            
            semaphore_of_add_0 = True
            
            
            i_counter_0 = 0
            
                    
            
            i_counter_3 = 0
            
            
            
                    
            i_content_0 = ""
            
            
            while (i_counter_0 < len(element_1)):
                
                
                
                
                i_counter_0 = i_counter_3
                
                i_counter_2 = 0
                
                #print(f"i_hello_0 . i_counter_3 = {i_counter_3} . i_counter_1 = {i_counter_1} .")
                
                
                while ((i_counter_2 < len(element_0)) and (i_counter_0 < len(element_1)) and (element_0[i_counter_2] == element_1[i_counter_0])):
                    
                    
                    #print(f"    i_hello_1 . in the loop of while . element_1[i_counter_0] = {element_1[i_counter_0]} .")
                    
                    i_counter_0 += 1
                    
                    i_counter_2 += 1
                
                
                #print(f"i_hello_4 . i_content_0 = \"{i_content_0}\" .")
                
                    
                
                if (i_counter_2 == len(element_0)):
                    
                    
                    return True
                    
                    
                    i_counter_1 += 1
                    
                    i_counter_3 = i_counter_0
                    
                    
                    # space to append into the list i_list_of_result_0 .
                    
                    
                    
                    #i_list_of_result_0.append(i_content_0)
                    
                    
                    #print(f"    i_hello_3 . in the first if . i_content_0 = \"{i_content_0}\" .")
                    
                    
                    semaphore_of_add_0 = False
                    
                    i_content_0 = ""
                    
                    
                    
                    
                else:
                
                    
                    # this space for the incrementation of string .
                    
                    
                    if (i_counter_3 < len(element_1)):
                        
                        
                        #i_content_0 += element_1[i_counter_3]
                        
                        semaphore_of_add_0 = True
                        
                        #print(f"    i_hello_2 . in the second if . i_content_0 = \"{i_content_0}\" .")
                        
                        
                        
                    
                    
                    
                    
                    i_counter_3 += 1
                    
                    
                    
                    
                #print(f"i_hello_5 . i_content_0 = \"{i_content_0}\" .")
                    
                
                
                
                
            
            #if (semaphore_of_add_0 == True):
    
                #i_list_of_result_0.append(i_content_0)
    
        else:
            
            i_counter_1 = -1
            
            
        return False
    
    
        
        
    
    def finder_3_1(element_0, element_1):
        
        
                
        counter_1 = 0
        
        
        if (len(element_0) > 0):
            
            
            
            counter_0 = 0
            
            
            
            while (counter_0 < len(element_1)):
            
            
            
                counter_2 = 0
                
            
                #print(f"i_hello_0 . counter_0 = {counter_0} . len(element_0) = {len(element_0)} . (counter_1 * len(element_0)) = {(counter_1 * len(element_0))} .")
                
                
                while ((counter_2 < len(element_0)) and (counter_0 < len(element_1)) and (element_0[counter_2] == element_1[counter_0])):
                    
    
                    counter_0 += 1
                    
                    counter_2 += 1
                    
                
                
                
                if (counter_2 == len(element_0)):
                    
                    
                    return True
                    
                    
                    
                else:
                
                    
                    counter_0 += 1
            
        else:
            
            counter_1 = -1
            
            
            
        return False
            
    
    
    
    
    
    
            
        
    def finder_1(element_0, list_0):
        
        
        
        
        content_0 = ""
        
        counter_0 = 0
        
        
        
        while (counter_0 < len(list_0)):
            
            
                    
            
            if (finder_3(element_0=element_0, element_1=list_0[counter_0][2]) == True):
              
                 
                content_0 += upload_the_content(list_0, counter_0)
            
            
            
    
                
                
            counter_0 += 1
        
        
        
        return content_0
        
        
        
    
    
    
    
    
    
    
    try:
    
    
        
        content_0 = ""
        
        
        list_of_element = []
        
        
        
        counter_5 = 0
        
        
        while (counter_5 < len(list_of_link)):
            
            
            with open(list_of_link[counter_5], "r", encoding=type_of_encoding_3) as f_:
            
                content_0 = f_.read(os.path.getsize(list_of_link[counter_5]))
                
            
            
            
            
            
            content_1 = ""
            
            
            v_0 = content_0.split("\n")
            
            
            
            
            list_of_element.append([])
            
            
            
            
            
            # reset to memory 
            
            
            pass_0 = False
            
            counter_0 = 0
            
            while (counter_0 < len(v_0)):
                        
                if (v_0[counter_0] != ""):
                        
                        
                        #content_1 += v_0[counter_0] + "\n"
                        
                        list_of_element[-1].append([v_0[counter_0], [], ""])
                        
                        
                        counter_0 += 1
                        
                        while ((counter_0 < len(v_0)) and (v_0[counter_0][:4] == "    ")):
                            
                            
                            #content_1 += v_0[counter_0] + "\n"
                            
                            
                            
                            list_of_element[-1][-1][0] += "\n" + v_0[counter_0][4:]
                            
                            list_of_element[-1][-1][2] += "\n" + v_0[counter_0][4:]
                            
                            
                            counter_0 += 1
                            
                            
                            pass_0 = True
                            
                            
                            
                            
                if (pass_0 == False):
                    
                    counter_0 += 1
                    
                else:
                    
                    pass_0 = False
            
            
            
            
            counter_5 += 1
            
            
            
            
            
            
            
    
    
        run_0 = True
        
        while (run_0 == True):
            
            

        
            continue_ = ""
        
        
            
            
            
            
            
            file_0 = os.path.join(cwd, "result_0.txt")
    
    
            file_1 = os.path.join(cwd, "research_0.txt")        
            
            
            if (os.path.exists(file_1) == True):
            
                
                with open(file_1, "r") as f_:
                
                    continue_ = f_.read(os.path.getsize(file_1))
            
            else:
            
            
                message_0 = "this file should contain 'True' to search ."
            
                with open(file_1, "w") as f_:
                
                    f_.write(message_0)
                
            
            
            
            
            if (continue_ == "True"):
            
                
                
                
                
                try:
                    
                    file_of_content_to_search_0 = os.path.join(cwd, "file_of_content_to_search_0.txt")
                    
                    if (os.path.exists(file_of_content_to_search_0) == True):
                        
                        
                        with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                            
                            content_2 = f_.read(os.path.getsize(file_of_content_to_search_0))
                            
                        
                    else:
                        
                        message = "this file should have the content to search for ."
                        
                        with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
                        
                            f_.write(message)
                    
                    
                except:
                
                    semaphore = True
                
                
                
                
                
                
                # section of finder
                    
                    
                content_0 = ""
                    
                    
                    
                    
                
                counter_5 = 0
                    
                    
                while (counter_5 < len(list_of_element)):
                    
                    
                    content_0 += finder_1(element_0=content_2, list_0=list_of_element[counter_5])
                    
                    
                    counter_5 += 1
                    
                
                
                with open(file_0, "w", encoding=type_of_encoding_2) as f_:
                
                    f_.write(content_0)
                
                
                
                
                                
                
                                
                message_0 = "this file should contain 'True' to search ."
                
                with open(file_1, "w") as f_:
                
                    f_.write(message_0)
                
                
                
                                
                
            
            
                
                
            
            file_2 = os.path.join(cwd, "runner_1.txt")
            
                    
            if (os.path.exists(file_2) == True):
            
                
                with open(file_2, "r") as f_:
                
                    continue_ = f_.read(os.path.getsize(file_2))
            
            else:
            
            
                message_0 = "this file should contain 'True' to stop the program ."
            
                with open(file_2, "w") as f_:
                
                    f_.write(message_0)
                
            
            
            
            
            if (continue_ == "True"):
            
                run_0 = False
            
                            
                message_0 = "this file should contain 'True' to stop the program ."
                
                with open(file_2, "w") as f_:
                
                    f_.write(message_0)
                
                
            
                    
                
            
            file_3 = os.path.join(cwd, "runner_2.txt")
            
                    
            if (os.path.exists(file_3) == True):
            
                
                with open(file_3, "r") as f_:
                
                    continue_ = f_.read(os.path.getsize(file_3))
            
            else:
            
            
                message_0 = "this file should contain 'True' to reset into the memory ."
            
                with open(file_3, "w") as f_:
                
                    f_.write(message_0)
                
            
            
            
            
            if (continue_ == "True"):
            
    
                            
                
                try:
                    
                    
                    list_of_link = []
                    
                    
                    
                    
                    content_of_file_of_links = ""
                    
                    
                    
                    try:
                        
        
                        if (os.path.exists(file_of_the_links_to_the_base_of_information_0) == True):
                            
                            
                            with open(file_of_the_links_to_the_base_of_information_0, "r", encoding=type_of_encoding_0) as f_:
                                
                                content_of_file_of_links = f_.read(os.path.getsize(file_of_the_links_to_the_base_of_information_0))
                                
                            
                            
                            list_of_link = content_of_file_of_links.split("\n")
                            
                            
                            
                            
                        else:
                            
                            message = "this file should have the links to the base of information ."
                            
                            with open(file_of_the_links_to_the_base_of_information_0, "w", encoding=type_of_encoding_0) as f_:
                            
                                f_.write(message)
                        
                        
                    except:
                    
                        semaphore = True
                    
                    
                    
                    
                    
                    
                    
                    
                    content_2 = ""
                    
                    
                    
                    
                    
                    
                    
                    try:
                        
        
                        if (os.path.exists(file_of_content_to_search_0) == True):
                            
                            
                            with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                                
                                content_2 = f_.read(os.path.getsize(file_of_content_to_search_0))
                                
                            
                        else:
                            
                            message = "this file should have the content to search for ."
                            
                            with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
                            
                                f_.write(message)
                        
                        
                    except:
                    
                        semaphore = True
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    list_of_element.clear()
                    
                    
                    
                    content_0 = ""
                    
                    
        
                    
                    counter_5 = 0
                    
                    
                    while (counter_5 < len(list_of_link)):
                        
                        
                        try:
                        
                        
                            
                            
                            with open(list_of_link[counter_5], "r", encoding=type_of_encoding_3) as f_:
                            
                                content_0 = f_.read(os.path.getsize(list_of_link[counter_5]))
                                
                            
                            
                            
                            
                            
                            content_1 = ""
                            
                            
                            v_0 = content_0.split("\n")
                            
                            
                            
                            
                            list_of_element.append([])
                            
                            
                            
                            # reset to memory 
                            
                            
                            pass_0 = False
                            
                            counter_0 = 0
                            
                            while (counter_0 < len(v_0)):
                                        
                                if (v_0[counter_0] != ""):
                                        
                                        
                                        #content_1 += v_0[counter_0] + "\n"
                                        
                                        list_of_element[-1].append([v_0[counter_0], [], ""])
                                        
                                        
                                        counter_0 += 1
                                        
                                        while ((counter_0 < len(v_0)) and (v_0[counter_0][:4] == "    ")):
                                            
                                            
                                            #content_1 += v_0[counter_0] + "\n"
                                            
                                            
                                            
                                            list_of_element[-1][-1][0] += "\n" + v_0[counter_0][4:]
                                            
                                            list_of_element[-1][-1][2] += "\n" + v_0[counter_0][4:]
                                            
                                            
                                            
                                            #list_of_element[-1][-1][1].append(v_0[counter_0])
                                            
                                            
                                            counter_0 += 1
                                            
                                            
                                            pass_0 = True
                                            
                                            
                                            
                                            
                                if (pass_0 == False):
                                    
                                    counter_0 += 1
                                    
                                else:
                                    
                                    pass_0 = False
                            
                            
                            
                                  
                        except:
                        
                                
                                        
                            traceback.print_exc()
                            
                            error = traceback.format_exc()
                            
                            semaphore = True
                            
                            print(f"file = '{list_of_link[counter_5]}'")
                            
                            
                            print(f"Erreur : {str(error)}")
                            
                        
                               
                        
                        counter_5 += 1
                        
                        
                                       
                except:
                
                        
                                
                    traceback.print_exc()
                    
                    error = traceback.format_exc()
                    
                    semaphore = True
                    
                    print(f"Erreur : {str(error)}")
                    
                
                        
                        
            
            
                                
                            
                message_0 = "this file should contain 'True' to reset into the memory ."
                
                with open(file_3, "w") as f_:
                
                    f_.write(message_0)
                
                    
            
                    
        
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
            
        


if __name__ == "__main__":
    
    
    main()
    
    
    
    



































