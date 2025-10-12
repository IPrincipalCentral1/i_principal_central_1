












































































































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

# عدد الرقاصات
n = 2

# الزوايا الأولية
theta = np.array([0.4, -0.3])   # زاويتان مختلفتان قليلاً
omega = np.zeros(n)

# الثوابت الفيزيائية
L = 1.0          # طول الخيط
g = 9.81         # الجاذبية
coupling = 0.3   # شدة الترابط بين الرقاصين
damping = 0.02   # الاحتكاك (يُخمد التذبذب الزائد)
dt = 0.05        # خطوة الزمن

# اللوح
x_plate = 0.0
v_plate = 0.0
mass_plate = 5.0   # كتلة اللوح
k_plate = 0.2      # مرونة اللوح (لمنع الانزياح المستمر)

# إعداد الرسم
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1.6, 0.4)
ax.set_aspect('equal')
ax.set_title("تناغم رقّاصين على لوح واحد (تجربة هوغنس)", fontsize=14)
ax.set_xlabel("الموضع الأفقي")
ax.set_ylabel("الارتفاع")

# رسم اللوح والرقّاصين
plate_line, = ax.plot([], [], 'k-', lw=4)  # اللوح
lines = [ax.plot([], [], lw=2)[0] for _ in range(n)]

# دالة التحديث
def update(frame):
    global theta, omega, x_plate, v_plate

    # متوسط الزاوية (تأثير مشترك)
    avg = np.mean(theta)

    # عزم الدوران على كل رقّاص
    torque = - (g / L) * np.sin(theta) + coupling * (avg - theta) - damping * omega
    omega += torque * dt
    theta += omega * dt

    # القوة الناتجة عن الرقّاصين + مرونة اللوح
    force_from_pendulums = np.sum(np.sin(theta)) * 0.02
    restoring_force = -k_plate * x_plate
    total_force = -force_from_pendulums + restoring_force

    v_plate += total_force / mass_plate
    x_plate += v_plate * dt

    # تحديث الرسم
    plate_line.set_data([-1, 1], [0, 0])  # اللوح

    for i in range(n):
        x0 = (i * 1.0) - 0.5 + x_plate
        x1 = x0 + L * np.sin(theta[i])
        y1 = -L * np.cos(theta[i])
        lines[i].set_data([x0, x1], [0, y1])

    return lines + [plate_line]

ani = FuncAnimation(fig, update, frames=400, interval=30, blit=True)
plt.show()




















