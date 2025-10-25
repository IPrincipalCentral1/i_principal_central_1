




















































































































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


class _____name_of_class_0_____(MovingCameraScene):
    
    
    def construct(self):
        # إعدادات عامة
        num_pendulums = 3
        gravity = 9.8
        length = 2.5
        dt = 0.05

        # قائمة إعدادات البندولات (يمكنك التحكم في كل بندول هنا)
        pendulum_settings = [
            {"color1": RED, "color2": BLUE, "angle": 0.6, "gravity": "down"},
            {"color1": GREEN, "color2": YELLOW, "angle": -0.4, "gravity": "up"},
            {"color1": PURPLE, "color2": ORANGE, "angle": 0.3, "gravity": "down"},
        ]

        # نقطة المركز (نقطة التأرجح المشتركة)
        origin = ORIGIN

        # قائمة تخزين بيانات كل بندول
        pendulums = []

        for i, settings in enumerate(pendulum_settings):
            # زاوية البداية
            angle = settings["angle"]
            # الموضع الأفقي لكل بندول حتى لا يتداخلوا
            x_offset = (i - len(pendulum_settings) / 2) * 3

            # نقطة المركز لكل بندول (نفس الارتفاع لكن على X مختلف)
            pivot = origin + RIGHT * x_offset

            # حساب موضع الطرف السفلي حسب الزاوية
            end_pos = pivot + length * np.array([np.sin(angle), -np.cos(angle), 0])

            # العمود الأول
            rod1 = Line(pivot, end_pos, stroke_width=6, color=settings["color1"])
            # العمود الثاني (ملتصق بالأول)
            rod2 = Line(pivot, end_pos + 0.2 * RIGHT, stroke_width=6, color=settings["color2"])

            # الكرة أسفل العمود الأول
            ball = Dot(end_pos, color=settings["color1"], radius=0.08)
            # الكرة الثانية أسفل العمود الثاني
            ball2 = Dot(end_pos + 0.2 * RIGHT, color=settings["color2"], radius=0.08)

            # تجميع الشكلين معاً
            group = VGroup(rod1, rod2, ball, ball2)
            self.add(group)

            pendulums.append({
                "pivot": pivot,
                "rod1": rod1,
                "rod2": rod2,
                "ball": ball,
                "ball2": ball2,
                "angle": angle,
                "angular_velocity": 0,
                "settings": settings,
            })

        
        
        # الكاميرا مسطحة (2D) - نقرب أو نبتعد
        #self.camera.scale(0.8)  # يمكنك تغيير القيمة (0.5 = تكبير، 2 = تصغير)

        
        
        self.camera.frame.set(width=12)
        self.camera.frame.set(height=7)
        
        

        # دالة التحديث الفيزيائي
        
        def update_pendulums(mob, dt):
            nonlocal angles1, vels1, angles2, vels2
            for i in range(num_pendulums):
                # فيزياء البندول الأول (عادية)
                acc1 = -gravity / length * math.sin(angles1[i])
                vels1[i] += acc1 * dt * 30
                angles1[i] += vels1[i] * dt * 30
        
                x1 = pivot_points[i][0] + length * math.sin(angles1[i])
                y1 = pivot_points[i][1] - length * math.cos(angles1[i])
                rods1[i].become(Line(pivot_points[i], [x1, y1, 0]))
                bobs1[i].move_to([x1, y1, 0])
        
                # فيزياء البندول الثاني (جاذبية معكوسة)
                acc2 = +gravity / length * math.sin(angles2[i])
                vels2[i] += acc2 * dt * 30
                angles2[i] += vels2[i] * dt * 30
        
                x2 = pivot_points[i][0] + length * math.sin(angles2[i])
                y2 = pivot_points[i][1] - length * math.cos(angles2[i])
                rods2[i].become(Line(pivot_points[i], [x2, y2, 0]))
                bobs2[i].move_to([x2, y2, 0])
        
        
        
        # تشغيل التحديث
        self.add_updater(update_pendulums)
        self.wait(20)
        self.remove_updater(update_pendulums)


if __name__ == "__main__":
    from manim import config
    config.pixel_height = 720
    config.pixel_width = 1280
    config.frame_height = 7.0
    config.frame_width = 7.0
    scene = PendulumScene()
    scene.render()







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
    
    
    
    



























