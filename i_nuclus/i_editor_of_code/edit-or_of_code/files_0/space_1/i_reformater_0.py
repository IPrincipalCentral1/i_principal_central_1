














import os

import time



cwd = os.path.dirname(os.path.abspath(__file__))




encoding_0 = "utf-8"











list_of_liberary_to_install = [

                            ["PyMuPDF"] ,
                            
                            
                            


]










import os


import traceback

import sys


import subprocess




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


    









def mesurer_of_time_0(time_0):
    
    
    t1 = time.time()
    
    t2 = time.time()
    
    while (t2 - t1 < time_0):
        
        t2 = time.time()
        
        
        
    





def mesurer_0():
    
    
    # this function return how much the speed of the computer per 1 second 
    
    
    i_counter_0 = 0
    
    t1 = time.time()
    
    t2 = time.time()
    
    while (t2 - t1 < 1):
        
        i_counter_0 += 1
        
        t2 = time.time()
        
        
        
    
    return len(str(i_counter_0))
    





def mesurer_1(number_of_depth):
    
    
    # this should help understanding the size of the number of the calcule per second 
    
    
    i_counter_0 = 0
    
    i_counter_1 = mesurer_0()
    
    
    
    while (i_counter_0 < number_of_depth):
        
        
        i_counter_1 = len(str(i_counter_1))
        
        i_counter_0 += 1
        
        
    
    
    
    return i_counter_1
    



def mesurer_2():
    
    
    # this function return how much calcule per second can be 
    
    i_counter_0 = 0
    
    while (mesurer_1(number_of_depth=i_counter_0) > 1):
        
        i_counter_0 += 1
        
        
    
    
    if (i_counter_0 > 0):
    
        i_counter_0 -= 1
        
        
        
    
    
    # return last_number , number_of_depth
    
    
    return [mesurer_1(number_of_depth=i_counter_0), i_counter_0]
    
    
    
    





def mesurer_3():
    
    
    # this function return how much calcule per second can be 
    
    
    
        
    
    i_counter_0 = 0
    
    i_counter_1 = mesurer_0()
    
    
    i_counter_2 = i_counter_1
    
    
    while (i_counter_1 > 1):
            
        i_counter_2 = i_counter_1    
        
        i_counter_1 = len(str(i_counter_1))
        
        i_counter_0 += 1
        
        
    
    
    
    
    if (i_counter_0 > 0):
    
        i_counter_0 -= 1
        
        
        
    
    
    # return last_number , number_of_depth
    
    
    return [i_counter_2, i_counter_0]
    
    




def mesurer_4(number_0):
    
    
    # this function return how much number_0 can be 
    
    
    
        
    
    i_counter_0 = 0
    
    i_counter_1 = number_0
    
    
    i_counter_2 = i_counter_1
    
    
    while (i_counter_1 > 1):
            
        i_counter_2 = i_counter_1    
        
        i_counter_1 = len(str(i_counter_1))
        
        i_counter_0 += 1
        
        
    
    
    
    
    if (i_counter_0 > 0):
    
        i_counter_0 -= 1
        
        
        
    
    
    # return last_number , number_of_depth
    
    
    return [i_counter_2, i_counter_0]
    
    







def mesurer_5(number_0, number_of_depth):
    
    
    # this function return how much number_0 can be with the number_of_depth  
    
    
    
        
    
    i_counter_0 = 0
    
    i_counter_1 = number_0
    
    
    
    while (i_counter_0 < number_of_depth):

        i_counter_1 = len(str(i_counter_1))
        
        i_counter_0 += 1
        
        
    
    
    
    
    # return last_number 
    
    
    return i_counter_1
    
    




def mesure_6():
    
    
    
    
    # this function return how much calcule per second can be . but much better than mesurer_3() .
    
    
    i_v_i_0 = mesurer_3()
    
    
    i_v_i_1 = mesurer_4(number_0=i_v_i_0[1])
    
    print(f"i_hello_i_0 . i_v_i_0 = {i_v_i_0} . i_v_i_1 = {i_v_i_1} .")
    
    
    
    return [i_v_i_0[0], i_v_i_1]
    
    
    






def i_mesure_7_i(i_number_0_i):
    
    
    '''
    
    this work the same as mesurer_4() but much better .
    
    
    '''
    
    
    
    i_v_1_i = mesurer_4(number_0=i_number_0_i)
    
    
    i_v_2_i = i_v_1_i
    
    
    
    while (i_v_1_i[1] >= 10):
        
        
        i_v_1_i[1] = mesurer_4(number_0=i_v_1_i[1])
        
        i_v_1_i = i_v_1_i[1]
        
        
        
    
    i_s_0_i = str(i_v_2_i)
    
    i_v_3_i = i_s_0_i.split("[")
    
    
    
    return [i_v_2_i, len(i_v_3_i)]
    
    





