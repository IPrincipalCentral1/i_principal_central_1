
















import os

import traceback

import sys

import i_math_2



type_of_encoding_0 = "utf-8"






def from_file_into_the_list(name_of_file_of_the_bank):


    
    
    list_of_result = []
    
    
    
    if (os.path.exists(name_of_file_of_the_bank) == True):
        
        
        content_0 = ""
        
        with open(name_of_file_of_the_bank, "r", encoding=type_of_encoding_0) as f_:
            
            content_0 = f_.read(os.path.getsize(name_of_file_of_the_bank))
            
        
        
        
        v_0 = content_0.split("\n")
        
        
        run_0 = True
        
        
        counter_0 = 0
        
        while (counter_0 < len(v_0)):
            
            
            if (v_0[counter_0] != ""):
                
                
                print(f"i_hello_0 . counter_0 = {counter_0} . v_0[counter_0][:4] = {v_0[counter_0][:4]} .")
                
                if (v_0[counter_0][:4] == " " * (4 * 1)):
                    
                    counter_1 = 0
                    
                    while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                    
                        counter_1 += 1
                    
                    str_identificater = ""
                    
                    
                    counter_1 += 1
                    
                    
                    while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                        
                        
                        str_identificater += v_0[counter_0][counter_1]
                        
                        counter_1 += 1
                        
                        
                    
                    list_of_result.append([int(str_identificater)])
                    
                    
                    
                    counter_0 += 1
                    
                    run_0 = True
                    
                    
                    
                    while ((run_0 == True) and (counter_0 < len(v_0))):
                        
                        
                        if (v_0[counter_0] != ""):
                            
                            print(f"i_hello_1 . counter_0 = {counter_0} . v_0[counter_0][:(4 * 2)] = {v_0[counter_0][:(4 * 2)]} .")
                            
                            if (v_0[counter_0][:(4 * 2)] == " " * (4 * 2)):
                                
                                
                                
                                                                
                                if (v_0[counter_0][(4 * 2):(4 * 2) + len("pocket")] == "pocket"):
                                
                                    
                                    list_of_result[-1].append([])
                                    
                                    counter_0 += 1
                                    
                                    run_1 = True
                                    
                                    while ((run_1 == True) and (counter_0 < len(v_0))):
                                        
                                        
                                        if (v_0[counter_0] != ""):
                                            
                                            
                                            
                                            if (v_0[counter_0][:(4 * 3)] == " " * (4 * 3)):
                                                
                                                                                                
                                                
                                                counter_1 = 0
                                                
                                                while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                                                
                                                    counter_1 += 1
                                                
                                                str_element = ""
                                                
                                                
                                                counter_1 += 1
                                                
                                                while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                                                    
                                                    
                                                    str_element += v_0[counter_0][counter_1]
                                                    
                                                    counter_1 += 1
                                                    
                                                    
                                                
                                                counter_0 += 1
                                                
                                                
                                                while ((counter_0 < len(v_0)) and (v_0[counter_0] == "")):
                                                    
                                                    counter_0 += 1
                                                
                                                                                                
                                                counter_1 = 0
                                                
                                                while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                                                
                                                    counter_1 += 1
                                                
                                                str_element_1 = ""
                                                
                                                
                                                counter_1 += 1
                                                
                                                while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                                                    
                                                    
                                                    str_element_1 += v_0[counter_0][counter_1]
                                                    
                                                    counter_1 += 1
                                                    
                                                    
                                                
                                                list_of_result[-1][-1].append([str_element, str_element_1])
                                                    
                                            
                                            else:
                                            
                                            
                                                counter_0 -= 1
                                            
                                                run_1 = False    
                                                
                                            
                                        
                                        if (run_1 == True):
                                            
                                            counter_0 += 1
                                        
                                        
                                    
                                    
                                    
                                    
                                    run_0 = False
                                    
                                else:
                                    
                                        
                                    
                                    
                                    counter_1 = 0
                                    
                                    while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                                    
                                        counter_1 += 1
                                    
                                    str_element = ""
                                    
                                    
                                    counter_1 += 1
                                    
                                    while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                                        
                                        
                                        str_element += v_0[counter_0][counter_1]
                                        
                                        counter_1 += 1
                                        
                                        
                                        
                                    list_of_result[-1].append(str_element)
                                        
                            
                            else:
                            
                            
                                run_0 = False
                            
                        
                        if (run_0 == True):
                            
                            counter_0 += 1
            
            
            
            
            counter_0 += 1
            
        

    return list_of_result


