














import os

import time



cwd = os.path.dirname(os.path.abspath(__file__))




encoding_0 = "utf-8"



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



















    

def main():
    
    
    
    
    file_0 = "/mnt/mydisk/shared_directory_on_PC/my_link_updated/i_directory/main_editor_of_code/edit-or_of_code_for_program/edit-or_of_code/files_0/space_1/file_0.txt"
    
    
    
    
    
    
    result_0 = i_function_reformater_0(name_of_file=file_0)
    
    
    print(f"result_0 = {result_0} .")
    
    
    result_1 = i_inverse_reformater_0(the_content_to_make_the_reverse_on_it=result_0)
    
    
    print(f"result_1 = {result_1} .")
    
    
    
    with open(file_0, "r", encoding=encoding_0) as f_:
        
        content_0 = f_.read(os.path.getsize(file_0))
        
    
    print(f"(content_0 == result_1) = {content_0 == result_1}")
    
    
    
    string_0 = "i_hello_0 .\ni_hello_1 ..\ni_hello_2 ..."
    
    caracter_0 = " " * 4
    
    number_0 = 10
    
    
    counter_0 = 0
    
    while (counter_0 < number_0):
        
        
        string_0 = shift_0(content_to_shift=string_0, caractere=caracter_0)
        
        counter_0 += 1
        
    
    string_1 = string_0
        
    print(f"string_1 = {string_1} .")
    
    
    
    
    counter_0 = 0
    
    while (counter_0 < number_0 - 1):
        
        
        string_1 = unshift_0(content_to_shift=string_1, length_of_caractere=len(caracter_0))
        
        counter_0 += 1
        
    
    
    string_2 = string_1
    
    
    print(f"string_2 = {string_2} .")
    


    # تجربة

    file_path = "example.pdf"
    
    for msg in check_pdf_content(file_path):
    
        print(f"msg = {msg}")
    
    


    
    number_0 = mesurer_1(number_of_depth)
    
    print(f"number_0 = {number_0} .")




if __name__ == "__main__":
    
    
    main()
    
    
    








