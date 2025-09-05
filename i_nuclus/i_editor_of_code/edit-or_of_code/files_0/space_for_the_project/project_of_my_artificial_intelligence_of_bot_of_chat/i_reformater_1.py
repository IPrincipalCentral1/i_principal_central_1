











import os


cwd = os.path.dirname(os.path.abspath(__file__))








def main_string_function(min_, ele, n):


    v = min_[0]



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

        return (ele, n, )

    elif (one):

        return (ele, n, )

    else:

        return min_




def sort_element_0_0(l):

    
    l_ = []
    
    while (0 < len(l)):
        
        i = 0
        
        min_ = (l[i][0], i, )
        
        
        
        while (i < len(l)):
            
            min_0 = main_string_function(min_=min_, ele=l[i][0], n=i)
            
            
            
            if (min_0 != min_):
            
                min_ = min_0
            
            i += 1
        
        
        l_.append(l[min_[1]])
        
        
        l.pop(min_[1])
    
    
    
    
    return l_






    
    

def finder_2_0(element_0, element_1):
    
    
            
    i_counter_1 = 0
    
    
    i_list_of_result_0 = []
    
    
    if (len(element_0) > 0):
        
        
        
        
        i_counter_0 = 0
        
                
        
        i_counter_3 = 0
        
        
        
                
        i_content_0 = ""
        
        
        while (i_counter_0 < len(element_1)):
            
            
            
            
            i_counter_0 = i_counter_3
            
            i_counter_2 = 0
            
            print(f"i_hello_0 . i_counter_3 = {i_counter_3} .")
            
            
            while ((i_counter_2 < len(element_0)) and (i_counter_0 < len(element_1)) and (element_0[i_counter_2] == element_1[i_counter_0])):
                
                
                print(f"    i_hello_1 . element_1[i_counter_0] = {element_1[i_counter_0]} .")
                
                i_content_0 += element_1[i_counter_0]
                
                i_counter_0 += 1
                
                i_counter_2 += 1
            
            
            print(f"            i_hello_4 . i_content_0 = \"{i_content_0}\" .")
            
                
            
            if (i_counter_2 == len(element_0)):
                
                i_counter_1 += 1
                
                i_counter_3 = i_counter_0
                
                
                # space to append into the list i_list_of_result_0 .
                
                
                
                i_list_of_result_0.append(i_content_0[:-len(element_0)])
                
                
                print(f"        i_hello_3 . i_content_0[:-len(element_0)] = \"{i_content_0[:-len(element_0)]}\" .")
                
                
                i_content_0 = ""
                
                
                
                
            else:
            
                        
                i_counter_3 += 1
                
                
                # this space for the incrementation of string .
                
                
                if (i_counter_3 < len(element_1)):
                    
                    
                    i_content_0 += element_1[i_counter_3]
                    
                    
                    print(f"        i_hello_2 . i_content_0 = \"{i_content_0}\" .")
                    
                    
                    
                
                
                
            print(f"            i_hello_5 . i_content_0 = \"{i_content_0}\" .")
                
                    
        
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







def i_split(text, list_of_separater):
    
    
    list_of_result_0 = []
    
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(text)):
        
        pass
        
        
        
        
    
    
    
    



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
    






def main():
    
    
    text = " a a a a aaa aa aa aa aa aa aa aa bb bb bb\ncc"
    
    separater_of_words = [" ", "\n"]
    
    not_counted_words = [""]
    
    
    print(f"text = \"{text}\"")
    
    
    
    list_result_0 = i_get_the_occerency_of_all_word_0(text=text, separater_of_words=separater_of_words, not_counted_words=not_counted_words)
    
    
    
    print(f"list_result_0 = {list_result_0}")
    
    
    
    i_counter_1 = finder_2(element_0="aa", element_1=text)
    
    print(f"i_counter_1 = {i_counter_1} .")
    
    
        
    i_v_2 = finder_2_0(element_0="aa", element_1=text)
    
    print(f"i_v_2[0] = {i_v_2[0]} .\n    i_v_2[1] = {i_v_2[1]} .")
    
    



if __name__ == "__main__":
    
    
    main()
    

























