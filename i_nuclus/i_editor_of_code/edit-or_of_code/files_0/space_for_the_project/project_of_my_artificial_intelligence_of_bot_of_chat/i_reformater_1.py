














list_of_liberary_to_install = [
                            
                            

]










import os


import traceback

import sys


import subprocess





#print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


#subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])




#try:

    #counter_0 = 0


    #while (counter_0 < len(list_of_liberary_to_install)):



        #try:


            #print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")

            #subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])



        #except:



            #traceback.print_exc()

            #error = traceback.format_exc()

            #semaphore = True

            #print(f"Erreur : {str(error)}")



        #counter_0 += 1



#except:



    #traceback.print_exc()

    #error = traceback.format_exc()

    #semaphore = True

    #print(f"Erreur : {str(error)}")









import time


import i_math_i_am_i_0



cwd = os.path.dirname(os.path.abspath(__file__))









def i_calculat_and_display_in_the_loop_0(first_time, amount_of_time_0, var_0):
    
    
    
    
    '''
    
    this function is designed so you add the code that you want to do each time in a loop .
    
    
    
    
    this is how to use this function :
    
    
    import time
        
    
    t1 = time.time()
    
    while (True):
        
        
        # do some calculations 
        
        
        # each 2.0 second .
        
        t1 = i_calculat_and_display_in_the_loop_0(first_time=t1, amount_of_time_0=2.0)
        
        
        # do some other calculations 
        
        
        
        
    
    
    
    
    
    
    '''
    
    
    
    if (time.time() - first_time > amount_of_time_0):
        
        
        # -------------------------------------------------
        
        # this place is for the main of your calculations :
        
        # you can display what you want right here .
        
        # you can add your code right here
        
        
        print(f"i_hello_0 .")
        
        print(f"i_hello_1 . var_0 = {var_0} .")
        
        
        
        
        
        
        
        pass
        
        
        
        
        
        return time.time()
    
    else:
        
        return first_time
        
        
        
    
    
    





def main_string_0(main_, ele, n):


    v = main_[0]



    v1 = ele

    one_ = True

    one = True

    # anné

    if (v <= v1):

        if (v < v1):

            one_ = False


    else:

        one = False


    if (not one_):

        return main_

    elif (one):

        return main_

    else:

        return (ele, n, )




def sort_element_0_1(l):

    
    l_ = []
    
    
    while (0 < len(l)):
        
        i_counter_0 = 0
        
        main_ = (l[i_counter_0][0], i_counter_0, )
        
        
        
        while (i_counter_0 < len(l)):
            
            main_0 = main_string_0(main_=main_, ele=l[i_counter_0][0], n=i_counter_0)
            
            
            
            if (main_0 != main_):
            
                main_ = main_0
            
            i_counter_0 += 1
        
        
        l_.append(l[main_[1]])
        
        
        l.pop(main_[1])
    
    
    
    
    return l_





def sort_element_1_1(l):

    
    l_ = []
    
    t1 = time.time()
    
    m_0 = len(l)
    
    
    while (0 < len(l)):
        
        i_counter_0 = 0
        
        main_ = (l[i_counter_0], i_counter_0, )
        
        
        
        while (i_counter_0 < len(l)):
            
            main_0 = main_string_0(main_=main_, ele=l[i_counter_0], n=i_counter_0)
            
            
            
            if (main_0 != main_):
            
                main_ = main_0
            
            i_counter_0 += 1
        
        
        
        l_.append(l[main_[1]])
        
        
        l.pop(main_[1])
    
    
    
    
    return l_










def main_string_1(main_, ele, n):


    v = main_[0]



    v1 = ele


    if (v > v1):

        return main_

    else:

        return (ele, n, )




def sort_element_0_0(l):

    
    l_ = []
    
    while (0 < len(l)):
        
        i = 0
        
        main_ = (l[i][0], i, )
        
        
        
        while (i < len(l)):
            
            main_0 = main_string_1(main_=main_, ele=l[i][0], n=i)
            
            
            
            if (main_0 != main_):
            
                main_ = main_0
            
            i += 1
        
        
        l_.append(l[main_[1]])
        
        
        l.pop(main_[1])
    
    
    
    
    return l_




    
    

