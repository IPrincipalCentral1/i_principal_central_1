




















































































































list_of_liberary_to_install = [
                            
                            
                            ["pillow"] ,
                            
                            
                            ["manim"] ,
                            
                            
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
            
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
            
            
            
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






global i_content_0_i



i_content_0_i = r"""











list_of_liberary_to_install = [
                            
                            
                            ["pillow"] ,
                            
                            
                            ["manim"] ,
                            
                            
                            ["PyOpenGL_accelerate"] ,
                            
                            
                            ["PyOpenGL"] ,
                            
                            
                            ["pygame"] ,
                            
                            
                            
                            
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
            
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
            
            
            
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






i_folder_0_i = os.path.join(cwd, "i_space_for_library_0_i")


sys.path.append(i_folder_0_i)



import i_main_of_library_0_i











'''

the part of the code .


'''







print(f"\n\n    rm -rf media \n\n")


os.system(f"rm -rf media")





from manim import *

class i_program_0_i(ThreeDScene):
    def construct(self):
        # إعداد الكاميرا
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # إنشاء المكعب
        cube = Cube(color=YELLOW, fill_opacity=0.3)
        self.add(cube)

        # قائمة النقاط التي ستمر منها الكاميرا
        list_of_points = [
            [0, 0, 4],
            [2, 1, 3],
            [1, 3, 2],
            [-1, 2, 4],
            [0, 0, 6],
        ]

        # تحريك الكاميرا بين النقاط
        for point in list_of_points:
            self.move_camera(
                phi=70 * DEGREES,
                theta=45 * DEGREES,
                frame_center=point,
                run_time=2,
            )
        
        self.wait(1)





"""





def i_main_0_i():
    
    
    
    global i_content_0_i
    
    
    
    i_name_of_project_0_i = "i_program_0_i"
    
    
    i_content_0_i = i_content_0_i.replace("_____name_of_class_0_____", i_name_of_project_0_i)
    
    
    
    
    i_name_of_file_0_i = "i_main_0_0_i.py"
    
    i_file_0_i = os.path.join(cwd, i_name_of_file_0_i)
    
    with open(i_file_0_i, "w") as f_:
        
        f_.write(i_content_0_i)
        
    
    
    os.system(f"{sys.executable} -m manim -pql {i_name_of_file_0_i} {i_name_of_project_0_i}")
    
    
    #os.system(f"{sys.executable} -m manim -pql {i_name_of_file_0_i} {i_name_of_project_0_i} --show_in_file_browser")
    
    
    
    
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    
    
    



























