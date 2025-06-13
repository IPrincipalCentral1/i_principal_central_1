















number_of_library = 0







if (number_of_library == 0):





    
    import i_principal_central
    
    import os
    
    import time
    
    
    
    cwd = os.path.dirname(os.path.abspath(__file__))
    
    
    #print(f"\n\n\n cwd = {cwd} .\n\n\n")
    
    
    #folder_that_you_want_to_extract_cash_from_it = r"___folder_that_you_want_to_extract_cash_from_it___"
    
    
    folder_that_you_want_to_extract_cash_from_it = r"/mnt/795EE18952C91665/shared_directory_on_PC/my_link_updated/i_nuclus/mains/i_Economic_Partner_official_send_and_receive/i_github/i_principal_central/i/i_main"
    
    
    #folder_that_you_want_to_extract_cash_into_it = r"___folder_that_you_want_to_extract_cash_into_it___"
    
    
    folder_that_you_want_to_extract_cash_into_it = r"/mnt/795EE18952C91665/shared_directory_on_PC/my_link_updated/i_nuclus/mains/i_Economic_Partner_official_send_and_receive/i_github/i_principal_central/i/new_folder_0"
    
    
    #the_unity_that_you_want_to_extract_cash_from_it = "___the_unity_that_you_want_to_extract_cash_from_it___"
    
    
    the_unity_that_you_want_to_extract_cash_from_it = "I"
    
    
    #the_quantity_that_you_want_to_extract_from_the_total_amount = int("___the_quantity_that_you_want_to_extract_from_the_total_amount___")
    
    
    the_quantity_that_you_want_to_extract_from_the_total_amount = int("1")
    
    
    
    
    
    
    
    
    
    
    
    global i
    
        
    i = {}
    
    i["i_class"] = i_principal_central.i_class()
    
    i["i_class"].i_am_you()
    
    i["i_class"].i_develope()
    
    
    



    i["i_i_calcul_from_folder"] = i["i_class"].extract_cash(folder_from=folder_that_you_want_to_extract_cash_from_it, folder_to=folder_that_you_want_to_extract_cash_into_it, unity=the_unity_that_you_want_to_extract_cash_from_it, quantity=the_quantity_that_you_want_to_extract_from_the_total_amount, folder_of_source_of_unity=cwd)







elif (number_of_library == 1):










    
    
    
    import i_principal_central_1
    
    import os
    
    import time
    
        
    
    cwd = os.path.dirname(os.path.abspath(__file__))
    
    
    print(f"\n\n\n cwd = {cwd} .\n\n\n")
    
    
    
    global i
        
    
    i = {}
    
    i["i_class"] = i_principal_central_1.i_class()
    
    i["i_class"].i_am_you()
    
    i["i_class"].i_develope()
    
    




    i["i_i_calcul_from_folder"] = i["i_class"].extract_cash(folder_from=new_folder_2, folder_to=new_folder, unity="I", quantity=9, folder_of_source_of_unity=cwd)