def finder_and_spliter_2(element_0, element_1):
    
    
            
    i_counter_1 = 0
    
    
    i_list_of_result_0 = []
    
    
    if (len(element_0) > 0):
        
        
        
        semaphore_of_add_0 = True
        
        
        i_counter_0 = 0
        
                
        
        i_counter_3 = 0
        
        
        
                
        i_content_0 = ""
        
        
        while (i_counter_0 < len(element_1)):
            
            
            
            
            i_counter_0 = i_counter_3
            
            i_counter_2 = 0
            
            #print(f"i_hello_0 . i_counter_3 = {i_counter_3} . i_counter_1 = {i_counter_1} .")
            
            
            while ((i_counter_2 < len(element_0)) and (i_counter_0 < len(element_1)) and (element_0[i_counter_2] == element_1[i_counter_0])):
                
                
                #print(f"    i_hello_1 . in the loop of while . element_1[i_counter_0] = {element_1[i_counter_0]} .")
                
                i_counter_0 += 1
                
                i_counter_2 += 1
            
            
            #print(f"i_hello_4 . i_content_0 = \"{i_content_0}\" .")
            
                
            
            if (i_counter_2 == len(element_0)):
                
                i_counter_1 += 1
                
                i_counter_3 = i_counter_0
                
                
                # space to append into the list i_list_of_result_0 .
                
                
                
                i_list_of_result_0.append(i_content_0)
                
                
                #print(f"    i_hello_3 . in the first if . i_content_0 = \"{i_content_0}\" .")
                
                
                semaphore_of_add_0 = False
                
                i_content_0 = ""
                
                
                
                
            else:
            
                
                # this space for the incrementation of string .
                
                
                if (i_counter_3 < len(element_1)):
                    
                    
                    i_content_0 += element_1[i_counter_3]
                    
                    semaphore_of_add_0 = True
                    
                    #print(f"    i_hello_2 . in the second if . i_content_0 = \"{i_content_0}\" .")
                    
                    
                    
                
                
                
                
                i_counter_3 += 1
                
                
                
                
            #print(f"i_hello_5 . i_content_0 = \"{i_content_0}\" .")
                
            
            
            
            
        
        if (semaphore_of_add_0 == True):
            
            i_list_of_result_0.append(i_content_0)
        
    else:
        
        i_counter_1 = -1
        
        
    return [i_counter_1, i_list_of_result_0]







def extracting_the_not_counted_words(i_list_of_result_0, not_counted_words):
    
    
    
        
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(not_counted_words)):
        
        
        i_counter_2 = 0
        
        
        while (i_counter_2 < len(i_list_of_result_0)):
            
            
            if (i_list_of_result_0[i_counter_2] == not_counted_words[i_counter_0]):
                
                i_list_of_result_0.pop(i_counter_2)
                
            else:
                
                i_counter_2 += 1
                
                
            
        i_counter_0 += 1
    
    
    return i_list_of_result_0






