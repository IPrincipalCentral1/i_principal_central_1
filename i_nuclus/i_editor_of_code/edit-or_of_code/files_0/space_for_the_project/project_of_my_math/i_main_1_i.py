





















































































































list_of_liberary_to_install = [
                            
                            
                            ["sympy"] ,
                            
                                                        
                            ["matplotlib"] ,
                            
                            
                            



]










import os


import traceback

import sys


import subprocess



cwd = os.path.dirname(os.path.abspath(__file__))



print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])





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
    
    
    


print("\n" * 10)







































































































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
    
    
    i_number_of_times_0_i = 1000
    
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
    
    
    i_list_1_i = []
    
    
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
        
        print(f"    relative_sub_to_prime_number = {relative_sub_to_prime_number} .")
        
        print(f"    relative_div_invers_to_prime_number = {relative_div_invers_to_prime_number} .")
        
        i_list_1_i.append(relative_div_invers_to_prime_number)
        
        
        if (relative_div_invers_to_prime_number > relative_div_invers_to_prime_number_1):
            
            print(f"    Up .")
            
            
        else:
            
            
            print(f"    Down .")
            
            
        
        relative_div_invers_to_prime_number_1 = relative_div_invers_to_prime_number
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
    
    import matplotlib.pyplot as plt
    
    # قائمة أعداد
    numbers = i_list_1_i
    
    # رسم القائمة
    plt.plot(numbers)
    
    # عناوين المحاور
    plt.title("Simple Plot Example")
    plt.xlabel("Index")
    plt.ylabel("Value")
    
    # عرض الرسم
    plt.show()
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    
    main()
    




































