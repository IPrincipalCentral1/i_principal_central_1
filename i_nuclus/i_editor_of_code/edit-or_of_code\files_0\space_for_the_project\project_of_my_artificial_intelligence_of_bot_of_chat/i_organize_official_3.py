

















'''





هاذا برنامج يضع مقياس بين عملات لكن يستعمل i_math_i_am_i_1_i انه جيد . و يعمل معه .

يعني يجب عليك تعيين :

    number_of_digit_after_the_floating_point
    
ثم تعمل .

عليك فقط  وضع الوحدات الأكثر أهمية في البدايات ثم الأقل منها أهمية تكون بعدها في هاذه القائمة list_to_organize . مثلا : 


    
    list_to_organize = [
                         
                         "EUR", "USD", "DZD",
                        
                        ]
    
هنا لدي ال EUR هو الأكثر أهمية . ثم يأتي بعده USD أقل منه أهمية . ثم في الأخير DZD .



ستظهر لك قائمة هاكذا : 

                
        
        
        ['EUR', '1', 'EUR'] ,
        
        ['EUR', '2', 'USD'] ,
        
        ['EUR', '3', 'DZD'] ,
        
        ['USD', '0.50000', 'EUR'] ,
        
        ['USD', '1', 'USD'] ,
        
        ['USD', '2', 'DZD'] ,
        
        ['DZD', '0.33333', 'EUR'] ,
        
        ['DZD', '0.50000', 'USD'] ,
        
        ['DZD', '1', 'DZD'] ,
        

    
هاذه يمكن وضعها في i_calculater_of_way_to_money_1.py هاكذا :


    list_of_result = [
    
    
                                        
                    
                    
                    ['EUR', '1', 'EUR'] ,
                    
                    ['EUR', '2', 'USD'] ,
                    
                    ['EUR', '3', 'DZD'] ,
                    
                    ['USD', '0.50000', 'EUR'] ,
                    
                    ['USD', '1', 'USD'] ,
                    
                    ['USD', '2', 'DZD'] ,
                    
                    ['DZD', '0.33333', 'EUR'] ,
                    
                    ['DZD', '0.50000', 'USD'] ,
                    
                    ['DZD', '1', 'DZD'] ,
                    
    
    
    
                    ]




و أيضا هاكذا : 

    supported_currencies = [
    
                     
                         "EUR", "USD", "DZD",   
                        
                        ]




ستحد حلا جيدا فيما بعد .


يمكنك إظافة نسبة الربح التي يتم أخذها في كل مرة هنا : 

    
    porcent_of_gain = "0.1"
    
إذا لم تلرد يمكنك فعل هاذا : 


    porcent_of_gain = "0.0"









This is a program that creates a scale between currencies, and it uses i_math_i_am_i_1_i. It's good and works with it.

That means you should set:


    number_of_digit_after_the_floating_point



Then it will work.


You should place the most important units first, and then the less important ones after them in the list called list_to_organize . For example:
    


    list_to_organize = [

        "EUR", "USD", "DZD",

    ]



Here, EUR is the most important, followed by USD, and then DZD is the least important.


A result list will appear like this:
    
    
    
    
    
        ['EUR', '1', 'EUR'] ,
    
        ['EUR', '2', 'USD'] ,
    
        ['EUR', '3', 'DZD'] ,
    
        ['USD', '0.50000', 'EUR'] ,
    
        ['USD', '1', 'USD'] ,
    
        ['USD', '2', 'DZD'] ,
    
        ['DZD', '0.33333', 'EUR'] ,
    
        ['DZD', '0.50000', 'USD'] ,
    
        ['DZD', '1', 'DZD'] ,
    
    
    
    
    
You can place this list in a file named i_calculater_of_way_to_money_1.py like this:
    
    
    list_of_result = [
    
                
                
                
                    ['EUR', '1', 'EUR'] ,
                
                    ['EUR', '2', 'USD'] ,
                
                    ['EUR', '3', 'DZD'] ,
                
                    ['USD', '0.50000', 'EUR'] ,
                
                    ['USD', '1', 'USD'] ,
                
                    ['USD', '2', 'DZD'] ,
                
                    ['DZD', '0.33333', 'EUR'] ,
                
                    ['DZD', '0.50000', 'USD'] ,
                
                    ['DZD', '1', 'DZD'] ,
                
                


    ]
    
    
    
    
    
Also, define the supported currencies like this:
    
    supported_currencies = [

        "EUR", "USD", "DZD",

    ]
    



You will find a good solution later on.





You can add the profit percentage that is taken each time here:


    porcent_of_gain = "0.1"  <==>  ( 10 % )




If you don’t want that, you can do this:


    porcent_of_gain = "0.0"  <==>  ( 0 % )













'''










