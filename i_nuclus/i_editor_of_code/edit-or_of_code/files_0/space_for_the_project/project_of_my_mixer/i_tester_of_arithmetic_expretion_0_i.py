
















'''




you should put the list of all your variables here :
    
    
    i_list_of_variables_0_i
    
    
    
and than you should put your expretion here :
    
    
    i_operation_0_i
    
    
    



you should make the variables in between 2 spaces :
    
    
    i_list_of_variables_0_i = [" i_v_0_i ", " i_v_1_i ", " i_v_2_i "]
    
    
    



the arithmetic expretion use just :
    
    
    [" + ", " - ", " * ", " / ", " // ", " ** ", " % " , " if ", " else ", " == ", " >= ", " <= ", " > ", " < ", " != ", " := ", " ( ", " ) ", " [ ", " ] ", " , ", " for ", " in "]
    
    
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    
    
    add your operators and put it between 2 spaces
    
    
    add the functions if you have ( do not put them in between 2 spaces ) . ( remember to declare your function in i_init_of_variables_0_i if they are not declared ) . Example :
        
        
        ["cos", "sin", "tan", "range", "len", ...]
        
        
    
    
    
    
    add ( your variables separatly . Ex : [" x1 ", " x2 ", ...] ) or ( as list . Ex : i_list_0_i . that contain all the values of your variables . 
    
        and remember to declare the list like : i_list_0_i = ["value_of_variable_1", "value_of_variable_2", ...] ) .
    
    
    
    
    




when you use it after the mix . you should include this range of mix in the mixer before :
    
    
    
    
    [" + ", " - ", " * ", " / ", " // ", " ** ", " % " , " if ", " else ", " == ", " >= ", " <= ", " > ", " < ", " != ", " := ", " ( ", " ) ", " [ ", " ] ", " , ", " for ", " in "]
    
    
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
    
    
    add your operators and put it between 2 spaces
    
    
    add the functions if you have ( do not put them in between 2 spaces ) . ( remember to declare your function in i_init_of_variables_0_i if they are not declared ) . Example :
        
        
        ["cos", "sin", "tan", "range", "len", ...]
        
        
        
    
    
    
    add ( your variables separatly . Ex : [" x1 ", " x2 ", ...] ) or ( as list . Ex : i_list_0_i . that contain all the values of your variables . 
    
        and remember to declare the list like : i_list_0_i = ["value_of_variable_1", "value_of_variable_2", ...] ) .
    
    
    
    
    



there is a constraint right here . wich is let it just calcule .


it means do not make function that do not just do the calcule .

for example :
    
    
    request
    
    print()
    
    time.time()
    
    
    
    and so on ...
    
    





# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------










i have an idea . if i want to build a compiler . i can use a program with the help of my mixer . to do it .


like when we have this string :
    
    
    i_string_0_i = " a * ( b + c ) "
    
    
and we want to make it like that :
    
    
    i_string_result_0_i = " a * b + a * c "
    
    


we can make a compiler that do that by finding the function in python that make it .

we should first transform the i_string_0_i into a list . like that :
    
    
    i_list_0_i = list(i_string_0_i)
    
    



and than we trandform each caractere in the utf-8 code into a number in the table . like : from 0 to 1_112_064


and than we represent the null value as : -1 


and than we represent the binary bytes like that : from 0 to 255 , like from -2 to -257 





and than we should give 10 examples about what we want . even by changing the name of variables . like that :
    
    
    Example_1 :
        
        
        from :
            
            i_string_0_i = " a * ( b + c ) "
            
        to : 
            
            
            i_string_result_0_i = " a * b + a * c "
            
            
        
    
    
    Example_2 :
        
        
        from :
            
            i_string_0_i = " a2 * ( b2 + c2 ) "
            
        to : 
            
            
            i_string_result_0_i = " a2 * b2 + a2 * c2 "
            
            
        
    
    
    Example_3 :
        
        
        from :
            
            i_string_0_i = " a3 * ( b3 + c3 ) "
            
        to : 
            
            
            i_string_result_0_i = " a3 * b3 + a3 * c3 "
            
            
        
    
    and so on ...
    
    
    

and what we do for each example is puting it into the list . 
    
    
    i_list_0_i = list(i_string_0_i)
    
    
    


and add the list into the table of mixer . like mentioned on the top .
    
    
    so we add the list : 
        
        
        i_list_0_i
        
    
    and add a bunch of variables for using it in loops :
        
        
        [" i_counter_0_i ", " i_counter_1_i ", ... " i_counter_n_i "]
        
        
        
        or a list of counters like that ( this is much better ) :
            
            
            [" i_list_of_counters_0_i "]
            
            
            you initialize this one like that :
                
                
                i_list_of_counters_0_i = [0]
                
                
            
              
    


and we use the get_list_dimenssion with 1 spliter ( so we should impliment in the table of mix all of that ) .



and we get each element of 1 dimenssion and we put it in the element of our list : i_list_0_i






lets take an example of :
    
    
    
    Example_1 :
        
        
        from :
            
            i_string_0_i = " a * ( b + c ) "
            
        to : 
            
            
            i_string_result_0_i = " a * b + a * c "
            
            
        
    
    

we have :
    
    
    i_list_0_i = list(i_string_0_i)
    

so the list will be :
    
    
    i_list_0_i = [" ", "a", " ", "*", " ", "(", " ", "b", " ", "+", " ", "c", " ", ")", " "]
    
    


we will change all the items to number . for example :
    
    
    

    
    
    
    def i_function_of_turning_list_into_numbers_0_i(i_list_0_i):
        
        
        
        
        i_list_1_i = []
        
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_0_i)):
            
            
            i_list_1_i.append(ord(i_list_0_i[i_counter_0_i]))
            
            
            i_counter_0_i += 1
            
        
        
        
        
        
        
        return i_list_1_i
    
    
    
    
    
    
    
    

and we will get this :
    
    
    i_list_1_i = [32, 97, 32, 42, 32, 40, 32, 98, 32, 43, 32, 99, 32, 41, 32] 
    
    

so this is the list that we do the calcule into it .


and the number of 1 dimenssions max is : len(i_list_1_i)


so we let the mixer find the function the transform for us : 
    
    
    
    from : 
        
        
        i_list_0_i = [" ", "a", " ", "*", " ", "(", " ", "b", " ", "+", " ", "c", " ", ")", " "]
        
        
        i_list_1_i = [32, 97, 32, 42, 32, 40, 32, 98, 32, 43, 32, 99, 32, 41, 32] 
        
        
    
    into :
        
        
        i_list_0_i = [' ', 'a', ' ', '*', ' ', 'b', ' ', '+', ' ', 'a', ' ', '*', ' ', 'c', ' '] 
        
        
        i_list_2_i = [32, 97, 32, 42, 32, 98, 32, 43, 32, 97, 32, 42, 32, 99, 32] 
            
    
    

there is something that we want . we want the smollest path to the solution ( we conclude that from the length of the list of the mix itself ) .


it means the same function will work for all the Examples .



if we do not want to use multi dimenssions . we should add the varibale that hold the index . like wich item we are using now .

for Example : 
    
    
    0 for i_list_1_i[0]
    
    1 for i_list_1_i[1]
    
    2 for i_list_1_i[2]
    
    
    and so on ...



like i_variable_of_index_0_i . and we initialize with his reel value . 


or we can use a list of dimenssion . like :
    
    
    i_list_of_index_of_dimenssions_0_i[0] for spliting 1 dimenssion ( like in a text linear ) 
    
    
    i_list_of_index_of_dimenssions_0_i[1] for spliting 2 dimenssion ( like in an image 2 dimensional ) 
    
    
    i_list_of_index_of_dimenssions_0_i[3] for spliting 3 dimenssion
    
    
    and so on ...
    

so like that :
    
    
    [" i_list_of_index_of_dimenssions_0_i "]
    
    
and initialize like that :
    
    
    i_list_of_index_of_dimenssions_0_i = [0] # for 1 dimension 
    
    
    i_list_of_index_of_dimenssions_0_i = [0, 0] # for 2 dimension 
    
    
    i_list_of_index_of_dimenssions_0_i = [0, 0, 0] # for 3 dimension 
    
    
    
    
    and so on ...
    
    


until we have the function of the compiler .






we can use this to train a neural net . with just 1 neuron . because the neuron is just a function . and if we find the function is like 

we have the training .














# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------





i have an idea .



if i want to play a game .


my artificial intelligance of bot of chat can speak any language .


so if we do :
    
    
    
    i_add_generater_of_phrase_0_i = True
    
    
    
    i_add_generater_of_word_0_i = False





and we do all the functions that the game allow . with a modification of each one . like that :
    
    
    function_1 :
        
        
        if it is possible to do this move :
            
            
            we do the move
            
            
        
        
    
    
    function_2 :
        
        
        if it is possible to do this move :
            
            
            we do the move
            
            
        
    


and we order all the functions in a list . like that :
    
    
    i_function_0_i
    
    i_function_1_i
    
    i_function_2_i
    
    
    and so on ...



and we put them into the input of my artificial intelligance of bot of chat .


the output will be something like that :
    
    
    i_function_0_i i_function_1_i i_function_2_i i_function_0_i . i_function_0_i i_function_2_i i_function_1_i i_function_0_i ...
    
    


and we do the resizeing in between the input ( variables or parametters ) and the output ( functions ) . 


it means : length_of_input == length_of_output .


and we make them the same :
    
    input :
        
        
        i_function_0_i
        
        i_function_1_i
        
        i_function_2_i
        
        
        ...
        
        i_function_n_i
        
        
        
    output :
        
        
        
        i_function_0_i
        
        i_function_1_i
        
        i_function_2_i
        
        
        ...
        
        i_function_n_i
        
    
    
    

and lets try to avoid loss . in the process of resizeing ( resize(i_list_of_items_0_i) ).


and than play the game . but lets play with the game . like in the discution between a person and an ai .


except we consider the input as the discution from the game . and the output as a respense back from us .


and in the way of doing that we regester the functions that have been executed . like what i said before :
    
    
    
    function_1 :
        
        
        if it is possible to do this move :
            
            
            we do the move .
            
            we register that .
            
        
    
    




and right here we start the work . 


now lets make a function like mentioned at the top . that have this interaction between the input and the output .


so the function receive some input . and than it produce some output .


acording to what have been regestered in the discution between my ai and the game . 





and we play a lot . so the function built get feeded nicely ( until all functions get used and played 


( we can mesure the power of the model ( function ) by making a new model from 0% use of all functions to 100% of use of all functions ,


the number of functions is relaying on the number of disction between my ai and the game ) ) .







and than we have a function that can play nicely a game .









# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------








be careful . if the compiler python can not handel the length of the function :
    
    
    length of code exceed limits .
    
    

you should plan to do the compiler python using this maker of function . as was showen before ( give 10 diffrent Examples and build the function ) .





so now target : make the compiler python .





Example :
    
    
    
    input
    {
    
    
    print(f"i_hello_i .")
    
    
    
    }
    
    
    
    the_output should be step by step until to get the binary file .
    
    
    








# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------





i have an idea .



we can do a function that do anything we want .


now lets play with it .


lets make a dictionary . like that :
    
    
    {i_length_of_what_coming_next_0_i} 
    {
        
        
        "the_name_of_language" : {the_name_of_language},
        
        
        "words" : [{the_words_with_there_description_in_list : ["word_0" , "description_0", "we_can_impliment_extra_information_like_an_image_and_a_video_and_a_3D_format_of_the_thing_even_in_video (the essantial a very very powerful extra informations)"]}]
        
                
    }
    
    
    

all of that from : " " 

it means the function will generate from just " " to all of that .



now we add 10 languages to the function .




after that we do a syntax to speak with hte function . { input : text , output : text }


but we take account that the function in the future can bring new words when we expend the index to more than the range ( it is good ) .




and now we can start :



now we should start training more extra training to this funtion .


we should do train more this function to train the function until :
    
    
    {
        
        "the_name_of_language" : {the_name_of_language} , 
        
        
        "extra_informations" : {extra_informations} , 
        
        
        and than a question .
        
    }


and than the function will start answering the question ( at lest this is what it supose to do ).








and now each time we add a prompt of a new question we do ( retrain the function again at ) :
    
    
    
    {
        
        "the_name_of_language" : {the_name_of_language} , 
        
        
        "extra_informations" : {extra_informations} , 
        
        
        question_0
        
        answer_0
        
        
        question_1
        
        answer_1
        
        
        
        and so on ...
        
        
        
        question_n
        
        
        
        
        
        
    }
    
    
    
    
and than wait for the answer after that .



    



we can impliment even code in the extra information so we make the function capable of producing code . and files . i mean a file zip that 


contain the files and folders and code inside those files ( we can even impliment binary files in the zip file ) .








we can the degree of power of the function by adding more word in the dictionary ( from where those words just from the function ) . like that :
    
    
    
    
    {
        
        "the_name_of_language" : {the_name_of_language} , 
        
        
        
        "extra_informations" : {extra_informations__in_the_extra_information_we_add_more_words_to_make_it_more_powerful} , 
        
        
        question_0
        
        answer_0
        
        
        question_1
        
        answer_1
        
        
        
        and so on ...
        
        
        
        question_n
        
        
        
        
        
        
        
        
    }
    
    
    
    
    


if we want information in real time . we can add more extra information about the world around us in real time ( i mean from the current time ) .




( we can add even other functions ( well defined . i mean with the "import" and all the information to run the functions ) 

right there in the extra information )





lets make the number of words in that dictionary a variable called :
    
    
    i_var_of_number_of_words_in_dictionary_0_i 
    
    


lets make it minimum : 1_000_000 


and lets make the number of words given by the initialization ( i mean from us ) in a variable called :
    
    
    
    i_var_of_number_of_words_init_dictionary_0_i 
    
    



lets make it minimum : 1_000
    
    
    
    





# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------










    
    
    
    
    





    
    
    
    
    
    


 






    










    
    










'''




















