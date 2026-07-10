
















global i

    
i = {}






'''



(

I must make something clear. You should try both libraries. 

If one doesn't work for you, you should implement the other. 

This way you will be guaranteed full service.


)





If you want to withdraw change from money, you can use this program. 

You have to choose the column that contains the unit you want to withdraw change from :


(___number_of_library___ == 0) or (___number_of_library___ == 1)


and than replace ___number_of_library___ with the number of library that you chose .

and than replace ___folder_that_you_want_to_extract_cash_from_it___ with folder that you want to extract cash from it .

and than replace ___folder_that_you_want_to_extract_cash_into_it___ with folder that you want to extract cash into it .

and replace ___the_unity_that_you_want_to_extract_cash_from_it___ with the unity that you want to extract cash from it .

and replace ___the_quantity_that_you_want_to_extract_from_the_total_amount___ with the quantity that you want to extract from the total amount .


you can extract 1 from 10 . but you can not extract 10 from 1 .

because : ( 10 > 1 )






'''


number_of_library = int("___number_of_library___")







if (number_of_library == 0):





    
    import i_principal_central
    
    import os
    
    import time
    
    
    
    cwd = os.path.dirname(os.path.abspath(__file__))
    
    
    #print(f"\n\n\n cwd = {cwd} .\n\n\n")
    
    
    #folder_that_you_want_to_extract_cash_from_it = r"___folder_that_you_want_to_extract_cash_from_it___"
    
    
    folder_that_you_want_to_extract_cash_from_it = r"___folder_that_you_want_to_extract_cash_from_it___"
    
    
    #folder_that_you_want_to_extract_cash_into_it = r"___folder_that_you_want_to_extract_cash_into_it___"
    
    
    folder_that_you_want_to_extract_cash_into_it = r"___folder_that_you_want_to_extract_cash_into_it___"
    
    
    #the_unity_that_you_want_to_extract_cash_from_it = "___the_unity_that_you_want_to_extract_cash_from_it___"
    
    
    the_unity_that_you_want_to_extract_cash_from_it = "___the_unity_that_you_want_to_extract_cash_from_it___"
    
    
    #the_quantity_that_you_want_to_extract_from_the_total_amount = int("___the_quantity_that_you_want_to_extract_from_the_total_amount___")
    
    
    the_quantity_that_you_want_to_extract_from_the_total_amount = int("___the_quantity_that_you_want_to_extract_from_the_total_amount___")
    
    
    
    
    
    
    
    
    
    
    
    i["i_class"] = i_principal_central.i_class()
    
    i["i_class"].i_am_you()
    
    i["i_class"].i_develope()
    
    
    



    i["i_i_calcul_from_folder"] = i["i_class"].extract_cash(folder_from=folder_that_you_want_to_extract_cash_from_it, folder_to=folder_that_you_want_to_extract_cash_into_it, unity=the_unity_that_you_want_to_extract_cash_from_it, quantity=the_quantity_that_you_want_to_extract_from_the_total_amount, folder_of_source_of_unity=cwd)







elif (number_of_library == 1):







        
    
    #folder_that_you_want_to_extract_cash_from_it = r"___folder_that_you_want_to_extract_cash_from_it___"
    
    
    folder_that_you_want_to_extract_cash_from_it = r"___folder_that_you_want_to_extract_cash_from_it___"
    
    
    #folder_that_you_want_to_extract_cash_into_it = r"___folder_that_you_want_to_extract_cash_into_it___"
    
    
    folder_that_you_want_to_extract_cash_into_it = r"___folder_that_you_want_to_extract_cash_into_it___"
    
    
    #the_unity_that_you_want_to_extract_cash_from_it = "___the_unity_that_you_want_to_extract_cash_from_it___"
    
    
    the_unity_that_you_want_to_extract_cash_from_it = "___the_unity_that_you_want_to_extract_cash_from_it___"
    
    
    #the_quantity_that_you_want_to_extract_from_the_total_amount = int("___the_quantity_that_you_want_to_extract_from_the_total_amount___")
    
    
    the_quantity_that_you_want_to_extract_from_the_total_amount = int("___the_quantity_that_you_want_to_extract_from_the_total_amount___")
    
    
    


    
    
    
    import i_principal_central_1
    
    import os
    
    import time
    
        
    
    cwd = os.path.dirname(os.path.abspath(__file__))
    
    
    #print(f"\n\n\n cwd = {cwd} .\n\n\n")
    
    
    i["i_class"] = i_principal_central_1.i_class()
    
    i["i_class"].i_am_you()
    
    i["i_class"].i_develope()
    
    




    #i["i_i_calcul_from_folder"] = i["i_class"].extract_cash(folder_from=new_folder_2, folder_to=new_folder, unity="I", quantity=9, folder_of_source_of_unity=cwd)






    i["i_i_calcul_from_folder"] = i["i_class"].extract_cash(folder_from=folder_that_you_want_to_extract_cash_from_it, folder_to=folder_that_you_want_to_extract_cash_into_it, unity=the_unity_that_you_want_to_extract_cash_from_it, quantity=the_quantity_that_you_want_to_extract_from_the_total_amount, folder_of_source_of_unity=cwd)