def finder_and_spliter_0(element_0, element_1, not_counted_words):
    
    
    # element_0 is a list 
    
    '''
    
    element_1 : string 
    
    element_0 : list_of_string 
    
    not_counted_words : list_of_string 
    
    
    
    this function split the element_1 according to element_0 into a list . 
    
    after that it will delete not_counted_words from this list .
    
    
    
    '''
    
               
    i_counter_1 = 0
    
    
    i_list_of_result_0 = []
    
    
    if (len(element_0) > 0):
        
        
        
        semaphore_of_add_0 = True
        
        
        
        i_counter_3 = 0
        
        
        
                
        i_content_0 = ""
        
        
        while (i_counter_3 < len(element_1)):
            
            
            semaphore_of_find_0 = False
            
            

            i_max_0 = 0
            
            i_counter_4 = 0
            
            while ((i_counter_4 < len(element_0)) and (semaphore_of_find_0 == False)):
                
                
                i_counter_5 = 0
                
                
                while ((i_counter_5 < len(element_0[i_counter_4])) and (i_counter_3 + i_counter_5 < len(element_1)) and (element_0[i_counter_4][i_counter_5] == element_1[i_counter_3 + i_counter_5])):
                    
                    
                    i_counter_5 += 1
                    
                    
                    
                
                
                if (i_max_0 < i_counter_5):
                    
                    
                    i_max_0 = i_counter_5
                    
                    
                
                if (i_counter_5 == len(element_0[i_counter_4])):
                    
                    
                    semaphore_of_find_0 = True
                    
                    
                
                
                
                
                i_counter_4 += 1
                
                
            
                

            
            #print(f"i_hello_4 . i_content_0 = \"{i_content_0}\" .")
            
                
            
            if (semaphore_of_find_0 == True):
                
                i_counter_1 += 1
                
                i_counter_3 += i_max_0
                
                
                # space to append into the list i_list_of_result_0 .
                
                
                
                i_list_of_result_0.append(i_content_0)
                
                
                #print(f"    i_hello_3 . in the first if . i_content_0 = \"{i_content_0}\" .")
                
                
                semaphore_of_add_0 = False
                
                i_content_0 = ""
                
                
                
                
            else:
            
                
                # this space for the incrementation of string .
                
                
                if (i_counter_3 < len(element_1)):
                    
                    
                    i_content_0 += element_1[i_counter_3]
                    
                    semaphore_of_add_0 = True
                    
                    #print(f"    i_hello_2 . in the second if . i_content_0 = \"{i_content_0}\" .")
                    
                    
                    
                
                
                
                
                i_counter_3 += 1
                
                
                
                
            #print(f"i_hello_5 . i_content_0 = \"{i_content_0}\" .")
                
            
            
            
            
        
        if (semaphore_of_add_0 == True):
            
            i_list_of_result_0.append(i_content_0)
        
        
        # section of extracting the not_counted_words 
        
        
        i_counter_0 = 0
        
        while (i_counter_0 < len(not_counted_words)):
            
            
            i_counter_2 = 0
            
            
            while (i_counter_2 < len(i_list_of_result_0)):
                
                
                if (i_list_of_result_0[i_counter_2] == not_counted_words[i_counter_0]):
                    
                    i_list_of_result_0.pop(i_counter_2)
                    
                else:
                    
                    i_counter_2 += 1
                    
                    
                
            i_counter_0 += 1
        
        
    else:
        
        i_counter_1 = -1
        
        
    return [i_counter_1, i_list_of_result_0]
    
    
    
    
    






def finder_and_spliter_1(element_0, element_1, not_counted_words):
    
    
    # element_0 is a list 
    
    '''
    
    element_1 : string 
    
    element_0 : list_of_string 
    
    not_counted_words : list_of_string 
    
    
    
    this function split the element_1 according to element_0 into a list . 
    
    after that it will delete not_counted_words from this list .
    
    
    
    '''
    
               
    i_counter_1 = 0
    
    
    i_list_of_result_0 = []
    
    
    if (len(element_0) > 0):
        
        
        
        semaphore_of_add_0 = True
        
        
        
        i_counter_3 = 0
        
        
        
                
        i_content_0 = ""
        
        
        while (i_counter_3 < len(element_1)):
            
            
            semaphore_of_find_0 = False
            
            

            i_max_0 = 0
            
            i_counter_4 = 0
            
            while ((i_counter_4 < len(element_0)) and (semaphore_of_find_0 == False)):
                
                
                i_counter_5 = 0
                
                
                while ((i_counter_5 < len(element_0[i_counter_4])) and (i_counter_3 + i_counter_5 < len(element_1)) and (element_0[i_counter_4][i_counter_5] == element_1[i_counter_3 + i_counter_5])):
                    
                    
                    i_counter_5 += 1
                    
                    
                    
                
                
                if (i_max_0 < i_counter_5):
                    
                    
                    i_max_0 = i_counter_5
                    
                    
                
                if (i_counter_5 == len(element_0[i_counter_4])):
                    
                    
                    semaphore_of_find_0 = True
                    
                
                
                
                
                i_counter_4 += 1
                
                    
                
            
                

            
            #print(f"i_hello_4 . i_content_0 = \"{i_content_0}\" .")
            
                
            
            if (semaphore_of_find_0 == True):
                
                i_counter_1 += 1
                
                i_counter_3 += i_max_0
                
                
                # space to append into the list i_list_of_result_0 .
                
                
                
                i_list_of_result_0.append(i_content_0)
                
                
                
                
                i_list_of_result_0.append(element_0[i_counter_4 - 1])
                
                
                
                
                #print(f"    i_hello_3 . in the first if . i_content_0 = \"{i_content_0}\" .")
                
                
                semaphore_of_add_0 = False
                
                i_content_0 = ""
                
                
                
                
            else:
            
                
                # this space for the incrementation of string .
                
                
                if (i_counter_3 < len(element_1)):
                    
                    
                    i_content_0 += element_1[i_counter_3]
                    
                    semaphore_of_add_0 = True
                    
                    #print(f"    i_hello_2 . in the second if . i_content_0 = \"{i_content_0}\" .")
                    
                    
                    
                
                
                
                
                i_counter_3 += 1
                
                
                
                
            #print(f"i_hello_5 . i_content_0 = \"{i_content_0}\" .")
                
            
            
            
            
        
        if (semaphore_of_add_0 == True):
            
            i_list_of_result_0.append(i_content_0)
        
        
        # section of extracting the not_counted_words 
        
        
        i_counter_0 = 0
        
        while (i_counter_0 < len(not_counted_words)):
            
            
            i_counter_2 = 0
            
            
            while (i_counter_2 < len(i_list_of_result_0)):
                
                
                if (i_list_of_result_0[i_counter_2] == not_counted_words[i_counter_0]):
                    
                    i_list_of_result_0.pop(i_counter_2)
                    
                else:
                    
                    i_counter_2 += 1
                    
                    
                
            i_counter_0 += 1
        
        
    else:
        
        i_counter_1 = -1
        
        
    return [i_counter_1, i_list_of_result_0]
    
    
    
    
    








