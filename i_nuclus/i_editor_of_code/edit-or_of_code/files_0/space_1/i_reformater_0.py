














import os


cwd = os.path.dirname(os.path.abspath(__file__))




encoding_0 = "utf-8"




def i_reformater(name_of_file):
    
    
    
    result_0 = "\""
    
    content_0 = ""
    
    with open(name_of_file, "r", encoding=encoding_0) as f_:
        
        content_0 = f_.read(os.path.getsize(name_of_file))
        
        
    
    content_0 = content_0.replace("\n", "\\n")
    
    content_0 = content_0.replace("\"", "\\\"")
    
    
    result_0 = content_0 + "\""
    
    
    
    return result_0
    
    




    

def main():
    
    
    file_0 = "/mnt/mydisk/shared_directory_on_PC/my_link_updated/i_directory/main_editor_of_code/edit-or_of_code_for_program/edit-or_of_code/files_0/space_1/file_0.txt"
    
    
    
    
    
    result_0 = i_reformater(name_of_file=file_0)
    
    
    print(f"result_0 = {result_0} .")








if __name__ == "__main__":
    
    
    main()
    
    
    








