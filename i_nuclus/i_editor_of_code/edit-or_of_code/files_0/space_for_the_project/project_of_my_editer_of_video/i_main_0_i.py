




















































































































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
import numpy as np

class _____name_of_class_0_____(Scene):
    
    
    def construct(self):
        center = ORIGIN
        
        
        # إعدادات الأعمدة المتأرجحة:
        
        # كل عنصر يمثل بندولاً واحداً بالشكل التالي:
        
        # (اللون, زاوية البداية بالدرجات, طول العمود)
        
        # يمكنك إضافة أو تعديل القيم لتغيير عدد الأعمدة، ألوانها، أو نقاط بدايتها.
        
        
        
        pendulum_settings = [
            (RED, 20, 2.5),
            (GREEN, -25, 2.5),
            (BLUE, 15, 2.5),
            (YELLOW, -10, 2.5),
        ]

        g = 9.81

        rods = []
        bobs = []
        states = []

        for color, start_deg, length in pendulum_settings:
            theta = np.deg2rad(start_deg)
            omega = 0
            states.append([theta, omega, length])

            end = center + length * np.array([np.sin(theta), -np.cos(theta), 0])
            rod = Line(center, end, color=color, stroke_width=5)
            bob = Dot(end, radius=0.1, color=color)
            self.add(rod, bob)
            rods.append(rod)
            bobs.append(bob)

        def update_pendulums(mob, dt):
            for i, (theta, omega, length) in enumerate(states):
                alpha = -(g / length) * np.sin(theta)
                omega += alpha * dt
                theta += omega * dt
                states[i][0] = theta
                states[i][1] = omega

                end = center + length * np.array([np.sin(theta), -np.cos(theta), 0])
                rods[i].put_start_and_end_on(center, end)
                bobs[i].move_to(end)

        pendulum_group = VGroup(*rods, *bobs)
        pendulum_group.add_updater(update_pendulums)
        self.add(pendulum_group)

        # لا حاجة لضبط الكاميرا في 2D
        self.wait(150)







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
    
    
    
    



























