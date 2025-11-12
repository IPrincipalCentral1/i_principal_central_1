




































































































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
    



# ---------- واجهة بسيطة ----------
def main():
    
    
    
    i_number_0_i = 10
    
    
    i_v_0_i = i_get_binary_0_i(i_number_0_i=i_number_0_i)
    
    
    print(f"i_v_0_i = {i_v_0_i} .")
    
    
    
    
if __name__ == "__main__":
    
    main()
    





























