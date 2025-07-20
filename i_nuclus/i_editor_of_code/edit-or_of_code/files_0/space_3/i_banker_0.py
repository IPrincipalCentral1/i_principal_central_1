
















import os

import traceback

import sys




type_of_encoding_0 = "utf-8"






def create_personal_account(name_of_file_of_the_bank, identificater, name, pre_name, number_of_phone, e_mail, pass_word):
    
    
    if (os.path.exists(name_of_file_of_the_bank) == False):
        
        with open(name_of_file_of_the_bank, "w", encoding=type_of_encoding_0) as f_:
            
            
            f_.write(f"i_bank : \n\n")
            
            number_of_tab = 1
            
            f_.write(" " * (4 * number_of_tab) + f"{identificater} : \n\n")
            
                        
            number_of_tab += 1
            
            f_.write(" " * (4 * number_of_tab) + f"name : \"{name}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pre_name : \"{pre_name}\" : \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"number_of_phone : \"{number_of_phone}\" : \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"e_mail : \"{e_mail}\" : \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pass_word : \"{pass_word}\" : \n\n")
            
            
            f_.write(" " * (4 * number_of_tab) + f"pocket : \n\n")
            
            
            
    else:
        
        
        content_0 = ""
        
        with open(name_of_file_of_the_bank, "r", encoding=type_of_encoding_0) as f_:
            
            content_0 = f_.read(os.path.getsize(name_of_file_of_the_bank))
            
                
        with open(name_of_file_of_the_bank, "w", encoding=type_of_encoding_0) as f_:
            
            
            f_.write(content_0 + "\n\n")
            
            number_of_tab = 1
            
            f_.write(" " * (4 * number_of_tab) + f"{identificater} : \n\n")
            
                        
            number_of_tab += 1
            
            f_.write(" " * (4 * number_of_tab) + f"name : \"{name}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pre_name : \"{pre_name}\" : \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"number_of_phone : \"{number_of_phone}\" : \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"e_mail : \"{e_mail}\" : \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pass_word : \"{pass_word}\" : \n\n")
            
            
            f_.write(" " * (4 * number_of_tab) + f"pocket : \n\n")
            
            
            
            


def main():

    
    
    
    try:
        
        
        
        
        cwd = os.path.dirname(os.path.abspath(__file__))
        
        
        
        
        '''
        
        
        comment :
            
            
            function_0 :
                
                create_personal_account
            
            function_1 : 
                
                create_new_account_with_new_unity
                
            
            function_2 : 
                
                affect_amount_to_the_account_with_a_specific_unity
                
            function_3 :
                
                add_amount_to_the_account_with_a_specific_unity
            
                        
            function_4 :
                
                substrut_amount_to_the_account_with_a_specific_unity
                
            
            function_5 :
                
                transfer_amount_from_an_account_to_another_with_gain
                
            function_6 :
                            
                making_the_mesurment_between_unitys
            
                        
            function_7 :
            
                
                transforming_from_a_unity_to_another
                
            
        '''
        
        
        
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
    
        
        
        
    
    
    
    
    


if __name__ == "__main__":


    main()













