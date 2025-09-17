















list_of_liberary_to_install = [
                            
                            ["pyqt5"] ,
                            
                            


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
        
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
        
            
            
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





from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Label قابل للنسخ")
        layout = QVBoxLayout()

        # نص داخل QLabel
        label = QLabel("هذا نص داخل QLabel يمكن نسخه")
        label.setTextInteractionFlags(Qt.TextSelectableByMouse)  # تفعيل التحديد والنسخ

        layout.addWidget(label)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
















