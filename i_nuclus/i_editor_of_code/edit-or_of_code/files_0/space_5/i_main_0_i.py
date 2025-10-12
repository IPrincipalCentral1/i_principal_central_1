












































































































list_of_liberary_to_install = [
                            
                            
                            ["numpy"] ,
                            
                            
                            ["matplotlib"] ,
                            
                            



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








import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# المعاملات الفيزيائية
m = 1200         # كتلة السيارة بالكغ
Cd = 0.3         # معامل السحب الهوائي
A = 2.2          # مساحة المقطع الأمامي (م²)
rho = 1.225      # كثافة الهواء (كغ/م³)
mu = 0.015       # معامل احتكاك الإطارات
g = 9.81         # الجاذبية
F_engine = 4000  # قوة المحرك (نيوتن)

# الزمن
dt = 0.1
t_max = 30
steps = int(t_max / dt)

# المتغيرات
v = 0.0
x = 0.0

positions = [x]
velocities = [v]

# حساب تطور الحالة
for step in range(steps):
    F_air = 0.5 * Cd * rho * A * v**2
    F_friction = mu * m * g
    F_total = F_engine - F_air - F_friction
    a = F_total / m
    v += a * dt
    x += v * dt
    positions.append(x)
    velocities.append(v)

# إعداد الرسم
fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 200)
ax.set_ylim(-2, 2)
ax.set_title("🚗 محاكاة سيارة مع مقاومة هوائية", fontsize=14)
ax.set_xlabel("المسافة (متر)")
ax.set_ylabel("الطريق")

road_line, = ax.plot([0, 200], [0, 0], 'k', lw=2)
car_body, = ax.plot([], [], 'b', lw=6, solid_capstyle='round')
drag_arrow = ax.arrow(0, 0, 0, 0, color='red', head_width=0.3, head_length=2)

# لتحديث الأسهم بشكل ديناميكي
def make_arrow(x, v):
    length = 0.02 * v**2   # طول السهم متناسب مع مقاومة الهواء
    return ax.arrow(x, 0.3, -length, 0, color='red', head_width=0.3, head_length=1.5)

arrow_obj = None

def init():
    car_body.set_data([], [])
    return car_body,

def update(frame):
    global arrow_obj
    if arrow_obj:
        arrow_obj.remove()

    x = positions[frame] % 200  # ليتكرر المشهد
    v = velocities[frame]

    # السيارة
    car_body.set_data([x - 1, x + 1], [0.2, 0.2])

    # السهم الأحمر (الهواء)
    arrow_obj = make_arrow(x + 1, v)

    return car_body, arrow_obj

ani = FuncAnimation(fig, update, frames=steps, init_func=init, interval=50, blit=True)
plt.show()










