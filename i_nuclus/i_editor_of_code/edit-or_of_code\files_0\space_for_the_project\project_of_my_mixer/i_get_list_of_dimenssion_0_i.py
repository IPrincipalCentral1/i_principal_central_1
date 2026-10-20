










































































































'''


if you to use this program . you can do your range in my mixer .

for example :
    
    
    _____number_of_element_minus_1_____ == 1000
    


and after that . you do the spliters . for example :
    
    
    if ( 1 spliter ):
        
        
        
        i_first_spliter_0_i = 1
        
        
        i_last_spliter_0_i = 1
        
        
        
    
    if ( n spliters ==> (n > 1) ):
        
        
        
        i_first_spliter_0_i = 1
        
        
        i_last_spliter_0_i = n
        
        


and you adjust your range to be :
    
    
    
    if ( 1 spliter ):
        
        _____number_of_element_minus_1_____ += 1
        
    
    if ( n spliters ==> (n > 1) ):
        
        _____number_of_element_minus_1_____ += n
    


and you run my mixer .

and after that each time you make a step in my mixer . you run this program .

and you see the dimensions possible .


so the syntax is :
    
    
    region_of_content [0, 1_000]
    
    
    region_of_spliters [1_001, 1_000 + n]
    
    
    
    
    
    



'''






import os

import copy





cwd = os.path.dirname(os.path.abspath(__file__))







# start of parametter :

# -----------------------------------------------------------------------------------




i_first_spliter_0_i = 2


i_last_spliter_0_i = 5





# end of parametter .

# -----------------------------------------------------------------------------------









def main_string_0(main_, ele, n):
    
    
    '''
    
    this should be return-ing the min
    
    '''
    
    
    

    v = main_[0]
    
    v1 = ele
    
    if (v > v1):
        
        return (ele, n, )
        
    else:
        
        return main_
        



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




    
    



def i_get_list_of_dimenssion_1_i(i_list_0_i, i_separater_0_i):
    
    
    
    '''
    
    
    this is work with 1 spliter .
    
    
    
    if the i_list_0_i :
        
        [1, 0]
        
    
    the output will be with 1 spliter :
        
        [[], [0]]
        
        
    
    
    
    
    '''
    
    
    
    i_list_1_i = []
    
    
    
    
    i_counter_1_i = 0
    
    i_counter_0_i = 0
    
    
    while (i_counter_1_i < len(i_list_0_i)):
    
        
        i_list_2_i = []
        
        
        i_counter_0_i = i_counter_1_i
        
        
        while ((i_counter_0_i < len(i_list_0_i)) and (i_list_0_i[i_counter_0_i] != i_separater_0_i)):
            
            
            i_list_2_i.append(i_list_0_i[i_counter_0_i])
            
            i_counter_0_i += 1
            
            
         
        
        i_list_1_i.append(i_list_2_i)
        
        
        i_counter_0_i += 1
        
        
        i_counter_1_i = i_counter_0_i
        
        
    
    if ((0 <= i_counter_0_i - 1) and (i_counter_0_i - 1 < len(i_list_0_i)) and (i_list_0_i[i_counter_0_i - 1] == i_separater_0_i)):
        
        
        i_list_1_i.append([])
        
        
        
    
    
    
    if (len(i_list_0_i) == 0):
        
        
        i_list_1_i = [[]]
        
        
    
    
    
    i_list_of_pointers_of_i_list_1_i_0_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_1_i)):
        
        i_list_of_pointers_of_i_list_1_i_0_i.append([i_list_1_i[i_counter_0_i], i_separater_0_i])
        
        i_counter_0_i += 1
        
    
    
    
    
    
    
    return [i_list_1_i, i_list_of_pointers_of_i_list_1_i_0_i]





