










import os


cwd = os.path.dirname(os.path.abspath(__file__))






list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            



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
    
    
    







from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QProgressBar, QFileDialog

import sys

import time

from PyQt5.QtCore import QTimer

import threading

from pathlib import Path

import traceback










class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("i_dupliquor")

        self.setGeometry(100, 100, 300, 200)

        self.setMinimumSize(1, 1)



        # استدعاء دالة إعداد واجهة المستخدم

        # إنشاء Label

        
        self.lab_01 = QLabel("")

        self.lab_01.setStyleSheet("font-size: 20px; color: green; font-weight: bold;")


        
        
        self.lab_02 = QLabel("")

        self.lab_02.setStyleSheet("font-size: 20px; color: green; font-weight: bold;")




        self.lab_3 = QLabel("0 %")

        self.lab_3.setStyleSheet("font-size: 20px; color: green; font-weight: bold;")



        # إنشاء تخطيط

        layout = QVBoxLayout()

        layout.addWidget(self.lab_01)

        layout.addWidget(self.lab_02)

        layout.addWidget(self.lab_3)



        # تعيين التخطيط للنافذة

        self.setLayout(layout)


        self.file_coping = ""

        self.src = ""

        self.dist = ""

        file = os.path.join(cwd, "place_of_duplication.txt")

        with open(file, "r", encoding="utf-8") as f_:

            self.duplication_place = f_.read(os.path.getsize(file))

        if (os.path.exists(self.duplication_place) == True):

    
            self.starting = True
    
    
            if (self.starting):
    
                file = os.path.join(cwd, "time_max_of_duplication.txt")
    
                with open(file, "r", encoding="utf-8") as f_:
    
                    duplication_time_s = f_.read(os.path.getsize(file))
    
    
                self.duplication_time = 0.0
    
                v = duplication_time_s.split(".")
    
                if (len(v) == 2):
    
                    k = int(v[0])
    
                    k_0 = int(v[1])
    
                    self.duplication_time = k + (k_0 / (10 ** len(v[1])))
    
                else:
    
                    print(f"le temps max de duplication  égale à : {duplication_time_s} . ERREUR!")
                    
    
    
                
                #p1 = threading.Thread(target=self.update_progress, daemon=True).start()
    
                p2 = threading.Thread(target=self.rechercheur, daemon=True).start()
    
    
        else:
        
            print(f"the place specify-ed do not exist .")
    
    


    def rechercheur(self):





        # le rechercheur


        while (True):

            # print("la recherche commence .")
    
            self.file = os.path.join(cwd, "time_max_of_duplication.txt")

            
            self.single = True

            dirs = [""]

            srcs = [""]


            max_dup_time = self.duplication_time

            j = 0

            while (j < len(dirs)):

                for root, dirs_, files in os.walk(os.path.join(cwd, dirs[j])):


                    break



                i = 0

                while (i < len(dirs_)):

                    dirs.append(os.path.join(dirs[j], dirs_[i]))

                    srcs.append(os.path.join(srcs[j], dirs_[i]))

                    i += 1

                    
                src_ = os.path.join(cwd, srcs[j])
                
                dist_ = os.path.join(self.duplication_place, dirs[j])

                if (not (os.path.exists(dist_))):
                    
                    try:
                    
                        os.makedirs(dist_, exist_ok=True)
                    
                    except Exception as e:
                    
                        print(f"ERROR : {e} .")
                    

                i = 0

                while (i < len(files)):

                    try:
                        
                        
                        #print(f"i_hello_0 . os.path.join(src_, files[i]) = {os.path.join(src_, files[i])} .")
                        
                        m = os.path.getmtime(os.path.join(src_, files[i]))
                        

                        #print(f"i_hello_1 . m = {m} . ")

                        if (((not (os.path.exists(os.path.join(dist_, files[i])))) or (m > self.duplication_time)) and (self.file != os.path.join(src_, files[i]))):
                            
                            #print(f"i_hello_2 .")
                           
                            
                            #print("m = ", m, " . self.d_t = ", self.duplication_time)
                            
                            print(f"m = {m} . self.duplication_time = {self.duplication_time} .")
                            
                            d_0 = Path(os.path.join(src_, files[i]))
                            
                            d_1 = Path(os.path.join(dist_, files[i]))
                            
                            
                            self.file_coping = os.path.join(src_, files[i])
                            
                            
                            print(f"file_coping : {self.file_coping} . size = {str(os.path.getsize(self.file_coping))} Byte . time = {time.strftime("%Y/%m/%d %H:%M:%S")} .")
                            

                            d_1.write_bytes(d_0.read_bytes())



                            self.file_coping = ""

                    
                            self.single = False

                            if (max_dup_time < m):

                                max_dup_time = m

                            

                    except Exception as e:

                        print(f"Erreur :  {e} .")


                        #traceback.print_exc()

                        #error = traceback.format_exc()

                        #semaphore = True

                        #print(f"Erreur : {str(error)}")



                        semphore = True

                    
                    i += 1


                j += 1


            if ((self.duplication_time != max_dup_time) and (not (self.single))):
                
                self.duplication_time = max_dup_time

                file = os.path.join(cwd, "time_max_of_duplication.txt")

                with open(file, "w", encoding="utf-8") as f_:

                    f_.write(str(self.duplication_time))


                file = os.path.join(self.duplication_place, "time_max_of_duplication.txt")

                with open(file, "w", encoding="utf-8") as f_:

                    f_.write(str(self.duplication_time))

                
                print(f"file of time copy-ed with success .")






    

    def update_progress(self):

        run = True

        f_c = ""

        while (run):


            if (f_c != self.file_coping):

                if (self.file_coping == ""):

                    self.lab_3.setText(" 100 % . terminat-ed !")

                else:


                    self.lab_3.setText("file_coping : " + self.file_coping)

                    #print(f"file_coping : ", self.file_coping + " . size = " + str(os.path.getsize(self.file_coping)) + " Byte " + " . time = ", time.strftime("%Y/%m/%d %H:%M:%S"))
                    
                    
                    print(f"file_coping : {self.file_coping} . size = {str(os.path.getsize(self.file_coping))} Byte . time = {time.strftime("%Y/%m/%d %H:%M:%S")} .")

                f_c = self.file_coping






