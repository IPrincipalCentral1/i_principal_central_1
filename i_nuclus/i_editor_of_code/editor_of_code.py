








color_of_mode_of_night = ["#A0A0A0", "#FFFFFF"]


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------




# section of ai 





import re

from PyQt5.QtWidgets import QPlainTextEdit, QCompleter

from PyQt5.QtGui import QFont

from PyQt5.QtCore import Qt

from PyQt5.QtCore import QTimer

from PyQt5.QtGui import QTextCursor


from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                             QPlainTextEdit, QTabWidget, QAction, QFileDialog)
from PyQt5.QtGui import QPainter, QColor, QFont, QTextFormat

from PyQt5.QtWidgets import QTextEdit

import sys

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPlainTextEdit, QFileSystemModel,
    QTreeView, QSplitter, QWidget, QVBoxLayout
)

from PyQt5.QtCore import Qt, QDir




from PyQt5.QtCore import Qt, QRect, QSize

import sys


import os


from PyQt5.QtGui import QIcon



from PyQt5.QtWidgets import QMessageBox




from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp





from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PyQt5.QtCore import QRegExp

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent, keywords_with_colors):
        super().__init__(parent)

        self.rules = []

        # 🎨 بناء قواعد التلوين من dict
        for word, color in keywords_with_colors.items():
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(color))
            fmt.setFontWeight(QFont.Bold)
            pattern = QRegExp(r'\b' + word + r'\b')
            self.rules.append((pattern, fmt))

        # 🟠 التعليقات
        self.comment_format = QTextCharFormat()
        self.comment_format.setForeground(QColor("#6a9955"))
        self.comment_format.setFontItalic(True)
        self.comment_pattern = QRegExp(r"#.*$")


        self.string_format_0 = QTextCharFormat()
        self.string_format_0.setForeground(QColor("#f08d49"))
        self.string_format_0.setFontItalic(True)
        self.string_pattern_0 = QRegExp(r'"[^"\\]*(\\.[^"\\]*)*"')



        self.string_format_1 = QTextCharFormat()
        self.string_format_1.setForeground(QColor("#f08d49"))
        self.string_format_1.setFontItalic(True)
        self.string_pattern_1 = QRegExp(r"'[^'\\]*(\\.[^'\\]*)*'")


    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)

        index = self.comment_pattern.indexIn(text)

        while index >= 0:
            length = self.comment_pattern.matchedLength()
            self.setFormat(index, length, self.comment_format)
            index = self.comment_pattern.indexIn(text, index + length)


        index = self.string_pattern_0.indexIn(text)

        while index >= 0:
            length = self.string_pattern_0.matchedLength()
            self.setFormat(index, length, self.string_format_0)
            index = self.string_pattern_0.indexIn(text, index + length)



        index = self.string_pattern_1.indexIn(text)

        while index >= 0:
            length = self.string_pattern_1.matchedLength()
            self.setFormat(index, length, self.string_format_1)
            index = self.string_pattern_1.indexIn(text, index + length)




# -- كلاس LineNumberArea (كما قبل) --
class LineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.lineNumberAreaWidth(), 0)

    def lineNumberAreaWidth(self):
        digits = len(str(self.editor.blockCount()))
        return 10 + self.fontMetrics().width('9') * digits

    def paintEvent(self, event):
        self.editor.lineNumberAreaPaintEvent(event)