def i_mesure_8_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesure_7_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesure_7_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while (i_v_1_i[1] > 10):
        
        
        i_v_2_i = i_mesure_7_i(i_number_0_i=i_v_1_i[1])
        
        i_v_1_i[1] = i_v_2_i
        
        i_v_1_i = i_v_1_i[1]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    



def i_mesure_9_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesure_8_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesure_8_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesure_8_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    




def i_mesure_10_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesure_9_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesure_9_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesure_9_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    



def i_mesure_11_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesure_10_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesure_10_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesure_10_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    





def i_mesure_12_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesure_11_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesure_11_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesure_11_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    



def i_mesurer_13_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesure_12_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesure_12_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesure_12_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    



def i_mesurer_14_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesurer_13_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesurer_13_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesurer_13_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    



def i_mesurer_15_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesurer_14_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesurer_14_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesurer_14_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    
    



def i_mesurer_16_i(i_number_0_i):
    
    
    
    '''
    
    this work the same as i_mesurer_15_i() but much better .
    
    
    '''
    
    
    i_v_0_i = i_mesurer_15_i(i_number_0_i=i_number_0_i)
    
    i_v_1_i = i_v_0_i
    
    
    i_v_2_i = i_v_0_i
    
    
    i_counter_0_i = 0
    
    
    
    while ((type(i_v_1_i) == list) and (len(i_v_1_i) == 3) and (i_v_1_i[2] > 10)):
        
        
        i_v_2_i = i_mesurer_15_i(i_number_0_i=i_v_1_i[2])
        
        i_v_1_i[2] = i_v_2_i
        
        i_v_1_i = i_v_1_i[2]
        
        
        i_counter_0_i += 1
        
        
    
    
    '''
    
    return [final_list_0, last_len_0, number_of_step]
    
    
    '''
    
    return [i_v_0_i, i_v_2_i[1], i_counter_0_i]
    






def i_builder_of_number_0(last_number, number_of_depth):
    
    
    # this number_will be build with last_number and number_of_depth  . but with 1 at the beginning and all the rest are 0 .
    
    
    
    
    i_counter_0 = 0
    
    i_counter_1 = last_number
    
    
    
    while (i_counter_0 < number_of_depth):
        
        
        i_counter_1 = ( 10 ** ( i_counter_1 - 1 ) ) 
        
        i_counter_0 += 1
        
        
    
    
    
    
    # return number_0  
    
    
    return i_counter_1
    
    
    




def i_builder_of_number_1_i(i_list_of_the_number_0_i):
    
    
    
    
    
    
    '''
    
    i_builder_of_number_0(last_number, number_of_depth)
    
    
    type(x) == list
    
    '''
    
    
    i_v_0_i = i_list_of_the_number_0_i
    
    
    while ((len(i_v_0_i) > 1)):
        
        
        i_v_1_i = i_v_0_i
        
        i_v_2_i = i_v_1_i
        
        i_v_3_i = i_v_1_i
        
        if (type(i_v_1_i) == list) and (len(i_v_1_i) > 1) and (type(i_v_1_i[1]) == list):
            
            while ((type(i_v_1_i) == list) and (len(i_v_1_i) > 1) and (type(i_v_1_i[1]) == list)):
                
                
                i_v_3_i = i_v_1_i
                
                i_v_1_i = i_v_1_i[1]
            
                i_v_2_i = i_v_1_i
                
                i_v_1_i = i_v_1_i[1]
                
                
            
            
            
            i_number_0_i = i_builder_of_number_0(last_number=i_v_2_i[0], number_of_depth=i_v_2_i[1])
            
            
            i_v_3_i[1].clear()
            
            i_v_3_i.pop(1)
            
            i_v_3_i.append(i_number_0_i)
            
        
        elif (len(i_v_0_i) == 2):
            
            
            
            i_number_0_i = i_builder_of_number_0(last_number=i_v_0_i[0], number_of_depth=i_v_0_i[1])
            
            
            i_v_0_i.pop(0)
            
            i_v_0_i.pop(0)
            
            
            i_v_0_i.append(i_number_0_i)
            
            
        
        
    
    return i_v_0_i
    
    
    
    
    
    
    
    
    



def i_calculat_and_display_in_the_loop_0(first_time, amount_of_time_0):
    
    
    
    
    '''
    
    this function is designed so you add the code that you want to do each time in a loop .
    
    
    
    
    this is how to use this function :
    
    
    import time
        
    
    t1 = time.time()
    
    while (True):
        
        
        # do some calculations 
        
        
        # each 2.0 second .
        
        t1 = i_calculat_and_display_in_the_loop_0(first_time=t1, amount_of_time_0=2.0)
        
        
        # do some other calculations 
        
        
        
        
    
    
    
    
    
    
    '''
    
    
    
    if (time.time() - first_time > amount_of_time_0):
        
        
        # -------------------------------------------------
        
        # this place is for the main of your calculations :
        
        # you can display what you want right here .
        
        # you can add your code right here
        
        
        print(f"i_hello_0 .")
        
        
        
        
        
        
        
        
        pass
        
        
        
        
        
        return time.time()
    
    else:
        
        return first_time
        
        
        
    
    
    





