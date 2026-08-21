



















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






cwd = os.path.dirname(os.path.abspath(__file__))



print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])





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
        self.setWindowTitle("open the editor")

        self.path_of_file = path_of_file

        self.apply_night_mode()

        button = QPushButton("open_the_editor_of_code")
        button.clicked.connect(self.launch_in_terminal)

        layout = QVBoxLayout()
        layout.addWidget(button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def launch_in_terminal(self):
        script_path = os.path.join(os.getcwd(), "edit-or_of_code", "files_0", "editor_of_code_0.py")
        command = f"{sys.executable} {self.path_of_file}; exec ;"

        # أمر QProcess لفتح gnome-terminal وتشغيل الأمر
        
        process = QProcess(self)

        process.start("gnome-terminal", ["--", "bash", "-c", command])






    def apply_night_mode(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QTextEdit, QPlainTextEdit, QLineEdit {
                background-color: #252526;
                color: #d4d4d4;
                selection-background-color: #264f78;
            }
            QTreeView, QTreeWidget, QListView, QListWidget {
                background-color: #1e1e1e;
                color: #d4d4d4;
            }
            QTabWidget::pane {
                border: 1px solid #333;
            }
            QTabBar::tab {
                background: #2d2d2d;
                color: #ccc;
                padding: 6px;
            }
            QTabBar::tab:selected {
                background: #444;
                color: white;
            }
            QPushButton {
                background-color: #3c3c3c;
                color: white;
                border: 1px solid #555;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555;
            }
            QMenuBar {
                background-color: #2d2d2d;
                color: white;
            }
            QMenu {
                background-color: #2d2d2d;
                color: white;
            }
            QMenu::item:selected {
                background-color: #444;
            }
            QScrollBar:vertical, QScrollBar:horizontal {
                background: #2d2d2d;
            }
            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #5a5a5a;
                border-radius: 3px;
            }
        """)
    


if __name__ == "__main__":



        
    
    

    

        
           


    

        
    system = platform.system()

    path_of_file = os.path.join(os.getcwd(), "edit-or_of_code", "files_0", "editor_of_code_0.py")
    
    
    
    
    
    
    
    if system == "Windows":
    
    
        subprocess.run(["cmd", "/c", f"{sys.executable} {path_of_file}"])
    
    
    elif system == "Linux":



        app = QApplication(sys.argv)
        window = LauncherWindow(path_of_file)
        window.show()
        sys.exit(app.exec_())

        
        
        
        #subprocess.run(["gnome-terminal", "--", "bash", "-c", f"python3 {path_of_file} ; exit;"])
    

    elif system == "Darwin":
    
        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{sys.executable} {path_of_file} ; exit"'])
    
    


    while (True):
    
        pass










# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


# my code 