def print_into_file(name_of_file_of_the_bank, list_of_bank):
    
        
    
    with open(name_of_file_of_the_bank, "w", encoding="utf-8") as f_:
        
        
        f_.write(f"i_bank : \n\n")
        
        
        
        
        counter_0 = 0
        
        while (counter_0 < len(list_of_bank)):
            
            content_0 = f"    identificater : \"{list_of_bank[counter_0][0]}\" \n\n"
            
            
            content_0 += f"        name : \"{list_of_bank[counter_0][1]}\" \n\n"
            
            
            content_0 += f"        pre_name : \"{list_of_bank[counter_0][2]}\" \n\n"
            
            
            content_0 += f"        number_of_phone : \"{list_of_bank[counter_0][3]}\" \n\n"
            
            
            content_0 += f"        e_mail : \"{list_of_bank[counter_0][4]}\" \n\n"
        

            content_0 += f"        pass_word : \"{list_of_bank[counter_0][5]}\" \n\n"
            
            
            content_0 += f"        pocket : \n\n\n"
        
        
            f_.write(content_0)
            
            
            content_0 = ""
            
            counter_1 = 0
            
            while (counter_1 < len(list_of_bank[counter_0][-1])):
                
                
                content_0 += " " * (4 * 3) + f"name_of_unity : \"{list_of_bank[counter_0][-1][counter_1][0]}\" \n\n"
                
                
                content_0 += " " * (4 * 4) + f"amount : \"{list_of_bank[counter_0][-1][counter_1][1]}\" \n\n"
                
                
                
                counter_1 += 1
                
            
            f_.write(content_0)
            
            counter_0 += 1
            
        
        
    


def create_personal_account(name_of_file_of_the_bank, identificater, name, pre_name, number_of_phone, e_mail, pass_word):
    
    
    if (os.path.exists(name_of_file_of_the_bank) == False):
        
        with open(name_of_file_of_the_bank, "w", encoding=type_of_encoding_0) as f_:
            
            
            f_.write(f"i_bank : \n\n")
            
            number_of_tab = 1
            
            f_.write(" " * (4 * number_of_tab) + f"identificater : \"{identificater}\" \n\n")
            
                        
            number_of_tab += 1
            
            f_.write(" " * (4 * number_of_tab) + f"name : \"{name}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pre_name : \"{pre_name}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"number_of_phone : \"{number_of_phone}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"e_mail : \"{e_mail}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pass_word : \"{pass_word}\" \n\n")
            
            
            f_.write(" " * (4 * number_of_tab) + f"pocket : \n\n")
            
            
            
    else:
        
        
        content_0 = ""
        
        with open(name_of_file_of_the_bank, "r", encoding=type_of_encoding_0) as f_:
            
            content_0 = f_.read(os.path.getsize(name_of_file_of_the_bank))
            
                
        with open(name_of_file_of_the_bank, "w", encoding=type_of_encoding_0) as f_:
            
            
            f_.write(content_0 + "\n")
            
            number_of_tab = 1
            
            f_.write(" " * (4 * number_of_tab) + f"identificater : \"{identificater}\" \n\n")
            
                        
            number_of_tab += 1
            
            f_.write(" " * (4 * number_of_tab) + f"name : \"{name}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pre_name : \"{pre_name}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"number_of_phone : \"{number_of_phone}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"e_mail : \"{e_mail}\" \n\n")
            
            f_.write(" " * (4 * number_of_tab) + f"pass_word : \"{pass_word}\" \n\n")
            
            
            f_.write(" " * (4 * number_of_tab) + f"pocket : \n\n")
            
            
            
            



