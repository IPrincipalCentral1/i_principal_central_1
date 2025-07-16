

















import os




from pathlib import Path


cwd = os.path.dirname(os.path.abspath(__file__))









list_of_file = [

            
            os.path.join(cwd, "Economic_Partner_official_produced_mixer_9.c"),
            
            
            os.path.join(cwd, "i_run_mixer_1.txt"),
            
            
            os.path.join(cwd, "i_run_mixer_2.txt"),
            
            
            os.path.join(cwd, "refresher_0.py"),
            
            
            os.path.join(cwd, "i_runner_of_mixer_0.py"),
            
            
            
            ]










file_of_path_0 = os.path.join(cwd, "path_to_copy_0.txt")



with open(file_of_path_0, "r") as f_:

    path_0 = f_.read(os.path.getsize(file_of_path_0))






counter_0 = 0


while (counter_0 < len(list_of_file)):
    
    
    d_0 = Path(list_of_file[counter_0])
    
    d_1 = Path(os.path.join(path_0, os.path.basename(list_of_file[counter_0])))
    
    
    
    d_1.write_bytes(d_0.read_bytes())
    
    
    
    
    counter_0 += 1
    
    










































