
















import os

import traceback

import sys

import i_math_2



type_of_encoding_0 = "utf-8"


number_of_digit_after_the_floating_point = 20



cwd = os.path.dirname(os.path.abspath(__file__))



class i_banker():

    def __init__(self):
        
        pass
        

    
    
    def from_file_into_the_list(self, name_of_file_of_the_bank):
    
    
        
        
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
                    
                    
                    #print(f"i_hello_0 . counter_0 = {counter_0} . v_0[counter_0][:4] = {v_0[counter_0][:4]} .")
                    
                    if (v_0[counter_0][:4] == " " * (4 * 1)):
                        
                        counter_1 = 0
                        
                        while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                        
                            counter_1 += 1
                        
                        str_identificator = ""
                        
                        
                        counter_1 += 1
                        
                        
                        while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                            
                            
                            str_identificator += v_0[counter_0][counter_1]
                            
                            counter_1 += 1
                            
                            
                        
                        list_of_result.append([int(str_identificator)])
                        
                        
                        
                        counter_0 += 1
                        
                        run_0 = True
                        
                        
                        
                        while ((run_0 == True) and (counter_0 < len(v_0))):
                            
                            
                            if (v_0[counter_0] != ""):
                                
                                #print(f"i_hello_1 . counter_0 = {counter_0} . v_0[counter_0][:(4 * 2)] = {v_0[counter_0][:(4 * 2)]} .")
                                
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
    
    
    
    
    
    
    def from_file_into_the_list_1(self, name_of_file_of_the_bank, number_of_person):
    
    
        
        
        list_of_result = []
        
        
        
        if (os.path.exists(name_of_file_of_the_bank) == True):
            
            
            content_0 = ""
            
            with open(name_of_file_of_the_bank, "r", encoding=type_of_encoding_0) as f_:
                
                content_0 = f_.read(os.path.getsize(name_of_file_of_the_bank))
                
            
            
            
            v_0 = content_0.split("\n")
            
            
            
            counter_of_person_0 = 0
            
            run_2 = True
            
            
            run_0 = True
            
            
            counter_0 = 0
            
            while ((counter_0 < len(v_0)) and (run_2 == True)):
                
                
                if (v_0[counter_0] != ""):
                    
                    
                    #print(f"i_hello_0 . counter_0 = {counter_0} . v_0[counter_0][:4] = {v_0[counter_0][:4]} .")
                    
                    if (v_0[counter_0][:4] == " " * (4 * 1)):
                        
                        counter_1 = 0
                        
                        while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                        
                            counter_1 += 1
                        
                        str_identificator = ""
                        
                        
                        counter_1 += 1
                        
                        
                        while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\"")):
                            
                            
                            str_identificator += v_0[counter_0][counter_1]
                            
                            counter_1 += 1
                            
                            
                        
                        
                        
                        
                        #list_of_result.append([int(str_identificator)])
                        
                        list_of_result.append([str_identificator])
                        
                        
                        
                        counter_of_person_0 += 1
                        
                        if (counter_of_person_0 == number_of_person):
                        
                            run_2 = False
                        
                        
                        
                        
                        counter_0 += 1
                        
                        run_0 = True
                        
                        
                        
                        while ((run_0 == True) and (counter_0 < len(v_0))):
                            
                            
                            if (v_0[counter_0] != ""):
                                
                                #print(f"i_hello_1 . counter_0 = {counter_0} . v_0[counter_0][:(4 * 2)] = {v_0[counter_0][:(4 * 2)]} .")
                                
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
    
    
    
    
    
    
    
    
    def print_into_file(self, name_of_file_of_the_bank, list_of_bank):
        
            
        
        with open(name_of_file_of_the_bank, "w", encoding="utf-8") as f_:
            
            
            f_.write(f"i_bank : \n\n")
            
            
            
            
            counter_0 = 0
            
            while (counter_0 < len(list_of_bank)):
                
                content_0 = f"    identificator : \"{list_of_bank[counter_0][0]}\" \n\n"
                
                
                content_0 += f"        name : \"{list_of_bank[counter_0][1]}\" \n\n"
                
                
                content_0 += f"        pre_name : \"{list_of_bank[counter_0][2]}\" \n\n"
                
                
                content_0 += f"        number_of_phone : \"{list_of_bank[counter_0][3]}\" \n\n"
                
                
                content_0 += f"        e_mail : \"{list_of_bank[counter_0][4]}\" \n\n"
            
    
                content_0 += f"        pass_word : \"{list_of_bank[counter_0][5]}\" \n\n"
                
                
                content_0 += f"        pocket : \n\n\n"
            
            
                f_.write(content_0)
                
                
                content_0 = ""
                
                counter_1 = 0
                
                #print(f"i_hello_1 . list_of_bank[counter_0][-1] = {list_of_bank[counter_0][-1]} .")
                
                while (counter_1 < len(list_of_bank[counter_0][-1])):
                    
                    
                    
                    content_0 += " " * (4 * 3) + f"name_of_unity : \"{list_of_bank[counter_0][-1][counter_1][0]}\" \n\n"
                    
                    
                    content_0 += " " * (4 * 4) + f"amount : \"{list_of_bank[counter_0][-1][counter_1][1]}\" \n\n"
                    
                    
                    
                    counter_1 += 1
                    
                
                f_.write(content_0)
                
                counter_0 += 1
                
            
            
    
    
    def print_into_file_1(self, name_of_file_of_the_bank, list_of_bank, number_of_person):
        
            
        
        with open(name_of_file_of_the_bank, "w", encoding="utf-8") as f_:
            
            
            f_.write(f"i_bank : \n\n")
            
            
            
            
            counter_0 = 0
            
            while ((counter_0 < len(list_of_bank)) and (counter_0 < number_of_person)):
                
                content_0 = f"    identificator : \"{list_of_bank[counter_0][0]}\" \n\n"
                
                
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
                
            
            
        
    
    
    
    def create_personal_account(self, name_of_file_of_the_bank, identificator, name, pre_name, number_of_phone, e_mail, pass_word):
        
        
        if (os.path.exists(name_of_file_of_the_bank) == False):
            
            with open(name_of_file_of_the_bank, "w", encoding=type_of_encoding_0) as f_:
                
                
                f_.write(f"i_bank : \n\n")
                
                number_of_tab = 1
                
                f_.write(" " * (4 * number_of_tab) + f"identificator : \"{identificator}\" \n\n")
                
                            
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
                
                f_.write(" " * (4 * number_of_tab) + f"identificator : \"{identificator}\" \n\n")
                
                            
                number_of_tab += 1
                
                f_.write(" " * (4 * number_of_tab) + f"name : \"{name}\" \n\n")
                
                f_.write(" " * (4 * number_of_tab) + f"pre_name : \"{pre_name}\" \n\n")
                
                f_.write(" " * (4 * number_of_tab) + f"number_of_phone : \"{number_of_phone}\" \n\n")
                
                f_.write(" " * (4 * number_of_tab) + f"e_mail : \"{e_mail}\" \n\n")
                
                f_.write(" " * (4 * number_of_tab) + f"pass_word : \"{pass_word}\" \n\n")
                
                
                f_.write(" " * (4 * number_of_tab) + f"pocket : \n\n")
                
                
                
                
    
    
    
    
    def create_personal_account_1(self, list_of_bank, identificator, name, pre_name, number_of_phone, e_mail, pass_word):
    
    
        
        
        
        
        list_of_bank.append([identificator, name, pre_name, number_of_phone, e_mail, pass_word, []])
        
        
        
    
        return list_of_bank
    
    
    
    
    
    
    def create_new_account_of_amount(self, list_of_bank, identificator, name_of_unity):
        
        
        counter_0 = 0
        
        while ((counter_0 < len(list_of_bank)) and (list_of_bank[counter_0][0] != identificator)):
            
            counter_0 += 1
            
            
        if (counter_0 < len(list_of_bank)):
            
            
                    
            counter_1 = 0
            
            while ((counter_1 < len(list_of_bank[counter_0][-1])) and (list_of_bank[counter_0][-1][counter_1][0] != name_of_unity)):
                
                counter_1 += 1
                
            
            if (counter_1 == len(list_of_bank[counter_0][-1])):
                
                
                list_of_bank[counter_0][-1].append([name_of_unity, "0.0"])
                
            else:
                
                print(f"the name_of_unity = '{name_of_unity}' . exist from before .")
                
                
            
            
        else:
            
            
            print(f"the identificator do not exist .")
            
        
        return list_of_bank
    
    
    
    
    
    
    def affect_amount_to_the_account_with_a_specific_unity(self, list_of_bank, identificator, name_of_unity, amount):
        
        
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
    
    
    
    
    
    
    
    def read_amount_to_the_account_with_a_specific_unity(self, list_of_bank, identificator, name_of_unity):
        
        
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
    
    
    
    
    
    
    
    
    def add_amount_to_the_account_with_a_specific_unity(self, list_of_bank, identificator, name_of_unity, amount_to_add):
        
        
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
                
                operation = f"{amount}+{amount_to_add}"
                
                
                m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                
                if (m[0] == False):
                    
                    
                    list_of_bank[counter_0][-1][counter_1][1] = m[1][0]
                    
                
                
            
            else:
                
                print(f"the name_of_unity do not exist .")
                
                
            
            
                    
            
        else:
            
            
            print(f"the identificator do not exist .")
            
        
        return list_of_bank
    
    
    
    
    
    
    
    def transfer_amount_from_an_account_to_another_with_gain(self, list_of_bank, identificator_0, identificator_1, identificator_gainer_0, name_of_unity, amount_to_transfere, gain):
        
        
            
                
        
        
        counter_0 = 0
        
        while ((counter_0 < len(list_of_bank)) and (list_of_bank[counter_0][0] != identificator_0)):
            
            counter_0 += 1
            
        amount_0 = "0.0"
            
        if (counter_0 < len(list_of_bank)):
            
            
            counter_1 = 0
            
            while ((counter_1 < len(list_of_bank[counter_0][-1])) and (list_of_bank[counter_0][-1][counter_1][0] != name_of_unity)):
                
                counter_1 += 1
                
            
            
            if (counter_1 < len(list_of_bank[counter_0][-1])):
                
                amount_0 = list_of_bank[counter_0][-1][counter_1][1]
                
                
                
                            
                counter_2 = 0
                
                while ((counter_2 < len(list_of_bank)) and (list_of_bank[counter_2][0] != identificator_1)):
                    
                    counter_2 += 1
                    
                amount_1 = "0.0"
                    
                if (counter_2 < len(list_of_bank)):
                    
                    
                    counter_3 = 0
                    
                    while ((counter_3 < len(list_of_bank[counter_2][-1])) and (list_of_bank[counter_2][-1][counter_3][0] != name_of_unity)):
                        
                        counter_3 += 1
                        
                    
                    
                    if (counter_3 < len(list_of_bank[counter_2][-1])):
                        
                        amount_1 = list_of_bank[counter_2][-1][counter_3][1]
                        
                        
                        
                        
                        operation = f"{amount_0}-{amount_to_transfere}-{gain}"
                        
                        
                        m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                        
                        if (m[0] == False):
                            
                            
                            
                                                    
                            
                            s1 = m[1][0]
                            
                            s2 = "0.0"
                            
                            
                            bool_0 = i_math_2.my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                            
                            bool_1 = i_math_2.my_egale_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                            
                            print(f"i_hello_4 .operation = {operation} . m = {m} . bool_0 = {bool_0} . bool_1 = {bool_1} .")
                            
                            
                            
                            if ((bool_0 == True) or (bool_1 == True)):
                                
                                
                                list_of_bank[counter_0][-1][counter_1][1] = m[1][0]
                                
                                
                                
                                                        
                                operation = f"{amount_1}+{amount_to_transfere}"
                                
                                
                                
                                m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                                
                                
                                
                                print(f"i_hello_5 .operation = {operation} . m = {m} . bool_0 = {bool_0} . bool_1 = {bool_1} .")
                                                  
                                
                                if (m[0] == False):
                                    
                                              
                                    
                                    list_of_bank[counter_2][-1][counter_3][1] = m[1][0]
                                    
                                    
                                                                    
                                                            
                                    
                                    s1 = f"{gain}"
                                    
                                    s2 = "0.0"
                                    
                                    
                                    
                                    bool_2 = i_math_2.my_superieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
                                    
                                    
                                    if (bool_2 == True):
                                        
                                        
                                                                            
                                        counter_4 = 0
                                        
                                        while ((counter_4 < len(list_of_bank)) and (list_of_bank[counter_4][0] != identificator_gainer_0)):
                                            
                                            counter_4 += 1
                                            
                                        amount_2 = "0.0"
                                        
                                        if (counter_4 < len(list_of_bank)):
                                            
                                            print(f"i_hello_0 .")
                                            
                                            counter_5 = 0
                                            
                                            while ((counter_5 < len(list_of_bank[counter_4][-1])) and (list_of_bank[counter_4][-1][counter_5][0] != name_of_unity)):
                                                
                                                counter_5 += 1
                                                
                                            
                                            
                                            if (counter_5 < len(list_of_bank[counter_4][-1])):
                                                
                                                
                                                
                                                amount_2 = list_of_bank[counter_4][-1][counter_5][1]
                                                
                                                
                                                operation = f"{amount_2}+{gain}"
                                                
                                                
                                                
                                                m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                                                
                                                                                               
                                                
                                                if (m[0] == False):
                                                    
                                                              
                                                    
                                                    list_of_bank[counter_4][-1][counter_5][1] = m[1][0]
                                                    
                                                    
                                        
                                        
                                    
                                    
                            
                            else:
                                
                                print(f"the amount result-ed is negative .")
                                
                                
                            
            
            else:
                
                print(f"the name_of_unity do not exist .")
                
                
            
            
                    
            
        else:
            
            
            print(f"the identificator do not exist .")
            
        
        return list_of_bank
    
    
    
    
    def generate_new_identificator(self, list_of_bank):
        
            
        identificator_0 = 1
        
        
        
        run_0 = True
        
        
        while (run_0 == True):
        
        
            counter_0 = 0
            
            while ((counter_0 < len(list_of_bank)) and (list_of_bank[counter_0][0] != int(identificator_0))):
                
                counter_0 += 1
                
            
            if (counter_0 < len(list_of_bank)):
                
                
                identificator_0 += 1
                
            
            else:
                
                run_0 = False
                
            
        return identificator_0
        
    
    
    
    def create_personal_account_2(self, list_of_bank, name, pre_name, number_of_phone, e_mail, pass_word):
    
                
        new_identificator_1 = self.generate_new_identificator(list_of_bank=list_of_bank)
        
        list_of_bank = self.create_personal_account_1(list_of_bank=list_of_bank, identificator=str(new_identificator_1), name=name, pre_name=pre_name, number_of_phone=number_of_phone, e_mail=e_mail, pass_word=pass_word)
        
        return list_of_bank
        
    
    
    
    
    
    
    def from_list_of_file_into_the_list(self, list_of_name_of_file_of_the_bank):
    
        
        list_of_result = []
        
        
        
        counter_0 = 0
        
        while (counter_0 < len(list_of_name_of_file_of_the_bank)):
            
            
            element = self.from_file_into_the_list(name_of_file_of_the_bank=list_of_name_of_file_of_the_bank[counter_0])
            
            if (len(element) > 0):
                
                
                list_of_result.extend(self.from_file_into_the_list(name_of_file_of_the_bank=list_of_name_of_file_of_the_bank[counter_0]))
                
            
            element.clear()
            
            counter_0 += 1
            
            
        
        return list_of_result
    
    
    
    
    
    
    
    def make_big_number(self, length_of_number):
        
        
                
        
        # construction of : 'big_number' 
        
        
        
        
        
        big_amount = "1"
        
        counter_0 = 0
        
        while (counter_0 < length_of_number):
            
            big_amount += "0"
            
            counter_0 += 1
            
        
        big_amount += "."
        
        counter_0 = 0
        
        while (counter_0 < 1_000):
            
            big_amount += "0"
            
            counter_0 += 1
            
        
        
        return big_amount
    
        
    
        
    
    
    
    def print_official_account_1(self, file_of_bank_official, list_of_unity, identificator, name, pre_name, number_of_phone, e_mail, pass_word):
        
        
        
            
        
        

        
        # list_of_bank_official initialize-ed  
        
        
        list_of_bank_official = []
        
        
        
        # creation of my account : 'principal-central'
        
        
        list_of_bank_official = self.create_personal_account_1(list_of_bank=list_of_bank_official, identificator=identificator, name=name, pre_name=pre_name, number_of_phone=number_of_phone, e_mail=e_mail, pass_word=pass_word)        
        
        
        
        
        # construction of : 'big_number' 
        
        
        
        
        big_amount = self.make_big_number(length_of_number=1_000)
        
        

        

        
        
        # upload into the list_of_bank_official 
        
        
        
        
        
        counter_0 = 0
        
        while (counter_0 < len(list_of_unity)):
            
                        
            
            unity_0 = list_of_unity[counter_0]
            
            
            list_of_bank_official = self.create_new_account_of_amount(list_of_bank=list_of_bank_official, identificator=identificator, name_of_unity=f"[{unity_0}]")
                    
            self.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank_official, identificator=identificator, name_of_unity=f"[{unity_0}]", amount=big_amount)
            
            
            list_of_bank_official = self.create_new_account_of_amount(list_of_bank=list_of_bank_official, identificator=identificator, name_of_unity=f"the quality of [{unity_0}]")
                    
            self.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank_official, identificator=identificator, name_of_unity=f"the quality of [{unity_0}]", amount=big_amount)
            
            

            
            
            counter_0 += 1
            
            
        
        
        
        
        
        # print_into_file 
        
        
        
        self.print_into_file(name_of_file_of_the_bank=file_of_bank_official, list_of_bank=list_of_bank_official)
        
        
        
        
    
    
    
    def print_my_official_account(self):
        
        
        
            
        
        
        
        # name of file of the bank 
        
        
        file_bank_official_1 = os.path.join(cwd, "bank_official_1.i_bank")
        
        
        # list_of_bank_official initialize-ed  
        
        
        list_of_bank_official = []
        
        
        
        # creation of my account : 'principal-central'
        
        
        list_of_bank_official = self.create_personal_account_1(list_of_bank=list_of_bank_official, identificator="0", name="billal", pre_name="debouci", number_of_phone="+213 561577437", e_mail="deboubil24@gmail.com", pass_word="i_male_principal_central_pass_word_0")        
        
        
        
        
        # construction of : 'big_number' 
        
        
        big_amount = self.make_big_number(length_of_number=1_000)
        

        
        # list_of_unity 
        
        
        
        
        list_of_unity = [
                            "i", "resource", "money", "computer", "power", "intelli",
                            
                            
                            
                            
        ]
        
        
        
        
        
        
        
        # upload into the list_of_bank_official 
        
        
        
        
        counter_0 = 0
        
        while (counter_0 < len(list_of_unity)):
            
                        
            
            unity_0 = list_of_unity[counter_0]
            
            
            list_of_bank_official = self.create_new_account_of_amount(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"[{unity_0}]")
                    
            self.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"[{unity_0}]", amount=big_amount)
            
            
            list_of_bank_official = self.create_new_account_of_amount(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"the quality of [{unity_0}]")
                    
            self.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"the quality of [{unity_0}]", amount=big_amount)
            
            
                        
            
            list_of_bank_official = self.create_new_account_of_amount(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"[{unity_0}]-s")
                    
            self.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"[{unity_0}]-s", amount=big_amount)
            
            
            list_of_bank_official = self.create_new_account_of_amount(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"the quality of [{unity_0}]-s")
                    
            self.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank_official, identificator="0", name_of_unity=f"the quality of [{unity_0}]-s", amount=big_amount)
            
            
            
            
            counter_0 += 1
            
            
        
        
        
        
        
        # print_into_file 
        
        
        
        self.print_into_file(name_of_file_of_the_bank=file_bank_official_1, list_of_bank=list_of_bank_official)
        
        
        
        
    
        
        
    
    






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
                
            
            function_11 : 
                
                
                generate_new_identificator
                
            
        '''
        
        
        
        
        
        
        object_of_banker = i_banker()
        
        
        
        file_0 = os.path.join(cwd, "bank_0.the_bank")
        
        
        
        object_of_banker.create_personal_account(name_of_file_of_the_bank=file_0, identificator="2", name="billal", pre_name="debouci", number_of_phone="+213 123456789", e_mail="e_mil_0@e_mail.com", pass_word="i_male_principal_central_pass_word_0")
        
        
        #list_of_bank = from_file_into_the_list(name_of_file_of_the_bank=file_0)
        
        
        list_of_bank = object_of_banker.from_list_of_file_into_the_list(list_of_name_of_file_of_the_bank=[file_0])
        
        
        
        file_1 = os.path.join(cwd, "bank_1.the_bank")
        
        object_of_banker.print_into_file(name_of_file_of_the_bank=file_1, list_of_bank=list_of_bank)
        
        
        
        
        list_of_bank = object_of_banker.create_new_account_of_amount(list_of_bank=list_of_bank, identificator="2", name_of_unity="USD")
        
        #list_of_bank = create_new_account_of_amount(list_of_bank=list_of_bank, identificator="2", name_of_unity="USD")
        
        
        list_of_bank = object_of_banker.create_new_account_of_amount(list_of_bank=list_of_bank, identificator="0", name_of_unity="USD")
        
        
        object_of_banker.affect_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank, identificator="2", name_of_unity="USD", amount="100.0")
        
        
        amount = object_of_banker.read_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank, identificator="2", name_of_unity="USD")
        
        print(f"i_hello_2 . amount_read-ed = {amount} .")
        
        
        
        
        operation = "1+1"
        
        
        m = i_math_2.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
        
        print(f"i_hello_3 . m = {m} .")
        
        
        list_of_bank = object_of_banker.transfer_amount_from_an_account_to_another_with_gain(list_of_bank=list_of_bank, identificator_0="2", identificator_1="0", identificator_gainer_0="2", name_of_unity="USD", amount_to_transfere="10.0", gain="1.0")
        
        
        
        
        #list_of_bank = add_amount_to_the_account_with_a_specific_unity(list_of_bank=list_of_bank, identificator=2, name_of_unity="USD", amount_to_add="-10")
        
                
        file_2 = os.path.join(cwd, "bank_2.the_bank")
        
        object_of_banker.print_into_file(name_of_file_of_the_bank=file_2, list_of_bank=list_of_bank)
        
        
        
        
        
        list_of_bank_1 = object_of_banker.from_file_into_the_list_1(name_of_file_of_the_bank=file_2, number_of_person=10)
        
        
        new_identificator_0 = object_of_banker.generate_new_identificator(list_of_bank=list_of_bank)
        
        print(f"new_identificator_0 = {new_identificator_0} .")
        
        
        list_of_bank = object_of_banker.create_personal_account_1(list_of_bank=list_of_bank, identificator=str(new_identificator_0), name="billal", pre_name="debouci", number_of_phone="+213 123456789", e_mail="e_mil_0@e_mail.com", pass_word="i_male_principal_central_pass_word_0")
        
        
                
        file_3 = os.path.join(cwd, "bank_3.the_bank")
        
        object_of_banker.print_into_file(name_of_file_of_the_bank=file_3, list_of_bank=list_of_bank)
        
        
        
        list_of_bank_2 = []
        
        
        
        
        
        file_4 = os.path.join(cwd, "bank_4.the_bank")
        
        
        list_of_bank_2 = object_of_banker.from_file_into_the_list(name_of_file_of_the_bank=file_4)
        
                
        new_identificator_1 = object_of_banker.generate_new_identificator(list_of_bank=list_of_bank_2)
        
        print(f"new_identificator_1 = {new_identificator_1} .")
        

        list_of_bank_2 = object_of_banker.create_personal_account_1(list_of_bank=list_of_bank_2, identificator=str(new_identificator_1), name="billal", pre_name="debouci", number_of_phone="+213 123456789", e_mail="e_mil_0@e_mail.com", pass_word="i_male_principal_central_pass_word_0")        
        
        
        object_of_banker.print_into_file(name_of_file_of_the_bank=file_4, list_of_bank=list_of_bank_2)
        
        
        
        
        
        
        
        
        
        # my work 
        
        
        object_of_banker.print_my_official_account()
        
        
        
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
    
        
        
        
    
    
    
    
    


if __name__ == "__main__":


    main()













