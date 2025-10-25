




















































































































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
        gravity = 9.8
        damping = 0.995

        # (لون1, زاوية1°, طول1, لون2, زاوية2°, طول2)
        pendulum_settings = [
            (RED, 30, 2.5, BLUE, -10, 1.5),
            (GREEN, -20, 2.0, YELLOW, 15, 1.2),
            (PURPLE, 45, 2.2, ORANGE, -5, 1.6),
        ]

        pendulum_pairs = VGroup()
        pendulum_states = []
        origin = ORIGIN

        for color1, angle1, L1, color2, angle2, L2 in pendulum_settings:
            # إنشاء قضبان وبندولات مبدئيًا
            rod1 = Line(origin, origin + L1 * DOWN, stroke_color=color1, stroke_width=6)
            bob1 = Dot(rod1.get_end(), radius=0.1, color=color1)

            rod2 = Line(bob1.get_center(), bob1.get_center() + L2 * DOWN, stroke_color=color2, stroke_width=5)
            bob2 = Dot(rod2.get_end(), radius=0.08, color=color2)

            pair = VGroup(rod1, bob1, rod2, bob2)
            pendulum_pairs.add(pair)

            pendulum_states.append({
                "theta1": np.radians(angle1),
                "theta2": np.radians(angle2),
                "omega1": 0.0,
                "omega2": 0.0,
                "L1": L1,
                "L2": L2,
            })

        self.add(pendulum_pairs)

        def update_double_pendulums(mob, dt):
            for i, pair in enumerate(mob):
                s = pendulum_states[i]
                θ1, θ2, ω1, ω2, L1, L2 = s["theta1"], s["theta2"], s["omega1"], s["omega2"], s["L1"], s["L2"]

                # معادلات البندول المزدوج الصحيحة (زاويتان مرتبطتان)
                δ = θ2 - θ1
                denom = (2 - np.cos(2 * δ))

                α1 = (-gravity * (2 * np.sin(θ1) + np.sin(θ1 - 2 * θ2))
                      - 2 * np.sin(δ) * (ω2**2 * L2 + ω1**2 * L1 * np.cos(δ))) / (L1 * denom)

                α2 = (2 * np.sin(δ) * (ω1**2 * L1 * (2)
                      + gravity * np.cos(θ1)
                      + ω2**2 * L2 * np.cos(δ))) / (L2 * denom)

                ω1 += α1 * dt
                ω2 += α2 * dt
                ω1 *= damping
                ω2 *= damping
                θ1 += ω1 * dt
                θ2 += ω2 * dt

                s.update({"theta1": θ1, "theta2": θ2, "omega1": ω1, "omega2": ω2})

                # المواضع
                p1 = origin + L1 * np.array([np.sin(θ1), -np.cos(θ1), 0])
                p2 = p1 + L2 * np.array([np.sin(θ2), -np.cos(θ2), 0])

                rod1, bob1, rod2, bob2 = pair
                rod1.put_start_and_end_on(origin, p1)
                bob1.move_to(p1)
                rod2.put_start_and_end_on(p1, p2)
                bob2.move_to(p2)

        pendulum_pairs.add_updater(update_double_pendulums)
        self.wait(20)













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
    
    
    
    



























