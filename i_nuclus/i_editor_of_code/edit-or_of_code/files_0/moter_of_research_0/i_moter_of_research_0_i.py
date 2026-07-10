































































































































'''













'''





import os

import sys

import traceback

import subprocess






cwd = os.path.dirname(os.path.abspath(__file__))



path_0 = os.path.dirname(cwd)


sys.path.append(path_0)









list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            



]











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










try:
    
    
    
    
    class i_class_of_moter_of_research_0_i():
        
        def __init__(self):
            
            pass
            
            
            
            
        
        
    
    
    def i_main_0_i():
        
        
        i_v_0_i = i_class_of_moter_of_research_0_i()
        
        
        
        
        
    
    
    
    
    if __name__ == "__main__":
        
        
        i_main_0_i()
        
        
        
        
        





except:
    
    
    
    
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    



