def finder_2(element_0, element_1):
    
    
            
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




        
    
    
    
    



def i_get_the_occerency_of_all_word_0(text, separater_of_words, not_counted_words):
    
    
    list_result_0 = []
    
        
    list_0 = []
    
    
    
    i_counter_3 = 0
    
    i_counter_2 = 0
    
    
    while (i_counter_2 < len(separater_of_words)):
        
        
        
        
        
        
        v_0 = text.split(separater_of_words[i_counter_2])
        
        
        
        if (len(v_0) > 1):
            
            
            i_counter_0 = 0
            
            
            while (i_counter_0 < len(v_0)):
                
                if ((not (v_0[i_counter_0] in list_0)) and (not v_0[i_counter_0] in not_counted_words)):
                    
                    list_0.append(v_0[i_counter_0])
                    
                    
                
                
                i_counter_0 += 1
                
                
                
                
            
            
            while (i_counter_3 < len(list_0)):
                
                
                number_of_occurency_0 = 0
                
                
                i_counter_1 = 0
                
                while (i_counter_1 < len(v_0)):
                    
                    if (v_0[i_counter_1] == list_0[i_counter_3]):
                        
                        
                        number_of_occurency_0 += 1
                        
                        
                    
                    
                    i_counter_1 += 1
                    
                    
                
                list_result_0.append([number_of_occurency_0, list_0[i_counter_3]])
                
                
                i_counter_3 += 1
                
                
                
            
            
            list_result_0 = sort_element_0_0(l=list_result_0)
            
            
        
        i_counter_2 += 1
        
        
        
    
    return list_result_0
    








def i_get_the_occerency_of_all_word_1(list_1):
    
    
    list_result_0 = []
    
    
    list_result_1 = []
    
    
    list_result_2 = []
    
        
    list_0 = []
    
    
    
    i_counter_3 = 0
    
    i_counter_2 = 0

    
    
    
    v_0 = list_1
    
    
    
    if (len(v_0) > 1):
        
        
        i_counter_0 = 0
        
        
        while (i_counter_0 < len(v_0)):
            
            if ((not (v_0[i_counter_0] in list_0))):
                
                list_0.append(v_0[i_counter_0])
                
                
            
            list_result_2.append(v_0[i_counter_0])
            
            i_counter_0 += 1
            
            
            
            
        
        
        while (i_counter_3 < len(list_0)):
            
            
            number_of_occurency_0 = 0
            
            
            i_counter_1 = 0
            
            while (i_counter_1 < len(v_0)):
                
                if (v_0[i_counter_1] == list_0[i_counter_3]):
                    
                    
                    number_of_occurency_0 += 1
                    
                    
                
                
                i_counter_1 += 1
                
                
            
            list_result_0.append([number_of_occurency_0, list_0[i_counter_3]])
            
            
            i_counter_3 += 1
            
            
            
        
        
        
        
        list_result_0 = sort_element_0_0(l=list_result_0)
        
        
        
        
        
        
        
        i_counter_0 = 0
        
        
        while (i_counter_0 < len(list_result_0)):
            
            
            list_result_1.append(list_result_0[i_counter_0][1])
            
            
            i_counter_0 += 1
            
            
            
            
        
        
        
        
        
    
    return [list_result_0, list_result_1, list_result_2]
    







