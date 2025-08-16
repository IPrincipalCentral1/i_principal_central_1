













'''



when you click space . a window will popup and an inputtext there . you should put the full link of the image 

into that place and click enter . that will display the image .




'''






list_of_liberary_to_install = [
                            
                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            
                            
                            ["pillow"] ,
                            
                            
                            
                            ["opencv-python-headless"] ,
                            
                            
                            #["opencv-python"] ,




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





from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QDialog
)
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtCore import Qt
import cv2
import sys
import os




class InputDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("إدخال رابط أو مسار الصورة")
        self.setFixedSize(400, 100)

        layout = QVBoxLayout(self)
        self.input_path = QLineEdit()
        self.input_path.setPlaceholderText("أدخل مسار أو رابط الصورة هنا...")
        layout.addWidget(self.input_path)

        self.input_path.returnPressed.connect(self.accept)

    def get_path(self):
        return self.input_path.text().strip()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Image Viewer')
        self.setStyleSheet("background-color: black;")
        self.images = []
        self.current_image_index = 0

    def load_image(self, file_path):
        if os.path.exists(file_path):
            img = cv2.imread(file_path)
            if img is not None:
                self.images = [self.convert_cv_qt(img)]
                self.current_image_index = 0
                self.update()

    def convert_cv_qt(self, cv_img):
        height, width, channel = cv_img.shape
        bytes_per_line = 3 * width
        qt_image = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return qt_image.rgbSwapped()

    def paintEvent(self, event):
        if not self.images:
            return
        painter = QPainter(self)
        window_width = self.width()
        window_height = self.height()
        current_image = self.images[self.current_image_index]
        scaled_image = current_image.scaled(window_width, window_height, Qt.KeepAspectRatio)
        start_x = (window_width - scaled_image.width()) // 2
        start_y = (window_height - scaled_image.height()) // 2
        painter.drawImage(start_x, start_y, scaled_image)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            dialog = InputDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                path = dialog.get_path()
                self.load_image(path)


if __name__ == "__main__":
    
    
    
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
















