















from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTabWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl
import os

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
        browser = QWebEngineView()
        browser.setPage(page)
        browser.setUrl(QUrl(url))
        browser.urlChanged.connect(self.update_url_bar)
        return browser

    #def add_new_tab(self, url: str = "https://www.google.com"):
        #browser = self.create_browser_view(url)
        #index = self.tabs.addTab(browser, "New Tab")
        #self.tabs.setCurrentIndex(index)


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





