import ast


import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))










# start section of parameter 

# ------------------------------------------------------------------------------

# start_section_of_parameter 












i_list_of_variables_0_i = [" i_v_0_i ", " i_v_1_i ", " i_v_2_i "]






i_operation_0_i = " i_v_0_i  +  i_v_0_i "




i_content_of_import_0_i = r"""


import math





"""




i_init_of_variables_0_i = r"""



i_v_0_i = 1



"""









# end_section_of_parameter 

# -----------------------------------------------------------------------------

# end section of parameter 














i_file_0_i = os.path.join(cwd, "i_main_of_test_2_i.py")


i_file_1_i = os.path.join(cwd, "i_main_of_test_2_0_i.py")


i_file_4_i = os.path.join(cwd, "i_file_of_semaphore_of_error_compilation_0_i.txt")




i_content_of_testing_0_i = r"""













_____i_section_of_import_0_i_____






import os



cwd = os.path.dirname(os.path.abspath(__file__))







i_var_of_result_0_i = False






_____i_variables_0_i_____




_____i_init_of_variables_1_i_____





if ((_____i_expretion_0_i_____ + 1) >= 10):
    
    
    
    i_var_of_result_0_i = True
    
    
else:
    
    
    
    
    i_var_of_result_0_i = True
    
    
    



i_file_4_i = os.path.join(cwd, "i_file_of_semaphore_of_error_compilation_0_i.txt")





with open(i_file_4_i, "w") as f_:
    
    
    f_.write("False")
    









"""