def i_get_list_of_individual_amount_0_i(i_list_result_1_i, i_list_result_2_i):
    
    
    
    i_list_of_result_0_i = []
    
    
    
    
    if (len(i_list_result_1_i) > 0):
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_result_1_i)):
            
            
            i_counter_1_i = i_list_result_1_i[i_counter_0_i][0]
            
            
            i_list_of_result_0_i.append([])
            
            
            while ((i_counter_0_i < len(i_list_result_1_i)) and (i_counter_1_i == i_list_result_1_i[i_counter_0_i][0])):
                
                
                i_list_of_result_0_i[-1].append([0, i_list_result_1_i[i_counter_0_i][0], i_list_result_1_i[i_counter_0_i][1]])
                
                
                i_counter_0_i += 1
                
            
            
        
        
        
        i_counter_2_i = 0
        
        
        while (i_counter_2_i < len(i_list_of_result_0_i)):
            
            
            
            i_counter_1_i = 0
            
            
            while (i_counter_1_i < len(i_list_of_result_0_i[i_counter_2_i])):
                
                
                
                i_element_0_i = i_list_of_result_0_i[i_counter_2_i][i_counter_1_i][2]
                
                
                
                
                # get_the_position 
                
                
                i_counter_0_i = 0
                
                while ((i_counter_0_i < len(i_list_result_2_i)) and (i_element_0_i != i_list_result_2_i[i_counter_0_i])):
                    
                    
                    i_counter_0_i += 1
                    
                    
                
                i_list_of_result_0_i[i_counter_2_i][i_counter_1_i][0] = i_counter_0_i
                
                
                
                
                i_counter_1_i += 1
                
                
            
            
            

            
            i_list_of_result_0_i[i_counter_2_i] = sort_element_0_1(l=i_list_of_result_0_i[i_counter_2_i])
            
            
            i_counter_2_i += 1
            
            
        
        
        
        
        
    
    
    return i_list_of_result_0_i
    





def i_get_list_of_individual_amount_1_i(i_list_of_result_0_i):
    
    
    
    i_list_of_result_1_i = []
    
    
    i_counter_2_i = 0
    
    
    while (i_counter_2_i < len(i_list_of_result_0_i)):
        
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_of_result_0_i[i_counter_2_i])):
            
            
            i_list_of_result_1_i.append(i_list_of_result_0_i[i_counter_2_i][i_counter_1_i][2])
            
            
            i_counter_1_i += 1
            
            
            
        
        i_counter_2_i += 1
        
        
        
    
    
    
    
    return i_list_of_result_1_i
    
    
    
    
    




def extract_list_2(text, separater_of_words, not_counted_words):
    
    
    
    i_v_0 = finder_and_spliter_0(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)
    
    
    
    list_result_0 = i_get_the_occerency_of_all_word_1(list_1=i_v_0[1])
    
    
    
    return list_result_0[1]






def extract_list_0(text, separater_of_words, not_counted_words):
    
    
    
    i_v_0_i = finder_and_spliter_0(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)
    
    #print(f"\n\n    i_v_0_i = {i_v_0_i} .\n\n")
    
    
    i_list_result_0_i = i_get_the_occerency_of_all_word_1(list_1=i_v_0_i[1])
    
    
    #print(f"\n\n    i_list_result_0_i = {i_list_result_0_i} .\n\n")
    
    
    
    i_v_result_0_i = i_get_list_of_individual_amount_0_i(i_list_result_1_i=i_list_result_0_i[0], i_list_result_2_i=i_v_0_i[1])
    
    
    #print(f"\n\n    i_v_result_0_i = {i_v_result_0_i} .\n\n")
    
    
    
    i_v_result_1_i = i_get_list_of_individual_amount_1_i(i_list_of_result_0_i=i_v_result_0_i)
    
    
    
    #print(f"\n\n    i_v_result_1_i = {i_v_result_1_i} .\n\n")
    
    
    return i_v_result_1_i




