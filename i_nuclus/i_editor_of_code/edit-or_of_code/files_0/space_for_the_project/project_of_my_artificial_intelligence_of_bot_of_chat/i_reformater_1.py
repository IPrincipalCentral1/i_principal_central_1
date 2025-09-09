














list_of_liberary_to_install = [

                            ["googletrans"] ,
                            
                            
                            ["nltk"] ,
                            
                            
                            



]










import os


import traceback

import sys


import subprocess




try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
        
        
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
        
        
        counter_0 += 1
        
        
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    
    






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
        
        
        pourcent_0 = 0.0
        
        if (m_0 > 0):
            
            pourcent_0 = len(l_) / m_0
            
            
        
        
        
        t1 = i_calculat_and_display_in_the_loop_0(first_time=t1, amount_of_time_0=2.0, var_0=[f"len(l_) = {len(l_)} . len(l) = {len(l)} . pourcent = {pourcent_0} %"])
        
        
        
        #print(f"i_hello_1 . i_counter_0 = {i_counter_0} .")
        
        
        
        
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
    
        
    list_0 = []
    
    
    
    i_counter_3 = 0
    
    i_counter_2 = 0

    
    
    
    v_0 = list_1
    
    
    
    if (len(v_0) > 1):
        
        
        i_counter_0 = 0
        
        
        while (i_counter_0 < len(v_0)):
            
            if ((not (v_0[i_counter_0] in list_0))):
                
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
        
        
        
        i_counter_0 = 0
        
        
        while (i_counter_0 < len(list_result_0)):
            
            
            list_result_1.append(list_result_0[i_counter_0][1])
            
            
            i_counter_0 += 1
            
            
            
            
        
        
        
        
        
    
    return [list_result_0, list_result_1]
    





def extract_list_0(text, separater_of_words, not_counted_words):
    
    
    
    i_v_0 = finder_and_spliter_0(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)
    
    
    
    list_result_0 = i_get_the_occerency_of_all_word_1(list_1=i_v_0[1])
    
    
    
    return list_result_0[1]






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
    
    
    
    




def i_displayer_of_language_0():
    
    
    
    # تثبيت: pip install googletrans==4.0.0-rc1
    
    from googletrans import LANGUAGES
    
    # LANGUAGES هو dict فيه كل الأكواد كـ key واللغة بالإنجليزية كـ value
    
    
    for code, name in LANGUAGES.items():
        
        
        #list_of_langage_0.append([code, name])
        
        print(f"{code} : {name}")
        
    
    


def i_translate_word_0(word_0, language_from, language_to):
    
    
    
    from googletrans import Translator
    
    translator = Translator()
    
    # مثال: ترجمة من الإنجليزية إلى العربية
    
    result = translator.translate("Hello", src="en", dest="ar")
    
    print(f"result.text = {result.text} .") 

    
    
    
    
    








def main():
    
    
    text = " a a a a aaa aa aa aa aa aa aa aa bb bb bb\n\ncc"
    
    separater_of_words = [" ", "\n"]
    
    not_counted_words = [""]
    
    
    print(f"text = \"{text}\"")
    
    
    
    list_result_0 = i_get_the_occerency_of_all_word_0(text=text, separater_of_words=separater_of_words, not_counted_words=not_counted_words)
    
    
    
    print(f"list_result_0 = {list_result_0}")
    
    
    
    i_counter_1 = finder_2(element_0="aa", element_1=text)
    
    print(f"i_counter_1 = {i_counter_1} .")
    
    
        
    i_v_2 = finder_and_spliter_2(element_0="aa", element_1=text)
    
    print(f"i_v_2[0] = {i_v_2[0]} .\n    i_v_2[1] = {i_v_2[1]} .")
    
    
    
        
    i_v_3 = finder_and_spliter_0(element_0=["aa", "\n", "\n\n", "b "], element_1=text, not_counted_words=[" "])
    
    print(f"i_v_3[0] = {i_v_3[0]} .\n    i_v_3[1] = {i_v_3[1]} .")
    
    
        
    
    list_result_1 = i_get_the_occerency_of_all_word_1(list_1=i_v_3[1])
    
    
    
    print(f"list_result_1[0] = {list_result_1[0]} .\n    list_result_1[1] = {list_result_1[1]}")
    
    
    text_0 = "i_hello_0 . i_hello_1 . i_hello_3 ."
    
    
    text_1 = "i_hello_0 . i_hello_2 ."
    
    
    separater_of_words = [" ", "\n", "."]
    
    
    not_counted_words = [""]
    
    
    number_of_digit_after_the_floating_point = 20
    
    
    
    i_counter_1 = get_similarity_0(text_0=text_0, text_1=text_1, separater_of_words=separater_of_words, not_counted_words=not_counted_words, number_of_digit_after_the_floating_point=number_of_digit_after_the_floating_point)
    
    
    print(f"i_counter_1 = {i_counter_1} .")
    
    
    
    i_v_4 = get_the_golden_number_0(number_of_digit_after_the_floating_point=50)
    
    
    print(f"i_v_4 = {i_v_4} .")
    
    
    
    
    i_translate_word_0(word_0="", language_from="", language_to="")
    
    



if __name__ == "__main__":
    
    
    main()
    

























