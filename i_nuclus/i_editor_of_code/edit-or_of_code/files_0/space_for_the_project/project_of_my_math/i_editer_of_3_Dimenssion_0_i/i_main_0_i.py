



















































































































































































































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




print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


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
















import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------------------------
# إعداد المتغيرات الفيزيائية
# ---------------------------

g = 9.81              # تسارع الجاذبية (م/ث²)
rho = 1000            # كثافة السائل (كغ/م³)
A_small = 0.01        # مساحة المكبس الصغير (م²)
A_big = 2 * A_small   # مساحة المكبس الكبير (م²)
m_small = 1.0         # كتلة المكبس الصغير (كغ)
m_big = 1.0           # كتلة المكبس الكبير (كغ)
k_damp = 0.8          # معامل التخميد (احتكاك)
dt = 0.02             # خطوة الزمن (ثانية)

# مواضع المكبسين (y_small, y_big)
y_small = 0.0
y_big = 0.0
v_small = 0.0
v_big = 0.0

# ---------------------------
# دالة التحديث الفيزيائي
# ---------------------------

def update_physics():
    global y_small, y_big, v_small, v_big

    # علاقة الحجم الثابت: A_small*y_small + A_big*y_big = 0
    v_big = -(A_small / A_big) * v_small

    # فرق الارتفاع يولد فرق ضغط
    delta_h = y_small - y_big

    # القوى (تشمل الوزن + فرق الضغط + التخميد)
    F_small = -m_small * g - rho * g * delta_h - k_damp * v_small
    F_big   = -m_big * g + rho * g * delta_h - k_damp * v_big

    # التسارعات
    a_small = F_small / m_small
    a_big   = F_big / m_big

    # تحديث السرعة والموضع
    v_small += a_small * dt
    v_big   += a_big * dt
    y_small += v_small * dt
    y_big   += v_big * dt


# ---------------------------
# إعداد الرسم
# ---------------------------

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect("equal")
ax.set_title("Hydraulic Oscillation Simulation (U-Tube)")

# قلب المحور العمودي لجعل U طبيعي
ax.invert_yaxis()

# رسم الأنبوب على شكل U
tube_x = [-1, -1, 1, 1]
tube_y = [2, -1, -1, 2]
ax.plot(tube_x, tube_y, 'k', linewidth=3)

# المكبسان
piston_small, = ax.plot([], [], 'ro', markersize=20, label="Small piston")
piston_big, = ax.plot([], [], 'bo', markersize=30, label="Big piston")

ax.legend()

# ---------------------------
# دالة التحديث للرسم
# ---------------------------

def animate(frame):
    update_physics()
    piston_small.set_data([-1], [y_small])
    piston_big.set_data([1], [y_big])
    return piston_small, piston_big

# ---------------------------
# تشغيل المحاكاة
# ---------------------------

ani = FuncAnimation(fig, animate, frames=1000, interval=20, blit=True)
plt.show()














