

















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






import os
from flask import Flask, render_template, request, redirect
from multiprocessing import Process
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

current_process = None  # نخزن فيه العملية الحالية

def run_script(path):
    # تشغيل الملف
    subprocess.run([f"{sys.executable}", path])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global current_process

    if "python_file" not in request.files:
        return "لم يتم اختيار ملف"

    file = request.files["python_file"]
    if file.filename == "":
        return "الملف فارغ"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # إيقاف العملية القديمة إذا كانت تعمل
    if current_process and current_process.is_alive():
        current_process.terminate()

    # تشغيل العملية الجديدة
    current_process = Process(target=run_script, args=(filepath,))
    current_process.start()

    return redirect("/")

@app.route("/stop", methods=["POST"])
def stop():
    global current_process
    if current_process and current_process.is_alive():
        current_process.terminate()
        current_process = None
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
















