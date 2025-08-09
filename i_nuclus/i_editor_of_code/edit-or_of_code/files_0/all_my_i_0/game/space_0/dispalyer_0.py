

















list_of_liberary_to_install = [
                            
                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            
                            
                            ["pillow"] ,
                            
                            
                            ["opencv-python"] ,
                            
                            
                            ["opencv-contrib-python"] ,
                            



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






from PIL import Image

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





global cw


cw = os.getcwd() + "/"







class MyWidget(QWidget):


    def __init__(self):


        super().__init__()







        self.setWindowTitle('Simulator')

        self.setStyleSheet("background-color: black;")



        self.simulated_img = cw + "space_0/photo/simulator_2D.png"

        self.black = cw + "space_0/photo/a.png"

        self.image_of_display = cw + "space_0/photo/image_of_display.png"

        self.i_image_to_read = cw + "space_0/photo/image_of_display.png"


        self.color = (255, 255, 0)

        self.black_color = (0, 0, 0)


        self.size_of_img = (100, 100)

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


        # إعداد المؤقت للتبديل بين الصور كل 3 ثوانٍ

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






    def refresh(self):


        img = Image.open(self.black)

        img = img.resize(self.size_of_img)

        img.save(self.image_of_display, format="PNG")





    def refresh_(self):


        img = self.root_images_pil[0]

        img = img.resize(self.size_of_img)

        self.root_images_pil[2] = img.copy()

        while (len(self.list_of_points) > 0):

            self.list_of_points.pop(0)


    def my_div(self, a, b):


        c = a / b

        d = int(c)

        e = c - d

        if (e >= 0.5):

            return d + 1

        else:

            return d




    def line(self, img_pil, point_of_start, point_of_end, color):


        
        if (point_of_start[0] <= point_of_end[0]):

            first_point = point_of_start

            last_point = point_of_end 

        else:

            first_point = point_of_end

            last_point = point_of_start

        
        if (first_point[1] <= last_point[1]):

            incrimentor_of_y = 1

        else:

            incrimentor_of_y = -1

        a = 0.0

        semaphore_of_x_x_aline_ed = False

        b = first_point[1]

        if ((last_point[0] - first_point[0]) != 0):

            a = (last_point[1] - first_point[1]) / (last_point[0] - first_point[0])

        else:

            semaphore_of_x_x_aline_ed = True



        if (semaphore_of_x_x_aline_ed == False):


            x = first_point[0]

            x_ = 0

            while (x <= last_point[0]):

                if (0 <= int((a * x_) + b) < self.size_of_img[1]):

                    img_pil.putpixel((x, int((a * x_) + b)), color)

                    
                x += 1

                x_ += 1


        if (point_of_start[1] <= point_of_end[1]):

            first_point = point_of_start

            last_point = point_of_end 

        else:

            first_point = point_of_end

            last_point = point_of_start




        a = 0.0

        semaphore_of_y_y_aline_ed = False

        b = first_point[0]

        if ((last_point[1] - first_point[1]) != 0):

            a = (last_point[0] - first_point[0]) / (last_point[1] - first_point[1])

        else:

            semaphore_of_y_y_aline_ed = True






        if (semaphore_of_y_y_aline_ed == False):


            y = first_point[1]

            y_ = 0

            while (y <= last_point[1]):

                if (0 <= int((a * y_) + b) < self.size_of_img[0]):

                    img_pil.putpixel((int((a * y_) + b), y), color)

                    
                y += 1

                y_ += 1



        return img_pil


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



    def mousePressEvent(self, event):

        # الحصول على إحداثيات النقر

        x = event.x()

        y = event.y()



        if ((self.start_x <= x) and (x < self.img_width + self.start_x) and (self.start_y <= y) and (y < self.img_height + self.start_y)):

            pourc_width = 100 * self.img_width / self.original_img_width

            pourc_height = 100 * self.img_height / self.original_img_height

            self.mouse_x = int((x - self.start_x) * 100 / pourc_width)

            self.mouse_y = int((y - self.start_y) * 100 / pourc_height)

        else:

            self.mouse_x = 0

            self.mouse_y = 0

        print("self.mouse_x = ", self.mouse_x, " . self.mouse_y = ", self.mouse_y)




        if event.button() == Qt.LeftButton:

            self.semaphore_of_click_left = True

            self.update_mouse_position(event)

            while (len(self.list_of_points) > 0):

                self.list_of_points.pop(0)




        elif event.button() == Qt.RightButton:
        
            self.semaphore_of_click_right = True

            self.update_mouse_position(event)
            
            print("ضغطت الزر الأيمن")

            
        
        elif event.button() == Qt.MiddleButton:
        
            print("ضغطت الزر الأوسط")


    def mouseMoveEvent(self, event):


        
        if event.buttons() & Qt.LeftButton:
     
            self.semaphore_of_click_left = True

            self.update_mouse_position(event)


            if (len(self.list_of_points) > 2):

                self.list_of_points.pop(0)

            self.list_of_points.append((self.mouse_x, self.mouse_y))





        elif event.buttons() & Qt.RightButton:
        
            self.semaphore_of_click_right = True

            self.update_mouse_position(event)

            
            print("ضغطت الزر الأيمن")

            
        
        elif event.button() == Qt.MiddleButton:
        
            print("ضغطت الزر الأوسط")


    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.is_dragging = False



    def update_mouse_position(self, event):

        x = event.x()

        y = event.y()

        if ((self.start_x <= x) and (x < self.img_width + self.start_x) and (self.start_y <= y) and (y < self.img_height + self.start_y)):

            pourc_width = 100 * self.img_width / self.original_img_width

            pourc_height = 100 * self.img_height / self.original_img_height

            self.mouse_x = int((x - self.start_x) * 100 / pourc_width)

            self.mouse_y = int((y - self.start_y) * 100 / pourc_height)

        else:

            self.mouse_x = 0

            self.mouse_y = 0

        print("mouse_x = ", self.mouse_x, " . mouse_y = ", self.mouse_y)




    def keyPressEvent(self, event):
     
        """يتم استدعاء هذا الحدث عند الضغط على مفتاح"""
     
        if event.key() == Qt.Key_Escape:  # إذا تم الضغط على زر Escape
     
            print("Escape!")
     
        else:

            print(f" text : {event.text()} , (key : {event.key()})")

        self.key_pressed = event.text()


        self.semaphore_of_key_board_click = True

        if (self.key_pressed == "i"):

            while (len(self.list_of_points) > 0):

                self.list_of_points.pop(0)


    def keyReleaseEvent(self, event):

        """يتم استدعاء هذا الحدث عند إفلات المفتاح"""

        print(f"key releazed :{event.text()} (key : {event.key()})")

        # self.key_pressed = ""



    

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

            
            

            if (self.semaphore_of_click_left == True):

                img_ = self.root_images_pil[self.start_]

                img_.putpixel((self.mouse_x, self.mouse_y), self.color)

                if (len(self.list_of_points) > 1):

                    img_ = self.line(img_, self.list_of_points[-1], self.list_of_points[-2], self.color)

                img = np.array(img_)

                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                self.semaphore_of_click_left = False

                print("pixel add-ed .")

                refresh_screen = True



            if (self.semaphore_of_click_right == True):

                img_ = self.root_images_pil[self.start_]

                img_.putpixel((self.mouse_x, self.mouse_y), self.black_color)

                img = np.array(img_)

                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                self.semaphore_of_click_right = False

                print("pixel clean-ed .")

                refresh_screen = True



            if ((self.semaphore_of_key_board_click == True)):

                if ((self.key_pressed == "r")):


                    self.refresh_()

                    img_ = self.root_images_pil[self.start_]

                    img = np.array(img_)

                    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                    self.key_pressed = ""


                    print("image clean-ed .")

                    refresh_screen = True

                if ((self.key_pressed == "s")):

                    self.root_images_pil[3].save(self.image_of_display, format="PNG")

                    print("file save-ed succesfuly .")


                self.semaphore_of_key_board_click = False






            if (refresh_screen == True):


                self.images = [self.convert_cv_qt(img)]

                refresh_screen = False





app = QApplication(sys.argv)

window = MyWidget()

window.show()

sys.exit(app.exec_())

















