













'''

this file should be executed before . if you want to launch a new mix from the beginning



'''



import os


cwd = os.path.dirname(os.path.abspath(__file__))


files = []

for root, dirs, files in os.walk(os.path.join(cwd, "space_for_mix")):

    break



counter_0 = 0


while (counter_0 < len(files)):

    
    os.remove(os.path.join(cwd, "space_for_mix", files[counter_0]))


    counter_0 += 1



