def i_get_list_of_dimenssion_1_1_i(i_list_0_i, i_separater_0_i, i_path_of_dimenssion_0_i):
    
    
    
    '''
    
    
    this is work with 1 spliter .
    
    
    
    if the i_list_0_i :
        
        [1, 0]
        
    
    the output will be with 1 spliter :
        
        [[], [0]]
        
        
    
    
    
    
    '''
    
    
    
    i_list_1_i = []
    
    
    
    
    i_counter_1_i = 0
    
    i_counter_0_i = 0
    
    
    while (i_counter_1_i < len(i_list_0_i)):
    
        
        i_list_2_i = []
        
        
        i_counter_0_i = i_counter_1_i
        
        
        while ((i_counter_0_i < len(i_list_0_i)) and (i_list_0_i[i_counter_0_i] != i_separater_0_i)):
            
            
            i_list_2_i.append(i_list_0_i[i_counter_0_i])
            
            i_counter_0_i += 1
            
            
         
        
        i_list_1_i.append(i_list_2_i)
        
        
        i_counter_0_i += 1
        
        
        i_counter_1_i = i_counter_0_i
        
        
    
    if ((0 <= i_counter_0_i - 1) and (i_counter_0_i - 1 < len(i_list_0_i)) and (i_list_0_i[i_counter_0_i - 1] == i_separater_0_i)):
        
        
        i_list_1_i.append([])
        
        
        
    
    
    
    if (len(i_list_0_i) == 0):
        
        
        i_list_1_i = [[]]
        
        
    
    
    i_list_0_i.clear()
    
    
    i_list_0_i.extend(copy.deepcopy(i_list_1_i))
    
    
    
    
    i_list_of_pointers_of_i_list_0_i_0_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_0_i)):
        
        i_list_of_pointers_of_i_list_0_i_0_i.append([i_list_0_i[i_counter_0_i], i_separater_0_i, i_path_of_dimenssion_0_i + f"_{i_counter_0_i}"])
        
        i_counter_0_i += 1
        
    
    
    
    
    
    
    return [i_list_0_i, i_list_of_pointers_of_i_list_0_i_0_i]







def i_get_list_of_dimenssion_with_1_spliter_0_i(i_spliter_0_i):
    
    
    '''
    
    this function will give you all the Sets possible with the help of my mixer .
    
    the spliter should be the last number wich 1 spliter .
    
    
    
    when you start a mix . for example :
        
        [air, stone, water]
        
    
    in the range of posssibility you should add the spliter at the end . like this :
        
        
        
        [air, stone, water, spliter]
        
    
    
    
    so _____number_of_element_minus_1_____ should be : 3 . and not just 2 .
    
    so i can get the list of all possible Sets using this range of mix .
    
    right here the spliter is : 3 .
    
    
    so you do after :
        
        
        i_v_0_i = i_get_list_of_dimenssion_with_1_spliter_0_i(i_spliter_0_i=3)
        
        
    
    
    
    '''
    
    
    
    
    i_folder_0_i = os.path.join(cwd, "space_for_mix")
    
    
    i_files_0_i = []
    
    
    for root, dirs_, i_files_0_i in os.walk(i_folder_0_i):
        
        break
        
    
    i_files_1_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_files_0_i)):
        
        i_files_1_i.append([i_files_0_i[i_counter_0_i]])
        
        i_counter_0_i += 1
        
        
    
    
    i_files_1_i = sort_element_0_1(l=i_files_1_i)
    
    
    
    i_list_0_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_files_1_i)):
        
        
        i_content_0_i = ""
        
        i_file_0_i = os.path.join(i_folder_0_i, i_files_1_i[i_counter_0_i][0])
        
        
        with open(i_file_0_i, "r") as f_:
            
            
            i_content_0_i = f_.read(os.path.getsize(i_file_0_i))
            
            
        
        
        i_list_0_i.append(int(i_content_0_i))
        
        
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    i_list_from_the_mixer_0_i = i_list_0_i

    
    i_list_of_possible_Sets_1_i = i_get_list_of_dimenssion_1_i(i_list_0_i=i_list_from_the_mixer_0_i, i_separater_0_i=i_spliter_0_i)[0]


    
    
    return [i_list_from_the_mixer_0_i, i_list_of_possible_Sets_1_i]





