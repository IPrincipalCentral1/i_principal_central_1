













'''

this file should be executed before . if you want to launch a new mix from the beginning



'''



import os

import shutil


folder_0 = os.path.join(os.getcwd(), "space_for_mix")


if (os.path.exists(folder_0)):
    

    shutil.rmtree(folder_0)

    
    
    
file_0 = os.path.join(os.getcwd(), "i_run_mixer_1.txt")

with open(file_0, "w") as f_:

    f_.write("this file should contain just 'true' for the mixer to make the next step")

    
file_1 = os.path.join(os.getcwd(), "i_run_mixer_2.txt")

with open(file_1, "w") as f_:

    f_.write("this file should contain just 'true' to make the mixer stop")

    




os.makedirs(folder_0, exist_ok=True)














