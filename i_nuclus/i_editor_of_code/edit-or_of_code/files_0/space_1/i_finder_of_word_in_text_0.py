















'''



this program is a finder of a text_0 inside a text_1 .

you should run the program and do :

    1 - content of file ==> ___the_link_to_the_file_that_contain_the_text___.txt should contain :
    
        the link to the file that contain the text
    
    this one can contain multiple links .
    
    
    2 - content of file ==> file_of_content_to_search_0.txt should contain :
    
        content to search
    

and run the program with :

    making the content of the file ==> research_0.txt as 'True' if you want to search .
    
and the result will be in this file ==> result_0.txt as a number of repetition of the element to search in the file of content .



and finaly . if you want to stop the program you should insert 'True' to this file ==> runner_1.txt .









( type_of_encoding_0 = r"""_____type_of_encoding_0_____""" ) ==> ___the_link_to_the_file_that_contain_the_text___.txt


( type_of_encoding_1 = r"""_____type_of_encoding_1_____""" ) ==> file_of_content_to_search_0.txt


( type_of_encoding_2 = r"""_____type_of_encoding_2_____""" ) ==> refere to the files that contain the content in '___the_link_to_the_file_that_contain_the_text___.txt'











'''











import os


import traceback





cwd = os.path.dirname(os.path.abspath(__file__))











type_of_encoding_0 = r"""_____type_of_encoding_0_____"""


type_of_encoding_1 = r"""_____type_of_encoding_1_____"""


type_of_encoding_2 = r"""_____type_of_encoding_2_____"""






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
            
            message = "this file should have the link to the file that contain the text ."
            
            with open(file_of_the_link_to_the_file_that_contain_the_text_0, "w", encoding=type_of_encoding_0) as f_:
            
                f_.write(message)
        
        
    except:
    
        semaphore = True
    
    
    
    


    
    
    
    content_to_search_0 = ""
    
    
    
    
    
    
    
    try:
        
        file_of_content_to_search_0 = os.path.join(cwd, "file_of_content_to_search_0.txt")
        
        if (os.path.exists(file_of_content_to_search_0) == True):
            
            
            with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                
                content_to_search_0 = f_.read(os.path.getsize(file_of_content_to_search_0))
                
            
        else:
            
            message = "this file should have the content to search for ."
            
            with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
            
                f_.write(message)
        
        
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
            
                
                
                
                
                
                list_of_link_to_the_file_of_content.clear()
                
                
                
                
                content_of_file_of_link = ""
                
                
                
                try:
                    
                    if (os.path.exists(file_of_the_link_to_the_file_that_contain_the_text_0) == True):
                        
                        
                        with open(file_of_the_link_to_the_file_that_contain_the_text_0, "r", encoding=type_of_encoding_0) as f_:
                            
                            content_of_file_of_link = f_.read(os.path.getsize(file_of_the_link_to_the_file_that_contain_the_text_0))
                            
                        
                        
                        list_of_link_to_the_file_of_content = content_of_file_of_link.split("\n")
                        
                        
                        
                    else:
                        
                        message = "this file should have the link to the file that contain the text ."
                        
                        with open(file_of_the_link_to_the_file_that_contain_the_text_0, "w", encoding=type_of_encoding_0) as f_:
                        
                            f_.write(message)
                    
                    
                except:
                
                    semaphore = True
                
                
                
                
                
                
                
                try:
                    
                    if (os.path.exists(file_of_content_to_search_0) == True):
                        
                        
                        with open(file_of_content_to_search_0, "r", encoding=type_of_encoding_1) as f_:
                            
                            content_to_search_0 = f_.read(os.path.getsize(file_of_content_to_search_0))
                            
                        
                    else:
                        
                        message = "this file should have the content to search for ."
                        
                        with open(file_of_content_to_search_0, "w", encoding=type_of_encoding_1) as f_:
                        
                            f_.write(message)
                    
                    
                except:
                
                    semaphore = True
                
                
                
                
                
                
                
                # section of finder
                    
                    
                content_0 = 0
                    
                    
                    
                    
                
                counter_5 = 0
                    
                    
                while (counter_5 < len(list_of_link_to_the_file_of_content)):
                    
                    try:
                        
                        
                        with open(list_of_link_to_the_file_of_content[counter_5], "r", encoding=type_of_encoding_2) as f_:
                        
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
                
                
            

                        
                
            
                    
        
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
            
        
    
    
    
    



if __name__ == "__main__":
    
    
    main()
    
    
    