def i_main_0_i():
    
    
    
    
    i_content_0_i = i_content_of_testing_0_i
    
    
        
        
        
    
    
    
    
    
    
    
    i_content_of_variables_0_i = "\n\n"
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < len(i_list_of_variables_0_i)):
        
        
        
        
        i_var_0_i = i_list_of_variables_0_i[i_counter_0_i]
        
        
        i_counter_1_i = 0
        
        
        while ((i_counter_1_i < len(i_var_0_i)) and (i_var_0_i[i_counter_1_i] == " ")):
            
            
            i_counter_1_i += 1
            
            
            
        
        i_var_0_i = i_var_0_i[i_counter_1_i:]
        
        
        i_content_of_variables_0_i += i_var_0_i + " = 1\n\n"
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
    
    
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_section_of_import_0_i_____", i_content_of_import_0_i)
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_variables_0_i_____", i_content_of_variables_0_i)
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_expretion_0_i_____", i_operation_0_i)
    
    
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_init_of_variables_1_i_____", i_init_of_variables_0_i)
    
    
    
    
    
    
    
    
    with open(i_file_1_i, "w") as f_:
        
        
        f_.write(i_content_0_i)
        
        
        
        
        
    
    
    
    
    
    
    with open(i_file_4_i, "w") as f_:
        
        
        f_.write("True")
        
        
    
    
    
    
    os.system(f"{sys.executable} {i_file_1_i}")
    
    
    
    
    
    
    
    
    i_content_1_i = ""
    
    
    with open(i_file_4_i, "r") as f_:
        
        
        i_content_1_i = f_.read(os.path.getsize(i_file_4_i))
        
        
    
    
    
    
    
    #print(f"i_content_1_i = {i_content_1_i} .") 
    
    
    if (i_content_1_i == "True"):
        
        
        i_var_of_error_compilation_0_i = True
        
        
    elif (i_content_1_i == "False"):
        
        
        i_var_of_error_compilation_0_i = False
        
        
        
    
    
    
    
    return i_var_of_error_compilation_0_i










if __name__ == "__main__":
    
    
    
    
    i_var_of_error_compilation_0_i = i_main_0_i()
    
    
    print(f"i_var_of_error_compilation_0_i = {i_var_of_error_compilation_0_i}")
    
    
    


















