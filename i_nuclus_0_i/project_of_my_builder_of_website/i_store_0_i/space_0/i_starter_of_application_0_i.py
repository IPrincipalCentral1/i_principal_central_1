

















list_of_liberary_to_install = [

                            ["flask"] ,
                            
                            



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




#def thread_0(i_list_of_run_0_i, i_id_0_i):




    #i_p_0_i = threading.Thread(target=module.main(), daemon=True).start()


    #i_run_0_i = i_list_of_run_0_i[i_id_0_i]


    #while (i_run_0_i == True):    



        #i_run_0_i = i_list_of_run_0_i[i_id_0_i]






#i_list_of_run_1_i = [True]

#i_id_0_i = 0


#i_p_1_i = threading.Thread(target=thread_0, args=(i_list_of_run_1_i, i_id_0_i, ), daemon=True).start()














import os
import threading
import time
import importlib.util
from flask import Flask, render_template, request, redirect


cwd = os.path.dirname(os.path.abspath(__file__))





app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ----------------------------
# إدارة التشغيل
# ----------------------------
current_thread = None
stop_flags = [False]
module = None

global filepath, i_file_of_transmission_0_i

filepath = ""

i_file_of_transmission_0_i = os.path.join(cwd, "i_transmission_0_i.txt")



i_encoding_0_i = "utf-8"



def load_module(path):
    """تحميل الملف كـ module"""
    spec = importlib.util.spec_from_file_location("file_selected", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def thread_runner(module, flag_list, idx):
    
    """يشغل main داخل Thread ويراقب flag"""
    t = threading.Thread(target=module.main, daemon=True)
    t.start()

    
    i_run_0_i = flag_list[idx]
    
    
    while (i_run_0_i == True):
        
        
        i_run_0_i = flag_list[idx]
        
    


def i_runner_of_thread_0_i():
    
    
    
    os.system(f"{sys.executable} i_starter_of_application_1_i.py")
    
    
    




# ----------------------------
# Flask routes
# ----------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global current_thread, stop_flags, module

    if "python_file" not in request.files:
        return "لم يتم اختيار ملف"

    file = request.files["python_file"]
    if file.filename == "":
        return "الملف فارغ"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # تحميل module
    module = load_module(filepath)

    
    
    stop_flags[0] = False
    if current_thread and current_thread.is_alive():
        stop_flags[0] = False
        current_thread.join()

    # تشغيل الجديد
    stop_flags[0] = True
    
    
    with open(i_file_of_transmission_0_i, "w", encoding=i_encoding_0_i) as f_:
        
        f_.write(filepath + ";" + "True")
        
    
    
    
    
    
    
    

    return redirect("/")

@app.route("/stop", methods=["POST"])
def stop():
    global stop_flags, filepath
    stop_flags[0] = False
    
    with open(i_file_of_transmission_0_i, "w", encoding=i_encoding_0_i) as f_:
        
        f_.write(filepath + ";" + "False")
        
    
    
    
    return redirect("/")

if __name__ == "__main__":
    
    i_p_0_i = threading.Thread(target=i_runner_of_thread_0_i, daemon=True).start()
    
    
    
    app.run(host="0.0.0.0", port=8081, debug=True)






















