










import os









from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton, QProgressBar, QFileDialog

import sys

import time

from PyQt5.QtCore import QTimer

import threading

from pathlib import Path






def i_wait(i_time):

    time.sleep(i_time)




def str_to_dir(s):




    v = s.split("/")

    
    s_ = "/"


    i = 0

    while (i < len(v) - 1):

        if (v[i] != ""):

            s_ += v[i] + "/"

        i += 1

    
    s_ += v[i]


    return s_








class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("i_dupliquer")

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

        file = str_to_dir(s=cw + "place_of_duplication.txt")

        with open(file, "r", encoding="utf-8") as f_:

            self.duplication_place = f_.read(os.path.getsize(file))

        if (self.duplication_place[-1] != "/"):

            self.duplication_place += "/"

        v = self.duplication_place.split("/")

        i = 0

        place = ""

        while (i < len(v) - 2):

            place += v[i] + "/"

            i += 1

        

        self.starting = True

        # if (not (os.path.exists(str_to_dir(s=place + "disk_interne.txt")))):

        #     print("le fichier 'disk_interne.txt' n'existe pas dans '" + str_to_dir(s=place + "disk_interne.txt") + "' . ERREUR!")

        #     self.starting = False
            

        if (self.starting):

            file = str_to_dir(s=cw + "time_max_of_duplication.txt")

            with open(file, "r", encoding="utf-8") as f_:

                duplication_time_s = f_.read(os.path.getsize(file))


            self.duplication_time = 0.0

            v = duplication_time_s.split(".")

            if (len(v) == 2):

                k = int(v[0])

                k_0 = int(v[1])

                self.duplication_time = k + (k_0 / (10 ** len(v[1])))

            else:

                print("le temps max de duplication  égale à : " + duplication_time_s + " . ERREUR!")
                


            
            p1 = threading.Thread(target=self.update_progress, daemon=True).start()

            p2 = threading.Thread(target=self.rechercheur, daemon=True).start()





    def i_organize(i_self, i_list):


        i_list_result = []

        


    def rechercheur(self):





        # le rechercheur


        while (True):

            # print("la recherche commence .")
    
            self.file = str_to_dir(s=cw + "time_max_of_duplication.txt")

            
            self.single = True

            dirs = [""]

            srcs = [""]


            max_dup_time = self.duplication_time

            j = 0

            while (j < len(dirs)):

                for root, dirs_, files in os.walk(str_to_dir(s=cw + dirs[j])):


                    break



                i = 0

                while (i < len(dirs_)):

                    dirs.append(str_to_dir(s=dirs[j] + "/" + dirs_[i]))

                    srcs.append(str_to_dir(s=srcs[j] + "/" + dirs_[i]))

                    i += 1

                    
                src_ = str_to_dir(s=cw + srcs[j])
                
                dist_ = str_to_dir(s=self.duplication_place + dirs[j])

                if (not (os.path.exists(dist_))):

                    os.system("mkdir " + dist_)

                i = 0

                while (i < len(files)):

                    try:

                        m = os.path.getmtime(str_to_dir(s=src_ + "/" + files[i]))

                        if (((not (os.path.exists(str_to_dir(s=dist_ + "/" + files[i])))) or (m > self.duplication_time)) and (self.file != str_to_dir(s=(src_ + "/" + files[i])))):

                            
                            print("m = ", m, " . self.d_t = ", self.duplication_time)

                            d = Path(str_to_dir(s=src_ + "/" + files[i]))

                            d_ = Path(str_to_dir(s=dist_ + "/" + files[i]))


                            self.file_coping = str_to_dir(s=src_ + "/" + files[i])

                            d_.write_bytes(d.read_bytes())

                            self.file_coping = ""


                            self.single = False

                            if (max_dup_time < m):

                                max_dup_time = m

                            

                    except Exception as e:

                        print("Erreur : ", e)

                        semphore = True

                    
                    i += 1


                j += 1

            
            # print("fin de recherche . time = ", time.strftime("%Y/%m/%d %H:%M:%S"))

            if ((self.duplication_time != max_dup_time) and (not (self.single))):
                
                self.duplication_time = max_dup_time

                file = str_to_dir(s=cw + "time_max_of_duplication.txt")

                with open(file, "w", encoding="utf-8") as f_:

                    f_.write(str(self.duplication_time))


                file = str_to_dir(s=self.duplication_place + "time_max_of_duplication.txt")

                with open(file, "w", encoding="utf-8") as f_:

                    f_.write(str(self.duplication_time))

                print("fichier de temps copier avec succe .")






    

    def update_progress(self):

        run = True

        f_c = ""

        while (run):


            if (f_c != self.file_coping):

                if (self.file_coping == ""):

                    self.lab_3.setText(" 100 % . terminat-ed !")

                else:


                    self.lab_3.setText("file_coping : " + self.file_coping)

                    print("file_coping : ", self.file_coping + " . size = " + str(os.path.getsize(self.file_coping)) + " Byte " + " . time = ", time.strftime("%Y/%m/%d %H:%M:%S"))

                f_c = self.file_coping






if __name__ == "__main__":



    global cw

    cw = str_to_dir(s=os.getcwd() + "/")




    global i

    i = {}



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



    # إنشاء التطبيق

    app = QApplication(sys.argv)

    # إنشاء النافذة الرئيسية

    window = MainWindow()

    window.show()

    # تشغيل التطبيق

    sys.exit(app.exec_())
