def i_get_list_of_dimenssion_2_i(i_list_from_the_mixer_0_i, i_first_spliter_0_i, i_last_spliter_0_i):
    
    
    
    
    
    
    i_list__0_i = copy.deepcopy(i_list_from_the_mixer_0_i)
    
    
    i_list_0_i = [[i_list__0_i, i_list__0_i]]
    
    
    i_list_4_i = [[i_list_0_i[0][0], i_list_0_i[0][1], 0]]
    
    
    i_counter_0_i = i_last_spliter_0_i
    
    i_counter_1_i = 0
    
    
    
    while ((i_counter_1_i < len(i_list_4_i)) and (i_list_4_i[i_counter_1_i][2] < i_last_spliter_0_i) and (i_first_spliter_0_i <= i_last_spliter_0_i - i_list_4_i[i_counter_1_i][2])):
        
        
        i_list_2_i = i_list_4_i[i_counter_1_i][0]
        
        
        i_counter_2_i = 0
        
        
        while ((type(i_list_2_i) == list) and (len(i_list_2_i) > 0) and (type(i_list_2_i[0]) == list)):
            
            
            i_list_2_i = i_list_2_i[0]
            
            i_counter_2_i += 1
            
            
            
           
        
        
        
        
        i_list_1_i = i_get_list_of_dimenssion_1_i(i_list_0_i=i_list_2_i, i_separater_0_i=i_last_spliter_0_i - i_list_4_i[i_counter_1_i][2])
        
        
        
        i_list_2_i.clear()
        
        
        i_list_2_i.extend(i_list_1_i)
        
        
        
        
        i_list_3_i = i_list_1_i
        
        i_counter_3_i = 0
        
        while (i_counter_3_i < i_counter_2_i):
            
            i_list_3_i = [i_list_3_i]
            
            i_counter_3_i += 1
            
            
        
        i_list_0_i.append([i_list_3_i, i_list_1_i])
        
        
        
        
        i_number_0_i = len(i_list_4_i)
        
        i_counter_4_i = 0
        
        while (i_counter_4_i < len(i_list_1_i)):
            
            i_list_4_i.append([i_list_1_i[i_counter_4_i], i_list_1_i, i_list_4_i[i_number_0_i - 1][2] + 1])
            
            i_counter_4_i += 1
            
        
        
        
        
        
        
        
        i_counter_0_i -= 1
        
        i_counter_1_i += 1
        
        
    
    i_list_of_possible_Sets_1_i = i_list_4_i[0][0]
    
    
    i_list_of_all_steps_0_i = i_list_4_i
    
    
    
    return [i_list_from_the_mixer_0_i, i_list_of_possible_Sets_1_i, i_list_of_all_steps_0_i]
    
    
    
    
    




def i_get_list_of_dimenssion_3_i(i_list_from_the_mixer_0_i, i_first_spliter_0_i, i_last_spliter_0_i):
    
    
    
    
    i_list_0_i = i_list_from_the_mixer_0_i
    
    
    i_list_1_i = i_get_list_of_dimenssion_1_1_i(i_list_0_i=i_list_0_i, i_separater_0_i=i_last_spliter_0_i, i_path_of_dimenssion_0_i="")
    
    
    i_list_of_pointers_0_i = i_list_1_i[1]
    
    
    i_history_of_all_steps_0_i = []
    
    
    i_history_of_all_steps_0_i.extend(copy.deepcopy(i_list_1_i[1]))
    
    
    i_counter_1_i = 0
    
    
    while (i_counter_1_i < len(i_list_of_pointers_0_i)):
        
        
        
        if (i_first_spliter_0_i <= i_list_of_pointers_0_i[i_counter_1_i][1] - 1 <= i_last_spliter_0_i):
            
            
            i_list_1_i = i_get_list_of_dimenssion_1_1_i(i_list_0_i=i_list_of_pointers_0_i[i_counter_1_i][0], i_separater_0_i=i_list_of_pointers_0_i[i_counter_1_i][1] - 1, i_path_of_dimenssion_0_i=i_list_of_pointers_0_i[i_counter_1_i][2])
            
            
            i_list_of_pointers_0_i.extend(i_list_1_i[1])
            
            
            i_history_of_all_steps_0_i.extend(copy.deepcopy(i_list_1_i[1]))
            
            
            
        
        
        
        i_counter_1_i += 1
        
        
    
    
    
    i_list_of_result_0_i = []
    
    i_counter_1_0 = 0
    
    
    while ((i_counter_1_0 < len(i_list_of_pointers_0_i)) and (i_list_of_pointers_0_i[i_counter_1_0][1] == i_last_spliter_0_i)):
        
        
        i_list_of_result_0_i.append(i_list_of_pointers_0_i[i_counter_1_0][0])
        
        
        i_counter_1_0 += 1
        
    
    
    
    
    return [i_list_of_pointers_0_i, i_list_1_i, i_list_of_result_0_i, i_history_of_all_steps_0_i]




def i_check_if_content_exist_0_i(i_list_0_i):
    
    
    i_v_of_result_0_i = False
    
    
    if ((type(i_list_0_i) == list) and (not (type(i_list_0_i[0]) == list))):
        
        
        i_v_of_result_0_i = True
        
            
        
        
    
    return i_v_of_result_0_i
    
    



