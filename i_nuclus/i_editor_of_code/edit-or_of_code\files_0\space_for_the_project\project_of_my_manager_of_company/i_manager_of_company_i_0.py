



















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
    
    from PyQt5.QtCore import Qt, QSize
    
    from PyQt5.QtGui import QPalette, QColor, QBrush, QPixmap, QIcon, QFont

    from PyQt5.QtWidgets import (

        QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
        QGridLayout, QScrollArea, QFrame, QSizePolicy
    
    )
    
    
    from PyQt5.QtWidgets import QLineEdit

    
    
    
    
    
    
    
    
    
    
    
    
    class i_information_i_0():
        
        '''
        
        button_of_ground_0 = "allways present"
        
        
        
        
        
        '''
        
        
        
        def __init__(self):
            
            
            pass
            
            
            
        
        
        
        def i_regulater_of_QPushButton_i_0(self):
            
            
            
            
            pass
            
            
            
            
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
            
            
            
            self.i_golden_number_0 = 1.6180339887498
            
            
            
            
            
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
            
            
            
            # the theme :
            
            
            self.themes = ["classic", "violet", "hacker", "light"]
            
            self.current_theme_index = 0
            
            self.apply_theme(self.themes[self.current_theme_index])
    
            
            
            
            self.font_size_title = 20
            
            self.font_size_description = 20
            
            self.font_size_button = 20
            
            self.button_size_0 = 120
            
            self.button_size = (int(self.button_size_0), int(self.button_size_0 // self.i_golden_number_0))
            
            
            
            
            self.search_font_family = "Arial"
            
            self.search_font_size = 24
            
            self.size_bar_of_search_0 = 800
            
            self.search_bar_size = (int(self.size_bar_of_search_0), int(self.button_size_0 // self.i_golden_number_0))

            
            
            
            
            
            
            self.update_background()

            
            
    
    
            # الواجهة الرئيسية
            central = QWidget()
            
            
            self.setCentralWidget(central)

            self.size_of_button_of_ground = [120, 0]

            self.size_of_button_of_ground[1] = int(self.size_of_button_of_ground[0] // self.i_golden_number_0)


            
            
            
                        
            
            # ScrollArea للقائمة (في الأعلى)
            
            self.scroll = QScrollArea()
            
            self.scroll.setWidgetResizable(True)
            
            self.scroll_content = QWidget()
            
            self.grid = QGridLayout(self.scroll_content)
            
            self.scroll.setWidget(self.scroll_content)
            
            
            # في البداية تكون فارغة
            
            self.scroll.hide()
            
            
            
            
            
            # الأزرار
            
            
            
            
            
            
            
            self.i_folder_i_1 = "i_folder_i_1"
            
            
            self.i_file_of_icon_i_0 = os.path.join(cwd, self.i_folder_i_1, "icon_of_index_i_0.png")
            
            
            self.i_button_of_index_i_0 = self.i_creation_of_button_of_ground_i_0(
                            i_text_of_button_i_0="", 
                            
                            i_image_i_0=self.i_file_of_icon_i_0, 
                            
                            i_size_of_button_i_0=self.size_of_button_of_ground,
                            
                            i_callback_i_0=self.show_grid
                            
                            )
            
            

            
            self.i_file_of_icon_i_1 = os.path.join(cwd, self.i_folder_i_1, "i_icon_of_work_i_0.png")
            
                        
            self.i_button_of_index_i_1 = self.i_creation_of_button_of_ground_i_0(
                            i_text_of_button_i_0="", 
                            
                            i_image_i_0=self.i_file_of_icon_i_1, 
                            
                            i_size_of_button_i_0=self.size_of_button_of_ground,
                            
                            i_callback_i_0=self.i_function_of_i_button_of_index_i_1
                            
                            )
            
            
            
            self.i_file_of_icon_i_2 = os.path.join(cwd, self.i_folder_i_1, "i_icon_of_background_i_0.png")
            
                        
            self.i_button_of_index_i_2 = self.i_creation_of_button_of_ground_i_0(
                            i_text_of_button_i_0="", 
                            
                            i_image_i_0=self.i_file_of_icon_i_2, 
                            
                            i_size_of_button_i_0=self.size_of_button_of_ground,
                            
                            i_callback_i_0=self.toggle_background
                            
                            )
            
            
                        
            self.i_file_of_icon_i_3 = os.path.join(cwd, self.i_folder_i_1, "i_icon_of_theme_i_0.png")
            
                        
            self.i_button_of_index_i_3 = self.i_creation_of_button_of_ground_i_0(
                            i_text_of_button_i_0="", 
                            
                            i_image_i_0=self.i_file_of_icon_i_3, 
                            
                            i_size_of_button_i_0=self.size_of_button_of_ground,
                            
                            i_callback_i_0=self.cycle_theme
                            
                            )
            
            
            
            
            
            
            # شريط البحث
            self.search_bar = QLineEdit()
            
            self.search_bar.setPlaceholderText("i search here i")
            
            # التحكم في الخط
            
            self.search_bar.setFont(QFont(self.search_font_family, self.search_font_size))
            
            # التحكم في الحجم
            
            #self.search_bar.setFixedSize(*self.search_bar_size)
            
            self.search_bar.resize(*self.search_bar_size)  # يعطي حجم مبدئي
            
                        
            self.search_bar.setMinimumWidth(0)
            
            self.search_bar.setMinimumSize(0, 0)           # يخليه يقدر يصغر
            
            self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            
            
                        

            
            
              
            # ربط الضغط على Enter بالدالة search
            
            self.search_bar.returnPressed.connect(self.filter_grid)
            
            
            
            
                        
            # Layout أفقي للأزرار
            h_layout = QHBoxLayout()
            h_layout.addStretch()
            h_layout.addWidget(self.i_button_of_index_i_0)
            h_layout.addWidget(self.i_button_of_index_i_1)
            h_layout.addWidget(self.i_button_of_index_i_2)
            h_layout.addWidget(self.i_button_of_index_i_3)
            h_layout.addStretch()
            
            # Layout رئيسي: القائمة فوق + Stretch + الأزرار تحت
            v_layout = QVBoxLayout(central)
            
            v_layout.addWidget(self.search_bar)   
            
            v_layout.addWidget(self.scroll)   # القائمة
            v_layout.addStretch()
            v_layout.addLayout(h_layout)      # الأزرار
            
            
        
        
        
        
        
        
        def filter_grid(self):
            
            text = self.search_bar.text()
            

            #if not hasattr(self, "items"):
                #return  # إذا لم يتم إنشاء العناصر بعد

            if text == "":
                filtered = self.items
            else:
                
                filtered = [
                    (title, desc, btn) 
                    for title, desc, btn in self.items 
                    if ((text in title) or (text in desc))
                ]
        
        
            print(f"i_hello_i_1 . len(filtered) = {len(filtered)} . len(self.items) = {len(self.items)} .")
            
        
            self.display_items(items=filtered)
        
            
            
        def i_clear_all_element_i_0(self):

            # إزالة أي عناصر قديمة
            
            try:
                
                
                while self.grid.count():
                    
                    item = self.grid.takeAt(0)
                    
                    # إذا كان العنصر Widget (مثلاً بطاقة)
                    widget = item.widget()
                    if widget is not None:
                        widget.setParent(None)
                    
                    # إذا كان العنصر Layout (nested)
                    child_layout = item.layout()
                    if child_layout is not None:
                        self.i_clear_all_element_i_0(child_layout)
                
                
                
                
                

            except:
                
                
                traceback.print_exc()
                
                error = traceback.format_exc()
                
                semaphore = True
                
                #print(f"Erreur : {str(error)}")
                
                
                
                
                
            
        

        def show_grid(self):
        
        
            
            
            
            
            self.items = [
                ("العنوان 1", "هذا وصف قصير للعنصر الأول", "زر 1"),
                ("العنوان 2", "الوصف الثاني موجود هنا", "زر 2"),
                ("العنوان 3", "الوصف الثالث موجود هنا", "زر 3"),
                ("العنوان 4", "الوصف الرابع موجود هنا", "زر 4"),

            ]
            
            i_counter_i_0 = 0
            
            while (i_counter_i_0 < 100):
                
                self.items.append((f"title {i_counter_i_0} ", f"description number {i_counter_i_0} ", f"button {i_counter_i_0} "))
                
                i_counter_i_0 += 1
                
                
                

            
            
            self.display_items(items=self.items)
            
            
            
            
            
        
        def display_items(self, items):
            
            
            
            self.i_clear_all_element_i_0()
            
            for index, (title, desc, btn_text) in enumerate(items):
                
                card = QFrame()
                
                card.setFrameShape(QFrame.StyledPanel)
                
                card_layout = QVBoxLayout(card)
                
                
                title_label = QLabel(f"<b>{title}</b>")
                
                title_label.setFont(QFont("Arial", self.font_size_title, QFont.Bold))
                
                
                desc_label = QLabel(desc)
                
                desc_label.setFont(QFont("Arial", self.font_size_description))
                
                desc_label.setWordWrap(True)
                
                
                btn = QPushButton(btn_text)
                
                btn.setFixedSize(*self.button_size)
                btn.setFont(QFont("Arial", self.font_size_button))
            
                
                btn.clicked.connect(lambda _, t=title: print(f"تم الضغط على: {t}"))
            
                card_layout.addWidget(title_label)
                card_layout.addWidget(desc_label)
                card_layout.addWidget(btn)
            
                row = index // 2
                col = index % 2
                
                self.grid.addWidget(card, row, col)
            
            
            self.scroll.show()
        

        def update_background(self):
            
            if (self.background_on == True):
                
                pixmap = QPixmap(self.i_file_of_image_i_0)
                scaled = pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
                
                palette = QPalette()
                palette.setBrush(QPalette.Window, QBrush(scaled))
                self.setPalette(palette)
                
                
        
        def resizeEvent(self, event):
            self.update_background()
            super().resizeEvent(event)
    
            
            
            
                
        def i_function_of_i_button_of_index_i_1(self):
            
            
            
            self.i_clear_all_element_i_0()
            
            print(f"i_hello_i_0 . button 'i_function_of_i_button_of_index_i_1' is click-ed .")
            
            
            
            
        
    
    
        def toggle_background(self):
            """تشغيل/إيقاف الخلفية"""
            if (self.background_on == True):
                
                
                
                # إزالة الخلفية
                
                
                self.background_on = False
                                
                
                
                palette = QPalette()
                
                self.setPalette(palette)
                
                
                
                
            else:
                
                # إرجاع الخلفية
                
                
                self.background_on = True
                
                self.update_background()
                
            
            
            
        def i_creation_of_button_of_ground_i_0(self, i_text_of_button_i_0, i_image_i_0, i_size_of_button_i_0, i_callback_i_0):
            
            
            
            
            
            i_button_i_0 = QPushButton(i_text_of_button_i_0, self)
            
            i_button_i_0.clicked.connect(i_callback_i_0)
            
            
            #i_button_i_0.setFixedSize(i_size_of_button_i_0[0], i_size_of_button_i_0[1])
            
            i_button_i_0.setIcon(QIcon(i_image_i_0))
            
            i_button_i_0.setIconSize(QSize(i_size_of_button_i_0[0], i_size_of_button_i_0[1]))
            
                        
            
            #i_button_i_0.setMinimumWidth(0)
            
            #i_button_i_0.setMinimumSize(0, 0)
            
            
            
            i_button_i_0.resize(i_size_of_button_i_0[0], i_size_of_button_i_0[1])
            
            i_button_i_0.setMinimumSize(0, 0)
            
            i_button_i_0.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            
            
            
            
            
            return i_button_i_0
            
            
            
            
        
    
        
        def apply_theme(self, theme_name):
            
            
            # أولاً باليت أساسي
            
            palette = QPalette()
        
            if theme_name == "classic":
                palette.setColor(QPalette.Window, Qt.lightGray)
                palette.setColor(QPalette.WindowText, Qt.black)
                self.setPalette(palette)
                self.setStyleSheet("")
        
            elif theme_name == "violet":
                palette.setColor(QPalette.Window, QColor("#8A2BE2"))  # بنفسجي غامق
                palette.setColor(QPalette.WindowText, Qt.white)
                self.setPalette(palette)
                self.setStyleSheet("""
                    QPushButton {
                        background-color: #6A0DAD; 
                        color: white; 
                        border-radius: 8px; 
                        padding: 6px 12px;
                    }
                    QPushButton:hover {
                        background-color: #7B1FA2;
                    }
                """)
        
            elif theme_name == "hacker":
                palette.setColor(QPalette.Window, Qt.black)
                palette.setColor(QPalette.WindowText, Qt.green)
                self.setPalette(palette)
                self.setStyleSheet("""
                    QLabel { color: #00FF00; }
                    QPushButton {
                        background-color: #111; 
                        color: #00FF00; 
                        border: 1px solid #00FF00;
                    }
                    QPushButton:hover {
                        background-color: #222;
                    }
                """)
        
            elif theme_name == "light":
                palette.setColor(QPalette.Window, Qt.white)
                palette.setColor(QPalette.WindowText, Qt.black)
                self.setPalette(palette)
                self.setStyleSheet("""
                    QPushButton {
                        background-color: #f0f0f0; 
                        color: black; 
                        border-radius: 5px;
                        padding: 5px 10px;
                    }
                    QPushButton:hover {
                        background-color: #ddd;
                    }
                """)
            else:
                # إذا ما كان الثيم معروف
                self.setPalette(self.style().standardPalette())
                self.setStyleSheet("")
        
        
        
                
        def cycle_theme(self):
            
            self.current_theme_index = (self.current_theme_index + 1) % len(self.themes)
            
            self.apply_theme(self.themes[self.current_theme_index])
            
            
            
        
    
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
    
    
    
    
    
    











