












































































































list_of_liberary_to_install = [
                            
                            
                            ["numpy"] ,
                            
                            
                            ["matplotlib"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess


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





import numpy as np

## 1) نسخة مُكبِّرة من ربع الدائرة (آمنة باستخدام clip لتجنّب القيم المعقدة)
#def deep_scaled_arc(x, depth=1.3):
    #"""أعمق من ربع الدائرة: يضرب قيمة الجذر بمعامل depth>1.
    #x: array-like أو scalar في [0,1]
    #"""
    #val = np.clip(1 - (1 - x)**2, 0.0, None)   # حماية من القيم السالبة صغيرة
    #return - depth * np.sqrt(val)



def deep_scaled_arc(x, depth=1.3):
    """
    منحنى أعمق من ربع الدائرة، مضبوط بحيث f(0)=0 و f(1)=-1 دائمًا.
    depth > 1 يجعل المنحنى أكثر انحناءً نحو الأسفل.
    """
    # نحسب الشكل الأساسي (ربع دائرة) بعمق إضافي
    val = np.clip(1 - (1 - x)**3, 0.0, None)
    y = - depth * np.sqrt(val)
    
    # نضبطه ليصبح f(1) = -1
    y /= abs(y[-1])  # الآن y[-1] = -1
    return y




# 2) منحنى بستطاعة (power) يعطي انحناءًا أعمق كلما زادت الأسّ
def deep_power(x, power=1.8):
    """منحنى أكثر انخفاضًا كلما كانت 'power' أكبر من 1."""
    x = np.asarray(x)
    return - x**power


# 3) منحنى سيكلويد (parametric) — يعطي انحدارًا طبيعيًا وعميقًا
def cycloid_path(num=200, a=1.0):
    """يرجع arrays (x, y) منحنى سايكلويد مناسب للمجال [0,1] أفقياً.
    a: مقياس العمق (يزيد القيمة المطلقة للانخفاض)
    """
    t = np.linspace(0, np.pi, num)               # 0..pi لتكوين قوس واحد
    x = (t - np.sin(t)) / np.pi                  # يطبع x في [0,1]
    y = - a * (1 - np.cos(t)) / 2                # y سالبة، مع مقياس a
    return x, y



# إعداد الزمن والثوابت الفيزيائية
dt = 0.02
t_max = 5
g = 9.81

# إعداد البيانات
x = np.linspace(0, 1, 200)

# تعريف المنحنيات
def curve_line(x):   return -x
def curve_arc(x):    return -np.sqrt(1 - (1 - x)**2)
def curve_mid(x):    return -x**1.5
def curve_deep(x):   return -x**2.2  # أكثر انحناءً للأسفل



def curve_arc_1(x):    return -np.sqrt(1 - (1 - x)**(1.293))


def curve_arc_2(x):    return ( ( ( x - 1 ) ** (2)) - 1 ) 

# قائمة الكرات والمنحنيات
list_of_balls = [
    ("blue", curve_line, "منحنى مستقيم"),
    ("green", curve_arc, "ربع دائرة"),
    ("orange", curve_mid, "منحنى متوسط"),
    ("red", curve_deep, "منحنى أكثر انحناءً"),
    
    ("#000000", curve_arc_1, "منحنى أكثر انحناءً 2"),
    
    ("#a0a0a0", curve_arc_2, "منحنى أكثر انحناءً 3"),
    
    
]

# حساب طول المسار تقريبياً
def path_length(x, y):
    dx, dy = np.diff(x), np.diff(y)
    return np.sum(np.sqrt(dx**2 + dy**2))

# حساب السرعة من الطاقة الميكانيكية
def speed(y):
    return np.sqrt(2 * g * (-y))

# الزمن التراكمي على المسار
def time_along_path(x, y):
    dx, dy = np.diff(x), np.diff(y)
    ds = np.sqrt(dx**2 + dy**2)
    v = speed((y[:-1] + y[1:]) / 2)
    t = np.cumsum(ds / v)
    return np.concatenate(([0], t))

# تجهيز بيانات كل كرة
balls_data = []
for color, curve_func, label in list_of_balls:
    y = curve_func(x)
    t = time_along_path(x, y)
    balls_data.append({
        "color": color,
        "x": x,
        "y": y,
        "t": t,
        "label": label,
        "t_final": t[-1]
    })

# الرسم
fig, ax = plt.subplots(figsize=(6, 4))
ax.set_xlim(0, 1.05)
ax.set_ylim(-1.1, 0.1)
ax.set_aspect('equal')
ax.set_title("محاكاة انحدار الكرات على منحنيات مختلفة", fontsize=12)
ax.set_xlabel("المسافة الأفقية")
ax.set_ylabel("الارتفاع")

# رسم المسارات والكرات
plots = []
texts = []

for ball in balls_data:
    ax.plot(ball["x"], ball["y"], '--', color=ball["color"], label=ball["label"])
    point, = ax.plot([], [], 'o', color=ball["color"], markersize=8)
    text = ax.text(0.5, 0.05 - 0.1 * len(texts), "", color=ball["color"], fontsize=9)
    plots.append(point)
    texts.append(text)

ax.legend()

# دالة إيجاد الموضع
def get_position(t_array, x_array, y_array, t):
    if t >= t_array[-1]:
        return x_array[-1], y_array[-1]
    i = np.searchsorted(t_array, t)
    return x_array[i], y_array[i]

# تحديث الإطار
def update(frame):
    t = frame * dt
    for i, ball in enumerate(balls_data):
        x_now, y_now = get_position(ball["t"], ball["x"], ball["y"], t)
        plots[i].set_data([x_now], [y_now])

        # تحديث النص بالزمن عند الوصول
        if t < ball["t_final"]:
            texts[i].set_text(f"{ball['label']}: t = {t} s")
        else:
            texts[i].set_text(f"{ball['label']}: t_final = {ball['t_final']} s ✅")

    return plots + texts

# تشغيل الأنميشن
ani = FuncAnimation(fig, update, frames=int(t_max / dt), interval=20, blit=True)
plt.show()


























