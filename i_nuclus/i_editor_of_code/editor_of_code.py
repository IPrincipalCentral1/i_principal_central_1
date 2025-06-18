














# i_hello










# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
     
     
 


  
   
# hello 














import os




    
    
    
    





# section of ai 






import traceback


import subprocess

import platform


import os





list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            



]










import traceback

import sys


import subprocess








try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    
    
        print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
    
        #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
    
        
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
    
    
        counter_0 += 1
    
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    







from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QProcess
import sys
import os

class LauncherWindow(QMainWindow):
    def __init__(self, path_of_file):
        super().__init__()
        self.setWindowTitle("open_the editor")

        self.path_of_file = path_of_file

        button = QPushButton("تشغيل المحرر في Terminal")
        button.clicked.connect(self.launch_in_terminal)

        layout = QVBoxLayout()
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def launch_in_terminal(self):
        script_path = os.path.join(os.getcwd(), "edit-or_of_code", "files_0", "editor_of_code_0.py")
        command = f"python3 {self.path_of_file}; exec bash"

        # أمر QProcess لفتح gnome-terminal وتشغيل الأمر
        
        #process = QProcess(self)

        #process.start("gnome-terminal", ["--", "bash", "-c", command])

        # أمر التشغيل: konsole -e "python3 script.py"
        
        command = f'konsole -e "python3 \\"{self.path_of_file}\\""'

        # استخدم startDetached لتشغيله بشكل مستقل
        
        QProcess.startDetached("/bin/bash", ["-c", command])




if __name__ == "__main__":



        
    
    

    

        
           


    

        
    system = platform.system()

    path_of_file = os.path.join(os.getcwd(), "edit-or_of_code", "files_0", "editor_of_code_0.py")
    
    
    
    
    
    
    
    if system == "Windows":
    
    
        subprocess.run(["cmd", "/c", f"python {path_of_file}"])
    
    
    elif system == "Linux":



        app = QApplication(sys.argv)
        window = LauncherWindow(path_of_file)
        window.show()
        sys.exit(app.exec_())

        
        
        
        #subprocess.run(["gnome-terminal", "--", "bash", "-c", f"python3 {path_of_file} ; exit;"])
    

    elif system == "Darwin":
    
        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "python3 {path_of_file} ; exit"'])
    
    


    while (True):
    
        pass










# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


# my code 













