











'''


convert from binary to string .



'''








import os





cwd = os.path.dirname(os.path.abspath(__file__))



i_length_of_byte_0_i = 8





i_name_of_file_0_i = os.path.join(cwd, "i_file_to_transforme_into_string_0_i.binary")








def i_convert_from_decimal_to_binary_0_i(i_number_0_i):
    
    
    
    i_binary_0_i = ""
    
    
    if i_number_0_i <= 0:
        
        i_binary_0_i = "0"
        
    
    while i_number_0_i > 0:
        
        i_remainder_0_i = i_number_0_i % 2
        
        i_binary_0_i = str(i_remainder_0_i) + i_binary_0_i
        
        i_number_0_i = i_number_0_i // 2
    
    
    
    while (len(i_binary_0_i) < i_length_of_byte_0_i):
        
        
        i_binary_0_i = "0" + i_binary_0_i
        
        
        
    
    
    
    return i_binary_0_i




















def i_convert_from_binary_to_string_0_i():


    
    
    
    
    i_string_of_binary_0_i = ""
    
    
    
    
    with open(i_name_of_file_0_i, "rb") as i_f_0_i:
        
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < os.path.getsize(i_name_of_file_0_i)):
            
            
            i_information_in_binary_0_i = i_f_0_i.read(1)
            
            
            i_number_0_i = int.from_bytes(i_information_in_binary_0_i, byteorder="big")
            
            
            i_number_in_binary_0_i = i_convert_from_decimal_to_binary_0_i(i_number_0_i=i_number_0_i)
            
            
            
            if (i_counter_0_i == 0):
                
                
                i_string_of_binary_0_i += i_number_in_binary_0_i
                
            else:
                
                i_string_of_binary_0_i += " " + i_number_in_binary_0_i
                
            
            #print(f"i_counter_0_i = {i_counter_0_i} . i_number_0_i = {i_number_0_i} . i_number_in_binary_0_i = '{i_number_in_binary_0_i}' .")
            
            
            
            
            
            i_counter_0_i += 1
            
            
            
            
        
        
    
    return i_string_of_binary_0_i
    
    
    
    
    
    




def i_main_0_i():
    
    
    
    
    i_list_0_i = []
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < 256):
        
        i_list_0_i.append(i_counter_0_i)
        
        i_counter_0_i += 1
        
        
    
    
    
    
    with open(i_name_of_file_0_i, "wb") as i_f_0_i:
            
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_0_i)):
        
            
            
            i_number_0_i = i_list_0_i[i_counter_0_i]
            
            
            i_information_in_binary_1_i = i_number_0_i.to_bytes(1, byteorder="big")
            
            
            i_f_0_i.write(i_information_in_binary_1_i)
            
            
            
            i_counter_0_i += 1
            
            
            
            
            
    
    
    
    
    
    i_string_of_binary_0_i = ""
    
    
    
    i_string_of_binary_0_i = i_convert_from_binary_to_string_0_i()
    
    
        
    print(f"i_string_of_binary_0_i = '{i_string_of_binary_0_i}' .")
    
    
    
    
    



if __name__ == "__main__":
    
    
    
    i_main_0_i()
    











