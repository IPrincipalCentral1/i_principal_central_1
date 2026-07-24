



















































































































































































































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











# Dynamic simulation & animation of the two-piston hydraulic system
# - Incompressible fluid, pistons connected by volume conservation: A_s * x = A_b * y  (x down positive for small piston, y up positive for big piston)
# - Dynamics reduced to single coordinate x (small piston displacement), with y = x / k
# - Effective mass: M = m_s + m_b / k^2
# - Effective spring (from hydrostatic pressure): K = rho * g * A_s * (1 + 1/k)
# - Gravity imbalance provides a constant forcing term: Fg = g*(m_s - m_b/k)
# - Light viscous damping c included
#
# The script integrates the ODE M x'' + c x' + K x = Fg and animates the two pistons and connecting tube.
# You can change A_s_cm2, k, masses, damping, initial conditions, and runtime.
#
# Run this cell to display the animation in the notebook. The animation will loop automatically.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# --- Parameters (changeable) ---
A_s_cm2 = 10.0       # small piston area in cm^2
k = 2.0              # A_b = k * A_s
m_s = 1.0            # mass on small piston (kg)
m_b = 2.0           # mass on big piston (kg)
rho = 1000.0         # fluid density (kg/m^3)
g = 9.81             # gravity (m/s^2)
c = 5.0e-1           # viscous damping coefficient (N s / m) -- tune for more/less damping

# Simulation settings
t_max = 120.0         # seconds to simulate per run
dt = 0.005           # timestep
save_every = 4       # only draw every N steps to speed up animation rendering
repeat = True        # animation will repeat/loop

# Initial conditions (release from rest at x0)
x0 = 0.0             # starting small-piston displacement from nominal reference (m). Set to 0 to see motion to equilibrium.
xdot0 = 0.0          # initial velocity (m/s)

# Derived params
A_s = A_s_cm2 * 1e-4
A_b = k * A_s
M_eff = m_s + m_b / (k**2)
K = rho * g * A_s * (1.0 + 1.0/k)
Fg = g * (m_s - m_b / k)    # right-hand side forcing (N)

print(f"A_s = {A_s} m^2, A_b = {A_b} m^2, k={k}")
print(f"M_eff = {M_eff} kg, K = {K} N/m, Fg = {Fg} N, damping c = {c} N s/m")

# ODE: x'' = (Fg - c x' - K x) / M_eff
def step_rk4(x, v, dt):
    # state s = [x, v]
    def accel(x_local, v_local):
        return (Fg - c * v_local - K * x_local) / M_eff
    # RK4
    k1x = v
    k1v = accel(x, v)
    k2x = v + 0.5*dt*k1v
    k2v = accel(x + 0.5*dt*k1x, v + 0.5*dt*k1v)
    k3x = v + 0.5*dt*k2v
    k3v = accel(x + 0.5*dt*k2x, v + 0.5*dt*k2v)
    k4x = v + dt*k3v
    k4v = accel(x + dt*k3x, v + dt*k3v)
    x_new = x + (dt/6.0)*(k1x + 2*k2x + 2*k3x + k4x)
    v_new = v + (dt/6.0)*(k1v + 2*k2v + 2*k3v + k4v)
    return x_new, v_new

# Integrate and store trajectory
num_steps = int(t_max / dt)
times = np.zeros(num_steps//save_every + 1)
xs = np.zeros_like(times)
vxs = np.zeros_like(times)

x = x0
v = xdot0
idx = 0
xs[idx] = x
vxs[idx] = v
times[idx] = 0.0

for n in range(1, num_steps+1):
    x, v = step_rk4(x, v, dt)
    if (n % save_every) == 0:
        idx += 1
        times[idx] = n * dt
        xs[idx] = x
        vxs[idx] = v

# Convert to big piston displacement y = x / k
ys = xs / k

# Equilibrium value (analytic)
x_eq = Fg / K
y_eq = x_eq / k

print(f"Analytic equilibrium: x_eq = {x_eq:.6f} m ({x_eq*1000:.1f} mm), y_eq = {y_eq*1000:.1f} mm")

# --- Animation drawing setup ---
fig, ax = plt.subplots(figsize=(7,5))
ax.set_xlim(-0.8, 0.8)
ax.set_ylim(-0.2, 0.6)
ax.set_title("Dynamic two-piston hydraulic simulation (looping)")
ax.axis('off')

# Visual sizes (for display only)
h_base = 0.0   # baseline y of reference
piston_thickness = 0.02  # m
scale_w = 50.0  # scale factor to visualize widths

w_small = np.sqrt(A_s) * scale_w
w_big = np.sqrt(A_b) * scale_w

# Initial coordinates for drawing
h_small_initial = 0.15  # initial top height
h_big_initial = 0.45

# Create drawing elements
# pistons as rectangles
small_rect = plt.Rectangle((-0.5*w_small, h_small_initial - piston_thickness), w_small, piston_thickness, ec='k', lw=1.2)
big_rect = plt.Rectangle((0.2, h_big_initial - piston_thickness), w_big, piston_thickness, ec='k', lw=1.2)
ax.add_patch(small_rect)
ax.add_patch(big_rect)

# connecting tube (a polygon or line between piston tops through a curved path)
tube_line, = ax.plot([], [], lw=3)

# text info
time_text = ax.text(-0.75, 0.52, '', fontsize=10)
pos_text = ax.text(-0.75, 0.46, '', fontsize=10)
vel_text = ax.text(-0.75, 0.40, '', fontsize=10)
eq_text = ax.text(0.05, 0.52, f"analytic x_eq={x_eq*1000:.1f} mm\nanalytic y_eq={y_eq*1000:.1f} mm", fontsize=9)

# Function to compute display coordinates given physical displacement x (down positive for small)
def display_positions(x_phys):
    # small piston top goes down by x_phys from initial
    y_small_top = h_small_initial - x_phys
    # big piston top goes up by y = x/k
    y_big_top = h_big_initial + (x_phys / k)
    return y_small_top, y_big_top

# init and animate
def init():
    tube_line.set_data([], [])
    time_text.set_text('')
    pos_text.set_text('')
    vel_text.set_text('')
    return small_rect, big_rect, tube_line, time_text, pos_text, vel_text

def animate(i):
    x_now = xs[i]
    y_now = ys[i]
    t_now = times[i]
    v_now = vxs[i]
    # compute display coords
    small_top, big_top = display_positions(x_now)
    # update piston rectangles
    small_rect.set_xy((-0.5*w_small, small_top - piston_thickness))
    big_rect.set_xy((0.2, big_top - piston_thickness))
    # draw a curved tube between piston edges (simple polyline)
    xs_tube = np.linspace(-0.5*w_small + w_small, 0.2, 6)
    ys_tube = np.linspace(small_top - piston_thickness/2, big_top - piston_thickness/2, 6)
    tube_line.set_data(xs_tube, ys_tube)
    # update texts
    time_text.set_text(f"t = {t_now:.2f} s")
    pos_text.set_text(f"small x = {x_now*1000:.1f} mm\nbig y = {y_now*1000:.1f} mm")
    vel_text.set_text(f"v_small = {v_now:.3f} m/s")
    return small_rect, big_rect, tube_line, time_text, pos_text, vel_text

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(times), interval=dt*1000*save_every, blit=True, repeat=repeat)

# Display animation
plt.show()

# If you want to save the animation to an mp4 file locally, uncomment the following lines:
# anim.save('hydraulic_simulation.mp4', fps=30, dpi=150, writer='ffmpeg')
# print("Saved animation to hydraulic_simulation.mp4")













