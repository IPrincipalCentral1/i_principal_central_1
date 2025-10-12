












































































































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

# ثوابت فيزيائية
rho = 1.225       # كثافة الهواء (كغ/م³)
Cd = 0.3          # معامل السحب الهوائي
A = 2.2           # مساحة واجهة السيارة (م²)
m = 1200          # كتلة السيارة (كغ)
F_engine = 4000   # قوة المحرك (نيوتن)
dt = 0.1          # خطوة الزمن (ث)
t_max = 60        # مدة المحاكاة (ث)

# متغيرات أولية
v = 0.0           # السرعة الابتدائية
x = 0.0           # المسافة المقطوعة
times, speeds, forces = [], [], []

# المحاكاة الزمنية
for t in np.arange(0, t_max, dt):
    F_drag = 0.5 * rho * Cd * A * v**2
    F_net = F_engine - F_drag
    a = F_net / m
    v += a * dt
    x += v * dt

    times.append(t)
    speeds.append(v)
    forces.append(F_drag)

# رسم النتائج
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(times, speeds, label='السرعة')
plt.xlabel('الزمن (ثانية)')
plt.ylabel('السرعة (م/ث)')
plt.title('تغير السرعة مع مقاومة الهواء')
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.plot(times, forces, 'r', label='قوة السحب الهوائي')
plt.xlabel('الزمن (ثانية)')
plt.ylabel('القوة (نيوتن)')
plt.title('تزايد مقاومة الهواء مع السرعة')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()














