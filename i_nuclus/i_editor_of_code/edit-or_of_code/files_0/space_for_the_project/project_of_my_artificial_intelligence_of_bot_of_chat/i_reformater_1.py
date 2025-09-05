











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







def i_get_the_occerency_of_all_word_0(text, separater_of_words, not_counted_words):
    
    
    list_result_0 = []
    
    
    
    
    v_0 = text.split(separater_of_words)
    
    list_0 = []
    
    
    
    
    
    i_counter_0 = 0
    
    
    while (i_counter_0 < len(v_0)):
        
        if ((not (v_0[i_counter_0] in list_0)) and (not v_0[i_counter_0] in not_counted_words)):
            
            list_0.append(v_0[i_counter_0])
            
            
        
        
        i_counter_0 += 1
        
        
        
        
    
    
    
    i_counter_0 = 0
    
    
    while (i_counter_0 < len(list_0)):
        
        
        number_of_occurency_0 = 0
        
        
        i_counter_1 = 0
        
        while (i_counter_1 < len(v_0)):
            
            if (v_0[i_counter_1] == list_0[i_counter_0]):
                
                
                number_of_occurency_0 += 1
                
                
            
            
            i_counter_1 += 1
            
            
        
        list_result_0.append([number_of_occurency_0, list_0[i_counter_0]])
        
        
        i_counter_0 += 1
        
        
        
    
    
    list_result_0 = sort_element_0_0(l=list_result_0)
    
    
    return list_result_0
    






def main():
    
    
    text = "a a a a aa aa aa aa aa aa aa aa bb bb bb"
    
    separater_of_words = " "
    
    not_counted_words = []
    
    
    print(f"text = \"{text}\"")
    
    
    
    list_result_0 = i_get_the_occerency_of_all_word_0(text=text, separater_of_words=separater_of_words, not_counted_words=not_counted_words)
    
    
    
    print(f"list_result_0 = {list_result_0}")
    
    
    



if __name__ == "__main__":
    
    
    main()
    

























