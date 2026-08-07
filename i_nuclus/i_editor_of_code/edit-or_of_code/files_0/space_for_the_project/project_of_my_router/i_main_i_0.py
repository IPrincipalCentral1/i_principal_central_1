
















































































































list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess



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









'''







'''





class i_simulation_of_router_0_i():
    
    
    def __init__(self):
        
        
        self.i_content_of_json_0_i = "\n\n[\n\n]"
        
        
        
        
        
    
    
    def i_create_router_0_i(self, i_identificator_0_i, i_name_0_i, i_detail_0_i):
        
        
        
        i_counter_0_i = len(self.i_content_of_json_0_i) - 1
        
        while ((i_counter_0_i >= 0) and (self.i_content_of_json_0_i[i_counter_0_i] != "]")):
            
            i_counter_0_i -= 1
            
            
            
        
        self.i_content_of_json_0_i = self.i_content_of_json_0_i[:i_counter_0_i]
        
        
        i_v_0_i = (self.i_content_of_json_0_i).split("}")
        
        if (len(i_v_0_i) == 1):
            
            
            self.i_content_of_json_0_i += "\n    { \n"
            
        else:
            
            
            self.i_content_of_json_0_i += "\n     , \n"
            
            self.i_content_of_json_0_i += "\n    { \n"
            
            
            
        
        
        
        self.i_content_of_json_0_i += "\n" + f"        \"i_identificator_0_i\" : \"{i_identificator_0_i}\" , " + "\n"
        
        
        self.i_content_of_json_0_i += "\n" + f"        \"i_name_0_i\" : \"{i_name_0_i}\" , " + "\n"
        
        
        self.i_content_of_json_0_i += "\n" + f"        \"i_detail_0_i\" : \"{i_detail_0_i}\"  " + "\n"
        
        
        self.i_content_of_json_0_i += "\n    } \n"
        
            
        
        self.i_content_of_json_0_i += "\n\n]"
        
    
    
    
    def i_from_list_to_json_0_i(self, i_list_0_i):
        
        
        i_content_0_i = " { "
        
        
        if (len(i_list_0_i) > 0):
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(i_list_0_i) - 1):
                
                
                i_content_0_i += f"\\\"{i_list_0_i[i_counter_0_i][0]}\\\" : \\\"{i_list_0_i[i_counter_0_i][1]}\\\" , "
                
                
                i_counter_0_i += 1
                
            
            
            i_content_0_i += f"\\\"{i_list_0_i[i_counter_0_i][0]}\\\" : \\\"{i_list_0_i[i_counter_0_i][1]}\\\" "
            
        
        
        i_content_0_i += " } "
        
        
        return i_content_0_i



    def i_from_json_to_list_0_i(self, i_content_of_json_0_i):
        
        
        '''
        
        this should be respecting my format of json .
        
        '''
        
        
        i_list_of_result_0_i = []
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_content_of_json_0_i)):
            
            
            while ((i_counter_0_i < len(i_content_of_json_0_i) - 1)):
                
                
                
                if ((((i_content_of_json_0_i[i_counter_0_i - 1] != "\\") and (i_content_of_json_0_i[i_counter_0_i] == "\"")))):
                    
                    break
                    
                else:    
                    
                    
                    i_counter_0_i += 1
                    
                
            
            i_counter_0_i += 1
            
            
            
            i_content_0_i = ""
            
            
            
            while ((i_counter_0_i < len(i_content_of_json_0_i))):
                
                
                    
                if ((((i_content_of_json_0_i[i_counter_0_i - 1] != "\\") and (i_content_of_json_0_i[i_counter_0_i] == "\"")))):
                    
                    break
                    
                    
                else:
                
                    
                    i_content_0_i += i_content_of_json_0_i[i_counter_0_i]
                    
                    
                    i_counter_0_i += 1
                    
                
            
            i_counter_0_i += 1
            
            
            while ((i_counter_0_i < len(i_content_of_json_0_i))):
                
                
                    
                if ((((i_content_of_json_0_i[i_counter_0_i - 1] != "\\") and (i_content_of_json_0_i[i_counter_0_i] == "\"")))):
                    
                    break
                    
                else:
                    
                    i_counter_0_i += 1
                    
                
            
            
            
            i_counter_0_i += 1
            
            i_content_1_i = ""
            
            
            
            while ((i_counter_0_i < len(i_content_of_json_0_i))):
                
                
                if ((((i_content_of_json_0_i[i_counter_0_i - 1] != "\\") and (i_content_of_json_0_i[i_counter_0_i] == "\"")))):
                    
                    break
                    
                    
                else:
                
                    
                    i_content_1_i += i_content_of_json_0_i[i_counter_0_i]
                    
                    
                    i_counter_0_i += 1
                    
                
            
            
            i_list_of_result_0_i.append([i_content_0_i, i_content_1_i])
            
            
            
            i_counter_0_i += 1
            
            
            
            
        
        
        return i_list_of_result_0_i





def i_main_0_i():
    
    
    
    
    i_class_0_i = i_simulation_of_router_0_i()
    
    
    i_content_1_i = i_class_0_i.i_from_list_to_json_0_i(i_list_0_i=[["ip", "127.0.0.1"], ["port", "5000"]])
    
    
    i_class_0_i.i_create_router_0_i(i_identificator_0_i="0", i_name_0_i="i_router_0_i", i_detail_0_i=i_content_1_i)
    
    
    i_content_1_i = i_class_0_i.i_from_list_to_json_0_i(i_list_0_i=[["ip", "127.0.0.1"], ["port", "5001"]])
    
    i_class_0_i.i_create_router_0_i(i_identificator_0_i="1", i_name_0_i="i_router_1_i", i_detail_0_i=i_content_1_i)
    
    
    i_content_0_i = i_class_0_i.i_content_of_json_0_i
    
    
    print(f"i_content_0_i = {i_content_0_i} .")
    
    
    i_v_0_i = i_class_0_i.i_from_json_to_list_0_i(i_content_of_json_0_i=i_content_0_i)
    
    
    print(f"i_v_0_i = {i_v_0_i} .")
    
    
    
    print(f"_ = \"{i_v_0_i[2][1]}\" .")








if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    
    