def i_function_reformater_0(name_of_file):
    
    
    
    result_0 = "\""
    
    content_0 = ""
    
    with open(name_of_file, "r", encoding=encoding_0) as f_:
        
        content_0 = f_.read(os.path.getsize(name_of_file))
        
        
    
    content_0 = content_0.replace("\n", "\\n")
    
    content_0 = content_0.replace("\"", "\\\"")
    
    
    result_0 += content_0 + "\""
    
    
    
    return result_0
    
 



def i_function_reformater_1(the_content_to_make_on_it):
    
    
    
    result_0 = "\""
    
    content_0 = the_content_to_make_on_it
    
    
        
    
    content_0 = content_0.replace("\n", "\\n")
    
    content_0 = content_0.replace("\"", "\\\"")
    
    
    result_0 += content_0 + "\""
    
    
    
    return result_0
    
    




def i_inverse_reformater_0(the_content_to_make_the_reverse_on_it):
    
    
    
    
    
    content_0 = the_content_to_make_the_reverse_on_it[1:-1]
        
    content_0 = content_0.replace("\\n", "\n")
    
    content_0 = content_0.replace("\\\"", "\"")
    
    
    
    
    result_0 = content_0
    
    
    return result_0
    



def i_inverse_reformater_1(name_of_file):
    
    
        
    content_0 = ""
    
    with open(name_of_file, "r", encoding=encoding_0) as f_:
        
        content_0 = f_.read(os.path.getsize(name_of_file))
        
        
    
    
    content_0 = content_0[1:-1]
        
    content_0 = content_0.replace("\\n", "\n")
    
    content_0 = content_0.replace("\\\"", "\"")
    
    
    
    
    result_0 = content_0
    
    
    return result_0
    




def shift_0(content_to_shift, caractere=" " * 4):
    
    
    v_0 = content_to_shift.split("\n")
    
    result_0 = ""
    
    
    counter_0 = 0
    
    while (counter_0 < len(v_0) - 1):
        
        
        result_0 += caractere + v_0[counter_0] + "\n"
        
        
        counter_0 += 1
        
        
    
    result_0 += caractere + v_0[counter_0]
    
    
    return result_0
    
    




def unshift_0(content_to_shift, length_of_caractere=4):
    
    
    # length_of_caractere = len(caractere)
    
    v_0 = content_to_shift.split("\n")
    
    result_0 = ""
    
    
    counter_0 = 0
    
    while (counter_0 < len(v_0) - 1):
        
        
        result_0 += v_0[counter_0][length_of_caractere:] + "\n"
        
        
        counter_0 += 1
        
        
    
    result_0 += v_0[counter_0][length_of_caractere:]
    
    
    return result_0
    
    






# PyMuPDF


import fitz  




def check_pdf_content(pdf_path):

    doc = fitz.open(pdf_path)

    results = []

    for page_num in range(len(doc)):

        page = doc[page_num]

        # 1) التحقق من الصور

        images = page.get_images(full=True)

        if images:

            results.append(f"📷 وُجدت صورة في الصفحة {page_num + 1}")

        # 2) التحقق من الرسومات المتجهية

        drawings = page.get_drawings()

        if drawings:

            results.append(f"✏️ وُجدت رسمة متجهية في الصفحة {page_num + 1}")


    if not results:

        return ["✅ الملف يحتوي فقط على نصوص"]


    return results










def i_counter_from_n_to_m_with_incrimenter_0(n, m, incrementer):
    
    
    i_counter_0 = n
    
    i_content_0 = ""
    
    
    while (i_counter_0 <= m):
        
        i_content_0 += f"{i_counter_0:.2f} , "
        
        i_counter_0 += incrementer
        
        
        
    
    return i_content_0
    
    








    

def main():
    
    
    
    
    
    
    i_v_0_i = i_mesure_7_i(i_number_0_i=1_000_000_000_000)
    
    
    print(f"i_v_0_i = {i_v_0_i} .")

    
    i_v_1_i = i_builder_of_number_0(last_number=i_v_0_i[0][0], number_of_depth=i_v_0_i[0][1])
    
    
    print(f"i_v_1_i = {i_v_1_i} .")
    
        
    
    i_list_0_i = [2, 2]
    

    i_v_1_i = i_builder_of_number_1_i(i_list_of_the_number_0_i=i_v_0_i[0])


    print(f"i_v_1_i = {i_v_1_i} .")
    
    
    
    i_number_0_i = 10 ** 100
    
    i_v_2_i = i_mesure_8_i(i_number_0_i=i_number_0_i)
    
    print(f"i_v_2_i = {i_v_2_i} .")
    
    
    
    i_v_3_i = i_mesurer_16_i(i_number_0_i=i_number_0_i)
    
    print(f"i_v_3_i = {i_v_3_i} .")
    
    
    






if __name__ == "__main__":
    
    
    main()
    
    
    








