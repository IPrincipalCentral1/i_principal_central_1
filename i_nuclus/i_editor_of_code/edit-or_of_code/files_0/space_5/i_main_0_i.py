












































































































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

# إعداد القيم الفيزيائية
n = 5  # عدد الرقاصات
theta = np.random.uniform(-0.5, 0.5, n)  # الزوايا الأولية
omega = np.zeros(n)  # السرعات الزاوية
L = 1.0  # طول الخيط
g = 9.81  # الجاذبية
coupling = 0.05  # مقدار التأثير بين الرقاصات
dt = 0.05  # خطوة الزمن

# إعداد الرسم
fig, ax = plt.subplots()
ax.set_xlim(-n, n)
ax.set_ylim(-1.5, 0.2)
lines = []
for i in range(n):
    line, = ax.plot([], [], lw=2)
    lines.append(line)

# دالة التحديث لكل إطار
def update(frame):
    global theta, omega
    # معادلات الحركة البسيطة مع تأثير التناغم
    avg = np.mean(theta)
    torque = - (g / L) * np.sin(theta) + coupling * (avg - theta)
    omega += torque * dt
    theta += omega * dt

    for i in range(n):
        x = i - n/2
        line_x = [x, x + L * np.sin(theta[i])]
        line_y = [0, -L * np.cos(theta[i])]
        lines[i].set_data(line_x, line_y)
    return lines

ani = FuncAnimation(fig, update, frames=400, interval=30, blit=True)
plt.show()






