# -- محرر النصوص مع أرقام الأسطر ووضع الليل --
class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()

        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setNightModeStyle()




        self.completer = QCompleter([], self)
        self.completer.setWidget(self)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.activated.connect(self.insert_completion)
        
        
        # إعداد الخط والخلفية
        self.setFont(QFont("Courier New", 12))
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setNightModeStyle()

        
        self.completer.highlighted.connect(self.print_selected_suggestion)


        word_colors = {
            'def': '#7ec699',
            'class': '#f08d49',
            'import': '#61afef',
            'print': '#c678dd',
            'for': '#d19a66',
            'while': '#d19a66',
            'return': '#7ec699',
            'if': '#7ec699',
            'else': '#7ec699',
            'pass' : '#7ec699'
        }



        self.highlighter = PythonHighlighter(self.document(), word_colors)


        self.suggestion_visible = False  # 💡 تتبع الظهور اليدوي للاقتراحات

        self.setUndoRedoEnabled(True)


    def print_selected_suggestion(self, text):

        # print("Selected suggestion:", text)

        self.suggestion_visible = True
        


    def setNightModeStyle(self):
        self.setStyleSheet("QPlainTextEdit { background-color: #1e1e1e; color: #d4d4d4; selection-background-color: #264f78; }")
        self.setFont(QFont("Courier New", 12))

    def lineNumberAreaWidth(self):
        digits = len(str(max(1, self.blockCount())))
        space = 10 + self.fontMetrics().width('9') * digits
        return space

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), QColor("#2d2d2d"))

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(QColor("#888888"))
                painter.drawText(0, top, self.lineNumberArea.width() - 5, self.fontMetrics().height(),
                                 Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            blockNumber += 1

    def highlightCurrentLine(self):
        extraSelections = []
        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            selection.format.setBackground(QColor("#333344"))
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)
        self.setExtraSelections(extraSelections)



    def print_current_word(self):
        cursor = self.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)
        word = cursor.selectedText()
        # print("Current word under cursor:", word)


    def keyPressEvent(self, event):
        # ✅ Ctrl + Space = إظهار/إخفاء نافذة الاقتراحات يدويًا
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Space:
            if self.suggestion_visible:
                self.completer.popup().hide()
                self.suggestion_visible = False
            else:
                prefix = self.textUnderCursor()
                self.update_completer_words()  # ← حدث قائمة الكلمات

                self.completer.setCompletionPrefix(prefix)
                self.completer.popup().setCurrentIndex(
                    self.completer.completionModel().index(0, 0)
                )

                cr = self.cursorRect()
                cr.setWidth(
                    self.completer.popup().sizeHintForColumn(0)
                    + self.completer.popup().verticalScrollBar().sizeHint().width()
                )
                self.completer.complete(cr)
                self.suggestion_visible = True
            return  # منع تنفيذ أي شيء آخر

        # 👇 تابع الإكمال التلقائي إذا ظهرت النافذة
        if self.completer.popup().isVisible():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return):
                completion = self.completer.currentCompletion()
                if completion:
                    self.insert_completion(completion)
                return
            elif event.key() == Qt.Key_Escape:
                self.completer.popup().hide()
                self.suggestion_visible = False
                return
            elif event.key() in (Qt.Key_Up, Qt.Key_Down):
                QApplication.sendEvent(self.completer.popup(), event)
                return

        # السلوك العادي
        super().keyPressEvent(event)



    def insert_completion(self, completion):
        tc = self.textCursor()
        extra = len(self.completer.completionPrefix())
        if extra > 0:
            tc.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, extra)
        tc.insertText(completion)
        self.setTextCursor(tc)


    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(tc.WordUnderCursor)
        return tc.selectedText()

    def update_completer_words(self):
        text = self.toPlainText()
        words = list(set(re.findall(r'\b[a-zA-Z_]\w{2,}\b', text)))  # كلمات بطول ≥3 فقط
        words.sort()
        self.completer.model().setStringList(words)




import os
import subprocess
from PyQt5.QtWidgets import (
    QMainWindow, QFileSystemModel, QTreeView, QTabWidget, QWidget,
    QVBoxLayout, QSplitter, QAction, QFileDialog, QMessageBox, QMenu
)
from PyQt5.QtCore import QDir, Qt
from PyQt5.QtGui import QIcon

import json



import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QFileDialog, QLabel, QMainWindow
from PyQt5.QtCore import pyqtSignal

