




















































































































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
        
        
        gravity = 9.8  # تسارع الجاذبية
        dt = 0.03      # خطوة الزمن
        damping = 0.995  # تخميد خفيف
        
        # (لون1, زاوية1°, طول1, لون2, زاوية2°, طول2)
        pendulum_settings = [
            (RED, 25, 2.5, BLUE, -10, 1.5),
            (GREEN, -30, 2.0, YELLOW, 20, 1.2),
        ]

        pendulum_pairs = VGroup()
        pendulum_states = []

        for color1, angle1, length1, color2, angle2, length2 in pendulum_settings:
            # الذراع الأول
            rod1 = Line(ORIGIN, length1 * DOWN, stroke_color=color1, stroke_width=6)
            bob1 = Dot(rod1.get_end(), radius=0.1, color=color1)

            # الذراع الثاني (مرتبط بنهاية الأول)
            rod2 = Line(bob1.get_center(), bob1.get_center() + length2 * DOWN, stroke_color=color2, stroke_width=5)
            bob2 = Dot(rod2.get_end(), radius=0.08, color=color2)

            pair = VGroup(rod1, bob1, rod2, bob2)
            pair.move_to(ORIGIN)
            pendulum_pairs.add(pair)

            pendulum_states.append({
                "theta1": np.radians(angle1),
                "theta2": np.radians(angle2),
                "omega1": 0.0,
                "omega2": 0.0,
                "L1": length1,
                "L2": length2,
            })

        self.add(pendulum_pairs)

        def update_double_pendulums(mob, dt_):
            for i, pair in enumerate(mob):
                state = pendulum_states[i]

                # تحديث المعادلات (تقريب مبسّط للبندول المزدوج)
                theta1, theta2 = state["theta1"], state["theta2"]
                omega1, omega2 = state["omega1"], state["omega2"]
                L1, L2 = state["L1"], state["L2"]

                delta = theta2 - theta1

                num1 = -gravity * (2 * np.sin(theta1) + np.sin(theta1 - 2 * theta2))
                num2 = -2 * np.sin(delta) * (omega2**2 * L2 + omega1**2 * L1 * np.cos(delta))
                denom = L1 * (2 - np.cos(2 * delta))
                alpha1 = (num1 + num2) / denom

                num3 = 2 * np.sin(delta) * (omega1**2 * L1 * (2) + gravity * (2) * np.cos(theta1) + omega2**2 * L2 * np.cos(delta))
                denom2 = L2 * (2 - np.cos(2 * delta))
                alpha2 = num3 / denom2

                # تكامل عددي بسيط
                omega1 += alpha1 * dt
                omega2 += alpha2 * dt
                omega1 *= damping
                omega2 *= damping
                theta1 += omega1 * dt
                theta2 += omega2 * dt

                # حفظ القيم الجديدة
                state.update({"theta1": theta1, "theta2": theta2, "omega1": omega1, "omega2": omega2})

                # تحديث الرسم
                origin = ORIGIN
                p1 = origin + L1 * np.array([np.sin(theta1), -np.cos(theta1), 0])
                p2 = p1 + L2 * np.array([np.sin(theta2), -np.cos(theta2), 0])

                rod1, bob1, rod2, bob2 = pair

                rod1.put_start_and_end_on(origin, p1)
                bob1.move_to(p1)
                rod2.put_start_and_end_on(p1, p2)
                bob2.move_to(p2)

        pendulum_pairs.add_updater(update_double_pendulums)
        self.wait(15)








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
    
    
    
    



























