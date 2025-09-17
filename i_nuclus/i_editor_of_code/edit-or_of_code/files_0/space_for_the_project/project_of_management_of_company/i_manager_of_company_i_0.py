



















list_of_liberary_to_install = [
                            
                            ["pyqt5"] ,
                            
                            


]










import os


import traceback

import sys


import subprocess



cwd = os.path.dirname(os.path.abspath(__file__))




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





try:

    from PyQt5.QtWidgets import QPushButton, QHBoxLayout
    
    from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
    
    from PyQt5.QtWidgets import QMainWindow
    
    from PyQt5.QtCore import Qt
    
    from PyQt5.QtGui import QPalette, QColor, QBrush, QPixmap

    
    
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
    
    
    class Window(QMainWindow):
    
        def __init__(self):
            super().__init__()
    
            self.setWindowTitle("i_manager_of_company_i")
            
            
            self.setGeometry(100, 100, 800, 600)
    
            
            
            layout = QVBoxLayout()

            # نص داخل QLabel
            
            label = QLabel("")
            
            # تفعيل التحديد والنسخ

            label.setTextInteractionFlags(Qt.TextSelectableByMouse)

            layout.addWidget(label)

            self.setLayout(layout)

            
            # خلفية افتراضية
            self.background_on = True
           
            
            self.i_folder_i_0 = "i_folder_i_0"
            
            self.i_file_of_image_i_0 = os.path.join(cwd, self.i_folder_i_0, "image_of_background_1.png")
            
            
            
             # إعداد الباليت مع الصورة
            palette = QPalette()
            palette.setBrush(QPalette.Window, QBrush(QPixmap(self.i_file_of_image_i_0)))
            self.setPalette(palette)
            
            
            
    
    
            # الواجهة الرئيسية
            central = QWidget()
            self.setCentralWidget(central)
    
            # الأزرار
            
            button1 = QPushButton("button_1")
            
            button2 = QPushButton("button_2")
            
            button3 = QPushButton("i_background_i_0")
            
            # ربط الزر الثالث مع دالة
            button3.clicked.connect(self.toggle_background)
    
            # Layout أفقي للأزرار
            h_layout = QHBoxLayout()
            h_layout.addStretch()
            h_layout.addWidget(button1)
            h_layout.addWidget(button2)
            h_layout.addWidget(button3)
            h_layout.addStretch()
    
            # Layout عمودي لوضع الأزرار في الأسفل
            v_layout = QVBoxLayout(central)
            v_layout.addStretch()
            v_layout.addLayout(h_layout)
    
        def toggle_background(self):
            """تشغيل/إيقاف الخلفية"""
            if self.background_on:
                # إزالة الخلفية
                palette = QPalette()
                self.setPalette(palette)
                self.background_on = False
            else:
                # إرجاع الخلفية
                palette = QPalette()
                palette.setBrush(QPalette.Window, QBrush(QPixmap(self.i_file_of_image_i_0)))
                self.setPalette(palette)
                self.background_on = True
    
            
            
            
            
    
    
    
    
    if __name__ == "__main__":    
        
        app = QApplication(sys.argv)
        
        apply_night_classic(app)
        
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
    
    
    
    
    
    











