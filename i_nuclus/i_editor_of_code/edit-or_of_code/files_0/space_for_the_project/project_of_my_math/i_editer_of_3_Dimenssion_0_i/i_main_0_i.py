



















































































































































































































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
import numpy as np

# مكعب بحجم 2x2x2
cube = o3d.geometry.TriangleMesh.create_box(width=2.0, height=2.0, depth=2.0)

# تحريك المكعب قليلاً حتى لا يكون متمركزًا عند الأصل
cube.translate([-1, -1, -1])

# تلوين كل رأس بلون مختلف (تدرج RGB)
colors = np.array([
    [1, 0, 0], [0, 1, 0], [0, 0, 1],
    [1, 1, 0], [0, 1, 1], [1, 0, 1],
    [0.5, 0.5, 0.5], [1, 0.5, 0]
])
cube.vertex_colors = o3d.utility.Vector3dVector(colors)

# حساب النورمالز
cube.compute_vertex_normals()

# العرض
o3d.visualization.draw_geometries([cube])






























