


















list_of_liberary_to_install = [
                            
                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            
                            
                            ["pillow"] ,
                            
                            
                            
                            ["opencv-python-headless"] ,
                            
                            
                            ["opencv-python"] ,




                            #["opencv-contrib-python"] ,
                            



]










import os


cwd = os.path.dirname(os.path.abspath(__file__))



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
import sys
import cv2  # opencv-python-headless
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtCore import QTimer, Qt, pyqtSignal


class MyWidget(QMainWindow):

    update_image_signal = pyqtSignal(QImage)  # إشارة لتحديث الصورة

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Simulator')
        self.setStyleSheet("background-color: black;")

        # روابط الصور
        self.simulated_img = os.path.join(cwd, "space_0", "photo", "simulator_2D.png")
        self.black = os.path.join(cwd, "space_0", "photo", "a.png")
        self.image_of_display = os.path.join(cwd, "space_0", "photo", "image_of_display.png")
        self.i_image_to_read = os.path.join(cwd, "space_0", "photo", "white.png")

        # تحميل الصور
        self.root_images = [
            cv2.imread(self.simulated_img),
            cv2.imread(self.black),
            cv2.imread(self.image_of_display),
            cv2.imread(self.i_image_to_read),
        ]

        self.images = [self.convert_cv_qt(self.root_images[0])]
        self.current_image_index = 0

        # مؤقت لتحديث الواجهة
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(16)  # ~60 FPS

        # قائمة الملفات
        self.init_menu()

        # ربط الإشارة بالدالة
        self.update_image_signal.connect(self.safe_update_image)

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("ملف")

        open_action = QAction("فتح صورة", self)
        open_action.triggered.connect(self.open_image)
        file_menu.addAction(open_action)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "اختر صورة", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            img = cv2.imread(file_path)
            if img is not None:
                self.images = [self.convert_cv_qt(img)]
                self.current_image_index = 0

    def convert_cv_qt(self, cv_img):
        """تحويل صورة OpenCV إلى QImage"""
        height, width, channel = cv_img.shape
        bytes_per_line = 3 * width
        qt_image = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qt_image.rgbSwapped()

    def paintEvent(self, event):
        painter = QPainter(self)
        window_width = self.width()
        window_height = self.height()
        current_image = self.images[self.current_image_index]
        scaled_image = current_image.scaled(window_width, window_height, Qt.IgnoreAspectRatio)
        start_x = (window_width - scaled_image.width()) // 2
        start_y = (window_height - scaled_image.height()) // 2
        painter.drawImage(start_x, start_y, scaled_image)

    def safe_update_image(self, qt_img):
        """تحديث الصورة بأمان"""
        self.images = [qt_img]
        self.current_image_index = 0

    def keyPressEvent(self, event):
        """التعامل مع ضغطات الكيبورد"""
        if event.key() == Qt.Key_Space:  # إذا ضغطت space
            self.open_image()
        else:
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())









