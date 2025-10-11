

















































































































import os

cwd = os.path.dirname(os.path.abspath(__file__))







# start of parametter :

# -----------------------------------------------------------------------------------




i_first_spliter_0_i = 1


i_last_spliter_0_i = 1





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




    
    





def i_get_list_of_dimenssion_0_i():
    
    
    
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
        
        
        
    
    
    return i_list_0_i




if __name__ == "__main__":
    
    
    
    i_v_0_i = i_get_list_of_dimenssion_0_i()
    
    print(f"i_v_0_i = {i_v_0_i} .")
    
    




































