















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





try:

    
    
    from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
    from PyQt5.QtCore import Qt
    import sys
    
    
    
    
    def apply_night_classic(app):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(30, 30, 30))
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(35, 35, 35))
        palette.setColor(QPalette.Text, QColor(220, 220, 220))
        palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
        palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))
        palette.setColor(QPalette.Highlight, QColor(45, 140, 240))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(40, 40, 40))
        palette.setColor(QPalette.Link, QColor(100, 150, 255))
        app.setPalette(palette)
    
    
    
    
    
    def apply_night_violet(app):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(40, 30, 60))
        palette.setColor(QPalette.Base, QColor(35, 25, 55))
        palette.setColor(QPalette.AlternateBase, QColor(50, 35, 70))
        palette.setColor(QPalette.Text, QColor(220, 200, 255))
        palette.setColor(QPalette.WindowText, QColor(230, 210, 255))
        palette.setColor(QPalette.ButtonText, QColor(200, 180, 250))
        palette.setColor(QPalette.Highlight, QColor(130, 70, 200))
        palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
        palette.setColor(QPalette.Button, QColor(45, 30, 65))
        palette.setColor(QPalette.Link, QColor(170, 120, 255))
        app.setPalette(palette)
    
    
    
    
    def apply_night_hacker(app):
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(10, 20, 10))
        palette.setColor(QPalette.Base, QColor(5, 15, 5))
        palette.setColor(QPalette.AlternateBase, QColor(15, 25, 15))
        palette.setColor(QPalette.Text, QColor(0, 255, 0))
        palette.setColor(QPalette.WindowText, QColor(0, 255, 0))
        palette.setColor(QPalette.ButtonText, QColor(0, 255, 0))
        palette.setColor(QPalette.Highlight, QColor(0, 100, 0))
        palette.setColor(QPalette.HighlightedText, QColor(0, 255, 0))
        palette.setColor(QPalette.Button, QColor(10, 20, 10))
        palette.setColor(QPalette.Link, QColor(0, 255, 100))
        app.setPalette(palette)
    
    
    
    
    
    
    def apply_light_theme(app):
        app.setPalette(QApplication.style().standardPalette())
    
    
    class Window(QWidget):
        def __init__(self):
            super().__init__()
    
            self.setWindowTitle("Label قابل للنسخ")
            layout = QVBoxLayout()
    
            # نص داخل QLabel
            label = QLabel("هذا نص داخل QLabel يمكن نسخه")
            # تفعيل التحديد والنسخ
            
            label.setTextInteractionFlags(Qt.TextSelectableByMouse)
            
            layout.addWidget(label)
            
            self.setLayout(layout)
    
    
    
    
    if __name__ == "__main__":    
        
        app = QApplication(sys.argv)
        window = Window()
        window.show()
        sys.exit(app.exec_())
        
    
    
except:    
    
    
        
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
        
    file = os.path.join(cwd, "file_of_error_1.txt")
    
    with open(file, "w") as f_:
    
        f_.write(str(error))
    
    
    
    
    
    











