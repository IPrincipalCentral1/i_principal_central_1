












import os





i_content_0_i = """








identificator : 0

    name : Billal

    pre_name : Debouci

    phone_number : +213561577437

    e_mail : deboubil4@outlook.com

    pass_word : male_principal-central_pass_word_0






start : 




"""




i_content_1_i = ""


i_file_0_i = os.path.join(os.getcwd(), "list_of_diploma.txt")


with open(i_file_0_i, "r") as f_:
    
    
    i_content_1_i = f_.read(os.path.getsize(i_file_0_i))
    
    
    




i_content_1_i = i_content_1_i.split(i_content_0_i)[1]


i_v_0_i = i_content_1_i.split("\n")

print(f"len(i_content_1_i) = {len(i_content_1_i)}")




i_counter_0_i = 0

while (i_counter_0_i < len(i_v_0_i)):
    
    
    if (i_v_0_i[i_counter_0_i] != ""):
        
        
        i_v_1_i = i_v_0_i[i_counter_0_i].split(":")
        
        
        i_content_0_i += "{ " + f"\"thing\" : {i_v_1_i[0]} , \"type\" : \"diploma_official\" , \"amount\" : {i_v_1_i[3]} , \"amount_of_quality\" : {i_v_1_i[3]}" + " }\n\n"
        
        
        
    
    
    i_counter_0_i += 1
    
    
    
    
    
i_file_1_i = os.path.join(os.getcwd(), "i_list_of_diploma_1_i.txt")



with open(i_file_1_i, "w") as f_:
    
    
    f_.write(i_content_0_i)












