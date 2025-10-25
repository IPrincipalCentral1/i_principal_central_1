




















































































































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

class _____name_of_class_0_____(ThreeDScene):
    def construct(self):
        
        
        # إعداد الكاميرا
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        
        # عدد الأعمدة
        num_pendulums = 5
        
        # طول العمود
        
        length = 2

        # نقاط البداية لكل عمود (يمكنك تعديل المسافات بين الأعمدة)
        start_points = [np.array([i - num_pendulums/2, 2, 0]) for i in range(num_pendulums)]

        pendulums = []
        rods = []
        bobs = []

        for start in start_points:
            # زاوية البداية (تحديد مقدار الميل)
            angle = 30 * DEGREES

            # نقطة النهاية (الكرة)
            end = start + length * np.array([np.sin(angle), -np.cos(angle), 0])

            # إنشاء العمود (rod)
            rod = Line(start, end, color=YELLOW)
            # إنشاء الكرة (bob)
            bob = Dot(end, radius=0.1, color=RED)

            pendulums.append(VGroup(rod, bob))
            rods.append(rod)
            bobs.append(bob)

            self.add(rod, bob)

        # مدة التأرجح
        swing_time = 4
        swing_angle = 30 * DEGREES

        # حركة التأرجح لكل عمود
        def update_pendulum(mob, dt):
            t = self.time
            for i in range(num_pendulums):
                angle = swing_angle * np.sin(t * 2)
                start = start_points[i]
                end = start + length * np.array([np.sin(angle), -np.cos(angle), 0])
                rods[i].put_start_and_end_on(start, end)
                bobs[i].move_to(end)

        pendulum_group = VGroup(*pendulums)
        pendulum_group.add_updater(update_pendulum)

        self.add(pendulum_group)

        # تشغيل التأرجح لمدة معينة
        self.wait(10)





















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
    
    
    
    



