def i_get_content_if_it_exist_0_i(i_list_of_all_steps_0_i):
    
    
    
    i_list_of_result_0_i = []
    
    
    
    i_counter_0_i = len(i_list_of_all_steps_0_i) - 1
    
    
    
    while (i_counter_0_i >= 0):
        
        
        
        
        if (i_check_if_content_exist_0_i(i_list_0_i=i_list_of_all_steps_0_i[i_counter_0_i][0]) == True):
            
            
            i_list_of_result_0_i.insert(0, i_list_of_all_steps_0_i[i_counter_0_i][0])            
        
        
        i_counter_0_i -= 1
        
        
    
    
    
    return i_list_of_result_0_i
    
    
    



def i_get_content_if_it_exist_1_i(i_list_of_all_steps_0_i):
    
    
    
    i_list_of_result_0_i = []
    
    
    
    i_counter_0_i = len(i_list_of_all_steps_0_i) - 1
    
    
    
    while ((i_counter_0_i >= 0) and (i_list_of_all_steps_0_i[i_counter_0_i][1] == i_first_spliter_0_i)):
        
        
        
        
        
        i_list_of_result_0_i.insert(0, i_list_of_all_steps_0_i[i_counter_0_i][0])            
        
        
        i_counter_0_i -= 1
        
        
    
    
    
    return i_list_of_result_0_i
    
    
    


def i_extract_the_length_of_each_deepth_0_i(i_history_of_all_steps_0_i):
    
    
    
    i_list_of_result_0_i = []
    

    i_counter_0_i = 0
    
    
    while (i_counter_0_i < len(i_history_of_all_steps_0_i)):
        
        
        i_number_spliter_0_i = i_history_of_all_steps_0_i[i_counter_0_i][1]
        
        
        i_number_of_deepth_0_i = 0
        
        
        
        
        while ((i_counter_0_i < len(i_history_of_all_steps_0_i)) and (i_history_of_all_steps_0_i[i_counter_0_i][1] == i_number_spliter_0_i)):
            
            
            i_number_of_deepth_0_i += 1
            
            
            i_counter_0_i += 1
            
        
        
        
        i_list_of_result_0_i.append([i_number_spliter_0_i, i_number_of_deepth_0_i])
        
        
    
    
    return [i_list_of_result_0_i]
    
    
    


def i_get_list_of_dimenssion_0_1_i():
    
    
    
    
    '''
    
    
    
    this function i believe can give you all dimenssions possible .
    
    
    
    '''
    
    
    
    
    i_folder_0_i = os.path.join(cwd, "space_for_mix")
    
    
    i_files_0_i = []
    
    
    for root, dirs_, i_files_0_i in os.walk(i_folder_0_i):
        
        break
        
    
    i_files_1_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_files_0_i)):
        
        i_files_1_i.append([i_files_0_i[i_counter_0_i]])
        
        i_counter_0_i += 1
        
        
    
    
    i_files_1_i = sort_element_0_1(l=i_files_1_i)
    
    
    
    i_list_0_i = []
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_files_1_i)):
        
        
        i_content_0_i = ""
        
        i_file_0_i = os.path.join(i_folder_0_i, i_files_1_i[i_counter_0_i][0])
        
        
        with open(i_file_0_i, "r") as f_:
            
            
            i_content_0_i = f_.read(os.path.getsize(i_file_0_i))
            
            
        
        
        i_list_0_i.append(int(i_content_0_i))
        
        
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    i_list_from_the_mixer_0_i = i_list_0_i.copy()
    
    i_list_of_possible_Sets_1_i = []
    
    
    i_list_of_all_steps_0_i = []
    
    
    
    if (i_last_spliter_0_i - i_first_spliter_0_i == 0):
        
        
        
        
        i_list_of_possible_Sets_1_i = i_get_list_of_dimenssion_1_i(i_list_0_i=i_list_from_the_mixer_0_i, i_separater_0_i=i_first_spliter_0_i)[0]
        
        
        
    
    else:
        
        
        
        
        i_v_0_i = i_get_list_of_dimenssion_2_i(i_list_from_the_mixer_0_i=i_list_from_the_mixer_0_i, i_first_spliter_0_i=i_first_spliter_0_i, i_last_spliter_0_i=i_last_spliter_0_i)
        
        
        
        

        i_list_of_possible_Sets_1_i = i_v_0_i[1]
        
        
        
        i_list_of_all_steps_0_i = i_v_0_i[2]
        
        

    
    
    
    
    return [i_list_from_the_mixer_0_i, i_list_of_possible_Sets_1_i, i_list_of_all_steps_0_i, i_last_spliter_0_i]