class MountPointExplorer(QWidget):
    # إنشاء إشارة (Signal) تبعث المسار المختار كـ str
    folderSelected = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mount Points Explorer")
        self.resize(400, 300)
        
        self.layout = QVBoxLayout()
        self.label = QLabel("اختر نقطة التثبيت لفتح المجلد:")
        self.layout.addWidget(self.label)
        
        self.listWidget = QListWidget()
        self.layout.addWidget(self.listWidget)
        
        self.openButton = QPushButton("فتح المجلد المحدد")
        self.openButton.clicked.connect(self.open_selected_mount)
        self.layout.addWidget(self.openButton)
        
        self.setLayout(self.layout)
        
        self.load_mount_points()
    
    def load_mount_points(self):
        partitions = psutil.disk_partitions(all=False)
        self.listWidget.clear()
        for p in partitions:
            self.listWidget.addItem(f"{p.device} -> {p.mountpoint}")
    
    def open_selected_mount(self):
        selected_items = self.listWidget.selectedItems()
        if not selected_items:
            return
        
        item_text = selected_items[0].text()
        mount_path = item_text.split("->")[-1].strip()
        
        directory = QFileDialog.getExistingDirectory(self, "اختر مجلد داخل نقطة التثبيت", mount_path)
        if directory:
            # أرسل المسار المختار عبر الإشارة
            self.folderSelected.emit(directory)
            self.close()




from PyQt5.QtWidgets import QMainWindow, QTreeView, QFileSystemModel, QApplication, QTabWidget, QWidget, QVBoxLayout, QMenu
from PyQt5.QtCore import QDir, QPoint
import sys
import os

class FileExplorer(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())
        self.setModel(self.model)
        self.setRootIndex(self.model.index(QDir.homePath()))
    
    def expand_to_path(self, file_path):
        # نحدد مجلد الملف
        folder = os.path.dirname(file_path)
        index = self.model.index(folder)
        if not index.isValid():
            return
        
        self.setRootIndex(index)
        
        # الآن نبحث عن الملف داخل المجلد
        # ونجعل التحديد عليه إذا موجود
        file_index = self.model.index(file_path)
        if file_index.isValid():
            self.selectionModel().select(file_index, 
                self.selectionModel().ClearAndSelect)
            self.scrollTo(file_index)

class EditorTab(QWidget):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        # محتوى التبويبة يمكن يكون محرر نصوص أو غيره
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QTreeView())  # مؤقت فقط
    
    def get_file_path(self):
        return self.file_path



import os
import json
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileSystemModel, QTreeView,
    QTabWidget, QWidget, QVBoxLayout, QMessageBox,
    QAction, QMenu, QFileDialog
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QDir, QPoint




from PyQt5.QtWidgets import QMainWindow, QTreeView, QFileSystemModel, QApplication, QTabWidget, QWidget, QVBoxLayout, QMenu, QDockWidget

from PyQt5.QtCore import QDir, QPoint, Qt



import shutil

from PyQt5.QtWidgets import QMenu, QAction


from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence



from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPlainTextEdit, QWidget,
    QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QShortcut
)
from PyQt5.QtGui import QKeySequence, QTextCursor, QTextCharFormat, QColor
from PyQt5.QtCore import Qt
import sys

from PyQt5.QtGui import QTextDocument


class FindWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        self.setFixedHeight(40)

        self.label = QLabel("Find:")
        self.line_edit = QLineEdit()
        self.next_btn = QPushButton("Next")
        self.prev_btn = QPushButton("Prev")
        self.close_btn = QPushButton("X")

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.prev_btn)
        layout.addWidget(self.next_btn)
        layout.addWidget(self.close_btn)
        self.setLayout(layout)

        self.next_btn.clicked.connect(self.find_next)
        self.prev_btn.clicked.connect(self.find_prev)
        self.close_btn.clicked.connect(self.hide)
        self.line_edit.textChanged.connect(self.highlight_all)

        self.editor = None
        self.last_search = ""
        self.current_pos = 0


        self.search_input = QLineEdit()


    def set_editor(self, editor):
        self.editor = editor

    # def find_next(self):
    #     if not self.editor:
    #         return
    #     text = self.line_edit.text()
    #     if not text:
    #         return
    #     print("Editor is:", self.editor)

    #     document = self.editor.document()
    #     cursor = self.editor.textCursor()
    #     start_pos = cursor.position() if self.last_search == text else 0

    #     found_cursor = document.find(text, start_pos)
    #     if not found_cursor.isNull():
    #         self.editor.setTextCursor(found_cursor)
    #         self.current_pos = found_cursor.position()
    #     else:
    #         # بحث من البداية لو ما لقى بعد الموضع الحالي
    #         found_cursor = document.find(text, 0)
    #         if not found_cursor.isNull():
    #             self.editor.setTextCursor(found_cursor)
    #             self.current_pos = found_cursor.position()
    #     self.last_search = text

    # def find_prev(self):
    #     if not self.editor:
    #         return
    #     text = self.line_edit.text()
    #     if not text:
    #         return


    #     document = self.editor.document()
    #     cursor = self.editor.textCursor()
    #     pos = cursor.position() - len(text) - 1 if self.last_search == text else document.characterCount()

    #     found_cursor = document.find(text, pos, QTextDocument.FindBackward)
    #     if not found_cursor.isNull():
    #         self.editor.setTextCursor(found_cursor)
    #         self.current_pos = found_cursor.position()
    #     else:
    #         # بحث من النهاية لو ما لقى قبل الموضع الحالي
    #         found_cursor = document.find(text, document.characterCount(), QTextDocument.FindBackward)
    #         if not found_cursor.isNull():
    #             self.editor.setTextCursor(found_cursor)
    #             self.current_pos = found_cursor.position()
    #     self.last_search = text



    def find_next(self):
        text = self.line_edit.text()
        if not text:
            return

        document = self.editor.document()
        cursor = self.editor.textCursor()
        found_cursor = document.find(text, cursor)

        if not found_cursor.isNull():
            self.editor.setTextCursor(found_cursor)
            self.editor.centerCursor()
        else:
            QMessageBox.information(self, "Not Found", f"'{text}' not found.")

    def find_prev(self):
        text = self.line_edit.text()
        if not text:
            return

        document = self.editor.document()
        cursor = self.editor.textCursor()
        found_cursor = document.find(text, cursor, QTextDocument.FindBackward)

        if not found_cursor.isNull():
            self.editor.setTextCursor(found_cursor)
            self.editor.centerCursor()
        else:
            QMessageBox.information(self, "Not Found", f"'{text}' not found.")



    def highlight_all(self):
        # خيار إضافي: تمييز كل النصوص المطابقة
        # يمكن إضافته لاحقاً حسب الحاجة
        pass






