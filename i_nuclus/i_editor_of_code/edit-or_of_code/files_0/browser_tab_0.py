














list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            ["PyQtWebEngine"] ,
                            



]










import os



import sys

import subprocess




counter_0 = 0


while (counter_0 < len(list_of_liberary_to_install)):

    #os.system(f"pip install {list_of_liberary_to_install[counter_0][0]}")

    subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])


    counter_0 += 1



cwd = os.path.dirname(os.path.abspath(__file__))


from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTabWidget

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage

from PyQt5.QtCore import QUrl



import time

import traceback



import importlib


from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl


from PyQt5.QtWebEngineWidgets import QWebEngineScript


from PyQt5.QtWidgets import QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView



class CustomWebView(QWebEngineView):
    def __init__(self, browser_tabs, parent=None):
        super().__init__(parent)
        self.browser_tabs = browser_tabs  # نحتفظ بالمرجع الأصلي

    def contextMenuEvent(self, event):
        menu_data = self.page().contextMenuData()
        menu = QMenu(self)

        if menu_data.linkUrl().isValid():
            menu.addAction("فتح في تبويب جديد", lambda: self.open_link_in_new_tab(menu_data.linkUrl()))
            menu.addAction("نسخ الرابط", lambda: self.copy_link(menu_data.linkUrl()))

        menu.addSeparator()
        menu.addAction("تحديث", self.reload)

        menu.exec_(event.globalPos())

    def open_link_in_new_tab(self, url):
        self.browser_tabs.add_new_tab(url.toString())  # ✅ المرجع المباشر

    def copy_link(self, url):
        from PyQt5.QtWidgets import QApplication
        QApplication.clipboard().setText(url.toString())






class BrowserTabWithTabs(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # 1. إعداد التخزين الدائم للجلسات
        profile_storage_path = os.path.expanduser("~/.my_code_editor_browser_profile")
        self.profile = QWebEngineProfile("MyBrowserProfile", self)
        self.profile.setPersistentStoragePath(profile_storage_path)
        self.profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)

        # 2. أدوات التصفح العامة (زر رجوع، تقدم، إعادة تحميل، عنوان)
        self.url_bar = QLineEdit()
        self.back_button = QPushButton("←")
        self.forward_button = QPushButton("→")
        self.reload_button = QPushButton("⟳")
        self.go_button = QPushButton("Go")
        self.new_tab_button = QPushButton("+")

        # 3. نظام التبويبات
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.update_url_bar)

        self.new_tab_button.clicked.connect(self.add_new_tab)
        self.go_button.clicked.connect(self.navigate_to_url)
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.back_button.clicked.connect(self.go_back)
        self.forward_button.clicked.connect(self.go_forward)
        self.reload_button.clicked.connect(self.reload_page)

        # 4. التخطيط
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addWidget(self.forward_button)
        top_layout.addWidget(self.reload_button)
        top_layout.addWidget(self.url_bar)
        top_layout.addWidget(self.go_button)
        top_layout.addWidget(self.new_tab_button)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addLayout(top_layout)
        layout.addWidget(self.tabs)

        self.setLayout(layout)

        # 5. أول تبويبة
        self.add_new_tab("https://www.google.com")



    
    def create_browser_view(self, url):
        page = QWebEnginePage(self.profile, self)
    
        # 🌓 كود JavaScript للوضع الليلي
        dark_mode_script = """
            (function() {
                let css = `
                    html, body {
                        background-color: #121212 !important;
                        color: #e0e0e0 !important;
                    }
                    * {
                        background-color: transparent !important;
                        color: #e0e0e0 !important;
                        border-color: #444 !important;
                    }
                    a { color: #8ab4f8 !important; }
                    img, video { filter: brightness(0.9) contrast(1.1); }
                `;
                let style = document.createElement('style');
                style.type = 'text/css';
                style.appendChild(document.createTextNode(css));
                document.head.appendChild(style);
            })();
        """
    
        # 🧠 إنشاء كائن Script
        script = QWebEngineScript()
        script.setName("NightMode")
        script.setSourceCode(dark_mode_script)
        script.setInjectionPoint(QWebEngineScript.DocumentReady)
        script.setWorldId(QWebEngineScript.MainWorld)
        script.setRunsOnSubFrames(True)
    
        # ⬅️ إدراج السكربت في الصفحة
        page.profile().scripts().insert(script)
    
        # 🔍 إنشاء واجهة التصفح
        

        #browser = QWebEngineView()
        #browser.setPage(page)
        #browser.setUrl(QUrl(url))
        #browser.urlChanged.connect(self.update_url_bar)


        browser = CustomWebView(browser_tabs=self, parent=self) 

        browser.setPage(page)
        browser.setUrl(QUrl(url))
        browser.urlChanged.connect(self.update_url_bar)
    
        
        return browser
    


    def add_new_tab(self, url="https://www.google.com"):
        if not isinstance(url, str):
            url = "https://www.google.com"
        browser = self.create_browser_view(url)
        
        
        
        index = self.tabs.addTab(browser, "New Tab")
        self.tabs.setCurrentIndex(index)
    



    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

    def current_browser(self):
        return self.tabs.currentWidget()

    def navigate_to_url(self):
        browser = self.current_browser()
        url_text = self.url_bar.text().strip()
        if not url_text.startswith("http"):
            url_text = "https://" + url_text
        browser.setUrl(QUrl(url_text))

    def update_url_bar(self, qurl=None):
        browser = self.current_browser()
        if browser:
            self.url_bar.setText(browser.url().toString())

    def go_back(self):
        browser = self.current_browser()
        if browser:
            browser.back()

    def go_forward(self):
        browser = self.current_browser()
        if browser:
            browser.forward()

    def reload_page(self):
        browser = self.current_browser()
        if browser:
            browser.reload()






if __name__ == "__main__":
    
    
    #time.sleep(10)
    
    try:
        
        app = QApplication(sys.argv)
        window = BrowserTabWithTabs()
        window.resize(1200, 800)
        window.setWindowTitle("browser")
        window.show()
        sys.exit(app.exec_())
        
    except:
    
                
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        file = os.path.join(cwd, "file_of_error_0.txt")
        
        with open(file, "w") as f_:
        
            f_.write(str(error))
        
        print(f"Erreur : {str(error)}")
        
            


#time.sleep(100)