def extract_list_1(text, separater_of_words, not_counted_words):
    
    
    '''
    
    this is in ( generater_of_phrase == True )
    
    
    '''
    
    
    i_v_0_i = finder_and_spliter_0(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)
    
    #print(f"\n\n    i_v_0_i = {i_v_0_i} .\n\n")
    
    
    
    i_v_1_i = finder_and_spliter_1(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)
    
    
    
    i_list_result_0_i = i_get_the_occerency_of_all_word_1(list_1=i_v_0_i[1])
    
    
    #print(f"\n\n    i_list_result_0_i = {i_list_result_0_i} .\n\n")
    
    
    
    i_v_result_0_i = i_get_list_of_individual_amount_0_i(i_list_result_1_i=i_list_result_0_i[0], i_list_result_2_i=i_v_0_i[1])
    
    
    #print(f"\n\n    i_v_result_0_i = {i_v_result_0_i} .\n\n")
    
    
    
    i_v_result_1_i = i_get_list_of_individual_amount_1_i(i_list_of_result_0_i=i_v_result_0_i)
    
    
    
    #print(f"\n\n    i_v_result_1_i = {i_v_result_1_i} .\n\n")
    
    
    
    '''
    
    
        return [ i_v_result_1_i , the_list_of_the_first_spliter ]
    
    
    '''
    
    
    return [i_v_result_1_i, i_v_0_i]
    
    
    
    
    
    
    





def extract_list_5(text, separater_of_words, not_counted_words):
    
    
    '''
    
    this is in ( generater_of_phrase == True )
    
    
    '''
    
    
    i_v_0_i = finder_and_spliter_1(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)
    
    #print(f"\n\n    i_v_0_i = {i_v_0_i} .\n\n")
    
    
    
    
    
    
    i_list_result_0_i = i_get_the_occerency_of_all_word_1(list_1=i_v_0_i[1])
    
    
    #print(f"\n\n    i_list_result_0_i = {i_list_result_0_i} .\n\n")
    
    
    
    i_v_result_0_i = i_get_list_of_individual_amount_0_i(i_list_result_1_i=i_list_result_0_i[0], i_list_result_2_i=i_v_0_i[1])
    
    
    #print(f"\n\n    i_v_result_0_i = {i_v_result_0_i} .\n\n")
    
    
    
    i_v_result_1_i = i_get_list_of_individual_amount_1_i(i_list_of_result_0_i=i_v_result_0_i)
    
    
    
    #print(f"\n\n    i_v_result_1_i = {i_v_result_1_i} .\n\n")
    
    
    
    '''
    
    
        return [ i_v_result_1_i , the_list_of_the_first_spliter ]
    
    
    '''
    
    
    return [i_v_result_1_i, i_v_0_i]
    
    
    
    
    
    
    



def extract_list_3(text, not_counted_words):
    
    
    
    
    '''
    
    this is in ( generater_of_word == True )
    
    
    '''
    
    
    
    i_v_0 = i_get_the_occerency_of_all_word_1(list_1=text)
    
    
    #print(f"i_v_0 = {i_v_0} .")
    
    
    
    i_v_result_0_i = i_get_list_of_individual_amount_0_i(i_list_result_1_i=i_v_0[0], i_list_result_2_i=i_v_0[2])
    
    
    #print(f"\n\n    i_v_result_0_i = {i_v_result_0_i} .\n\n")
    
    
    
    i_v_result_1_i = i_get_list_of_individual_amount_1_i(i_list_of_result_0_i=i_v_result_0_i)
    
    
    
    #print(f"\n\n    i_v_result_1_i = {i_v_result_1_i} .\n\n")
    
    
    
    
    
    
    list_result_0 = i_v_result_1_i
    
    
    #print(f"list_result_0 = {list_result_0} .")
    
    
    
    
    list_result_1 = i_v_0[2]
    
    
    
    #print(f"list_result_1 = {list_result_1} .")
    
    
    
    
        
    # section of extracting the not_counted_words 
    
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(not_counted_words)):
        
        
        i_counter_2 = 0
        
        
        while (i_counter_2 < len(list_result_0)):
            
            
            if (list_result_0[i_counter_2] == not_counted_words[i_counter_0]):
                
                list_result_0.pop(i_counter_2)
                
            else:
                
                i_counter_2 += 1
                
                
            
        i_counter_0 += 1
    
    
    
    
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(not_counted_words)):
        
        
        i_counter_2 = 0
        
        
        while (i_counter_2 < len(list_result_1)):
            
            
            if (list_result_1[i_counter_2] == not_counted_words[i_counter_0]):
                
                list_result_1.pop(i_counter_2)
                
            else:
                
                i_counter_2 += 1
                
                
            
        i_counter_0 += 1
    
    
    
    
    
    
    
    return [list_result_0, list_result_1]





