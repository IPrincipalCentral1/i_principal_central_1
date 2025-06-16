










from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

import os

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class BrowserTab(QWidget):
    def __init__(self, url="https://www.google.com", parent=None):
        super().__init__(parent)

        # 1. المكونات
        
        
        #self.browser = QWebEngineView()
        
        
        # مسار تخزين الجلسة (ملف تعريف دائم)
        
        profile_storage_path = os.path.expanduser("~/.my_code_editor_browser_profile")
        
        # إنشاء بروفايل دائم
        profile = QWebEngineProfile("MyBrowserProfile", self)
        profile.setPersistentStoragePath(profile_storage_path)
        profile.setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        
        # ربط البروفايل بالصفحة والمتصفح
        page = QWebEnginePage(profile, self)
        self.browser = QWebEngineView()
        self.browser.setPage(page)
        
        
        
        
        self.url_bar = QLineEdit()
        self.back_button = QPushButton("←")
        self.forward_button = QPushButton("→")
        self.reload_button = QPushButton("⟳")
        self.go_button = QPushButton("Go")

        # 2. الأحداث
        self.back_button.clicked.connect(self.browser.back)
        self.forward_button.clicked.connect(self.browser.forward)
        self.reload_button.clicked.connect(self.browser.reload)
        self.go_button.clicked.connect(self.load_url_from_bar)
        self.url_bar.returnPressed.connect(self.load_url_from_bar)

        self.browser.urlChanged.connect(self.update_url_bar)

        # 3. تخطيط الأدوات العلوية
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addWidget(self.forward_button)
        top_layout.addWidget(self.reload_button)
        top_layout.addWidget(self.url_bar)
        top_layout.addWidget(self.go_button)

        # 4. التخطيط العام
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.browser)

        self.setLayout(main_layout)

        # 5. تحميل عنوان ابتدائي
        self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))

    def load_url_from_bar(self):
        url_text = self.url_bar.text().strip()
        if not url_text.startswith("http"):
            url_text = "https://" + url_text
        self.browser.setUrl(QUrl(url_text))

    def update_url_bar(self, qurl):
        self.url_bar.setText(qurl.toString())














