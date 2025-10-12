












































































































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

# إعداد المنحنيات
x = np.linspace(0, 10, 500)
y1 = 10 - x                # منحنى 1: مستقيم
y2 = 10 - np.sqrt(100 - (x - 10)**2)  # منحنى 2: ربع دائرة
y3 = 10 - 0.5*x**1.5       # منحنى 3: انحناء متوسط
y4 = 10 - 0.8*x**1.7       # منحنى 4: أكثر انحناءً إلى الأسفل

# إعداد الشكل
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 11)
ax.set_xlabel("المسافة الأفقية")
ax.set_ylabel("الارتفاع")
ax.set_title("محاكاة انحدار كرات على منحنيات مختلفة")

# رسم المنحنيات
ax.plot(x, y1, label="منحنى 1 (مستقيم)")
ax.plot(x, y2, label="منحنى 2 (ربع دائرة)")
ax.plot(x, y3, label="منحنى 3 (انحناء متوسط)")
ax.plot(x, y4, label="منحنى 4 (أكثر انحناء)")
ax.legend()

# مواضع البداية للكرات
ball1, = ax.plot([], [], 'ro', markersize=10)
ball2, = ax.plot([], [], 'go', markersize=10)
ball3, = ax.plot([], [], 'bo', markersize=10)
ball4, = ax.plot([], [], 'mo', markersize=10)

# تهيئة البيانات
def init():
    ball1.set_data([], [])
    ball2.set_data([], [])
    ball3.set_data([], [])
    ball4.set_data([], [])
    return ball1, ball2, ball3, ball4

# عدد الإطارات
frames = len(x)

# دالة التحديث
def update(frame):
    ball1.set_data(x[frame], y1[frame])
    ball2.set_data(x[frame], y2[frame])
    ball3.set_data(x[frame], y3[frame])
    ball4.set_data(x[frame], y4[frame])
    return ball1, ball2, ball3, ball4

# إنشاء الرسوم المتحركة
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init,
                              interval=10, blit=True)

plt.show()










