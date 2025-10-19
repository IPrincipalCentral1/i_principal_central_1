



















































































































































































































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






# Python simulation (static equilibrium + simple schematic) for the two-piston hydraulic setup
# - Small piston area A_s, big piston area A_b = 2 * A_s
# - Mass m_s = m_b = 1 kg placed on each piston
# - Incompressible fluid, no friction (quasi-static equilibrium)
# - Computes analytic equilibrium displacements and draws a simple schematic
#
# You can change `A_s_cm2` to any area in cm^2 (for example 10 cm^2).
# The script prints numeric results and shows a schematic plot of initial and final piston heights.
# This code runs here and displays the resulting plot and numbers.

import numpy as np
import matplotlib.pyplot as plt

# Parameters (change these to experiment)
A_s_cm2 = 10.0        # small piston area in cm^2 (changeable)
k = 2.0               # A_b = k * A_s (problem states k = 2)
m_small = 1.0         # mass on small piston (kg)
m_big = 1.0           # mass on big piston (kg)
rho = 1000.0          # fluid density (kg/m^3), water ~1000
g = 9.81              # gravity (m/s^2)

# Convert area to m^2
A_s = A_s_cm2 * 1e-4
A_b = k * A_s

# Analytic equilibrium displacements derived earlier (for k=2)
# For Ab = 2 As:
# y = m / (6 rho A_s)  (big piston upward)
# x = 2*y             (small piston downward)
y_eq = m_small / (6.0 * rho * A_s)    # big piston rise (m)
x_eq = 2.0 * y_eq                     # small piston descent (m)

# Sanity: If both masses differ, general formula from pressure balance:
# (m_s/A_s) - (m_b/A_b) = rho * (x + y)
# With volume conservation: A_s*x = A_b*y => x = k*y => (m_s/A_s - m_b/A_b) = rho*(k+1)*y
# So y = (m_s/A_s - m_b/A_b) / (rho*(k+1))
# For m_s = m_b = m and A_b = k A_s => m/A_s - m/(k A_s) = m(1-1/k)/A_s = m(k-1)/(k A_s)
# So y = [m (k-1) / (k A_s)] / [rho (k+1)] = m (k-1) / (k (k+1) rho A_s)
# For k=2 this becomes m / (6 rho A_s) (matches above).

# Print numeric results
print(f"Parameters: A_s = {A_s_cm2:.3f} cm^2 = {A_s:.6e} m^2, A_b = {A_b:.6e} m^2 (k={k})")
print(f"Masses: m_small = {m_small} kg, m_big = {m_big} kg, rho = {rho} kg/m^3")
print()
print("Equilibrium displacements (analytic):")
print(f"  Small piston descends x = {x_eq:.6f} m = {x_eq*1000:.3f} mm")
print(f"  Big piston rises     y = {y_eq:.6f} m = {y_eq*1000:.3f} mm")

# Simple schematic plot (side view)
fig, ax = plt.subplots(figsize=(5, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-0.1, 1.5)

# Draw fixed ground baseline for reference
ax.hlines(0, -0.8, 0.8, linewidth=1)

# Define piston geometry (widths proportional to sqrt(area) just for visualization)
w_small = np.sqrt(A_s) * 30.0
w_big   = np.sqrt(A_b) * 30.0

# Initial piston top heights (start both at same baseline height)
h0 = 0.2  # initial top height (m)
# Final top heights after displacement
h_small_final = h0 - x_eq   # small piston top decreases
h_big_final   = h0 + y_eq   # big piston top increases

# Draw initial pistons (dashed)
ax.add_patch(plt.Rectangle((-0.5*w_small, h0-0.02), w_small, 0.02, fill=None, linestyle='--', label='initial small'))
ax.add_patch(plt.Rectangle((0.1, h0-0.02), w_big, 0.02, fill=None, linestyle='--', label='initial big'))

# Draw final pistons (solid)
ax.add_patch(plt.Rectangle((-0.5*w_small, h_small_final-0.02), w_small, 0.02, label='final small'))
ax.add_patch(plt.Rectangle((0.1, h_big_final-0.02), w_big, 0.02, label='final big'))

# Draw connecting fluid column as a simple line between piston bottoms (visual only)
# Connect bottom points (approx)
ax.plot([-0.5*w_small + w_small/2, 0.1 + w_big/2], [h_small_final-0.02, h_big_final-0.02], linestyle='-', linewidth=2)

# Annotate
ax.text(-0.5*w_small, h_small_final-0.06, f"small top = {h_small_final:.3f} m\n(descend {x_eq*1000:.1f} mm)", va='top')
ax.text(0.1 + w_big, h_big_final-0.06, f"big top = {h_big_final:.3f} m\n(rise {y_eq*1000:.1f} mm)", va='top')

ax.set_title("Two-piston hydraulic system — initial (dashed) and equilibrium (solid)")
ax.axis('off')
plt.show()

