def create_new_account_of_amount(list_of_bank, identificator, name_of_unity):
    
    
    counter_0 = 0
    
    while ((counter_0 < len(list_of_bank)) and (list_of_bank[counter_0][0] != identificator)):
        
        counter_0 += 1
        
        
    if (counter_0 < len(list_of_bank)):
        
        
        list_of_bank[counter_0][-1].append([name_of_unity, "0.0"])
        
        
    else:
        
        
        print(f"the identificator do not exist .")
        
    
    return list_of_bank






def affect_amount_to_the_account_with_a_specific_unity(list_of_bank, identificator, name_of_unity, amount):
    
    
    counter_0 = 0
    
    while ((counter_0 < len(list_of_bank)) and (list_of_bank[counter_0][0] != identificator)):
        
        counter_0 += 1
        
        
    if (counter_0 < len(list_of_bank)):
        
        
        counter_1 = 0
        
        while ((counter_1 < len(list_of_bank[counter_0][-1])) and (list_of_bank[counter_0][-1][counter_1][0] != name_of_unity)):
            
            counter_1 += 1
            
        
        
        if (counter_1 < len(list_of_bank[counter_0][-1])):
            
            list_of_bank[counter_0][-1][counter_1][1] = amount
        
        else:
            
            print(f"the name_of_unity do not exist .")
            
            
        
        
                
        
    else:
        
        
        print(f"the identificator do not exist .")
        
    
    return list_of_bank







def read_amount_to_the_account_with_a_specific_unity(list_of_bank, identificator, name_of_unity):
    
    
    counter_0 = 0
    
    while ((counter_0 < len(list_of_bank)) and (list_of_bank[counter_0][0] != identificator)):
        
        counter_0 += 1
        
    amount = "0.0"
        
    if (counter_0 < len(list_of_bank)):
        
        
        counter_1 = 0
        
        while ((counter_1 < len(list_of_bank[counter_0][-1])) and (list_of_bank[counter_0][-1][counter_1][0] != name_of_unity)):
            
            counter_1 += 1
            
        
        
        if (counter_1 < len(list_of_bank[counter_0][-1])):
            
            amount = list_of_bank[counter_0][-1][counter_1][1]
        
        else:
            
            print(f"the name_of_unity do not exist .")
            
            
        
        
                
        
    else:
        
        
        print(f"the identificator do not exist .")
        
    
    return amount






def main():

    
    
    
    try:
        
        
        
        
        
        
        '''
        
        
        comment :
            
            
            function_0 :
                
                
                create_personal_account
                
                
            function_1 : 
                
                
                create_new_account_of_amount
                
            
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
                
                
            function_8 :
                
                
                from_file_into_the_list
                
                
            function_9 :
                
                
                print_into_file
                
                
            function_10 : 
            
                read_amount_to_the_account_with_a_specific_unity
                
                
        '''
        
        
        
        
        
        cwd = os.path.dirname(os.path.abspath(__file__))
        
        
        
        file_0 = os.path.join(cwd, "bank_0.the_bank")
        
        create_personal_account(name_of_file_of_the_bank=file_0, identificater="2", name="billal", pre_name="debouci", number_of_phone="+213 123456789", e_mail="e_mil_0@e_mail.com", pass_word="i_male_principal_central_pass_word_0")
        
        
        list_of_bank = from_file_into_the_list(name_of_file_of_the_bank=file_0)
        
        
        file_1 = os.path.join(cwd, "bank_1.the_bank")
        
        print_into_file(name_of_file_of_the_bank=file_1, list_of_bank=list_of_bank)
        
        
        
        
        list_of_bank = create_new_account_of_amount(list_of_bank=list_of_bank, identificator=2, name_of_unity="USD")
        
        
        list_of_bank = create_new_account_of_amount(list_of_bank=list_of_bank, identificator=2, name_of_unity="EUR")
        
        
        affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank, identificator=2, name_of_unity="USD", amount="100.0")
        
        
        amount = read_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank, identificator=2, name_of_unity="USD")
        
        print(f"i_hello_2 . amount_read-ed = {amount} .")
        
                
        file_2 = os.path.join(cwd, "bank_2.the_bank")
        
        print_into_file(name_of_file_of_the_bank=file_2, list_of_bank=list_of_bank)
        
        
        
        
        
        
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
    
        
        
        
    
    
    
    
    


if __name__ == "__main__":


    main()













