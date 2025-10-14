



















































































































































































































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

# ---------- إعداد المعاملات ----------
N = 150                # حجم الشبكة (N x N)
steps = 800            # عدد خطوات المحاكاة (أو اجعلها لانهائية في الأنيميشن)
flow_coeff = 0.2       # عامل سرعة النقل للثلج (كلما أكبر --> يتدفق أسرع)
friction = 0.03        # فقدان أثناء النقل (احتكاك/تبخّر)
min_snow_to_move = 0.0005  # عتبة لبدء الحركة
dt = 1.0               # خطوة زمنية (تؤثر على الثبات)

# ---------- إنشاء تضاريس جبلية بسيطة ----------
x = np.linspace(-1, 1, N)
X, Y = np.meshgrid(x, x)
# جبل مركزي: عدة قمم خفيفة لزيادة التعقيد
terrain = (
    0.9 * np.exp(-5 * (X**2 + Y**2)) +
    0.35 * np.exp(-30 * ((X-0.4)**2 + (Y+0.25)**2)) +
    0.25 * np.exp(-20 * ((X+0.35)**2 + (Y-0.35)**2))
)
# أضف بعض خَشونة صغيرة
terrain += 0.02 * np.random.randn(N, N)

# ---------- وضع ثلوج ابتدائي (مثلاً تساقط في القمة) ----------
snow = np.zeros_like(terrain)
# مثال: ضع ثلج مركزياً
snow += 0.8 * np.exp(-10 * (X**2 + Y**2))
# أو فكرة أخرى: طبقة موحدة رقيقة
snow += 0.05

# ---------- دوال مساعدة ----------
def neighbors_indices(i, j, N):
    # إرجاع إحداثيات الجيران (4-جاية أو 8-جاية). نستخدم 8 جيران هنا.
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di == 0 and dj == 0:
                continue
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                yield ni, nj

def step_snow(terrain, snow):
    N = terrain.shape[0]
    total = terrain + snow
    # مصفوفات للتدفُّق الوارد والصادر
    out = np.zeros_like(snow)
    incoming = np.zeros_like(snow)

    # نحسب للتبسيط بتوجيه لكل خلية: ننقل إلى كل جار أدنى حسب فرق الارتفاع
    for i in range(N):
        for j in range(N):
            h = total[i, j]
            s = snow[i, j]
            if s <= min_snow_to_move:
                continue
            # اجمع الفروق الموجبة فقط إلى الجيران
            potentials = []
            for (ni, nj) in neighbors_indices(i, j, N):
                dh = h - total[ni, nj]
                if dh > 0:
                    # نريد أن يتناسب النقل مع dh و مع المسافة (قطري أو مباشر)
                    dist = max(abs(ni - i), abs(nj - j))
                    # وزن بسيط: الجيران القريبة تحصل على حصة أكبر
                    potentials.append(((ni, nj), dh / dist))
            if not potentials:
                continue
            # نوزع كمية من الثلج وفق توزيع النسبي ل potentials
            total_pot = sum(p for (_, p) in potentials)
            # كمية إجمالية تخرج من الخلية هذه خلال dt
            amount_out = min(s, flow_coeff * total_pot * dt)
            # نطبق احتكاك / فقدان
            amount_out *= (1.0 - friction)
            out[i, j] = amount_out
            for (ni, nj), weight in potentials:
                frac = weight / total_pot
                incoming[ni, nj] += amount_out * frac

    # تحديث الثلج: نضيف الوارد ونطرح الصادر
    new_snow = snow + incoming - out
    # منع القيم السالبة لسبب رقمي
    new_snow = np.maximum(new_snow, 0.0)
    return new_snow

# ---------- إعداد الرسم ----------
fig, ax = plt.subplots(figsize=(7, 6))
im = ax.imshow(terrain + snow, cmap='Blues', origin='lower')
ax.set_title("محاكاة انجراف الثلوج (المجموع: تضاريس + ثلج)")
plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)

# ---------- وظيفة التحديث للأنيميشن ----------
frame_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, color='white')
step_counter = {'t': 0}

def update(frame):
    step_counter['t'] += 1
    global snow
    # خطوة محاكاة
    snow = step_snow(terrain, snow)
    im.set_data(terrain + snow)
    frame_text.set_text(f"step = {step_counter['t']}")
    return im, frame_text

ani = FuncAnimation(fig, update, frames=steps, interval=30, blit=False)
plt.show()




























