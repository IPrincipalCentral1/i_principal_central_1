


















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
        
            
            #subprocess.check_call([sys.executable, "-m", "pip", "uninstall", f"{list_of_liberary_to_install[counter_0][0]}"])
            
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






from PIL import Image, PngImagePlugin

import os

import threading

import time

import sys

import cv2

import numpy as np

from PyQt5.QtWidgets import QApplication, QWidget

from PyQt5.QtGui import QPainter, QImage, QPalette, QColor

from PyQt5.QtCore import QTimer, Qt


import ctypes









class MyWidget(QWidget):


    def __init__(self):


        super().__init__()
        
        
        
        
        #self.images = [QImage(200, 200, QImage.Format_RGB888)]
        
        #self.current_image_index = 0
        
        
        
        
        self.setWindowTitle('Simulater')
        
        self.setStyleSheet("background-color: black;")
        


        self.simulated_img = os.path.join(cwd , "space_0", "photo", "simulator_2D.png")

        self.black = os.path.join(cwd, "space_0", "photo", "a.png")

        self.image_of_display = os.path.join(cwd, "space_0", "photo", "image_of_display.png")


        self.i_image_black = os.path.join(cwd, "space_0", "photo", "black.png")
        
        
        
        
        
        
        self.i_image_to_read = os.path.join(cwd, "space_0", "photo", "new_image.png")

                
        
        self.size_of_img = (10, 10)
        
        self.head_of_snake = [0, 0]
        
        
        self.path_of_snake = [[0, 1], [1, 1], [1, 0], self.head_of_snake, ]
        
        
        
        
        # section of create-ing the image 
        
        

        
        
        image_1 = Image.open(self.i_image_black)
        
        image_1 = image_1.resize(self.size_of_img)
        
        image_1.putpixel((image_1.size[0] // 2, image_1.size[1] // 2), (255, 0, 0))
        
        image_1.putpixel((self.head_of_snake[0], self.head_of_snake[1]), (0, 255, 0))


        
        # إنشاء metadata جديدة

        metadata = PngImagePlugin.PngInfo()

        metadata.add_text("head_of_the_snake", f"{self.head_of_snake[0]},{self.head_of_snake[1]}")

        
        
        image_1.save(self.i_image_to_read, pnginfo=metadata)
        
        
        img = Image.open(self.i_image_to_read)
        
        string_0 = str(img.text)
        
        v_0 = string_0.split(":")
        
        v_1 = v_0[1].split("'")
        
        v_2 = v_1[1].split(",")
        
        
        print(f"img.text = {string_0} . v_2 = {v_2} .")  # سيعرض {"Comment": "هذا النص مخفي في بيانات الصورة"}
        
        
        



        self.color = (255, 255, 0)

        self.black_color = (0, 0, 0)

        
        
        self.list_of_points = []


        self.start_ = 3

        #self.refresh()

        self.root_images = [

                cv2.imread(self.simulated_img),

                cv2.imread(self.black),

                cv2.imread(self.image_of_display),

                cv2.imread(self.i_image_to_read),

                ]






        self.root_images_pil = [

                Image.open(self.simulated_img),

                Image.open(self.black),

                Image.open(self.image_of_display),

                Image.open(self.i_image_to_read),


                ]



        self.images = [self.root_images[self.start_]]


        # فهرس الصورة الحالية

        self.current_image_index = 0



        self.timer = QTimer(self)

        self.timer.timeout.connect(self.next_image)

        self.timer.start(1)  # 3000 ميلي ثانية (3 ثوانٍ)

        self.semaphore_of_click_right = False

        self.semaphore_of_click_left = False

        self.key_pressed = ""

        self.semaphore_of_key_board_click = False






        p = threading.Thread(target=self.main, daemon=True).start()


        self.mouse_x = 0

        self.mouse_y = 0




    def get_the_head_from_image(self):
        
                
        
        img = Image.open(self.i_image_to_read)
        
        string_0 = str(img.text)
        
        v_0 = string_0.split(":")
        
        v_1 = v_0[1].split("'")
        
        v_2 = v_1[1].split(",")
        
        
        print(f"string_0 = {string_0} . v_2 = {v_2} .")
        
        
        
        

    def build_the_snake(self):
        
                
        
        
        image_1 = Image.open(self.i_image_black)
        
        image_1 = image_1.resize(self.size_of_img)
        
        #image_1.putpixel((image_1.size[0] // 2, image_1.size[1] // 2), (255, 0, 0))
        
        
        
        image_1.putpixel((self.head_of_snake[0], self.head_of_snake[1]), (0, 255, 0))
        
        counter_0 = 0
        
        while (counter_0 < len(self.path_of_snake)):
            
            
            
            counter_0 += 1
            
        
        
        
        # إنشاء metadata جديدة
        
        metadata = PngImagePlugin.PngInfo()
        
        metadata.add_text("head_of_the_snake", f"{self.head_of_snake[0]},{self.head_of_snake[1]}")
        
        
        
        image_1.save(self.i_image_to_read, pnginfo=metadata)
        
        
        
        


    def convert_cv_qt(self, cv_img):

        """تحويل صورة من OpenCV إلى QImage"""

        height, width, channel = cv_img.shape

        self.original_img_width = width

        self.original_img_height = height

        bytes_per_line = 3 * width

        # print("hello .")

        qt_image = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # print("hello_1 .")


        return qt_image.rgbSwapped()


    def next_image(self):
    
        # طباعة النص عند الانتقال بين الصور

        t1 = time.time()

        # تغيير الصورة الحالية
        self.current_image_index = self.current_image_index
        self.update()  # تحديث واجهة المستخدم لإعادة رسم الصورة

        t2 = time.time()

        #if (t2 - t1 > 0):

        #    print("update fps = ", 1 / (t2 - t1))



    def paintEvent(self, event):

        painter = QPainter(self)

        # احصل على أبعاد النافذة
        window_width = self.width()
        window_height = self.height()

        # احصل على الصورة الحالية وقم بتعديل حجمها لتتناسب مع أبعاد النافذة
        
        current_image = self.images[self.current_image_index]
        

        scaled_image = current_image.scaled(window_width, window_height, Qt.IgnoreAspectRatio)



        # تحديد نقطة البداية لرسم الصورة في منتصف النافذة
        start_x = (window_width - scaled_image.width()) // 2
        start_y = (window_height - scaled_image.height()) // 2

        self.img_width = scaled_image.width()

        self.img_height = scaled_image.height()

        self.start_x = start_x

        self.start_y = start_y


        #print("x = ", start_x, "  . y = ", start_y, " . width_img = ", scaled_image.width(), " . height_img = ", scaled_image.height(), " . window_width = ", window_width, "  . window_height = ", window_height)

        # رسم الصورة المحجمة في النافذة
        painter.drawImage(start_x, start_y, scaled_image)



    

    def crop(self, img_cv):


        img = Image.fromarray(img_cv)

        box = (40, 70, 370, 250)

        img = img.crop(box)

        return np.array(img)



    def main(self):



        run = True

        img = self.root_images[self.start_].copy()

        refresh_screen = True


        while (run):

            
            if (refresh_screen == True):
            
                self.images = [self.convert_cv_qt(img)]
                
                refresh_screen = False



if __name__ == "__main__":


        
    
    
    app = QApplication(sys.argv)
    
    window = MyWidget()
    
    window.show()
    
    sys.exit(app.exec_())
    
    















