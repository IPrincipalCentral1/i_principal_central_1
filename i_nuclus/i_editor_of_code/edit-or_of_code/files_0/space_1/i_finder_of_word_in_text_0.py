











import os


import traceback





cwd = os.path.dirname(os.path.abspath(__file__))











type_of_encoding_0 = r"""utf-8"""


type_of_encoding_1 = r"""utf-8"""


type_of_encoding_2 = r"""utf-8"""






def main():


        
        
    
    
    
    list_of_link_to_the_file_of_content = []
    
    
    
    
    content_of_file_of_link = ""
    
    
    
    try:
        
        file_of_the_link_to_the_file_that_contain_the_text_0 = os.path.join(cwd, "___the_link_to_the_file_that_contain_the_text___.txt")
        
        if (os.path.exists(file_of_the_link_to_the_file_that_contain_the_text_0) == True):
            
            
            with open(file_of_the_link_to_the_file_that_contain_the_text_0, "r", encoding=type_of_encoding_0) as f_:
                
                content_of_file_of_link = f_.read(os.path.getsize(file_of_the_link_to_the_file_that_contain_the_text_0))
                
            
            
            list_of_link_to_the_file_of_content = content_of_file_of_link.split("\n")            
            
            
        else:
            
            massage = "this file should have the link to the file that contain the text ."
            
            with open(file_of_the_link_to_the_file_that_contain_the_text_0, "w", encoding=type_of_encoding_0) as f_:
            
                f_.write(massage)
        
        
    except:
    
        semaphore = True
    
    
    
    



    #list_of_link = []



    #content_of_file_of_links = ""



    #try:

        #file_of_the_links_to_the_base_of_information_0 = os.path.join(cwd, "___the_links_to_the_base_of_information___.txt")

        #if (os.path.exists(file_of_the_links_to_the_base_of_information_0) == True):


            #with open(file_of_the_links_to_the_base_of_information_0, "r", encoding=type_of_encoding_0) as f_:

                #content_of_file_of_links = f_.read(os.path.getsize(file_of_the_links_to_the_base_of_information_0))



            #list_of_link = content_of_file_of_links.split("\n")




        #else:

            #massage = "this file should have the links to the base of information ."

            #with open(file_of_the_links_to_the_base_of_information_0, "w", encoding=type_of_encoding_0) as f_:

                #f_.write(massage)


    #except:

        #semaphore = True
    
    
    
    
    
    
    
    
    content_to_search_0 = ""
    
    
    
    
    
    
    
    try:
        
        file_of_content_to_search_0 = os.path.join(cwd, "file_of_content_to_search_0.txt")
        
        if (os.path.exists(file_of_content_to_search_0) == True):
            
            
            with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                
                content_to_search_0 = f_.read(os.path.getsize(file_of_content_to_search_0))
                
            
        else:
            
            massage = "this file should have the content to search for ."
            
            with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
            
                f_.write(massage)
        
        
    except:
    
        semaphore = True
    
    
    
    
        
    
    def finder_0(element_0, element_1):
        
        
        counter_0 = 0
        
        
        while ((counter_0 < len(element_0)) and (counter_0 < len(element_1)) and (element_0[counter_0] == element_1[counter_0])):
            
            
            counter_0 += 1
            
            
        if (counter_0 == len(element_0)):
            
            return True
            
        else:
            
            return False
            
            
    
    
        
    
    def finder_1(element_0, element_1):
        
        
                
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
    
        
        
        
                        
        message_0 = "this file should contain 'True' to search ."
        
        with open(file_1, "w") as f_:
        
            f_.write(message_0)
        
        
    
    
    
    
    
    number_0 = finder_1(element_0="i_hello", element_1="i_hello__________________hello__________hello_____________hello_0   hello   hello   \n  hello  hello")
    
    
    
    
    
        
    print(f"number_0 = {number_0} .")
    
    
    
    
        
    
    
    
    
    
    
    
    try:
    
    

            
            
            
    
    
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
            
                
                
                
                                
                message_0 = "this file should contain 'True' to search ."
                
                with open(file_1, "w") as f_:
                
                    f_.write(message_0)
                
                
                
                
                
                list_of_link_to_the_file_of_content.clear()
                
                
                
                
                content_of_file_of_link = ""
                
                
                
                try:
                    
                    file_of_the_link_to_the_file_that_contain_the_text_0 = os.path.join(cwd, "___the_link_to_the_file_that_contain_the_text___.txt")
                    
                    if (os.path.exists(file_of_the_link_to_the_file_that_contain_the_text_0) == True):
                        
                        
                        with open(file_of_the_link_to_the_file_that_contain_the_text_0, "r", encoding=type_of_encoding_0) as f_:
                            
                            content_of_file_of_link = f_.read(os.path.getsize(file_of_the_link_to_the_file_that_contain_the_text_0))
                            
                        
                        
                        list_of_link_to_the_file_of_content = content_of_file_of_link.split("\n")
                        
                        
                        
                    else:
                        
                        massage = "this file should have the link to the file that contain the text ."
                        
                        with open(file_of_the_link_to_the_file_that_contain_the_text_0, "w", encoding=type_of_encoding_0) as f_:
                        
                            f_.write(massage)
                    
                    
                except:
                
                    semaphore = True
                
                
                
                
                
                
                
                try:
                    
                    file_of_content_to_search_0 = os.path.join(cwd, "file_of_content_to_search_0.txt")
                    
                    if (os.path.exists(file_of_content_to_search_0) == True):
                        
                        
                        with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                            
                            content_to_search_0 = f_.read(os.path.getsize(file_of_content_to_search_0))
                            
                        
                    else:
                        
                        massage = "this file should have the content to search for ."
                        
                        with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
                        
                            f_.write(massage)
                    
                    
                except:
                
                    semaphore = True
                
                
                
                
                
                
                
                # section of finder
                    
                    
                content_0 = 0
                    
                    
                    
                    
                
                counter_5 = 0
                    
                    
                while (counter_5 < len(list_of_link_to_the_file_of_content)):
                    
                    try:
                        
                        
                        with open(list_of_link_to_the_file_of_content[counter_5], "r", encoding="utf-8") as f_:
                        
                            content_1 = f_.read(os.path.getsize(list_of_link_to_the_file_of_content[counter_5]))
                            
                        
                        
                        
                        
                        
                        
                        content_0 += finder_1(element_0=content_to_search_0, element_1=content_1)
                        
                        
                        
                        
                    
                    
                    except:
                    
                    
                    
                        traceback.print_exc()
                        
                        error = traceback.format_exc()
                        
                        semaphore = True
                        
                        print(f"list_of_link_to_the_file_of_content[{counter_5}] = {list_of_link_to_the_file_of_content[counter_5]} .")
                        
                        print(f"Erreur : {str(error)}")
                        
                    
                            
                            
                     
                        
                    
                    counter_5 += 1
                    
                
                
                with open(file_0, "w", encoding=type_of_encoding_2) as f_:
                
                    f_.write(str(content_0))
                
                
                
                
                
            
            
            
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
                
                
            

                        
                
            
                    
        
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
            
        
    
    
    
    



if __name__ == "__main__":
    
    
    main()
    
    
    












