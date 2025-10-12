












































































































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
t_max = 60
steps = int(t_max / dt)

# المتغيرات
v = 0.0
x = 0.0

velocities = []
positions = []
times = []

for step in range(steps):
    # القوى
    F_air = 0.5 * Cd * rho * A * v**2
    F_friction = mu * m * g
    F_total = F_engine - F_air - F_friction

    # التسارع
    a = F_total / m

    # تحديث السرعة والموقع
    v += a * dt
    x += v * dt

    # تخزين النتائج
    times.append(step * dt)
    velocities.append(v)
    positions.append(x)

# الرسم
fig, ax1 = plt.subplots()
ax1.plot(times, velocities, label="السرعة (م/ث)", color='b')
ax1.set_xlabel("الزمن (ث)")
ax1.set_ylabel("السرعة", color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(times, positions, label="المسافة (م)", color='r')
ax2.set_ylabel("المسافة", color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title("محاكاة السيارة مع المقاومة الهوائية")
plt.show()












