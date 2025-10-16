



















































































































































































































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

# حجم الشبكة
N = 200
x = np.linspace(-1, 1, N)
X, Y = np.meshgrid(x, x)

# تضاريس جبلية (قمة في المركز)
terrain = np.exp(-4 * (X**2 + Y**2))

# طبقة ثلج ابتدائية
snow = 0.6 * np.exp(-8 * (X**2 + Y**2))

# مصدر صوتي في مكان محدد
sound_center = (0.3, -0.4)

# إعداد الشكل
fig, ax = plt.subplots(figsize=(6, 5))
img = ax.imshow(terrain + snow, cmap='Blues', origin='lower', vmin=0, vmax=1.2)
ax.set_title("محاكاة انجراف الثلوج بتأثير الصوت")

# دالة حساب تأثير الموجة الصوتية
def sound_wave(t):
    dist = np.sqrt((X - sound_center[0])**2 + (Y - sound_center[1])**2)
    wave = np.exp(-((dist - 0.2*t)**2) / 0.005)  # موجة دائرية تنتشر
    return wave

def update(frame):
    global snow
    # نحسب الموجة الصوتية في هذا الإطار
    wave = sound_wave(frame * 0.1)

    # التأثير: الموجة تقلل ثبات الثلج => ينزلق باتجاه الأسفل
    slope_x, slope_y = np.gradient(terrain)
    flow = -0.1 * (slope_x + slope_y) * wave

    snow += flow  # تعديل الثلج
    snow = np.clip(snow, 0, 1.0)  # لا تسمح بقيم سالبة أو كبيرة جدًا

    # تحديث الصورة
    img.set_data(terrain + snow + 0.2 * wave)
    return [img]

ani = FuncAnimation(fig, update, frames=200, interval=60, blit=True)
plt.show()



























