





















































































































list_of_liberary_to_install = [
                            
                            
                            ["sympy"] ,
                            
                            
                            



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















from sympy import symbols, simplify, expand


x = symbols('x')

#expr = (x**2 + 2*x + 1) / (x + 1)

expr = (x**2 + 2*x + 1) / x ** 10


simplified = simplify(expr)

print(f"simplified = {simplified} .")



print("\n" * 10)





expr = (x + 1)**3

expanded = expand(expr)

print(f"expanded = {expanded} .")

















