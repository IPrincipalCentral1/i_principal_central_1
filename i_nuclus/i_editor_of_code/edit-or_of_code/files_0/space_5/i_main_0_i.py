












































































































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
import matplotlib.animation as animation

# بيانات المحاور
x = np.linspace(0, 10, 500)

# منحنيات الانحدار
y1 = 10 - x                                 # مستقيم
y2 = 10 - np.sqrt(100 - (x - 10)**2)        # ربع دائرة
y3 = 10 - 0.5 * x**1.5                      # منحنى بينهما
y4 = 10 - 1.3 * np.sqrt(100 - (x - 10)**2)  # أعمق من الدائرة (أسفل)

# ضبط ارتفاع المنحنى الرابع
shift = (min(y4) - min(y2)) * 0.5
y4 -= shift

# إعداد الشكل
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(-6, 11)
ax.set_xlabel("المسافة الأفقية")
ax.set_ylabel("الارتفاع")
ax.set_title("محاكاة انحدار الكرات على منحنيات مختلفة")

# رسم المنحنيات
ax.plot(x, y1, 'r', label="منحنى 1 (مستقيم)")
ax.plot(x, y2, 'g', label="منحنى 2 (ربع دائرة)")
ax.plot(x, y3, 'b', label="منحنى 3 (انحناء متوسط)")
ax.plot(x, y4, 'm', label="منحنى 4 (أعمق)")
ax.legend()

# رسم الكرات
ball1, = ax.plot([], [], 'ro', markersize=10)
ball2, = ax.plot([], [], 'go', markersize=10)
ball3, = ax.plot([], [], 'bo', markersize=10)
ball4, = ax.plot([], [], 'mo', markersize=10)

def init():
    for ball in [ball1, ball2, ball3, ball4]:
        ball.set_data([], [])
    return ball1, ball2, ball3, ball4

frames = len(x)

def update(frame):
    # ملاحظة مهمة: يجب تمرير القيم على شكل قوائم
    ball1.set_data([x[frame]], [y1[frame]])
    ball2.set_data([x[frame]], [y2[frame]])
    ball3.set_data([x[frame]], [y3[frame]])
    ball4.set_data([x[frame]], [y4[frame]])
    return ball1, ball2, ball3, ball4

ani = animation.FuncAnimation(
    fig, update, frames=frames,
    init_func=init, interval=10, blit=True
)

plt.show()