if __name__ == "__main__":




    '''


    Guid :


        If you want to use this program you have to create a file in the same location where this program is located. 
        
        This file is named place_of_duplication.txt and then you have to put in it the link of the place where you copy 
        
        what you have in the place where this copier is located. Also you have to create another file named time_max_of_duplication.txt 
        
        which contains exactly 0.0. These two files are in the same location where this program is located. This will make this program 
        
        copy everything that is in the place where it is located to the place in the file place_of_duplication.txt. And whenever there is 
        
        a change it copies it automatically. You just have to run it and not turn it off for this to work.



        اذا اردت استخدام هاذا البرنامج عليك صنع ملف في نفس المكان الموجود فيه هاذا البرنامج 
        
        . هاذا الملف اسمه place_of_duplication.txt ثم عليك ان تضع فيه رابط المكان الذي تنسخ فيه ما لديك في المكان
        
         الذي هاذا الناسخ موجود فيه . و ايضا عليك صنع ملف آخر اسمه time_max_of_duplication.txt و
         
          يحتوي على ٠.٠ بالضبط . هاذين الملفين في نفس
          
          
           الموقع الموجود فيه هاذا البرنامج . هاذا سيجعل  هاذا البرنامج ينسخ كل ما هو موجود في المكان الذي هو موجود فيه للمكان الذي الموجود
           
            في الملف place_of_duplication.txt . و كلما يحدث هناك تغيير ينسخه تلقائيا . عليك فقط تشغيله و عدم اطفاؤه كي يعمل هاذا .


    '''


    # file = str_to_dir(s=cw + "time_max_of_duplication.txt")

    # with open(file, "w") as f_:

    #     f_.write(str(time.time()))


    
    
    
    
    
    
    try:
        
        file_of_place_of_duplication_0 = os.path.join(cwd, "place_of_duplication.txt")
        
        if (os.path.exists(file_of_place_of_duplication_0) == True):
            
            
            with open(file_of_place_of_duplication_0, "r", encoding="utf-8") as f_:
                
                content_2 = f_.read(os.path.getsize(file_of_place_of_duplication_0))
                
            
        else:
            
            message = "this file should contain the place of duplication ."
            
            with open(file_of_place_of_duplication_0, "w", encoding="utf-8") as f_:
            
                f_.write(message)
        
        
    except:
    
        semaphore = True
    
    

        
    
    
    
    try:
        
        file_of_time_max_of_duplication_0 = os.path.join(cwd, "time_max_of_duplication.txt")
        
        if (os.path.exists(file_of_time_max_of_duplication_0) == True):
            
            
            with open(file_of_time_max_of_duplication_0, "r", encoding="utf-8") as f_:
                
                content_2 = f_.read(os.path.getsize(file_of_time_max_of_duplication_0))
                
            
        else:
            
            message = "0.0"
            
            with open(file_of_time_max_of_duplication_0, "w", encoding="utf-8") as f_:
            
                f_.write(message)
        
        
    except:
    
        semaphore = True
    
    
    

    # إنشاء التطبيق

    app = QApplication(sys.argv)

    # إنشاء النافذة الرئيسية

    window = MainWindow()

    window.show()

    # تشغيل التطبيق

    sys.exit(app.exec_())
