def i_get_list_of_dimenssion_0_i(i_list_0_i):
    
    
    
    
    '''
    
    
    this is the function target .
    
    this function i believe can give you all dimenssions possible .
    
    
    
    '''
    
    
    
    
    
    i_list_from_the_mixer_0_i = copy.deepcopy(i_list_0_i)
    
    i_list_of_possible_Sets_1_i = []
    
    
    i_list_of_all_steps_0_i = []
    
    
    i_history_of_all_steps_0_i = []
    
    
    
    if (i_last_spliter_0_i - i_first_spliter_0_i == 0):
        
        
        
        
        i_list_of_possible_Sets_1_i = i_get_list_of_dimenssion_1_i(i_list_0_i=i_list_from_the_mixer_0_i, i_separater_0_i=i_first_spliter_0_i)[0]
        
        
        
    
    else:
        
        
        
        
        i_v_0_i = i_get_list_of_dimenssion_3_i(i_list_from_the_mixer_0_i=i_list_from_the_mixer_0_i, i_first_spliter_0_i=i_first_spliter_0_i, i_last_spliter_0_i=i_last_spliter_0_i)
        
        
        
        
        
        i_list_of_possible_Sets_1_i = i_v_0_i[2]
        
        
        i_list_of_all_steps_0_i = i_v_0_i[0]
        
        
        i_history_of_all_steps_0_i = i_v_0_i[3]
    
    


    
    
    i_list_of_all_contents_0_i = i_get_content_if_it_exist_1_i(i_list_of_all_steps_0_i=i_list_of_all_steps_0_i)
    
    
    
    i_list_of_length_of_each_deepth_0_i = i_extract_the_length_of_each_deepth_0_i(i_history_of_all_steps_0_i=i_history_of_all_steps_0_i)
    
    
    
    
    
    
    '''
    
    you should read only this list that are returned  
    
    if you want to catch this result you should do a deep_copy . for example :
        
        
        import copy
        
        
        original_list = [[1, 2], 3, 4]
        
        new_list = copy.deepcopy(original_list)
        
        
    
    
    '''
    
    
    
    return [i_list_from_the_mixer_0_i, i_list_of_possible_Sets_1_i, i_list_of_all_steps_0_i, i_last_spliter_0_i, i_list_of_all_contents_0_i, i_history_of_all_steps_0_i, i_list_of_length_of_each_deepth_0_i]






if __name__ == "__main__":
    
    
    
    
    
    
    i_list_0_i = [0, 1, 2, 0, 3, 1, 0, 2, 0, 4, 2, 0, 0, 1, 2, 1, 1]
    
    
    print(f"i_list_0_i = {i_list_0_i} .")
    
    
    
    
    i_v_0_i = i_get_list_of_dimenssion_0_i(i_list_0_i=i_list_0_i)
    
    
    i_v_1_i = copy.deepcopy(i_v_0_i)
    
    

    i_list_of_possible_Sets_1_i = i_v_1_i[1]


    i_list_of_all_contents_0_i = i_v_1_i[4]
    
    
    i_history_of_all_steps_0_i = i_v_1_i[5]
    
    
    i_list_of_all_steps_0_i = i_v_1_i[2]
    
    
    i_list_of_length_of_each_deepth_0_i = i_v_1_i[6]
    
    
    
    print(f"\n i_list_of_possible_Sets_1_i = {i_list_of_possible_Sets_1_i} .\n")


    print(f"\n i_list_of_all_contents_0_i = {i_list_of_all_contents_0_i} .\n\n")
    
    
    print(f"\n i_history_of_all_steps_0_i = {i_history_of_all_steps_0_i} .\n\n")
    
    
    print(f"\n i_list_of_all_steps_0_i = {i_list_of_all_steps_0_i} .\n\n")
    
    
    print(f"\n i_list_of_length_of_each_deepth_0_i = {i_list_of_length_of_each_deepth_0_i} .\n\n")
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    
    0 == "0"
    
    1 == "1"
    
    2 == "end_of_file"
    
    3 == "end_of_folder"
    
    
    
    
    
    
    i_list_0_i = [0, 1, 2, 0, 3, 1, 0, 2, 0, 4, 2, 0, 0, 1, 2, 1, 1] .
    
    
    i_list_of_possible_Sets_1_i = [[[[0, 1], [0]], [[1, 0], [0]]], [[[], [0, 0, 1], [1, 1]]]] .
    
    
    i_list_of_all_contents_0_i = [[0, 1], [0], [1, 0], [0], [], [0, 0, 1], [1, 1]] .
    
    
    
    
    
    
    
    '''
    
    
    



































