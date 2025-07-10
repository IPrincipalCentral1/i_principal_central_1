

















'''





هاذا برنامج يضع مقياس بين عملات لكن يستعمل i_math_0 انه جيد . و يعمل معه .

يعني يجب عليك تعيين :

    number_of_digit_after_the_floating_point
    
ثم تعمل .

عليك فقط  وضع الوحدات الأكثر أهمية في البدايات ثم الأقل منها أهمية تكون بعدها في هاذه القائمة list_to_organize . مثلا : 


    
    list_to_organize = [
                         
                         "EUR", "USD", "DZD",
                        
                        ]
    
هنا لدي ال EUR هو الأكثر أهمية . ثم يأتي بعده USD أقل منه أهمية . ثم في الأخير DZD .



ستظهر لك قائمة هاكذا : 

        
        ['go to bed', '1', 'go to bed'] ,
    
        ['go to bed', '2', 'eat machwi'] ,
    
        ['go to bed', '3', 'drink water'] ,
    
        ['go to bed', '4', 'produce machwi'] ,
    
        ['go to bed', '5', 'produce water'] ,
    
        ['go to bed', '6', 'produce bed'] ,
    
        ['eat machwi', '0.50000', 'go to bed'] ,
    
        ['eat machwi', '1', 'eat machwi'] ,
    
        ['eat machwi', '2', 'drink water'] ,
    
        ['eat machwi', '3', 'produce machwi'] ,
    
        ['eat machwi', '4', 'produce water'] ,
    
        ['eat machwi', '5', 'produce bed'] ,
    
        ['drink water', '0.33333', 'go to bed'] ,
    
        ['drink water', '0.50000', 'eat machwi'] ,
    
        ['drink water', '1', 'drink water'] ,
    
        ['drink water', '2', 'produce machwi'] ,
    
        ['drink water', '3', 'produce water'] ,
    
        ['drink water', '4', 'produce bed'] ,
    
        ['produce machwi', '0.25000', 'go to bed'] ,
    
        ['produce machwi', '0.33333', 'eat machwi'] ,
    
        ['produce machwi', '0.50000', 'drink water'] ,
    
        ['produce machwi', '1', 'produce machwi'] ,
    
        ['produce machwi', '2', 'produce water'] ,
    
        ['produce machwi', '3', 'produce bed'] ,
    
        ['produce water', '0.20000', 'go to bed'] ,
    
        ['produce water', '0.25000', 'eat machwi'] ,
    
        ['produce water', '0.33333', 'drink water'] ,
    
        ['produce water', '0.50000', 'produce machwi'] ,
    
        ['produce water', '1', 'produce water'] ,
    
        ['produce water', '2', 'produce bed'] ,
    
        ['produce bed', '0.16666', 'go to bed'] ,
    
        ['produce bed', '0.20000', 'eat machwi'] ,
    
        ['produce bed', '0.25000', 'drink water'] ,
    
        ['produce bed', '0.33333', 'produce machwi'] ,
    
        ['produce bed', '0.50000', 'produce water'] ,
    
        ['produce bed', '1', 'produce bed'] ,
    
    
هاذه يمكن وضعها في i_calculater_of_way_to_money_1.py هاكذا :


    list_of_result = [
    
    
                                        
                    ['go to bed', '1', 'go to bed'] ,
                    
                    ['go to bed', '2', 'eat machwi'] ,
                    
                    ['go to bed', '3', 'drink water'] ,
                    
                    ['go to bed', '4', 'produce machwi'] ,
                    
                    ['go to bed', '5', 'produce water'] ,
                    
                    ['go to bed', '6', 'produce bed'] ,
                    
                    ['eat machwi', '0.50000', 'go to bed'] ,
                    
                    ['eat machwi', '1', 'eat machwi'] ,
                    
                    ['eat machwi', '2', 'drink water'] ,
                    
                    ['eat machwi', '3', 'produce machwi'] ,
                    
                    ['eat machwi', '4', 'produce water'] ,
                    
                    ['eat machwi', '5', 'produce bed'] ,
                    
                    ['drink water', '0.33333', 'go to bed'] ,
                    
                    ['drink water', '0.50000', 'eat machwi'] ,
                    
                    ['drink water', '1', 'drink water'] ,
                    
                    ['drink water', '2', 'produce machwi'] ,
                    
                    ['drink water', '3', 'produce water'] ,
                    
                    ['drink water', '4', 'produce bed'] ,
                    
                    ['produce machwi', '0.25000', 'go to bed'] ,
                    
                    ['produce machwi', '0.33333', 'eat machwi'] ,
                    
                    ['produce machwi', '0.50000', 'drink water'] ,
                    
                    ['produce machwi', '1', 'produce machwi'] ,
                    
                    ['produce machwi', '2', 'produce water'] ,
                    
                    ['produce machwi', '3', 'produce bed'] ,
                    
                    ['produce water', '0.20000', 'go to bed'] ,
                    
                    ['produce water', '0.25000', 'eat machwi'] ,
                    
                    ['produce water', '0.33333', 'drink water'] ,
                    
                    ['produce water', '0.50000', 'produce machwi'] ,
                    
                    ['produce water', '1', 'produce water'] ,
                    
                    ['produce water', '2', 'produce bed'] ,
                    
                    ['produce bed', '0.16666', 'go to bed'] ,
                    
                    ['produce bed', '0.20000', 'eat machwi'] ,
                    
                    ['produce bed', '0.25000', 'drink water'] ,
                    
                    ['produce bed', '0.33333', 'produce machwi'] ,
                    
                    ['produce bed', '0.50000', 'produce water'] ,
                    
                    ['produce bed', '1', 'produce bed'] ,
                    
    
    
    
                    ]




و أيضا هاكذا : 

    supported_currencies = [
    
                     
                         "EUR", "USD", "DZD",   
                        
                        ]




ستحد حلا جيدا فيما بعد .







This is a program that creates a scale between currencies, and it uses i_math_0. It's good and works with it.

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
















'''










import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))

path_0 = os.path.dirname(cwd)

path_0 = os.path.dirname(path_0)

path_0 = os.path.dirname(path_0)

path_0 = os.path.dirname(path_0)







sys.path.append(path_0)



import i_math_0



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






list_to_organize = [
                     
                     "EUR", "USD", "DZD",

                    ]









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





print("\n" * 10)




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
            
                m = i_math_0.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
            
                if (m[0] != True):
            
                    organized_list_1.append([list_to_organize[counter_0], m[1][0], list_to_organize[counter_1]])
            
            
            else:
            
            
                                
                operation = f"(1 / {organized_list_0[counter_4][1]})"
                
                m = i_math_0.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                
                if (m[0] != True):
                
            
                    organized_list_1.append([list_to_organize[counter_0], m[1][0], list_to_organize[counter_1]])
            
            
        
        else:
            
            
            organized_list_1.append([organized_list_0[counter_3][0], organized_list_0[counter_3][1], organized_list_0[counter_3][2]])
            
            
            
        
        #print(f"    organized_list_1[{counter_2}] = {organized_list_1[counter_2]} .\n")    
        
        print(f"    {organized_list_1[counter_2]} ,\n")    
            
        
        
        counter_2 += 1
        
        counter_1 += 1
    
    
    counter_0 += 1










