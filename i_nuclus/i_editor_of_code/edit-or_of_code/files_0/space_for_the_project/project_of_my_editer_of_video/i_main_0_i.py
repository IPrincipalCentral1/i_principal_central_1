




















































































































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

        # الكاميرا مسطحة (2D)
        
        self.camera.set_frame_height(7)
        
        self.camera.set_frame_width(12)
        

        # دالة التحديث الفيزيائي
        def update_pendulums(mob, dt):
            for p in pendulums:
                settings = p["settings"]

                # اختيار اتجاه الجاذبية (للأعلى أو للأسفل)
                g = gravity if settings["gravity"] == "down" else -gravity

                # قوانين الحركة الفيزيائية
                angle = p["angle"]
                angular_velocity = p["angular_velocity"]

                angular_acceleration = -(g / length) * np.sin(angle)
                angular_velocity += angular_acceleration * dt
                angle += angular_velocity * dt

                # تحديث القيم
                p["angle"] = angle
                p["angular_velocity"] = angular_velocity

                # إعادة حساب مواضع الأعمدة والكرات
                pivot = p["pivot"]
                end_pos = pivot + length * np.array([np.sin(angle), -np.cos(angle), 0])

                p["rod1"].put_start_and_end_on(pivot, end_pos)
                p["rod2"].put_start_and_end_on(pivot, end_pos + 0.2 * RIGHT)
                p["ball"].move_to(end_pos)
                p["ball2"].move_to(end_pos + 0.2 * RIGHT)

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
    
    
    
    



