class ReplaceWidget(QWidget):
    def __init__(self, editor, parent=None):
        super().__init__(parent)
        self.editor = editor

        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search for...")
        self.replace_input = QLineEdit()
        self.replace_input.setPlaceholderText("Replace with...")

        self.replace_button = QPushButton("Replace All")
        self.replace_button.clicked.connect(self.replace_all)

        layout.addWidget(QLabel("Search:"))
        layout.addWidget(self.search_input)
        layout.addWidget(QLabel("Replace with:"))
        layout.addWidget(self.replace_input)
        layout.addWidget(self.replace_button)

        self.setLayout(layout)

    def replace_all(self):
        search_text = self.search_input.text()
        replace_text = self.replace_input.text()

        if not search_text:
            QMessageBox.warning(self, "Warning", "Search term is empty.")
            return

        full_text = self.editor.toPlainText()
        new_text = full_text.replace(search_text, replace_text)

        if full_text == new_text:
            QMessageBox.information(self, "Info", "No matches found.")
        else:
            self.editor.setPlainText(new_text)
            QMessageBox.information(self, "Success", f"All '{search_text}' replaced with '{replace_text}'.")





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("edit-or of code")
        # أيقونة حسب مسارك
        # self.setWindowIcon(QIcon(os.path.join(os.getcwd(), "edit-or_of_code", "icon", "icon_0.png")))

        # 1. نموذج تصفح الملفات
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.homePath())

        self.showMaximized()

        # 2. عرض الشجرة
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.homePath()))
        self.tree.setColumnWidth(0, 400)

        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.tree.customContextMenuRequested.connect(self.show_explorer_context_menu)
        
        self.tree.clicked.connect(self.open_file_from_tree)

        # 3. التبويبات
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab_by_index)
        self.tabs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabs.customContextMenuRequested.connect(self.show_tab_context_menu)

        self.tab_file_paths = {}  # لتخزين مسارات الملفات حسب التبويبة

        self.new_tab()

        # 4. التقسيم
        from PyQt5.QtWidgets import QSplitter
        splitter = QSplitter()
        splitter.addWidget(self.tree)
        splitter.addWidget(self.tabs)
        splitter.setStretchFactor(1, 1)

        # 5. الحاوية
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(splitter)
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 6. القائمة
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        file_menu.addAction(self.create_action("open root", "Ctrl+R", self.open_root_0))
        file_menu.addAction(self.create_action("open file", "Ctrl+O", self.open_file))
        file_menu.addAction(self.create_action("save file", "Ctrl+S", self.save_file))
        file_menu.addAction(self.create_action("new tab", "Ctrl+T", self.new_tab))
        file_menu.addAction(self.create_action("close current tab", "Ctrl+W", self.close_current_tab))


        # 🎯 اختصارات التراجع والإعادة
        
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.trigger_undo)

        redo_shortcut = QShortcut(QKeySequence("Ctrl+Y"), self)
        redo_shortcut.activated.connect(self.trigger_redo)

        replace_shortcut = QShortcut(QKeySequence("Ctrl+H"), self)
        
        replace_shortcut.activated.connect(self.show_replace_widget)


        edit_menu = menu.addMenu("edit")
        edit_menu.addAction(self.create_action("Undo", "Ctrl+Z", self.trigger_undo))
        edit_menu.addAction(self.create_action("Redo", "Ctrl+Y", self.trigger_redo))


        # استرجاع الملفات المفتوحة سابقًا
        opened_files_path = "opened_files.json"
        if os.path.exists(opened_files_path):
            try:
                with open(opened_files_path, "r", encoding="utf-8") as f:
                    paths = json.load(f)
                for path in paths:
                    if os.path.exists(path):
                        with open(path, "r", encoding="utf-8") as file:
                            editor = CodeEditor()
                            editor.setPlainText(file.read())
                            editor.file_path = path
                            index = self.tabs.addTab(editor, os.path.basename(path))
                if self.tabs.count() > 0:
                    self.tabs.setCurrentIndex(0)
            except Exception as e:
                print("فشل تحميل الملفات المفتوحة:", e)


        # استرجاع آخر root
        path_file = os.path.join(os.getcwd(), "path_of_root.txt")
        if os.path.exists(path_file):
            with open(path_file, "r") as f:
                self.path_of_root = f.read()
        else:
            self.path_of_root = QDir.homePath()



        self.model.setRootPath(self.path_of_root)
        self.tree.setRootIndex(self.model.index(self.path_of_root))


        try:

            self.expand_tree_to_file(file_path=os.path.join(os.getcwd(), "editor_of_code.py"))

        except:

            semaphore = True





        self.clipboard_action = None  # "copy" or "cut"
        
        self.clipboard_path = None


        # ⏲️ مؤقت التحديث كل 5 ثواني
        self.refresh_timer = QTimer(self)
        self.refresh_timer.timeout.connect(self.refresh_tree_view)
        self.refresh_timer.start(5000)  # 5000 ميلي ثانية = 5 ثواني


        self.find_widget = FindWidget(self)
        self.find_widget.set_editor(self.current_editor())
        self.find_widget.hide()

        # ربط Ctrl+F لفتح نافذة البحث
        self.find_shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.find_shortcut.activated.connect(self.toggle_find)



    def show_replace_widget(self):
        editor = self.current_editor()  # تأكد أن لديك هذه الدالة
        if editor:
            self.replace_widget = ReplaceWidget(editor)
            self.replace_widget.setWindowTitle("Replace in File")
            self.replace_widget.setFixedSize(300, 200)
            self.replace_widget.show()




    def toggle_find(self):

        self.find_widget.set_editor(self.current_editor())

        self.find_widget.hide()

        if self.find_widget.isVisible():
            self.find_widget.hide()
        else:
            self.find_widget.show()
            self.find_widget.line_edit.setFocus()


    def trigger_undo(self):

        print("i_hello .")
        editor = self.current_editor()
        if editor:
            editor.undo()

    def trigger_redo(self):
        
        print("i_hello .")
        editor = self.current_editor()
        if editor:
            editor.redo()



    def refresh_tree_view(self):
        current_index = self.tree.currentIndex()
        current_path = self.model.filePath(current_index) if current_index.isValid() else None

        self.model.setRootPath("")  # Trick to force refresh
        self.model.setRootPath(self.path_of_root)
        self.tree.setRootIndex(self.model.index(self.path_of_root))

        # إعادة تحديد العنصر السابق إن أمكن
        if current_path and os.path.exists(current_path):
            index = self.model.index(current_path)
            if index.isValid():
                self.tree.setCurrentIndex(index)

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "تأكيد الإغلاق",
            "هل أنت متأكد أنك تريد إغلاق المحرر؟",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
            
            with open(os.path.join(os.getcwd(), "path_of_root.txt"), "w") as f:

                f.write(self.path_of_root)




            # حفظ الملفات المفتوحة

            open_files = []

            for i in range(self.tabs.count()):

                editor = self.tabs.widget(i)

                if hasattr(editor, "file_path") and editor.file_path:

                    open_files.append(editor.file_path)

            with open("opened_files.json", "w", encoding="utf-8") as f:

                json.dump(open_files, f, ensure_ascii=False, indent=2)



        else:
            event.ignore()

    def create_action(self, text, shortcut, slot):
        action = QAction(text, self)
        action.setShortcut(shortcut)
        action.triggered.connect(slot)
        return action

    def new_tab(self):
        editor = CodeEditor()
        editor.setUndoRedoEnabled(True)  # تأكد من تفعيل undo/redo
        QShortcut(QKeySequence("Ctrl+Z"), editor).activated.connect(editor.undo)
        QShortcut(QKeySequence("Ctrl+Y"), editor).activated.connect(editor.redo)
        
        editor.file_path = None
        index = self.tabs.addTab(editor, "new tab")
        self.tabs.setCurrentIndex(index)

    def close_tab_by_index(self, index):
        self.tabs.removeTab(index)
        if self.tabs.count() == 0:
            self.new_tab()

    def close_current_tab(self):
        index = self.tabs.currentIndex()
        if index != -1:
            self.tabs.removeTab(index)
            if self.tabs.count() == 0:
                self.new_tab()

    def current_editor(self):
        return self.tabs.currentWidget()

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "open file", "", "All Files (*)")
        if path:
            self.open_file_in_tab(path)

    def open_file_in_tab(self, file_path):
        # إذا الملف مفتوح بالفعل نذهب إليه
        for i in range(self.tabs.count()):
            editor = self.tabs.widget(i)
            if hasattr(editor, "file_path") and editor.file_path == file_path:
                self.tabs.setCurrentIndex(i)
                return

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            editor = CodeEditor()
            editor.setPlainText(text)
            editor.file_path = file_path
            index = self.tabs.addTab(editor, os.path.basename(file_path))
            self.tabs.setCurrentIndex(index)
            self.tab_file_paths[index] = file_path
        except Exception as e:
            QMessageBox.warning(self, "خطأ", f"فشل فتح الملف:\n{e}")

    def save_file(self):
        editor = self.current_editor()
        if editor:
            if hasattr(editor, "file_path") and editor.file_path:
                try:
                    with open(editor.file_path, 'w', encoding='utf-8') as f:
                        f.write(editor.toPlainText())
                    self.tabs.setTabText(self.tabs.currentIndex(), os.path.basename(editor.file_path))
                except Exception as e:
                    QMessageBox.warning(self, "خطأ", f"فشل حفظ الملف:\n{e}")
            else:
                path, _ = QFileDialog.getSaveFileName(self, "save file", "", "Text Files (*.txt);;All Files (*)")
                if path:
                    try:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.write(editor.toPlainText())
                        editor.file_path = path
                        self.tabs.setTabText(self.tabs.currentIndex(), os.path.basename(path))
                    except Exception as e:
                        QMessageBox.warning(self, "خطأ", f"فشل حفظ الملف:\n{e}")

    def open_file_from_tree(self, index):
        file_path = self.model.filePath(index)
        if QDir(file_path).exists():
            # إذا هو مجلد لا نفعل شيء
            return
        self.open_file_in_tab(file_path)

    # def show_explorer_context_menu(self, position):


    def show_explorer_context_menu(self, position):



        # if not os.path.exists(file_path):
        #     return  # لا يوجد مسار حقيقي

        # تحقق مما إذا كانت نقرة على عمود فارغ مثلاً، تجاهلها
        if self.tree.columnAt(position.x()) != 0:
            return




        index = self.tree.indexAt(position)
        if not index.isValid():
            return

        file_path = self.model.filePath(index)


        is_dir = QDir(file_path).exists() and os.path.isdir(file_path)
        
        menu = QMenu()


        terminal_action = QAction("open terminal from here", self)
        
        
        


        # # index = self.tree.indexAt(position)
        # if not index.isValid():
        #     return

        # file_path = self.model.filePath(index)


        # menu = QMenu()

        copy_action = QAction("📋 Copy", self)
        cut_action = QAction("✂️ Cut", self)
        paste_action = QAction("📎 Paste", self)
        delete_action = QAction("❌ Delete", self)

        
        terminal_action.triggered.connect(lambda: self.open_terminal_at(file_path))
        
        copy_action.triggered.connect(lambda: self.copy_item(file_path))
        cut_action.triggered.connect(lambda: self.cut_item(file_path))
        paste_action.triggered.connect(lambda: self.paste_item(file_path))
        delete_action.triggered.connect(lambda: self.delete_item(file_path))


        menu.addAction(terminal_action)
        
        # menu.exec_(self.tree.viewport().mapToGlobal(position))


        menu.addAction(copy_action)
        menu.addAction(cut_action)
        menu.addAction(paste_action)
        menu.addAction(delete_action)

        menu.exec_(self.tree.viewport().mapToGlobal(position))


    def copy_item(self, file_path):
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "خطأ", "المسار غير موجود.")
            return

        self.clipboard_mode = "copy"
        self.clipboard_path = file_path
        print("📋 تم النسخ:", file_path)


    # def copy_item(self, path):

    #     self.clipboard_action = "copy"

    #     self.clipboard_path = path



    def cut_item(self, path):
        self.clipboard_action = "cut"
        self.clipboard_path = path



    def paste_item(self, target_path):
        if not hasattr(self, "clipboard_path") or not os.path.exists(self.clipboard_path):
            QMessageBox.warning(self, "⚠️ خطأ", "لا يوجد عنصر لِلصق.")
            return

        # إذا ضغطت على ملف، نأخذ المجلد الذي يحتويه
        if os.path.isfile(target_path):
            target_path = os.path.dirname(target_path)

        base_name = os.path.basename(self.clipboard_path)
        dest_path = os.path.join(target_path, base_name)

        if os.path.exists(dest_path):
            QMessageBox.warning(self, "⚠️ موجود", f"العنصر '{base_name}' موجود بالفعل.")
            return

        try:
            if self.clipboard_mode == "copy":
                if os.path.isdir(self.clipboard_path):
                    shutil.copytree(self.clipboard_path, dest_path)
                else:
                    shutil.copy2(self.clipboard_path, dest_path)
            elif self.clipboard_mode == "cut":
                shutil.move(self.clipboard_path, dest_path)
        except Exception as e:
            QMessageBox.critical(self, "❌ خطأ", f"فشل في اللصق:\n{e}")


    # def paste_item(self, target_folder):
    #     if not self.clipboard_path or not self.clipboard_action:
    #         return

    #     source = self.clipboard_path
    #     name = os.path.basename(source)
    #     destination = os.path.join(target_folder, name)

    #     try:
    #         if os.path.exists(destination):
    #             QMessageBox.warning(self, "تحذير", f"العنصر '{name}' موجود مسبقًا.")
    #             return

    #         if os.path.isdir(source):
    #             shutil.copytree(source, destination)
    #         else:
    #             shutil.copy2(source, destination)

    #         if self.clipboard_action == "cut":
    #             if os.path.isdir(source):
    #                 shutil.rmtree(source)
    #             else:
    #                 os.remove(source)

    #         QTimer.singleShot(100, self.refresh_tree_view)

    #     except Exception as e:
    #         QMessageBox.warning(self, "خطأ", f"فشل عملية اللصق:\n{e}")


    #     QTimer.singleShot(100, self.refresh_tree_view)




    def delete_item(self, path):
        reply = QMessageBox.question(self, "تأكيد الحذف", f"هل تريد حذف '{os.path.basename(path)}'؟",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)

                QTimer.singleShot(100, self.refresh_tree_view)

            except Exception as e:
                QMessageBox.warning(self, "خطأ", f"فشل حذف الملف:\n{e}")

        QTimer.singleShot(100, self.refresh_tree_view)



    def open_terminal_at(self, path):
        if os.name == 'nt':  # Windows
            os.startfile(path)
        else:  # Linux / macOS
            subprocess.Popen(["gnome-terminal", "--working-directory", path])

    def show_tab_context_menu(self, pos):
        index = self.tabs.tabBar().tabAt(pos)
        if index == -1:
            return

        file_name = self.tabs.tabText(index)
        # نحصي عدد التبويبات التي تحمل نفس الاسم
        count_same_name = sum(1 for i in range(self.tabs.count()) if self.tabs.tabText(i) == file_name)

        if count_same_name > 1:
            menu = QMenu()
            open_location_action = QAction("فتح موقع الملف في المستكشف", self)
            menu.addAction(open_location_action)

            action = menu.exec_(self.tabs.mapToGlobal(pos))
            if action == open_location_action:
                file_path = self.tab_file_paths.get(index)
                if file_path:
                    self.expand_tree_to_file(file_path)

    
    def expand_tree_to_file(self, file_path):
        index = self.model.index(file_path)
        if not index.isValid():
            return

        # لا تغير root هنا
        # فقط قم بتوسيع الشجرة للملف
        self.tree.expand(index.parent())  # وسّع المجلد الأب للملف (يمكنك توسيع سلسة المجلدات إن أردت)

        # اختر الملف وحدده في الشجرة
        self.tree.selectionModel().select(index, self.tree.selectionModel().ClearAndSelect)
        self.tree.scrollTo(index)
        self.tree.setCurrentIndex(index)


    def open_root_0(self):



        self.explorer = MountPointExplorer()
        
        # ربط إشارة folderSelected بدالة تستقبل المجلد المختار
        self.explorer.folderSelected.connect(self.open_root_1)
        
        self.explorer.show()
    



    def open_root_1(self, folder_path):



        folder = folder_path

        
        if folder:
            self.model.setRootPath(folder)
            self.tree.setRootIndex(self.model.index(folder))
            self.path_of_root = folder




    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "تأكيد الإغلاق",
            "هل أنت متأكد أنك تريد إغلاق المحرر؟",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()

            with open(os.path.join(os.getcwd(), "path_of_root.txt"), "w") as f:
                f.write(self.path_of_root)

            open_files = []
            for i in range(self.tabs.count()):
                editor = self.tabs.widget(i)
                if hasattr(editor, "file_path") and editor.file_path:
                    open_files.append(editor.file_path)

            with open("opened_files.json", "w", encoding="utf-8") as f:
                json.dump(open_files, f, ensure_ascii=False, indent=2)

        else:
            event.ignore()



from PyQt5.QtGui import QPalette, QColor

def apply_night_theme(app):
    night_palette = QPalette()

    # الخلفيات العامة
    night_palette.setColor(QPalette.Window, QColor(30, 30, 30))
    night_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    night_palette.setColor(QPalette.AlternateBase, QColor(35, 35, 35))

    # النصوص
    night_palette.setColor(QPalette.Text, QColor(220, 220, 220))
    night_palette.setColor(QPalette.WindowText, QColor(220, 220, 220))
    night_palette.setColor(QPalette.ButtonText, QColor(220, 220, 220))
    night_palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))

    # التحديد
    night_palette.setColor(QPalette.Highlight, QColor(45, 140, 240))

    # الأزرار
    night_palette.setColor(QPalette.Button, QColor(40, 40, 40))

    # الروابط
    night_palette.setColor(QPalette.Link, QColor(100, 150, 255))

    app.setPalette(night_palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    apply_night_theme(app)  # ⬅️ أضف هذا السطر هنا

    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())





# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------


# my code 