def extract_list_4(text, not_counted_words):
    
    
    
    
    
    
    i_v_0 = i_get_the_occerency_of_all_word_1(list_1=text)
    
    
    
    list_result_0 = i_v_0[1]
    
    
        
    # section of extracting the not_counted_words 
    
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(not_counted_words)):
        
        
        i_counter_2 = 0
        
        
        while (i_counter_2 < len(list_result_0)):
            
            
            if (list_result_0[i_counter_2] == not_counted_words[i_counter_0]):
                
                list_result_0.pop(i_counter_2)
                
            else:
                
                i_counter_2 += 1
                
                
            
        i_counter_0 += 1
    
    
    
    
    
    
    return list_result_0






def get_similarity_0(text_0, text_1, separater_of_words, not_counted_words, number_of_digit_after_the_floating_point):
    
    
    
    
    '''
    
    this function is designed to find the similarity between 2 text : text_0 , text_1 
    
    useing my i_math .
    
    
    '''
    
    
    # i_math_i_am_i_0 
    
    
    
    list_0 = extract_list_0(text=text_0, separater_of_words=separater_of_words, not_counted_words=not_counted_words)
    
    
    
    list_1 = extract_list_0(text=text_1, separater_of_words=separater_of_words, not_counted_words=not_counted_words)
    

    #print(f"list_0 = {list_0} .")


    #print(f"list_1 = {list_1} .")

    
    i_counter_1 = "0.0"
    
    
    if (len(list_0) > 0):
        
        
        
        i_counter_0 = 0
        
        while (i_counter_0 < len(list_0)):
            
            
            if (list_0[i_counter_0] in list_1):
                
                
                
                operation_0 = f"{i_counter_1} + (1 / {len(list_0)})"
                
                
                m = i_math_i_am_i_0.calculatrice_2(s=operation_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
                
                if (m[0] == False):
                    
                    
                    i_counter_1 = m[1][0]
                    
                
            
            i_counter_0 += 1
            
            
            
    
    
    
    return i_counter_1
    
    
    



def get_the_golden_number_0(number_of_digit_after_the_floating_point):
    
    
    
    '''
    
    this function return the golden number like : "1.6180339887505"
    
    
    '''
    
    
    
    u_0 = 1
    
    u_1 = 1
    
    u_2 = 0
    
    i_counter_0 = 0
    
        
    i_counter_2 = "0.0"
    
    
    i_counter_3 = "init"
    
    
    
    while (i_counter_3 != i_counter_2):
        
        
        
        i_counter_3 = i_counter_2
        
        
        operation_0 = f"{u_1}/{u_0}"
        
        
        m = i_math_i_am_i_0.calculatrice_2(s=operation_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
        
                
        if (m[0] == False):
            
            
            i_counter_2 = m[1][0]
            
        
        u_2 = u_0 + u_1
        
        u_0 = u_1
        
        u_1 = u_2
        
        
        i_counter_0 += 1
        
        
    
    
        
    
    
    i_counter_4 = "0.0"
    
    operation_0 = f"2-{i_counter_2}"
    
    
    m = i_math_i_am_i_0.calculatrice_2(s=operation_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
    
            
    if (m[0] == False):
        
        
        i_counter_4 = m[1][0]
        
    
    
        
    
    i_counter_5 = "0.0"
    
    operation_0 = f"1/{i_counter_2}"
    
    
    m = i_math_i_am_i_0.calculatrice_2(s=operation_0, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
    
            
    if (m[0] == False):
        
        
        i_counter_5 = m[1][0]
        
    
    
    
    
    
    #print(f"i_counter_0 = {i_counter_0} .")
    
    
    
    # return [ the_golden_number , the_number_of_calcule_to_get_there , 2 - the_golden_number, 1 / the_golden_number] 
    
    
    return [i_counter_2, i_counter_0, i_counter_4, i_counter_5]
    
    
    
    






def i_produce_the_length_of_1_complete_number_of_your_int_i_0(number_of_bit_in_the_type_0):
    
    
    
    
    '''
    
    
    this function can lead you to get the_length_of_1_complete_number_of_your_int .
    
    it means from : [ ( int64_t ==> 64 ) to 18 ].
    
    
    
    number_of_bit_in_the_type_0 should be equal to the number of bit in your type . like :
        
        int64_t ==> [ 64 bit ] ==> (number_of_bit_in_the_type_0=64)
    
    
        
    
    the bit is the smallest memory possible . and right here i am speaking about the memory 
    
    that can have : 
        
        [ 0 , 1 ]
        
    just one of them . ( 0 , 1 ) .
    
    
    '''
    
    
    
    import i_math_i_am_i_0
    
    number_of_digit_after_the_floating_point = 2
    
    operation = f"2^({number_of_bit_in_the_type_0} - 1)"
    
    
    m = i_math_i_am_i_0.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
    
    
    i_number_i_1 = m[1][0]
    
    
    
    
    i_number_i_0 = f"1.0"
    
    
    s1 = f"{i_number_i_0}"
    
    s2 = f"{i_number_i_1}"
    

    bool_0 = i_math_i_am_i_0.my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
    
        
        
        
    
    while (bool_0 == True):
        
            
        operation = f"{i_number_i_0}*10"
        
        m = i_math_i_am_i_0.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
        
        
        i_number_i_0 = m[1][0]
        
                
        s1 = f"{i_number_i_0}"
        
        s2 = f"{i_number_i_1}"
        
        
        bool_0 = i_math_i_am_i_0.my_inferieur_s_n_1(s1=s1, s2=s2, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point)
        
        
        
    
    
        
    operation = f"{i_number_i_0}/10"
    
    m = i_math_i_am_i_0.calculatrice_2(s=operation, l_=[], n=0, number_of_digit_after_the_floating_point_=number_of_digit_after_the_floating_point, e=False)
    
    
    i_number_i_0 = m[1][0]
    
    
    
    i_v_i_0 = i_number_i_0.split(".")
    
    
    
    
    return len(i_v_i_0[0]) - 1
    
    




def i_extract_sentences_from_html_0_i(i_text_of_input_0_i):
    
    
    
    '''
    
    this function extract sentences from html .
    
    
    
    '''
    
    
    
    
    
    i_list_of_result_0_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_text_of_input_0_i)):
        
        
        
        while ((i_counter_0_i < len(i_text_of_input_0_i)) and (i_text_of_input_0_i[i_counter_0_i] != "<")):
            
            
            if ((i_text_of_input_0_i[i_counter_0_i] == "\"") or (i_text_of_input_0_i[i_counter_0_i] == "\'") or (i_text_of_input_0_i[i_counter_0_i] == "`")):
                
                
                i_c_0_i = i_text_of_input_0_i[i_counter_0_i]
                
                
                while ((i_counter_0_i < len(i_text_of_input_0_i)) and (i_text_of_input_0_i[i_counter_0_i] != i_c_0_i)):
                    
                    
                    i_counter_0_i += 1
                    
                    
                
                
                i_counter_0_i += 1
                
                
            
            i_counter_0_i += 1
            
            
        
        if (i_counter_0_i < len(i_text_of_input_0_i)):
        
            
            i_counter_1_i = i_counter_0_i
            
            
            while ((i_counter_0_i > 0) and (i_text_of_input_0_i[i_counter_0_i] != ">")):
                
                
                i_counter_0_i -= 1
                
                
            
            i_counter_0_i += 1
            
            
            i_content_0_i = ""
            
            
            
            while (i_counter_0_i < i_counter_1_i):
                
                
                i_content_0_i += i_text_of_input_0_i[i_counter_0_i]
                
                i_counter_0_i += 1
                
                
            
            
            i_content_1_i = ""
            
            
            while ((i_counter_0_i < len(i_text_of_input_0_i)) and (i_text_of_input_0_i[i_counter_0_i] != ">")):
                
                
                i_content_1_i += i_text_of_input_0_i[i_counter_0_i]
                
                i_counter_0_i += 1
                
                
            
            if (i_counter_0_i < len(i_text_of_input_0_i)):
                
                i_content_1_i += i_text_of_input_0_i[i_counter_0_i]
                
            
            
            i_content_0_i = " ".join(i_content_0_i.split())
            
            
            if (
                
                (i_content_0_i != "") and 
                
                
                (i_content_1_i[1] == "/") and 
                
                
                (i_content_1_i != "</script>") and 
                
                
                (i_content_1_i != "</style>") 
                
                ):
       
                
                i_list_of_result_0_i.append([i_content_0_i, i_content_1_i])
                
            
            
            
            i_counter_0_i += 1
            
        
    
    
    return i_list_of_result_0_i
    


def main():
    
    
    
    text = "i get the apple and then i put  the drink"
    
    
    print(f"text = \"{text}\" .")
    
    
    separater_of_words = ["  ", " "]
    
    not_counted_words = []
    
    
    
    i_v_0_i = extract_list_5(text=text, separater_of_words=separater_of_words, not_counted_words=not_counted_words)
    
    
    print(f"i_v_0_i = {i_v_0_i} .")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



if __name__ == "__main__":
    
    
    main()
    

























