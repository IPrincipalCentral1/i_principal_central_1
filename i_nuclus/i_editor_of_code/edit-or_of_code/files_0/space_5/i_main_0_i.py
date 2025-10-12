












































































































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

# تعريف المحاور
x = np.linspace(0, 1, 200)

# تعريف المنحنيات (تُخزن في قاموس لتسهيل الوصول إليها)
curves = {
    "line": -x,                                  # خط مستقيم
    "arc": -np.sqrt(1 - (1 - x)**2),             # ربع دائرة
    "curve": -x**1.5,                            # منحنى متوسط
    "deep": -1.3 * np.sqrt(1 - (1 - x)**2)       # منحنى أعمق (إضافي)
}

# حساب السرعة والطول
def speed(y):
    return np.sqrt(2 * g * (-y))  # لأن y سالبة

def time_along_path(x, y):
    dx = np.diff(x)
    dy = np.diff(y)
    ds = np.sqrt(dx**2 + dy**2)
    v = speed((y[:-1] + y[1:]) / 2)
    t = np.cumsum(ds / v)
    return np.concatenate(([0], t))

# نحسب الزمن لكل منحنى مسبقًا
time_data = {name: time_along_path(x, y) for name, y in curves.items()}

# قائمة الكرات: [اللون, اسم_المنحنى]
list_of_ball = [
    ['b', 'line'],
    ['g', 'arc'],
    ['orange', 'curve'],
    ['m', 'deep']   # كرة إضافية لمنحنى أعمق
]

# إنشاء الرسم
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 1.05)
ax.set_ylim(-1.3, 0.1)
ax.set_aspect('equal')
ax.set_title("محاكاة انحدار كرات متعددة على منحنيات مختلفة", fontsize=12)
ax.set_xlabel("المسافة الأفقية")
ax.set_ylabel("الارتفاع")

# رسم المنحنيات
for name, y in curves.items():
    ax.plot(x, y, '--', label=f"منحنى {name}")

ax.legend()

# إنشاء الكرات من القائمة
balls = []
for color, curve_name in list_of_ball:
    ball, = ax.plot([], [], color=color, marker='o', markersize=8)
    balls.append((ball, curve_name))

# دالة لإيجاد الموضع عند زمن معين
def get_position(t_array, x_array, y_array, t):
    if t >= t_array[-1]:
        return x_array[-1], y_array[-1]
    i = np.searchsorted(t_array, t)
    return x_array[i], y_array[i]

# تهيئة البداية
def init():
    for ball, _ in balls:
        ball.set_data([], [])
    return [b for b, _ in balls]

# تحديث الإطار
def update(frame):
    t = frame * dt
    for ball, curve_name in balls:
        y = curves[curve_name]
        t_arr = time_data[curve_name]
        x_pos, y_pos = get_position(t_arr, x, y, t)
        ball.set_data([x_pos], [y_pos])
    return [b for b, _ in balls]

# تشغيل الأنيميشن
ani = FuncAnimation(fig, update, frames=int(t_max / dt),
                    init_func=init, interval=20, blit=True)

plt.show()






