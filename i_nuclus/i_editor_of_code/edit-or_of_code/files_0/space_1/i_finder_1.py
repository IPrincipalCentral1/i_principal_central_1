

















'''


the 'base of information' sould have this syntax :

element_0
    content_0
    content_1
    content_2
element_1    
    content_0
    content_1
    content_2   


and so on .



you should put the list of link of the 'base of infomration' that you want to find the element in it . and place it here :

    list_of_link :

    for example replace :
    
        ___the_link_to_the_base_of_information___
        
    by the link of the file that you want . 
    
    

and you should put the element that you want to find in the list right here :

     
    ___the_element___
    
    
    

you after that make :


    if (length_of(___the_element_in_the_list_that_are_found___) != 0):

        pourcentage_of_similarity = length_of(___the_element___) / length_of(___the_element_in_the_list_that_are_found___)
    


    
    
    







'''












import os







list_of_link = [

                r"___the_link_to_the_base_of_information___",

                ]





content_2 = r"""___the_element___"""







file_0 = os.path.join(os.getcwd(), "result_0.txt")





















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




counter_5 = 0


while (counter_5 < len(list_of_link)):
    
    
    with open(list_of_link[counter_5], "r") as f_:
    
        content_0 = f_.read(os.path.getsize(list_of_link[counter_5]))
        
    
    
    
    
    
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
    
    
    
    
    
    
    
    
    content_0 += finder_1(element_0=content_2, list_0=list_of_element)
    
    
    
    
    
    
    
    counter_5 += 1
    


with open(file_0, "w") as f_:

    f_.write(content_0)

































