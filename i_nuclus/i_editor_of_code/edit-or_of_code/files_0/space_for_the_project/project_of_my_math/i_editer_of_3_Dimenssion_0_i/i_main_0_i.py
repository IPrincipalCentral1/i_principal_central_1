



















































































































































































































list_of_liberary_to_install = [
                            
                            
                            ["numpy"] ,
                            
                            
                            ["matplotlib"] ,
                            
                            
                            ["vpython"] ,
                            
                            
                            ["open3d"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess




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






import open3d as o3d

# إنشاء مكعب بطول ضلع = 1
cube = o3d.geometry.TriangleMesh.create_box(width=1.0, height=1.0, depth=1.0)

# حساب النورمالز لتظهر الإضاءة والسطوع بشكل صحيح
cube.compute_vertex_normals()

# تغيير اللون إلى أزرق مثلاً
cube.paint_uniform_color([0.1, 0.1, 0.9])

# عرض المكعب في نافذة ثلاثية الأبعاد
o3d.visualization.draw_geometries([cube])
































