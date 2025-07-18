

















import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))




import i_math_2



number_of_digit_after_the_floating_point = 5




def finder_0(element_0, element_1, list_0):
    
    
    counter_0 = 0
    
    while (counter_0 < len(list_0)):
        
        if ((list_0[counter_0][0] == element_0) and (list_0[counter_0][2] == element_1)):
        
            break
        
        counter_0 += 1
    


    return counter_0






def finder_1(element_0, element_1, list_0):
    
    
    counter_0 = 0
    
    while (counter_0 < len(list_0)):
        
        if ((list_0[counter_0][0] == element_1) and (list_0[counter_0][2] == element_0)):
        
            break
        
        counter_0 += 1
    


    return counter_0






list_to_organize = _____list_to_organize_____











organized_list_0 = []



counter_2 = 0

counter_0 = 0


while (counter_0 < len(list_to_organize)):

    counter_1 = counter_0
    
    counter_3 = 0
    
    
    while (counter_1 < len(list_to_organize)):
        
            
        organized_list_0.append([list_to_organize[counter_0], f"{counter_3 + 1}", list_to_organize[counter_1]])
        
        
        
        
        
        #print(f"    organized_list_0[{counter_2}] = {organized_list_0[counter_2]} .\n")
        
        
        counter_3 += 1
        
        counter_2 += 1
        
        counter_1 += 1
        
        
    
    counter_0 += 1




content_0 = ""




organized_list_1 = []



counter_2 = 0

counter_0 = 0


while (counter_0 < len(list_to_organize)):
    
    
    counter_1 = 0
    
    while (counter_1 < len(list_to_organize)):
        
        
        #print(f"i_hello . list_to_organize[counter_0] = {list_to_organize[counter_0]} . list_to_organize[counter_1] = {list_to_organize[counter_1]} .")
        
        
        counter_3 = finder_0(element_0=list_to_organize[counter_0], element_1=list_to_organize[counter_1], list_0=organized_list_0)
        
        if (counter_3 >= len(organized_list_0)):
        

            counter_4 = finder_1(element_0=list_to_organize[counter_0], element_1=list_to_organize[counter_1], list_0=organized_list_0)
            
            
            #print(f"i_hello_1 . counter_4 = {counter_4} .")
            
            if (counter_4 >= len(organized_list_1)):
            
                
                counter_4 = finder_1(element_0=list_to_organize[counter_0], element_1=list_to_organize[counter_1], list_0=organized_list_1)
            
                operation = f"(1 / {organized_list_1[counter_4][1]})"
            
                m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
            
                if (m[0] != True):
            
                    organized_list_1.append([list_to_organize[counter_0], m[1][0], list_to_organize[counter_1]])
            
            
            else:
            
            
                                
                operation = f"(1 / {organized_list_0[counter_4][1]})"
                
                m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                
                if (m[0] != True):
                
            
                    organized_list_1.append([list_to_organize[counter_0], m[1][0], list_to_organize[counter_1]])
            
            
        
        else:
            
            
            organized_list_1.append([organized_list_0[counter_3][0], organized_list_0[counter_3][1], organized_list_0[counter_3][2]])
            
            
            
        
        #print(f"    organized_list_1[{counter_2}] = {organized_list_1[counter_2]} .\n")    
        
        #print(f"    {organized_list_1[counter_2]} ,\n")    
            
        content_0 += "    {organized_list_1[counter_2]} ,\n"
        
        counter_2 += 1
        
        counter_1 += 1
    
    
    counter_0 += 1




