import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))




import i_math_i_am_i_1_i



number_of_digit_after_the_floating_point = _____number_of_digit_after_the_floating_point_____



porcent_of_gain = "_____porcent_of_gain_____"





list_to_organize = _____list_to_organize_____



i_semaphore_of_print_0_i = _____i_semaphore_of_print_0__i_____





    
    
def main():
    
    
    
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
    
    
    
        
    
    content_organized = "[\n\n"
    
    
    
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
    
    
    
    
    
    #print("\n" * 10)
    
    
    
    
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
                
                                       
                    
                    s1 = f"{porcent_of_gain}"
                    
                    s2 = "0.0"
                    
                    
                    bool_0 = i_math_i_am_i_1_i.my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                    
                                     
                    
                    s1 = f"{porcent_of_gain}"
                    
                    s2 = "1.0"
                    
                    
                    bool_1 = i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                    
                    operation = "0.0"    
                    
                    if (bool_0 == True):
                
                        if (bool_1 == True):
                
                            operation = f"((1 / {organized_list_1[counter_4][1]}) * (1 - {porcent_of_gain}))"
    
                    
                    else:
                
                
                        operation = f"((1 / {organized_list_1[counter_4][1]}))"    
                    
                
                
                    m = i_math_i_am_i_1_i.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                
                    if (m[0] != True):
                
                        organized_list_1.append([list_to_organize[counter_0], m[1][0], list_to_organize[counter_1]])
                
                
                else:
                
                
                                      
                    
                    s1 = f"{porcent_of_gain}"
                    
                    s2 = "0.0"
                    
                    
                    bool_0 = i_math_i_am_i_1_i.my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                    
                    
                                    
                    
                    s1 = f"{porcent_of_gain}"
                    
                    s2 = "1.0"
                    
                    
                    bool_1 = i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                    
                    operation = "0.0"    
                    
                    
                    if (bool_0 == True):
                    
                    
                        if (bool_1 == True):
                        
                        
                
                            operation = f"((1 / {organized_list_0[counter_4][1]}) * (1 - {porcent_of_gain}))"
                    
                    
                    
                    else:
                    
                
                        operation = f"((1 / {organized_list_0[counter_4][1]}))"        
                    
                    
                    m = i_math_i_am_i_1_i.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                    
                    if (m[0] != True):
                
                        organized_list_1.append([list_to_organize[counter_0], m[1][0], list_to_organize[counter_1]])
                
                
            
            else:
            
                
                
                            
                
                s1 = f"{porcent_of_gain}"
                
                s2 = "0.0"
                
                
                bool_0 = i_math_i_am_i_1_i.my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                
                            
                
                s1 = f"{porcent_of_gain}"
                
                s2 = "1.0"
                
                
                bool_1 = i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                
                operation = "0.0"    
                
                
                
                if (bool_0 == True):
                    
                    
                    if (bool_1 == True):
                        
                        operation = f"({organized_list_0[counter_3][1]} * (1 - {porcent_of_gain}))"
                        
                        
                    
                    m = i_math_i_am_i_1_i.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                    
                    if (m[0] != True):
                        
                        
                        organized_list_1.append([organized_list_0[counter_3][0], m[1][0], organized_list_0[counter_3][2]])
                    
                    
                else:
                
                
                
                    organized_list_1.append([organized_list_0[counter_3][0], organized_list_0[counter_3][1], organized_list_0[counter_3][2]])
            
            
            #print(f"    organized_list_1[{counter_2}] = {organized_list_1[counter_2]} .\n")    
            
            #print(f"    {organized_list_1[counter_2]} ,\n")    
                
            
            content_organized += f"            {organized_list_1[counter_2]} ,\n\n"
            
            
            
            counter_2 += 1
            
            counter_1 += 1
        
        
        counter_0 += 1
    
    
    
    content_organized += "]"
    
    
    
    if (i_semaphore_of_print_0_i == True):
        
        print(f"\n\n\n\n\n\n    porcent_of_gain = '{porcent_of_gain}' .\n\n\n\n\n\n")
        
        
    
    
    
    #print(f"content_organized = {content_organized} .")
    
    return content_organized
    
    
    
if __name__ == "__main__":
    
    
    
    content_organized = main()
    
    
    print(f"content_organized = {content_organized} .")
    
    
    







