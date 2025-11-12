




































































































#!/usr/bin/env python3
"""

lucas_lehmer.py




is : ( ( 2 ** (82_589_933) ) - 1 ) a prime number ?






تحقق من أن M_p = 2^p - 1 عدد أولي باستخدام اختبار Lucas-Lehmer
(مناسب فقط للأعداد من شكل ميرسين حيث p يجب أن يكون أولياً).

مثال:
    python3 lucas_lehmer.py 7
    python3 lucas_lehmer.py 31
    
    
"""


def i_get_binary_0_i(i_number_0_i):
    
    
    i_content_result_0_i = ""
    
    
    i_counter_0_i = 0
    
    while (i_number_0_i > 0):
        
        
        i_mod_0_i = i_number_0_i % 2
        
        i_number_0_i = i_number_0_i // 2
        
        
        i_content_result_0_i = str(i_mod_0_i) + i_content_result_0_i
        
        
    
    
    
    return i_content_result_0_i
    


def i_get_next_prime_number_0_i(i_list_0_i):
    
    
    
    i_number_0_i = i_list_0_i[-1] + 2
    
    
    
    i_semaphore_of_find_prime_number_0_i = False 
    
    
    while (i_semaphore_of_find_prime_number_0_i == False):
        
        
        i_counter_0_i = 0
        
        while ((i_counter_0_i < len(i_list_0_i)) and (i_number_0_i % i_list_0_i[i_counter_0_i] != 0)):
                    
            i_counter_0_i += 1
            
            
        
        if (i_counter_0_i >= len(i_list_0_i)):
            
            
            i_list_0_i.append(i_number_0_i)
            
            i_semaphore_of_find_prime_number_0_i = True
            
            
        else:
            
            
            i_number_0_i += 2
            
            
        
    
    return i_list_0_i
    


# ---------- واجهة بسيطة ----------
def main():
    
    
    i_list_0_i = [2, 3]
    
    
    i_number_of_times_0_i = 100
    
    i_number_0_i = 2
    
    i_counter_0_i = 0
    
    
    
    print(f"\n i_counter_0_i = {i_counter_0_i} .\n i_number_0_i = {i_number_0_i} .")
    
    in_binary = i_get_binary_0_i(i_number_0_i=i_number_0_i)
    
    
    print(f"    in_binary = {in_binary} .")
    
    
    
    
    
    i_number_0_i = 3
    
    i_counter_0_i += 1
    
    
    print(f"\n i_counter_0_i = {i_counter_0_i} .\n i_number_0_i = {i_number_0_i} .")
    
    in_binary = i_get_binary_0_i(i_number_0_i=i_number_0_i)
    
    
    print(f"    in_binary = {in_binary} .")
    
    
    relative_div_invers_to_prime_number_1 = 1
    
    i_counter_0_i += 1
    
    
    while (i_counter_0_i < i_number_of_times_0_i):
    
        
        
        i_list_0_i = i_get_next_prime_number_0_i(i_list_0_i=i_list_0_i)
        
        i_number_0_i = i_list_0_i[-1]
        
        
        print(f"\n i_counter_0_i = {i_counter_0_i} .\n i_number_0_i = {i_number_0_i} .")
        
        in_binary = i_get_binary_0_i(i_number_0_i=i_number_0_i)
        
        
        relative_div_to_prime_number = i_list_0_i[-1] / len(i_list_0_i)
        
        
        relative_div_invers_to_prime_number = len(i_list_0_i) / i_list_0_i[-1]
        
        
        relative_sub_to_prime_number = i_list_0_i[-1] - len(i_list_0_i)
        
        print(f"    in_binary = {in_binary} .\n    relative_div_to_prime_number = {relative_div_to_prime_number} .")
        
        print(f"    relative_sub_to_prime_number = {relative_sub_to_prime_number} .\n    "
        
        "relative_div_invers_to_prime_number = {relative_div_invers_to_prime_number} .")
        
        if (relative_div_invers_to_prime_number > relative_div_invers_to_prime_number_1):
            
            print(f"    UP .")
            
            
        else:
            
            
            print(f"    UP .")
            
            
        
        relative_div_invers_to_prime_number_1 = relative_div_invers_to_prime_number
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
if __name__ == "__main__":
    
    main()
    





























