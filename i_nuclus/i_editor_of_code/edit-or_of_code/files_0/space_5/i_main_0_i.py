












































































































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

# إعداد الزمن
dt = 0.02
t_max = 5
g = 9.81

# المنحنيات
x = np.linspace(0, 1, 200)
y_line = -x             # خط مستقيم
y_arc = -np.sqrt(1 - (1 - x)**2)  # ربع دائرة
y_curve = -x**1.5       # منحنى بينهما

# حساب الطول التقريبي لكل مسار
def path_length(x, y):
    dx = np.diff(x)
    dy = np.diff(y)
    return np.sum(np.sqrt(dx**2 + dy**2))

L_line = path_length(x, y_line)
L_arc = path_length(x, y_arc)
L_curve = path_length(x, y_curve)

# السرعة لكل نقطة (من الطاقة الميكانيكية)
def speed(y):
    return np.sqrt(2 * g * (-y))  # لأن y سالبة

# دالة لحساب الزمن التراكمي لكل نقطة
def time_along_path(x, y):
    dx = np.diff(x)
    dy = np.diff(y)
    ds = np.sqrt(dx**2 + dy**2)
    v = speed((y[:-1] + y[1:]) / 2)
    t = np.cumsum(ds / v)
    return np.concatenate(([0], t))

t_line = time_along_path(x, y_line)
t_arc = time_along_path(x, y_arc)
t_curve = time_along_path(x, y_curve)

# إنشاء الرسم
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 1.05)
ax.set_ylim(-1.05, 0.1)
ax.set_aspect('equal')
ax.set_title("محاكاة انحدار 3 كرات على منحنيات مختلفة", fontsize=12)
ax.set_xlabel("المسافة الأفقية")
ax.set_ylabel("الارتفاع")

# رسم المسارات
ax.plot(x, y_line, 'b--', label="منحنى مستقيم")
ax.plot(x, y_arc, 'g--', label="ربع دائرة")
ax.plot(x, y_curve, 'orange', linestyle='--', label="منحنى متوسط")

# رسم الكرات
ball_line, = ax.plot([], [], 'bo', markersize=8)
ball_arc, = ax.plot([], [], 'go', markersize=8)
ball_curve, = ax.plot([], [], 'orange', marker='o', markersize=8)

ax.legend()

# دالة لإيجاد الموضع عند زمن معين
def get_position(t_array, x_array, y_array, t):
    if t >= t_array[-1]:
        return x_array[-1], y_array[-1]
    i = np.searchsorted(t_array, t)
    return x_array[i], y_array[i]

# تحديث الحركة
def update(frame):
    t = frame * dt
    x1, y1 = get_position(t_line, x, y_line, t)
    x2, y2 = get_position(t_arc, x, y_arc, t)
    x3, y3 = get_position(t_curve, x, y_curve, t)

    ball_line.set_data(x1, y1)
    ball_arc.set_data(x2, y2)
    ball_curve.set_data(x3, y3)

    return ball_line, ball_arc, ball_curve

ani = FuncAnimation(fig, update, frames=int(t_max / dt), interval=20, blit=True)
plt.show()










