














# i_hello





import os




cwd = os.path.dirname(os.path.abspath(__file__))


NAME_OF_FILE = os.path.join(os.getcwd(), "edit-or_of_code", "files_0", "editor_of_code_0.py")


color_of_mode_of_night = ["#A0A0A0", "#FFFFFF"]


size_of_font_of_horloge = 20




# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
     
     
 


  
   
# hello 






list_of_liberary_to_install = [

                            ["PyQt5"] ,
                            
                            
                            ["psutil"] ,
                            
                            
                            ["requests"] ,
                            



]





import os




counter_0 = 0


while (counter_0 < len(list_of_liberary_to_install)):

    os.system(f"pip install {list_of_liberary_to_install[counter_0][0]}")

    counter_0 += 1




#print(f"cwd = {cwd} .")





# section of ai 




import time

import traceback


import subprocess

import platform


import requests

import zipfile

import io

import threading


from pathlib import Path

from PyQt5.QtWidgets import QDialog



from PyQt5.QtWidgets import QApplication


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




from PyQt5.QtCore import QFileSystemWatcher


from PyQt5.QtWidgets import QWidget, QPlainTextEdit
from PyQt5.QtCore import Qt, QRect, QSize
from PyQt5.QtGui import QPainter, QColor, QFont












def i_number_to_str(number):

    string_0 = str(number)

    counter_4 = len(string_0) - 1

    counter_5 = 0

    string_1 = ""

    while (counter_4 >= 0):

        if (counter_5 == 3):

            string_1 = "_" + string_1

            counter_5 = 0

        string_1 = string_0[counter_4] + string_1


        counter_4 -= 1

        counter_5 += 1


    return string_1




def min_string_function(min_, ele, n):


    v = min_[0]



    v1 = ele

    one_ = True

    one = True

    # anné

    if (v <= v1):

        if (v < v1):

            one_ = False


    else:

        one = False


    if (not one_):

        return min_

    elif (one):

        return min_

    else:

        return (ele, n, )



def sort_element_0(l):


    l_ = []

    while (0 < len(l)):

        i = 0

        min_ = (l[i][0], i, )



        while (i < len(l)):

            min_0 = min_string_function(min_=min_, ele=l[i][0], n=i)



            if (min_0 != min_):

                min_ = min_0

            i += 1
        
        #print("min_ = ", min_)

        l_.append(l[min_[1]])

        l.pop(min_[1])

    return l_







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



        self.parameter_format_1 = QTextCharFormat()
        self.parameter_format_1.setForeground(QColor("#FFB300"))
        self.parameter_format_1.setFontItalic(True)
        
        self.parameter_pattern_1 = QRegExp(r"\([^()]*\)")





        # # 🟣 تلوين multi-line strings مثل ''' comment '''
        # self.multi_line_string_format = QTextCharFormat()
        # self.multi_line_string_format.setForeground(QColor("#6a9955"))  # أخضر مثل التعليقات
        # self.multi_line_string_format.setFontItalic(True)
        
        # self.triple_single_start = QRegExp("'''")
        # self.triple_single_end = QRegExp("'''")
        
        # self.triple_double_start = QRegExp('"""')
        # self.triple_double_end = QRegExp('"""')
        



        self.triple_single_start = QRegExp("'''")
        self.triple_single_end = QRegExp("'''")

        self.triple_double_start = QRegExp('"""')
        self.triple_double_end = QRegExp('"""')

        self.multi_line_string_format = QTextCharFormat()
        self.multi_line_string_format.setForeground(QColor("#6a9955"))  # لون التعليق
        self.multi_line_string_format.setFontItalic(True)


#        print("hello")
#


    # # 🟣 دعم ''' multi-line comments '''
    # def apply_multiline_highlight(self, text, start_pattern, end_pattern, in_state):
    #     if self.previousBlockState() == in_state:
    #         start_index = 0
    #     else:
    #         start_index = start_pattern.indexIn(text)

    #     while start_index >= 0:
    #         end_index = end_pattern.indexIn(text, start_index + 3)
    #         if end_index == -1:
    #             self.setCurrentBlockState(in_state)
    #             length = len(text) - start_index
    #         else:
    #             length = end_index - start_index + 3

    #         self.setFormat(start_index, length, self.multi_line_string_format)

    #         if end_index == -1:
    #             break
    #         else:
    #             start_index = start_pattern.indexIn(text, start_index + length)




    def apply_multiline_highlight(self, text, start_pattern, end_pattern, state_id):
        self.setCurrentBlockState(0)

        start_index = 0
        if self.previousBlockState() != state_id:
            start_index = start_pattern.indexIn(text)

        while start_index >= 0:
            end_index = end_pattern.indexIn(text, start_index + start_pattern.matchedLength())
            if end_index == -1:
                self.setCurrentBlockState(state_id)
                length = len(text) - start_index
            else:
                length = end_index - start_index + end_pattern.matchedLength()

            self.setFormat(start_index, length, self.multi_line_string_format)

            if end_index == -1:
                break
            else:
                start_index = start_pattern.indexIn(text, start_index + length)





    def highlight_multiline(self, text, delimiter_start, delimiter_end, state_id):
        self.setCurrentBlockState(0)

        if self.previousBlockState() == state_id:
            start = 0
        else:
            start = delimiter_start.indexIn(text)

        while start >= 0:
            if self.previousBlockState() == state_id:
                end = delimiter_end.indexIn(text, start)
                if end == -1:
                    self.setCurrentBlockState(state_id)
                    self.setFormat(start, len(text) - start, self.multi_line_string_format)
                    return
                length = end - start + delimiter_end.matchedLength()
                self.setFormat(start, length, self.multi_line_string_format)
                start = delimiter_start.indexIn(text, end + delimiter_end.matchedLength())
            else:
                end = delimiter_end.indexIn(text, start + delimiter_start.matchedLength())
                if end == -1:
                    self.setCurrentBlockState(state_id)
                    self.setFormat(start, len(text) - start, self.multi_line_string_format)
                    return
                length = end - start + delimiter_end.matchedLength()
                self.setFormat(start, length, self.multi_line_string_format)
                start = delimiter_start.indexIn(text, start + length)






















    def highlightBlock(self, text):









        index = self.parameter_pattern_1.indexIn(text)

        while index >= 0:
            length = self.parameter_pattern_1.matchedLength()
            self.setFormat(index, length, self.parameter_format_1)
            index = self.parameter_pattern_1.indexIn(text, index + length)


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




    
    
    
        # --- تلوين الأقواس غير المتطابقة ---
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        # brackets = {'(': ')', '[': ']', '{': '}', '\"' : "\"", '\'' : '\''}

        opening = brackets.keys()
        closing = brackets.values()

        unmatched_format = QTextCharFormat()
        unmatched_format.setForeground(QColor("#ff5555"))  # أحمر للأقواس غير المتطابقة

        for i, char in enumerate(text):
            if char in opening:
                stack.append((char, i))
            elif char in closing:
                if stack and brackets[stack[-1][0]] == char:
                    stack.pop()
                else:
                    self.setFormat(i, 1, unmatched_format)

        for bracket, i in stack:
            self.setFormat(i, 1, unmatched_format)




        # # استدعاء الوظيفة للمجموعة الأولى '''
        # self.apply_multiline_highlight(text, self.triple_single_start, self.triple_single_end, 1)

        # # استدعاء الوظيفة للمجموعة الثانية """
        # self.apply_multiline_highlight(text, self.triple_double_start, self.triple_double_end, 2)





        for pattern, fmt in self.rules:
            index = pattern.indexIn(text)
            while index >= 0:
                length = pattern.matchedLength()
                self.setFormat(index, length, fmt)
                index = pattern.indexIn(text, index + length)




        # # التعليقات متعددة الأسطر ''' و """
        # self.apply_multiline_highlight(text, self.triple_single_start, self.triple_single_end, 1)
        # self.apply_multiline_highlight(text, self.triple_double_start, self.triple_double_end, 2)



        # # تلوين تعليقات متعددة الأسطر
        # self.highlight_multiline(text, self.triple_single_start, self.triple_single_end, 1)
        # self.highlight_multiline(text, self.triple_double_start, self.triple_double_end, 2)








class CHighlighter(QSyntaxHighlighter):
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
        self.comment_pattern = QRegExp(r"//.*$")


        self.string_format_0 = QTextCharFormat()
        self.string_format_0.setForeground(QColor("#f08d49"))
        self.string_format_0.setFontItalic(True)
        self.string_pattern_0 = QRegExp(r'"[^"\\]*(\\.[^"\\]*)*"')



        self.string_format_1 = QTextCharFormat()
        self.string_format_1.setForeground(QColor("#f08d49"))
        self.string_format_1.setFontItalic(True)
        self.string_pattern_1 = QRegExp(r"'[^'\\]*(\\.[^'\\]*)*'")


        self.include_format_0 = QTextCharFormat()
        self.include_format_0.setForeground(QColor("#f08d49"))
        self.include_format_0.setFontItalic(True)
        self.include_pattern_0 = QRegExp(r'<[^<>]*>')




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
            self.setFormat(index, length, self.include_format_0)
            index = self.string_pattern_1.indexIn(text, index + length)




        index = self.include_pattern_0.indexIn(text)

        while index >= 0:
            length = self.include_pattern_0.matchedLength()
            self.setFormat(index, length, self.string_format_1)
            index = self.include_pattern_0.indexIn(text, index + length)


    
    
    
        # --- تلوين الأقواس غير المتطابقة ---
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        # brackets = {'(': ')', '[': ']', '{': '}', '\"' : "\"", '\'' : '\''}

        opening = brackets.keys()
        closing = brackets.values()

        unmatched_format = QTextCharFormat()
        unmatched_format.setForeground(QColor("#ff5555"))  # أحمر للأقواس غير المتطابقة

        for i, char in enumerate(text):
            if char in opening:
                stack.append((char, i))
            elif char in closing:
                if stack and brackets[stack[-1][0]] == char:
                    stack.pop()
                else:
                    self.setFormat(i, 1, unmatched_format)

        for bracket, i in stack:
            self.setFormat(i, 1, unmatched_format)







'''






text = self.document().toPlainText()


v_0 = text.split(word)


list_of_position = []

counter_0 = 0


q = 0

while (counter_0 < len(v_0)):

    v_1 = v_0[counter_0].split("\n")

    position_of_line = len(v_1) + q

    position_of_caracter = len(v_1[-1])


    list_of_position.append([position_of_line, position_of_caracter])

    q = -1

    counter_0 += 1


'''













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


from PyQt5.QtGui import QFontMetrics


from PyQt5.QtGui import QTextBlockFormat


from PyQt5.QtWidgets import QPlainTextEdit, QShortcut
from PyQt5.QtGui import QKeySequence

from PyQt5.QtGui import QTextFormat  # تأكد من وجود هذا الاستيراد
            


from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import QPoint


from PyQt5.QtGui import QTextCursor, QKeySequence
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPlainTextEdit



from PyQt5.QtGui import QTextCharFormat, QColor, QBrush
from PyQt5.QtWidgets import QTextEdit



from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtGui import QKeySequence, QTextCursor, QClipboard
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollBar
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QScrollBar, QStyle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyleOptionSlider


class JumpScrollBar(QScrollBar):
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # احصل على منطقة المقبض (slider/handle)
            style = self.style()
            opt = self.initStyleOption()
            handle_rect = style.subControlRect(
                QStyle.CC_ScrollBar, opt, QStyle.SC_ScrollBarSlider, self
            )

            # إذا كانت النقرة داخل المقبض، نفذ السلوك العادي
            if handle_rect.contains(event.pos()):
                super().mousePressEvent(event)
                return

            # إذا كانت النقرة خارج المقبض، قم بالقفز
            if self.orientation() == Qt.Vertical:
                y = event.pos().y()
                height = self.size().height()
                ratio = y / height
                new_value = round(ratio * (self.maximum() - self.minimum()))
                self.setValue(new_value)
                event.accept()
                return

        # افتراضي لأي حالة أخرى
        super().mousePressEvent(event)

    def initStyleOption(self):
        opt = QStyleOptionSlider()
        opt.initFrom(self)
        opt.minimum = self.minimum()
        opt.maximum = self.maximum()
        opt.sliderPosition = self.sliderPosition()
        opt.sliderValue = self.value()
        opt.singleStep = self.singleStep()
        opt.pageStep = self.pageStep()
        opt.upsideDown = False
        opt.orientation = self.orientation()
        return opt
    





from PyQt5.QtWidgets import QScrollBar
from PyQt5.QtCore import Qt, QTimer

class CustomScrollBar(QScrollBar):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.setMouseTracking(True)
        self._is_pressed = False
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._scroll_smoothly)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_pressed = True
            self._press_pos = event.pos()

           
            self._target_pos = self._pixel_pos_to_scroll_value(event.y())


            self.setValue(self._target_pos)
            self._timer.start(30)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self._is_pressed = False
        self._timer.stop()
        super().mouseReleaseEvent(event)

    def _scroll_smoothly(self):
        if self._is_pressed:
            global_pos = self.mapFromGlobal(self.cursor().pos())
            value = self._pixel_pos_to_scroll_value(global_pos.y())


            self.setValue(value)


    def _pixel_pos_to_scroll_value(self, y):
        height = self.height()
        if height == 0:
            return self.value()
        proportion = y / height
        value = self.minimum() + proportion * (self.maximum() - self.pageStep())
        return round(value)



from PyQt5.QtCore import pyqtSignal


class CodeEditor(QPlainTextEdit):
   
   
   
    content_changed = pyqtSignal()

    
   
    def __init__(self):
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)


        self.position_of_curser = -1

        # استبدال الـ ScrollBar الافتراضي
        self.setVerticalScrollBar(CustomScrollBar(Qt.Vertical))

        self.document().modificationChanged.connect(self._on_modification_changed)


        self.semaphore_of_hot_key = False

        self.semaphore_of_right_and_left_Key = False

        self.desired_column = None

        self.semaphore_of_copy_of_1_line = False            

        self.index = 0

        self.file_path = ""

        self.time_of_last_modification_of_file = 0.0

        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setNightModeStyle()

        # اتجاه واجهة المحرر (LTR)
        self.setLayoutDirection(Qt.LeftToRight)

        # ضبط اتجاه النص داخل المستند لليسار إلى اليمين
        option = self.document().defaultTextOption()
        option.setTextDirection(Qt.LeftToRight)
        self.document().setDefaultTextOption(option)

        # اتجاه تفاعل النص (لتحديد النص وتحريره)
        self.setTextInteractionFlags(Qt.TextEditorInteraction)

        # إعدادات الإكمال التلقائي (Completer)
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

        self.word_colors_Python = {
            'def': '#7ec699',
            'class': '#f08d49',
            'import': '#61afef',
            'print': '#c678dd',
            'break': '#c678dd',
            'for': '#d19a66',
            'while': '#d19a66',
            'return': '#7ec699',
            'if': '#7ec699',
            'else': '#7ec699',
            'pass': '#7ec699',
            'from': '#61afef',
            'elif' : '#7ec699',
            'with' : '#61afef',
            '__init__' : '#FFD700',

            'self' : '#61afef',

            'in' : '#d19a66',
            
            'True' : '#61afef',
            
            'False' : '#61afef',

        }


        self.word_colors_C = {


            'struct' : '#7ec699',

            'include' : '#61afef',

            'define' : '#61afef',



        }



        word_colors = {}

        word_colors.update(self.word_colors_Python)

        
        self.highlighter = PythonHighlighter(self.document(), word_colors)






        self.suggestion_visible = False



        # --- تم إزالة استدعاء الدوال غير الضرورية هنا ---


        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        # self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()


#        self.cursorPositionChanged.connect(self.matchBrackets)


        self.textChanged.connect(self.textChanged_connect_)


        QShortcut(QKeySequence("Ctrl+Space"), self, self.trigger_completer)





        self.cursorPositionChanged.connect(self.cursorPositionChanged_)


        

        self.text_selected_in_completer = ""


        self.file_of_tabs = ""


        font = QFont("Courier New", 12)
        self.setFont(font)

        tab_width = 4  # عدد المسافات لكل تبويبة
        metrics = QFontMetrics(font)
        self.setTabStopDistance(tab_width * metrics.horizontalAdvance(' '))



        comment_shortcut = QShortcut(QKeySequence("Ctrl+:"), self)
        comment_shortcut.activated.connect(self.toggle_comment_block)





        self.setUndoRedoEnabled(True)
        
        self.document().setMaximumBlockCount(0)  # اختياري: يمنع تقطيع الذاكرة


        self.document().setUndoRedoEnabled(True)
    
         
         
         
    
    def _on_modification_changed(self, modified):
        self.content_changed.emit()
       
    
    
    def textChanged_connect_(self):
    
    
#        self.highlight_unmatched_brackets()
        
        self.update_completer_model()
    
    
        self.matchBrackets()
    
    
    
    
    def trigger_completer(self):
        cursor = self.textCursor()
        cursor.select(cursor.WordUnderCursor)
        current_word = cursor.selectedText()
        
        if len(current_word) < 2:
            self.completer.popup().hide()
            return
    
        self.update_completer_model()
    
        self.completer.setCompletionPrefix(current_word)
        rect = self.cursorRect()
        rect.setWidth(self.completer.popup().sizeHintForColumn(0) + 10)
        self.completer.complete(rect)
    
    
    
    
    def extract_unique_words(self, text):

        # تستخرج كلمات كاملة فقط (بحد أدنى 2 حرف إن أردت)

        words = re.findall(r'\b\w{2,}\b', text)  # تجاهل الكلمات القصيرة مثل "i"

        return sorted(set(words))


    
    def update_completer_model(self):
        text = self.toPlainText()
        words = self.extract_unique_words(text)
        self.completer.model().setStringList(words)
    




    def toggle_comment_block(self):
        cursor = self.textCursor()
        start = cursor.selectionStart()
        end = cursor.selectionEnd()

        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.StartOfBlock)
        start_block = cursor.blockNumber()

        cursor.setPosition(end)
        cursor.movePosition(QTextCursor.EndOfBlock)
        end_block = cursor.blockNumber()

        lines = []
        for i in range(start_block, end_block + 1):
            block = self.document().findBlockByNumber(i)
            lines.append(block.text())

        # التحقق مما إذا كانت كل الأسطر تبدأ بـ #
        all_commented = all(line.lstrip().startswith(self.char_of_comment) for line in lines if line.strip())

        cursor.beginEditBlock()
        for i in range(start_block, end_block + 1):
            block = self.document().findBlockByNumber(i)
            block_text = block.text()

            cursor.setPosition(block.position())
            cursor.movePosition(QTextCursor.StartOfBlock)
            cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)

            if all_commented:
                # إزالة أول # فقط إن وجدت بعد الهوامش
                stripped = block_text.lstrip()

                

                if stripped.startswith(self.char_of_comment):
                    leading_spaces = len(block_text) - len(stripped)

                    leading_spaces = 0

                    # new_text = " " * leading_spaces + stripped[1:]
                    new_text = " " * leading_spaces + block_text[len(self.char_of_comment):]

                else:
                    new_text = block_text
            else:
                # إضافة # مباشرة بعد الهوامش
                leading_spaces = len(block_text) - len(block_text.lstrip())

                leading_spaces = 0


                new_text = " " * leading_spaces + self.char_of_comment + block_text


            cursor.insertText(new_text)

        cursor.endEditBlock()



    def hoghlight_Python(self):

        self.highlighter = PythonHighlighter(self.document(), self.word_colors_Python)

        self.char_of_comment = "#"


    def hoghlight_C(self):

        self.highlighter = CHighlighter(self.document(), self.word_colors_C)


        self.char_of_comment = "//"

    def get_project_files(self):



        self.opened_files_path = self.file_of_tabs

        list_of_path = []

        if os.path.exists(self.opened_files_path):
            try:
                with open(self.opened_files_path, "r", encoding="utf-8") as f:
                    paths = json.load(f)
                for path in paths:
                
                    list_of_path.append(path)

            except Exception as e:
                print("error upload-ing file-s:", e)


        return list_of_path



    def update_completer_words(self):
        


        # 1. اجلب الكلمات القديمة من الموديل الحالي
        old_words = set(self.completer.model().stringList())

        # 2. ابدأ بالقائمة من الملف الحالي
        all_text = self.toPlainText()

        # 3. ملفات أخرى من المشروع
        other_files = self.get_project_files()

        for file_path in other_files:
            try:
                if os.path.isfile(file_path) and file_path.endswith((".py", ".txt", ".md", ".c", ".cpp", ".html", ".css")):
                    with open(file_path, "r", encoding="utf-8") as f:
                        all_text += "\n" + f.read()
            except Exception as e:
                print(f"خطأ في قراءة {file_path}: {e}")

        # 4. استخراج مفردات جديدة ≥3 أحرف
        new_words = set(re.findall(r'\b[a-zA-Z_]\w{1,}\b', all_text))

        # 5. دمج القديم والجديد بدون تكرار
        merged = old_words.union(new_words)

        # 6. استبدال القائمة في الكومبليتر بالكامل
        final_list = sorted(merged)
        self.completer.model().setStringList(final_list)



    
    
    def on_cursor_moved(self):
        
        cursor = self.textCursor()
        
        line = cursor.blockNumber() + 1
        
        column = cursor.positionInBlock() + 1


        return column, line

    def cursorPositionChanged_(self):


        
    
#        self.position_of_curser = self.on_cursor_moved()[1]


        self.highlightCurrentLine()

        self.matchBrackets()


        self.highlight_matching_brackets()


    def highlight_unmatched_brackets(self):
        
    
        print("start_of_highlight_unmatched_brackets ")

        extra_selections = []

        cursor = self.textCursor()
        doc = self.document()
        text = doc.toPlainText()
        pos = cursor.position()

        # أبسط طريقة: نفحص القوس تحت المؤشر أو قبله مباشرة
        
        if (len(text) > pos - 1) and pos > 0 and text[pos-1] in '(){}[]':
            char = text[pos-1]
            match_pos = self.find_matching_bracket(pos-1, char, text)
            if match_pos == -1:
                # قوس غير متطابق، نميز هذا القوس
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(QColor('#ff9999'))  # لون أحمر فاتح
                selection.cursor = self.textCursor()
                selection.cursor.setPosition(pos-1)
                selection.cursor.movePosition(selection.cursor.Right, selection.cursor.KeepAnchor, 1)
                extra_selections.append(selection)
        elif pos < len(text) and text[pos] in '(){}[]':
            char = text[pos]
            match_pos = self.find_matching_bracket(pos, char, text)
            if match_pos == -1:
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(QColor('#ff9999'))
                selection.cursor = self.textCursor()
                selection.cursor.setPosition(pos)
                selection.cursor.movePosition(selection.cursor.Right, selection.cursor.KeepAnchor, 1)
                extra_selections.append(selection)

        self.setExtraSelections(extra_selections)











    
    
    def highlight_matching_brackets(self):


#        print("start_of_highlight_matched_brackets ")

        text = self.toPlainText()
        cursor = self.textCursor()
        pos = cursor.position()
    
        if not text or pos < 0 or pos > len(text):
            return
    
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        opening = bracket_pairs.keys()
        closing = bracket_pairs.values()
    
        match_format = QTextCharFormat()
        match_format.setBackground(QColor("#44475a"))
        match_format.setForeground(QColor("#ff79c6"))
        match_format.setFontWeight(QFont.Bold)
    
        matched_positions = []
    
        def find_match(start, direction, open_b, close_b):
            stack = 1
            i = start + direction
            while 0 <= i < len(text):
                if text[i] == open_b:
                    stack += 1
                elif text[i] == close_b:
                    stack -= 1
                    if stack == 0:
                        return i
                i += direction
            return -1
    
        # افحص الحرف السابق
        if pos > 0 and text[pos - 1] in opening:
            start = pos - 1
            end = find_match(start, +1, text[start], bracket_pairs[text[start]])
        elif pos > 0 and text[pos - 1] in closing:
            start = pos - 1
            # ابحث عن المفتاح العكسي
            rev_map = {v: k for k, v in bracket_pairs.items()}
            end = find_match(start, -1, text[start], rev_map[text[start]])
        # أو الحرف التالي
        elif pos < len(text) and text[pos] in opening:
            start = pos
            end = find_match(start, +1, text[start], bracket_pairs[text[start]])
        elif pos < len(text) and text[pos] in closing:
            start = pos
            rev_map = {v: k for k, v in bracket_pairs.items()}
            end = find_match(start, -1, text[start], rev_map[text[start]])
        else:
            self.setExtraSelections([])
            return
    
        if end == -1:
            self.setExtraSelections([])
            return
    
        # أنشئ التحديدين
        selections = []
    
        for bracket_pos in (start, end):
            match_cursor = QTextCursor(self.document())

#            print("start of coloration")

            match_cursor.setPosition(bracket_pos)
            match_cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 1)
    
            sel = QTextEdit.ExtraSelection()
            sel.cursor = match_cursor
            sel.format = match_format
            selections.append(sel)
    
        self.setExtraSelections(selections)
    





    
#    
#    
#    
#    def highlight_matching_brackets(self):
#
#
#
#        print("start_of_highlight_matched_brackets ")
#
#        self.setExtraSelections([])  # تنظيف التحديدات السابقة
#    
#        cursor = self.textCursor()
#        pos = cursor.position()
#    
#        if pos == 0:
#            return
#    
#        # الحرف السابق والتالي
#        doc = self.document()
#        prev_char = doc.characterAt(pos - 1)
#        next_char = doc.characterAt(pos)
#    
#        brackets = {'(': ')', '{': '}', '[': ']'}
#        opening = brackets.keys()
#        closing = brackets.values()
#    
#        if prev_char in opening:
#            direction = 1
#            start_pos = pos - 1
#            open_bracket = prev_char
#            close_bracket = brackets[prev_char]
#        elif next_char in opening:
#            direction = 1
#            start_pos = pos
#            open_bracket = next_char
#            close_bracket = brackets[next_char]
#        elif prev_char in closing:
#            direction = -1
#            start_pos = pos - 1
#            close_bracket = prev_char
#            open_bracket = [k for k, v in brackets.items() if v == prev_char][0]
#        elif next_char in closing:
#            direction = -1
#            start_pos = pos
#            close_bracket = next_char
#            open_bracket = [k for k, v in brackets.items() if v == next_char][0]
#        else:
#            return
#    
#        # بحث عن القوس المطابق
#        depth = 1
#        i = start_pos + direction
#    
#        while 0 <= i < doc.characterCount():
#            char = doc.characterAt(i)
#            if char == open_bracket:
#                depth += 1
#            elif char == close_bracket:
#                depth -= 1
#                if depth == 0:
#                    match_pos = i
#                    break
#            i += direction
#        else:
#            return  # لم يتم العثور على تطابق
#    
#        # تنسيق التمييز
#        format = QTextCharFormat()
#        format.setBackground(QColor("#44475a"))
#        format.setForeground(QColor("#ff79c6"))
#        format.setFontWeight(QFont.Bold)
#    
#        # إنشاء التحديدين للقوسين
#        selections = []
#    
#        for position in (start_pos, match_pos):
#            match_cursor = QTextCursor(self.document())
#            match_cursor.setPosition(position)
#            match_cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, 1)
#            selection = QTextEdit.ExtraSelection()
#            selection.cursor = match_cursor
#            selection.format = format
#            selections.append(selection)
#    
#        self.setExtraSelections(selections)
#    
#
#

    def find_matching_bracket(self, pos, char, text):
        pairs = {'(': ')', '{': '}', '[': ']',
                ')': '(', '}': '{', ']': '['}
        open_brackets = '({['
        close_brackets = ')}]'

        match_char = pairs[char]

        if char in open_brackets:
            # ابحث للأمام
            depth = 1
            for i in range(pos+1, len(text)):
                c = text[i]
                if c == char:
                    depth += 1
                elif c == match_char:
                    depth -= 1
                    if depth == 0:
                        return i
        else:
            # ابحث للخلف
            depth = 1
            for i in range(pos-1, -1, -1):
                c = text[i]
                if c == char:
                    depth += 1
                elif c == match_char:
                    depth -= 1
                    if depth == 0:
                        return i
        return -1


    def exist_in_list(self, element, list_0):

        counter_0 = 0
        
        while ((counter_0 < len(list_0)) and (list_0[counter_0] != element)):
        
            counter_0 += 1
            
        if (counter_0 < len(list_0)):
        
            return True
            
        else:
        
            return False
        
            

#
#
#    def matchBrackets(self):
#
#        color = "#444444"
#
#        cursor = self.textCursor()
#        doc = self.document()
#        pos = cursor.position()
#
#        if pos == 0:
#            self.setExtraSelections([])
#            return
#
#        text = doc.toPlainText()
#        
#        pos -= 1
#
#        print(f" text[pos - 1] = {text[pos - 1]} . text[pos] = {text[pos]} .") 
#
#
#        char_prev = text[pos - 1] if pos - 1 >= 0 else ''
#        char_curr = text[pos] if pos < len(text) else ''
#        
#        
#        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
#        opening = list(bracket_pairs.keys())
#        closing = list(bracket_pairs.values())
#        
#        print(f"opening = {opening} . closing = {closing} .")
#        
#        
#        print(f"char_prev = {char_prev} . char_curr = {char_curr} .")
#
#        match = None
#        highlight_pos = None
#
#        choice = 0
#
#        # إذا المؤشر على قوس مفتوح
#        if self.exist_in_list(element=char_curr, list_0=opening) == True:
#            match = self.findMatchingBracket(pos=pos, forward=True)
#            highlight_pos = pos
#            
#            choice = 1
#
#
#        elif self.exist_in_list(element=char_curr, list_0=closing) == True:
#            match = self.findMatchingBracket(pos=pos, forward=False)
#            highlight_pos = match
#            match = pos
#            
#            
#            choice = 2
#        
#
#        else:
#            self.setExtraSelections([])
#            
#            return
#
#        
#
#        
#        print(f"choice = {choice}")
#
#        print(f"highlight_pos = {highlight_pos} . match = {match} .")
#
#
#
#        if match is not None and highlight_pos is not None:
#
##
##            highlight_pos += 1
##                        
##            match += 1
##                        
#            print(f"coloration . highlight_pos = {highlight_pos} . text[highlight_pos] = {text[highlight_pos]} . match = {match} . text[match] = {text[match]} .")
#            
#            
#
#            extraSelections = []
#    
#            sel1 = QTextEdit.ExtraSelection()
#            sel1.cursor = QTextCursor(doc)
#            sel1.cursor.setPosition(highlight_pos)
#            sel1.cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
#            
#
#
#            sel1.format.setBackground(QColor(color))
#            extraSelections.append(sel1)
#    
#            sel2 = QTextEdit.ExtraSelection()
#            sel2.cursor = QTextCursor(doc)
#            sel2.cursor.setPosition(match)
#            sel2.cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
#            
#            
#
#            
#
#            sel2.format.setBackground(QColor(color))
#            extraSelections.append(sel2)
#    
#            self.setExtraSelections(extraSelections)
#    
#        else:
#
#            self.setExtraSelections([])
#
#
#

    
    def matchBrackets(self):
        color = "#444444"
        cursor = self.textCursor()
        doc = self.document()
        pos = cursor.position()
    
        if pos == 0:
            self.setExtraSelections([])
            return
    
        block = doc.findBlock(pos)
        text = block.text()
        block_start = block.position()
        pos_in_line = pos - block_start
    
        if pos_in_line < 0 or pos_in_line >= len(text):
            self.setExtraSelections([])
            return
    
        char_curr = text[pos_in_line]
        char_prev = text[pos_in_line - 1] if pos_in_line > 0 else ''
    
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        opening = list(bracket_pairs.keys())
        closing = list(bracket_pairs.values())
    
        match = None
        highlight_pos = None
    
        if char_curr in opening:
            match = self.findMatchingBracketInLine(text, pos_in_line, forward=True)
            highlight_pos = pos_in_line
    
        elif char_curr in closing:
            match = self.findMatchingBracketInLine(text, pos_in_line, forward=False)
            highlight_pos = match
            match = pos_in_line
        else:
            self.setExtraSelections([])
            return
    
        if match is not None and highlight_pos is not None:
            extraSelections = []
    
            # عوض الفرق لتحديد الموضع الكامل داخل المستند
            sel1 = QTextEdit.ExtraSelection()
            sel1.cursor = QTextCursor(doc)
            sel1.cursor.setPosition(block_start + highlight_pos)
            sel1.cursor.setPosition(block_start + highlight_pos + 1, QTextCursor.KeepAnchor)
            sel1.format.setBackground(QColor(color))
            extraSelections.append(sel1)
    
            sel2 = QTextEdit.ExtraSelection()
            sel2.cursor = QTextCursor(doc)
            sel2.cursor.setPosition(block_start + match)
            sel2.cursor.setPosition(block_start + match + 1, QTextCursor.KeepAnchor)
            sel2.format.setBackground(QColor(color))
            extraSelections.append(sel2)
    
            self.setExtraSelections(extraSelections)
        else:
            self.setExtraSelections([])
    




    def coloration(self, match, highlight_pos):


        if ( match != -1 ) and (highlight_pos != -1):

#            print("coloration")

            extraSelections = []

            sel1 = QTextEdit.ExtraSelection()
            sel1.cursor = QTextCursor(doc)
            sel1.cursor.setPosition(highlight_pos)
            sel1.cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            sel1.format.setBackground(QColor(color))
            extraSelections.append(sel1)

            sel2 = QTextEdit.ExtraSelection()
            sel2.cursor = QTextCursor(doc)
            sel2.cursor.setPosition(match)
            sel2.cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            sel2.format.setBackground(QColor(color))
            extraSelections.append(sel2)

            self.setExtraSelections(extraSelections)
        else:
            self.setExtraSelections([])





#
#    def findMatchingBracket(self, pos, forward=True):
#        text = self.toPlainText()
#        stack = []
#        brackets = {'(': ')', '{': '}', '[': ']'}
#        if not forward:
#            brackets = {v: k for k, v in brackets.items()}
#
#        open_b = brackets.keys()
#        close_b = brackets.values()
#
#        i = pos
#        while 0 <= i < len(text):
#            char = text[i]
#            if char in open_b:
#                stack.append(char)
#            elif char in close_b:
#                if not stack:
#                    return None
#                last = stack.pop()
#                if brackets[last] != char:
#                    return None
#                if not stack:
#                    return i
#            i += 1 if forward else -1
#        return None
#
#






#    
#    def findMatchingBracket(self, pos, forward=True):
#        text = self.toPlainText()
#        stack = []
#        brackets = {'(': ')', '{': '}', '[': ']'}
#        if not forward:
#            brackets = {v: k for k, v in brackets.items()}
#    
#        open_b = brackets.keys()
#        close_b = brackets.values()
#    
#        # ابدأ البحث بعد الحرف عند pos (أمامياً) أو قبله (خلفياً)
#        i = pos + 1 if forward else pos - 1
#    
#        # أضف الحرف عند pos كالقوس المفتوح/المغلق الذي نبحث له
#        # وسنستخدمه كعلامة للإغلاق
#        start_char = text[pos]
#        stack.append(start_char)
#    
#        while 0 <= i < len(text):
#            char = text[i]
#            if char in open_b:
#                stack.append(char)
#            elif char in close_b:
#                if not stack:
#                    return None
#                last = stack.pop()
#                if brackets[last] != char:
#                    # الأقواس غير متطابقة، ارجع None
#                    return None
#                if not stack:
#                    # الستاك أصبح فارغ يعني وجدنا القوس المطابق
#                    return i
#            i += 1 if forward else -1
#    
#        return None
#    
#






#
#    
#    def findMatchingBracket(self, pos, forward=True):
#        
#
#
#
#
#        text = self.toPlainText()
#        brackets = {'(': ')', '{': '}', '[': ']'}
#        
#        if forward:
#            open_b = text[pos]
#            if open_b not in brackets:
#                return None
#            close_b = brackets[open_b]
#            
#            count = 1
#            for i in range(pos + 1, len(text)):
#                c = text[i]
#                if c == open_b:
#                    count += 1
#                elif c == close_b:
#                    count -= 1
#                    if count == 0:
#                        return i
#        else:
#            close_b = text[pos]
#            reverse_brackets = {v: k for k, v in brackets.items()}
#            if close_b not in reverse_brackets:
#                return None
#            open_b = reverse_brackets[close_b]
#            
#            count = 1
#            for i in range(pos - 1, -1, -1):
#                c = text[i]
#                if c == close_b:
#                    count += 1
#                elif c == open_b:
#                    count -= 1
#                    if count == 0:
#                        return i
#        return None
#    
#
#
#

        
    

    
    
    def findMatchingBracketInLine(self, text, pos, forward=True):
        
    
    





        brackets = {'(': ')', '{': '}', '[': ']'}
        
        if forward == True:
            open_b = text[pos]
            
            
            brackets_ = [k for k, v in brackets.items()]
            

            if self.exist_in_list(element=open_b, list_0=brackets_) == False:
                return None
            close_b = brackets[open_b]
            

            
            count = 0
            
            
            first_step = True
        
            counter_0 = pos
            
            while (counter_0 < len(text)):
            
                            
                c = text[counter_0]
                if c == open_b:
                    count += 1
                elif c == close_b:
                    count -= 1
                    

                                
                if (first_step == False):
                    
                    if count == 0:
                        return counter_0
                
                first_step = False
                
        

            
                counter_0 += 1

        else:
            close_b = text[pos]
            reverse_brackets = {v: k for k, v in brackets.items()}
            
            reverse_brackets_ = [k for k, v in reverse_brackets.items()]

            
            if self.exist_in_list(element=close_b, list_0=reverse_brackets_) == False:
                return None
            open_b = reverse_brackets[close_b]

            count = 0
            
            first_step = True
            
            counter_0 = pos
            
            while (counter_0 >= 0):
            
                                
                c = text[counter_0]
                if c == close_b:
                    count += 1
                elif c == open_b:
                    count -= 1
                
                if (first_step == False):
                    
                    if count == 0:
                        return counter_0
            
                first_step = False
            
                counter_0 -= 1
            

        return None
    
    
    
    
    
    
    def findMatchingBracket(self, pos, forward=True):
        
    
    

        doc = self.document()    
    
        text = doc.toPlainText()
        
        print(f"text[pos - 1: pos + 2] = '{text[pos - 1: pos + 2]}' . text[pos] = '{text[pos]}' .")        
        
        


        brackets = {'(': ')', '{': '}', '[': ']'}
        
        if forward == True:
            open_b = text[pos]
            
            
            brackets_ = [k for k, v in brackets.items()]
            
            print(f"open_b = {open_b} . brackets_ = {brackets_} .")
            
            if self.exist_in_list(element=open_b, list_0=brackets_) == False:
                return None
            close_b = brackets[open_b]
            
            
            print(f"open_b = {open_b} . close_b = {close_b} .")
            
            count = 0
            
            
            first_step = True
        
            counter_0 = pos
            
            while (counter_0 < len(text)):
            
                            
                c = text[counter_0]
                if c == open_b:
                    count += 1
                elif c == close_b:
                    count -= 1
                    

                                
                if (first_step == False):
                    
                    if count == 0:
                        return counter_0
                
                first_step = False
                
        

            
                counter_0 += 1

        
        else:
            close_b = text[pos]
            reverse_brackets = {v: k for k, v in brackets.items()}
            
            reverse_brackets_ = [k for k, v in reverse_brackets.items()]
            
            print(f"close_b = '{close_b}' . reverse_brackets_ = {reverse_brackets_} ")
            
            if self.exist_in_list(element=close_b, list_0=reverse_brackets_) == False:
                return None
            open_b = reverse_brackets[close_b]
            
            print(f"open_b = '{open_b}' . close_b = '{close_b}' .")
            
            count = 0
            
            first_step = True
            
            counter_0 = pos
            
            while (counter_0 >= 0):
            
                                
                c = text[counter_0]
                if c == close_b:
                    count += 1
                elif c == open_b:
                    count -= 1
                
                if (first_step == False):
                    
                    if count == 0:
                        return counter_0
            
                first_step = False
            
                counter_0 -= 1

        
        return None
    
    
    
    

    def paintEvent(self, event):
        super().paintEvent(event)
        self.drawIndentationGuides()

    def drawIndentationGuides(self):
        painter = QPainter(self.viewport())
        painter.setPen(QPen(QColor("#404040")))  # لون الخطوط في النمط الليلي

        block = self.firstVisibleBlock()
        block_top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()

        while block.isValid() and block_top <= self.viewport().rect().bottom():
            text = block.text()
            indent_level = self.getIndentLevel(text)

            left_margin = self.contentOffset().x()
            char_width = self.fontMetrics().width(' ')
            top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
            bottom = top + self.blockBoundingRect(block).height()

            for i in range(indent_level):
                x = left_margin + i * char_width * 4  # ← 4 مسافات لكل مستوى

                painter.drawLine(QPoint(int(x), int(top)), QPoint(int(x), int(bottom)))

                
                # painter.drawLine(QPoint(x, top), QPoint(x, bottom))

            block = block.next()
            block_top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()

        painter.end()

    def getIndentLevel(self, text):
        count = 0
        for char in text:
            if char == ' ':
                count += 1
            elif char == '\t':
                count += 4  # حسب قيمة tab
            else:
                break
        return count // 4  # كل 4 مسافات = مستوى واحد






    def lineNumberAreaWidth(self):
        digits = len(str(max(1, self.blockCount())))
        space = 3 + self.fontMetrics().width('9') * digits
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
        painter.fillRect(event.rect(), QColor(240, 240, 240))

        painter.fillRect(event.rect(), QColor("#252526"))  # خلفية داكنة
        
        painter.setPen(QColor("#858585"))  # لون الأرقام رمادي فاتح


        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(blockNumber + 1)
                painter.setPen(Qt.gray)
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
            # lineColor = QColor(232, 242, 254)
            
            lineColor = QColor("#333842")  # لون داكن لطيف للسطر الحالي
            selection.format.setBackground(lineColor)
            
            
            
            selection.format.setProperty(QTextFormat.FullWidthSelection, True)

            
            # selection.format.setProperty(QTextEdit.ExtraSelection.FullWidthSelection, True)
            
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extraSelections.append(selection)

        self.setExtraSelections(extraSelections)


    def print_selected_suggestion(self, text):
        
        # print("text = ", text)

        self.text_selected_in_completer = text

        self.suggestion_visible = True

    def setNightModeStyle(self):
        self.setStyleSheet("QPlainTextEdit { background-color: #1e1e1e; color: #d4d4d4; selection-background-color: #264f78; }")
        self.setFont(QFont("Courier New", 12))

         




    def keyPressEvent(self, event):
        




        if event.key() == Qt.Key_Control:

            self.semaphore_of_hot_key = True
    
        elif event.key() == Qt.Key_Shift:
            
            self.semaphore_of_hot_key = True
    
        elif event.key() == Qt.Key_Alt:

            self.semaphore_of_hot_key = True
    
        else:    

            self.semaphore_of_hot_key = False    
        
        # إذا كنت تريد معرفة إن كان زر آخر تم ضغطه مع Ctrl أو Shift مثلاً

#
#        if event.modifiers() & Qt.ControlModifier:
#
#            self.semaphore_of_hot_key = True
#
#        else:    
#        
#            self.semaphore_of_hot_key = False    
#                        
#                        
#                        
#                        
#        if event.modifiers() & Qt.ShiftModifier:
#
#            self.semaphore_of_hot_key = True
#
#        else:    
#        
#            self.semaphore_of_hot_key = False    
#        
#
#    
#        if event.modifiers() & Qt.AltModifier:
#
#            self.semaphore_of_hot_key = True
#                            
#        else:    
#        
#            self.semaphore_of_hot_key = False    
#        

            
            
        if event.modifiers() == Qt.ControlModifier:
            if event.key() == Qt.Key_Up:
                cursor = self.textCursor()
                for _ in range(30):
                    cursor.movePosition(QTextCursor.Up)
                self.setTextCursor(cursor)
                return  # لا تمرر للوالد
            elif event.key() == Qt.Key_Down:
                cursor = self.textCursor()
                for _ in range(30):
                    cursor.movePosition(QTextCursor.Down)
                self.setTextCursor(cursor)
                return  # لا تمرر للوالد

                

        
        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_D:

            self.selectCurrentWord()

            return 
        

        semaphore_of_hide = False

        if ((event.text().isprintable() and event.text().strip())):

            prefix = self.textUnderCursor()
            self.update_completer_words()
            self.completer.setCompletionPrefix(prefix)
            self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))
            cr = self.cursorRect()
            cr.setWidth(self.completer.popup().sizeHintForColumn(0) +
                        self.completer.popup().verticalScrollBar().sizeHint().width())
            self.completer.complete(cr)
            self.suggestion_visible = True


        else:

            semaphore_of_hide = True

        if (event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Space):

            if self.suggestion_visible:
                self.completer.popup().hide()
                self.suggestion_visible = False
            else:
                prefix = self.textUnderCursor()
                self.update_completer_words()
                self.completer.setCompletionPrefix(prefix)
                self.completer.popup().setCurrentIndex(self.completer.completionModel().index(0, 0))
                cr = self.cursorRect()
                cr.setWidth(self.completer.popup().sizeHintForColumn(0) + self.completer.popup().verticalScrollBar().sizeHint().width())
                self.completer.complete(cr)
                self.suggestion_visible = True
            return





        if self.completer.popup().isVisible():
            if event.key() in (Qt.Key_Enter, Qt.Key_Return):
                completion = self.completer.currentCompletion()

                semaphore_of_hide = True


                if completion:

                    self.insert_completion(self.text_selected_in_completer)



                self.completer.popup().hide()
                self.suggestion_visible = False


                return

            elif event.key() == Qt.Key_Escape:
                self.completer.popup().hide()
                self.suggestion_visible = False
                return
            elif event.key() in (Qt.Key_Up, Qt.Key_Down):
                QApplication.sendEvent(self.completer.popup(), event)
                return


        if event.key() == Qt.Key_Space and self.completer.popup().isVisible():
            self.completer.popup().hide()
            self.suggestion_visible = False



        if event.key() in (Qt.Key_Return, Qt.Key_Enter):



            
            self.insert_indented_newline()            
            

            return 


        cursor = self.textCursor()

        if ((event.key() in (Qt.Key_Up, Qt.Key_Down)) and not self.textCursor().hasSelection() and not event.modifiers() == Qt.ShiftModifier):
            
            current_block = cursor.block()
            current_column = cursor.positionInBlock()
        
            if ((self.semaphore_of_right_and_left_Key == True) or self.desired_column is None):
        
                self.desired_column = current_column
        
                self.semaphore_of_right_and_left_Key = False
        
            if event.key() == Qt.Key_Up:
                target_block = current_block.previous()
            elif event.key() == Qt.Key_Down:
                target_block = current_block.next()
        
            if target_block.isValid():
                new_cursor = QTextCursor(target_block)
                block_text = target_block.text()
                new_pos = min(self.desired_column, len(block_text))
                new_cursor.setPosition(target_block.position() + new_pos)
                self.setTextCursor(new_cursor)
        
            
        
            return  # ❗ لا تستدعي super هنا
        
        elif ((event.key() in (Qt.Key_Left, Qt.Key_Right)) and not self.textCursor().hasSelection() and not event.modifiers() == Qt.ShiftModifier):
        
            
            self.semaphore_of_right_and_left_Key = True



        # تحقق من الضغط على Ctrl + C وعدم وجود تحديد
        if event.matches(QKeySequence.Copy) and not self.textCursor().hasSelection():
            
            self.semaphore_of_copy_of_1_line = True            
            cursor = self.textCursor()
            cursor.select(QTextCursor.LineUnderCursor)
            self.setTextCursor(cursor)  # مؤقتًا لتفعيله
            self.copy()  # نسخ السطر            
            cursor.clearSelection()  # إزالة التحديد بعد النسخ (اختياري)
            self.setTextCursor(cursor)



        if event.matches(QKeySequence.Copy) and self.textCursor().hasSelection():

            self.semaphore_of_copy_of_1_line = False   

        # else:

        #     super().keyPressEvent(event)

        #     return


        cursor = self.textCursor()








        if (semaphore_of_hide == True):

            self.completer.popup().hide()
            self.suggestion_visible = False


        if event.key() == Qt.Key_Tab and cursor.hasSelection():
            self.indentSelectedText()
            return

        elif event.key() == Qt.Key_Backtab and cursor.hasSelection():
            self.unindentSelectedText()
            return

        # ✅ Tab بدون تحديد = 4 مسافات
        elif event.key() == Qt.Key_Tab:
            self.insertPlainText(" " * 4)
            return






        if event.matches(QKeySequence.Paste):
            self.handle_paste()
            
            return







        cursor = self.textCursor()

        # افتح كتلة تحرير صغيرة فقط لحرف واحد
        cursor.beginEditBlock()


        super().keyPressEvent(event)
        
        
        cursor.endEditBlock()
        


        if (self.semaphore_of_hot_key == False):


            self.ensureCursorVisible()


                
    def insert_indented_newline(self):
        
        
        cursor = self.textCursor()
        
        
        current_line_text = self.get_current_line_text_up_to_cursor(cursor)
            

        
        column = cursor.positionInBlock() # موقع المؤشر داخل السطر
    
    



        # استخرج التراجع فقط من بداية السطر حتى المؤشر
        
        
        indent = ''
        
        
        for ch in current_line_text:
        
            if ch in (' ', '\t'):
                indent += ch
            else:
                break




        
        # cursor.movePosition(QTextCursor.Down)  # يتحرك إلى السطر التالي
        
        cursor.beginEditBlock()
        cursor.insertText(current_line_text + '\n' + indent)
        # cursor.movePosition(QTextCursor.EndOfBlock)

        # cursor.movePosition(QTextCursor.StartOfBlock)

        self.setTextCursor(cursor)
        
        cursor.endEditBlock()
    
    
    
        
            
                
                        
    def get_current_line_text_up_to_cursor(self, cursor):
        
        line_text = ""

        if (not cursor.hasSelection()):
            
            # نسخ موضع البداية الحالي
            original_pos = cursor.position()

            # الانتقال إلى بداية السطر
            cursor.movePosition(QTextCursor.StartOfBlock, QTextCursor.KeepAnchor)

            # قص النص حتى المؤشر الأصلي
            line_text = cursor.selectedText()



        return line_text
        
        
        
        

    def auto_indent(self):
        cursor = self.textCursor()
        cursor.select(cursor.LineUnderCursor)
        current_line = cursor.selectedText()
        indent = ''
        for ch in current_line:
            if ch in (' ', '\t'):
                indent += ch
            else:
                break
        super().keyPressEvent(QKeyEvent(QEvent.KeyPress, Qt.Key_Return, Qt.NoModifier))
        self.insertPlainText(indent)


    def get_minimum_tab(self, counter_of_start, text):
    
        v_0 = text[counter_of_start:].split("\n")
        
        
        
        
        
        max_ = 0
        
        
        counter_1 = 0
        
        while (counter_1 < len(v_0)):
        
            
            
            counter_0 = 0
            
            while ((counter_0 < len(v_0[counter_1])) and (counter_0 < len(v_0[counter_1]) - 3) and (v_0[counter_1][counter_0:counter_0 + 4] == " " * 4)):
            
                counter_0 += 4
            
            
            if (max_ < counter_0):
            
                max_ = counter_0
            
        
            counter_1 += 1
        
      

      
      
        
        min_ = max_
        
        
        counter_1 = 0
        
        while (counter_1 < len(text)):
        
            
            
            
                    
            
            counter_2 = 0
            
            counter_0 = self.get_first_line(counter_of_start=counter_1, text=text)
            
            while ((counter_0 < len(text)) and (counter_0 < len(text) - 3) and (text[counter_0:counter_0 + 4] == " " * 4)):
            
                counter_0 += 4
                
                counter_2 += 4
            
            
            
            
            if ((min_ > counter_2) and (counter_0 < len(text))):
            
                min_ = counter_2
            
            
            
            while ((counter_1 < len(text)) and (text[counter_1] != "\n")):
        
                counter_1 += 1

            if (counter_1 < len(text)):
             
                 counter_1 += 1

            
#            print(f"counter_1 = {counter_1} . min_ = {min_} . counter_2 = {counter_2} .")
            


        return min_




    def get_first_line(self, counter_of_start, text):
    
    
        
        
        counter_0 = counter_of_start
        
        if (len(text.split("\n")) > 1):
                
            while ((counter_0 < len(text)) and (text[counter_0] in (" ", "\n"))):
            
                counter_0 += 1
            
            
            if ((counter_0 < len(text)) and (counter_0 > 0) and (not (text[counter_0] in (" ", "\n")))):
            
                counter_0 -= 1
            
            
            while ((counter_0 < len(text)) and (counter_0 >= 0) and (text[counter_0] == " ")):
            
                counter_0 -= 1
            
                   
            if ((counter_0 < len(text)) and (text[counter_0] == "\n")):
             
                counter_0 += 1
            
            
            
        return counter_0
        


    def handle_paste(self):
    
        cursor = self.textCursor()

        # حدد بداية السطر الحالي
        # cursor.movePosition(cursor.StartOfBlock, cursor.KeepAnchor)
    
        current_indent = cursor.selectedText()

        # تحقق من أن التحديد فعلاً تراجع فقط
        if all(c in (' ', '\t') for c in current_indent):
            cursor.removeSelectedText()

        # نفذ اللصق
        clipboard_text = QApplication.clipboard().text()
        


        current_column = cursor.positionInBlock()

        clipboard_text_1 = clipboard_text
        
        current_line_text = self.get_current_line_text_up_to_cursor(cursor)
            




        counter_0 = 0

        if (len(clipboard_text.split("\n")) > 1):
    
            
            while ((counter_0 < len(clipboard_text)) and (clipboard_text[counter_0] in (" ", "\n"))):
    
                counter_0 += 1
    
    
            if ((counter_0 < len(clipboard_text)) and (counter_0 > 0) and (not (clipboard_text[counter_0] in (" ", "\n")))):
            
                counter_0 -= 1
    
    
            while ((counter_0 >= 0) and (clipboard_text[counter_0] == " ")):
    
                counter_0 -= 1
    
                   
            if (clipboard_text[counter_0] == "\n"):
             
                counter_0 += 1
        
        



            counter_of_minimum = self.get_minimum_tab(counter_of_start=counter_0, text=clipboard_text)
        
            counter_0 = 0
            
            while ((counter_0 < counter_of_minimum)):
            
                clipboard_text_1 = self.unindentSelectedText(text=clipboard_text_1)
            
                counter_0 += 4

            counter_0 = 0
            
            while ((counter_0 < len(current_line_text)) and (counter_0 < len(current_line_text) - 3) and (current_line_text[counter_0:counter_0 + 4] == " " * 4)):
    
                clipboard_text_1 = self.indentSelectedText(text=clipboard_text_1)
            
                counter_0 += 4
            
            
            
            


        

        
        
        clipboard_text = clipboard_text_1

        if (self.semaphore_of_copy_of_1_line == True):
    
            cursor.insertText(current_line_text + "\n" + clipboard_text)    
        
    

        else:

            cursor.insertText(current_line_text + clipboard_text)


    def indentSelectedText(self, text=""):
        
        if (text == ""):    
        
            cursor = self.textCursor()
            start = cursor.selectionStart()
            end = cursor.selectionEnd()
    
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.StartOfBlock)
            start = cursor.position()
    
            cursor.setPosition(end, QTextCursor.KeepAnchor)
            cursor.movePosition(QTextCursor.EndOfBlock)
            end = cursor.position()
    
            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.KeepAnchor)
    
            text = cursor.selection().toPlainText()
            lines = text.split("\n")
            lines = [" " * 4 + line for line in lines]
    
            # استبدال النص مع حفظ التحديد بعد التعديل
            cursor.beginEditBlock()
            cursor.removeSelectedText()
            cursor.insertText("\n".join(lines))
            cursor.endEditBlock()
    
            # إعادة تحديد النص بعد التعديل
            new_start = start
            new_end = start + len("\n".join(lines))
            cursor.setPosition(new_start)
            cursor.setPosition(new_end, QTextCursor.KeepAnchor)
            self.setTextCursor(cursor)
    
    
        else:    
    
    
            lines = text.split("\n")
            lines = [" " * 4 + line for line in lines]
    
#            # استبدال النص مع حفظ التحديد بعد التعديل
#            cursor.beginEditBlock()
#            cursor.removeSelectedText()
#            cursor.insertText("\n".join(lines))
#            cursor.endEditBlock()
#    
#            # إعادة تحديد النص بعد التعديل
#            new_start = start
#            new_end = start + len("\n".join(lines))
#            cursor.setPosition(new_start)
#            cursor.setPosition(new_end, QTextCursor.KeepAnchor)
#            self.setTextCursor(cursor)
#    
            return  "\n".join(lines) 
    
    
    
    def unindentSelectedText(self, text=""):
        
        if (text == ""):
        
            cursor = self.textCursor()
            start = cursor.selectionStart()
            end = cursor.selectionEnd()
    
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.StartOfBlock)
            start = cursor.position()
    
            cursor.setPosition(end, QTextCursor.KeepAnchor)
            cursor.movePosition(QTextCursor.EndOfBlock)
            end = cursor.position()
    
            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.KeepAnchor)
    
            text = cursor.selection().toPlainText()
            lines = text.split("\n")
    
            new_list_of_line = []
    
            for line in lines:
    
                
                if ((len(line) > 0) and (line[0] == "\t")):
    
                    new_list_of_line.append(line[1:])
                
                elif ((len(line) > 3) and (line[:4] == " " * 4)):
    
                    new_list_of_line.append(line[4:])
            
                else:
    
                    new_list_of_line.append(line)
    
    
        
            while (len(lines) > 0):
        
                lines.pop(0)
        
            lines = new_list_of_line
        
    
            # lines = [line[1:] if (line.startswith("\t") or line.startswith("    ")) else line for line in lines]
    
            cursor.beginEditBlock()
            cursor.removeSelectedText()
            cursor.insertText("\n".join(lines))
            cursor.endEditBlock()
    
            # إعادة تحديد النص بعد التعديل
            new_start = start
            new_end = start + len("\n".join(lines))
            cursor.setPosition(new_start)
            cursor.setPosition(new_end, QTextCursor.KeepAnchor)
            self.setTextCursor(cursor)
    
        else:
    


            lines = text.split("\n")
    
            new_list_of_line = []
    
            for line in lines:
    
                
                if ((len(line) > 0) and (line[0] == "\t")):
    
                    new_list_of_line.append(line[1:])
                
                elif ((len(line) > 3) and (line[:4] == " " * 4)):
    
                    new_list_of_line.append(line[4:])
            
                else:
    
                    new_list_of_line.append(line)
    
    
    
            while (len(lines) > 0):
    
                lines.pop(0)
    
            lines = new_list_of_line
    
    
            # lines = [line[1:] if (line.startswith("\t") or line.startswith("    ")) else line for line in lines]
#    
#            cursor.beginEditBlock()
#            cursor.removeSelectedText()
#            cursor.insertText("\n".join(lines))
#            cursor.endEditBlock()
#    
#            # إعادة تحديد النص بعد التعديل
#            new_start = start
#            new_end = start + len("\n".join(lines))
#            cursor.setPosition(new_start)
#            cursor.setPosition(new_end, QTextCursor.KeepAnchor)
#            self.setTextCursor(cursor)
#    
    
            return "\n".join(lines)


    def selectCurrentWord(self):
        
        cursor = self.textCursor()
        
        if not cursor.hasSelection():
            
            cursor.select(QTextCursor.WordUnderCursor)
            
            self.setTextCursor(cursor)




    def insert_completion(self, completion):
        cursor = self.textCursor()
        
        cursor.beginEditBlock()
        
        if cursor.hasSelection():
            cursor.removeSelectedText()
        else:
            extra = len(self.completer.completionPrefix())
            if extra > 0:
                cursor.movePosition(QTextCursor.Left, QTextCursor.KeepAnchor, extra)
                cursor.removeSelectedText()
        
        cursor.insertText(completion)

        cursor.endEditBlock()
        self.setTextCursor(cursor)




    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(tc.WordUnderCursor)
        return tc.selectedText()



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


from PyQt5.QtWidgets import QDialog


class FindWidget(QDialog):


    def __init__(self, parent=None):
    
        super().__init__(parent)
    
    
        # self.setWindowFlags(Qt.Tool | Qt.FramelessWindowHint)
        
        
        
        # self.setFixedHeight(40)


        self.setWindowFlags(Qt.Window | Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.setModal(False)


        # self.setWindowFlags(Qt.Widget)


        self.setWindowTitle("find")
        
        self.setFixedSize(400, 60)



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

        self.next_btn.clicked.connect(self.find_next)
        self.prev_btn.clicked.connect(self.find_prev)
        self.close_btn.clicked.connect(self.hide)
        self.line_edit.textChanged.connect(self.highlight_all)

        self.editor = None
        self.last_search = ""
        self.current_pos = 0

        QShortcut(QKeySequence("Esc"), self, self.close)





        self.counter_label = QLabel("0 of 0")  # عداد النتائج

        # ✏️ أضف هذا قبل أو بعد self.close_btn
        
        layout.addWidget(self.counter_label)



        self.matches = []  # قائمة مؤشرات النتائج
        
        self.current_index = -1  # أين نحن داخل القائمة




        self.setLayout(layout)


    


    def open_with_selected_text(self):
        
        
        try:
            
            if not self.editor:
                return

            cursor = self.editor.textCursor()
            if cursor.hasSelection():
                selected_text = cursor.selectedText()
                self.line_edit.setText(selected_text)
                self.highlight_all()  # اختيارية: تبدأ البحث مباشرة

            self.show()
            self.raise_()
            self.activateWindow()
            self.line_edit.setFocus()
        
        
        except Exception as e:

            print("e = ", e)

            semaphore = True



    def manual_find_positions(self, word):
        import re

        try:

            text = self.editor.toPlainText()

            # امنع مشاكل regex إن كانت الكلمة فيها رموز خاصة
            escaped = re.escape(word)

            # ابحث عن كل التطابقات في النص الكامل
            matches = list(re.finditer(escaped, text))

            # أنشئ قائمة بمواقع البداية والنهاية الدقيقة
            return [(m.start(), m.end()) for m in matches]
                
        except Exception as e:

            print("e = ", e)

            semaphore = True

            return []



    def find_next(self):
    
        try:

            if not self.matches:
                self.highlight_all()
            if not self.matches:
                return

            self.current_index = (self.current_index + 1) % len(self.matches)
            pos = self.matches[self.current_index]

            cursor = self.editor.textCursor()
            cursor.setPosition(pos)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.line_edit.text()))
            self.editor.setTextCursor(cursor)
            self.editor.centerCursor()

            self.counter_label.setText(f"{self.current_index + 1} of {len(self.matches)}")


            
        except Exception as e:

            print("e = ", e)

            semaphore = True




    def find_prev(self):

        try:
#
#            text = self.line_edit.text()
#            if not text:
#                return
#
#            document = self.editor.document()
#            cursor = self.editor.textCursor()
#            found_cursor = document.find(text, cursor, QTextDocument.FindBackward)
#
#            if not found_cursor.isNull():
#                self.editor.setTextCursor(found_cursor)
#                self.editor.centerCursor()
#            else:
#                QMessageBox.information(self, "Not Found", f"'{text}' not found.")
#




            if not self.matches:
                self.highlight_all()
            if not self.matches:
                return

            self.current_index = (self.current_index - 1) % len(self.matches)
            pos = self.matches[self.current_index]

            cursor = self.editor.textCursor()
            cursor.setPosition(pos)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.line_edit.text()))
            self.editor.setTextCursor(cursor)
            self.editor.centerCursor()

            self.counter_label.setText(f"{self.current_index + 1} of {len(self.matches)}")

        
        except Exception as e:

            print("e = ", e)

            semaphore = True



    def highlight_all(self):
    
    
        try:
        
            self.matches.clear()
            self.current_index = -1
            text = self.line_edit.text()
            if not text or not self.editor:
                self.counter_label.setText("0 of 0")
                return

            cursor = self.editor.textCursor()
            cursor.movePosition(QTextCursor.Start)
            document = self.editor.document()

            while True:
                found_cursor = document.find(text, cursor)
                if found_cursor.isNull():
                    break
                self.matches.append(found_cursor.selectionStart())
                cursor = found_cursor

            total = len(self.matches)
            self.counter_label.setText(f"0 of {total}")


            # 🎨 تحديد خافت
            extra_selections = []
            format = QTextCharFormat()
            format.setBackground(QColor(180, 180, 180, 100))  # رمادي شفاف

#            print("self.matches[0] = ", self.matches[0])

            for pos in self.matches:
                selection = QTextEdit.ExtraSelection()
                cursor = QTextCursor(self.editor.document())
                
                

                cursor.setPosition(pos)
                cursor.setPosition(pos + len(text), QTextCursor.KeepAnchor)
        
                # cursor.setPosition(start)
                # cursor.setPosition(end, QTextCursor.KeepAnchor)
                
                
                selection.cursor = cursor
                selection.format = format
                extra_selections.append(selection)

            self.editor.setExtraSelections(extra_selections)



        
        except Exception as e:

            print("e = ", e)

            semaphore = True



    def set_editor(self, editor):

        try:

            self.editor = editor
            self.matches.clear()
            self.current_index = -1
            self.counter_label.setText("0 of 0")


        
        except Exception as e:

            print("e = ", e)

            semaphore = True







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
    
        cursor = self.editor.textCursor()
        initial_position = cursor.position()
    
        doc = self.editor.document()
        cursor.beginEditBlock()
    
        count = 0
        temp_cursor = QTextCursor(doc)
        while True:
            found = doc.find(search_text, temp_cursor)
            if found.isNull():
                break
            found.insertText(replace_text)
            temp_cursor = found
            count += 1
    
        cursor.endEditBlock()
    
        # إعادة المؤشر لمكانه السابق
        cursor.setPosition(initial_position)
        self.editor.setTextCursor(cursor)
    
        if count == 0:
            QMessageBox.information(self, "Info", "No matches found.")
        else:
            QMessageBox.information(self, "Success", f"Replaced {count} occurrence(s).")
    

#
#    def replace_all(self):
#        search_text = self.search_input.text()
#        replace_text = self.replace_input.text()
#
#        if not search_text:
#            QMessageBox.warning(self, "Warning", "Search term is empty.")
#            return
#
#        full_text = self.editor.toPlainText()
#        new_text = full_text.replace(search_text, replace_text)
#
#        if full_text == new_text:
#            QMessageBox.information(self, "Info", "No matches found.")
#        else:
#            self.editor.setPlainText(new_text)
#            QMessageBox.information(self, "Success", f"All '{search_text}' replaced with '{replace_text}'.")
#
#

from PyQt5.QtCore import QModelIndex

from PyQt5.QtWidgets import QStatusBar


from PyQt5.QtGui import QColor, QBrush



from PyQt5.QtWidgets import QInputDialog, QMessageBox
import os

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QSplitter, QWidget, QVBoxLayout


from PyQt5.QtWidgets import QSplitter





import sys






from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPlainTextEdit, QSplitter, QLineEdit
from PyQt5.QtCore import QProcess, Qt



class TerminalWidget(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(False)
        self.process = QProcess(self)
        self.process.readyReadStandardOutput.connect(self.handle_stdout)
        self.process.readyReadStandardError.connect(self.handle_stderr)
#        self.process.start("/bin/bash")  # في ويندوز استخدم: "cmd"

        self.process.start("/bin/bash", ["-i"])


        self.prompt = ""
        self.insertPlainText(self.prompt)
        self.user_input = ""

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            if len(self.user_input) > 0:
                self.user_input = self.user_input[:-1]
                self.textCursor().deletePreviousChar()
            return

        elif event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.appendPlainText("")
            self.process.write((self.user_input + "\n").encode())
            self.user_input = ""
            return

        else:
            char = event.text()
            if char:
                self.user_input += char
                self.insertPlainText(char)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput().data().decode()
        self.insertPlainText(data)
        self.insertPlainText(self.prompt)

    def handle_stderr(self):
        data = self.process.readAllStandardError().data().decode()
        self.insertPlainText(data)
        self.insertPlainText(self.prompt)

from PyQt5.QtWidgets import QScrollArea

import time

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt5.QtCore import QTimer, QTime

class TerminalPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)



        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # الحاوية التي ستوضع داخل scroll
        container = QWidget()
        scroll_area.setWidget(container)

        # نستخدم layout عادي في الحاوية لتتمكن من التوسعة بسهولة
        layout = QVBoxLayout(container)


        size_of_font = size_of_font_of_horloge
        
        # نص طويل أو عنصر نريد وضعه بحرية
        self.label = QLabel("", container)  # مكرر 50 مرة
        self.label.setStyleSheet(f"font-size: {size_of_font}pt;")

        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # محاذاة من الأعلى
        self.label.setWordWrap(True)  # التفاف النص تلقائيًا

        layout.addWidget(self.label)


        self.size_of_font = size_of_font

        self.unity_1 = ["computer", 0]
        
        
        

        
        self.unity_0 = ["computer", "develope", "i"]
        
        self.unity_2 = ["computer", "not_sleep", "not_stop", "comfort", "lust"]
        
        
                
        self.unity_3 = []
        
        
        self.unity_1 = []
        
        
        counter_0 = 0
        
        while (counter_0 < len(self.unity_0)):
        
            self.unity_1.append([self.unity_0[counter_0], 0])
        
            counter_0 += 1
        
        
                
        counter_0 = 0
        
        while (counter_0 < len(self.unity_2)):
        
            self.unity_3.append([self.unity_2[counter_0], 0])
        
            counter_0 += 1
        
        
        self.incrimentor = 1_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000_000
        
        
        
        self.file_of_store = os.path.join(os.getcwd(), "file_of_store.txt")
        
        try:
            
            with open(self.file_of_store, "r") as f_:
            
                s = f_.read(os.path.getsize(self.file_of_store))
                
            v_0 = s.split("\n")
            
            
            
            
            
            counter_1 = 0
            
            
            while (counter_1 < len(self.unity_1)):
                
                counter_0 = 0
                
                
                while ((counter_0 < len(v_0))):
                
                    
                    if (v_0[counter_0] != ""):
                    
                        v_1 = v_0[counter_0].split(";")
                    
                        if (v_1[0] == self.unity_1[counter_1][0]):
                        
                            self.unity_1[counter_1][1] = int(v_1[1])
                        

                    counter_0 += 1
                
                counter_1 += 1
            
            
        except:
        
            semaphore = True
            
            
                
        try:
            
            with open(self.file_of_store, "r") as f_:
            
                s = f_.read(os.path.getsize(self.file_of_store))
                
            v_0 = s.split("\n")
            
            
            counter_1 = 0
            
            
            while (counter_1 < len(self.unity_3)):
                
                counter_0 = 0
                
                
                while ((counter_0 < len(v_0))):
                
                    
                    if (v_0[counter_0] != ""):
                    
                        v_1 = v_0[counter_0].split(";")
                    
                        if (v_1[0] == self.unity_3[counter_1][0]):
                        
                            self.unity_3[counter_1][1] = int(v_1[1])
                    

                                                
                        else:
                        
                            counter_2 = 0
                            
                            while ((counter_2 < len(self.unity_3)) and (v_1[0] != self.unity_3[counter_2][0])):
                            
                                counter_2 += 1
                            
                            if (counter_2 >= len(self.unity_3)):
                            
                                self.unity_3.append([v_1[0], int(v_1[1])])
                            
                        
                        
                        
                    counter_0 += 1
                
                counter_1 += 1
            
            
        except:
        
            semaphore = True
                
            
            
        self.unity_1 = sort_element_0(l=self.unity_1)            
            
        self.unity_3 = sort_element_0(l=self.unity_3)            
            
            
            
        
        
        counter_0 = 0

        while ((counter_0 < len(self.unity_3)) and (self.unity_3[counter_0][0] != "computer")):

            counter_0 += 1
            
        self.unity_terme = self.unity_3[counter_0] 
        
            
            
        # ⏱️ تحديث الساعة كل ثانية
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # كل 1000ms (1 ثانية)
        self.update_clock()  # تحديث فوري أول مرة


        self.size_of_squer = [500, 100]


        self.text_input = QLineEdit()
        
        
        
                
        self.text_input.setFixedSize(self.size_of_squer[0], self.size_of_squer[1])
        

        font = QFont()
        font.setPointSize(22)  # حجم الخط، مثلاً 16 نقطة
        self.text_input.setFont(font)
        
        self.text_input.textChanged.connect(self.on_text_changed)

        
        layout.addWidget(self.text_input)
        
        
        
        
        self.list_of_combobox = [element[0] for element in self.unity_3]
        
        

        # قائمة منسدلة وزر (كمثال)
        self.combo = QComboBox()
        self.combo.addItems(self.list_of_combobox)
        
        self.combo.setStyleSheet(f"font-size: {size_of_font}pt;")
        
        self.combo.setFixedSize(self.size_of_squer[0], self.size_of_squer[1])

        
        layout.addWidget(self.combo)


    

        self.button = QPushButton("Run unity")
        
        self.button.setStyleSheet(f"font-size: {size_of_font}pt;")
        
        self.button.setFixedSize(self.size_of_squer[0], self.size_of_squer[1])
        
        layout.addWidget(self.button)

        self.button.clicked.connect(self.print_selected_command)

        
        
                
        
        self.button = QPushButton("Add unity")
        
        self.button.setStyleSheet(f"font-size: {size_of_font}pt;")
        
        self.button.setFixedSize(self.size_of_squer[0], self.size_of_squer[1])
        
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.add_unity)
        

                
        self.button = QPushButton("Delete unity")
        
        self.button.setStyleSheet(f"font-size: {size_of_font}pt;")
        
        self.button.setFixedSize(self.size_of_squer[0], self.size_of_squer[1])
        
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.delete_unity)
        


        # Layout للنافذة الرئيسية
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)


        self.setLayout(main_layout)


        
        self.text_from_text_input = ""
        
    def on_text_changed(self, text):
    
        self.text_from_text_input = text
    

    def add_unity(self):
    
        if ((self.text_from_text_input != "")):
        
        
            counter_0 = 0
            
            while ((counter_0 < len(self.unity_3)) and (self.unity_3[counter_0][0] != self.text_from_text_input)):
            
                counter_0 += 1
        
            if (counter_0 >= len(self.unity_3)):
    
                self.unity_3.append([self.text_from_text_input, 0])
        
                
                self.unity_3 = sort_element_0(l=self.unity_3)
                
                self.list_of_combobox.append(self.text_from_text_input)
                
                
                self.list_of_combobox = sort_element_0(l=self.list_of_combobox)
                
                self.combo.clear()
                
                self.combo.addItems(self.list_of_combobox)
                
        
    def delete_unity(self):
    
                
        if ((self.text_from_text_input != "")):
        
        
            counter_0 = 0
            
            while ((counter_0 < len(self.unity_3)) and (self.unity_3[counter_0][0] != self.text_from_text_input)):
            
                counter_0 += 1
        
            if (counter_0 < len(self.unity_3)):
        
                self.unity_3.pop(counter_0)
        
        
                
                self.unity_3 = sort_element_0(l=self.unity_3)
                                
                self.list_of_combobox.pop(counter_0)
                
                
                
                self.list_of_combobox = sort_element_0(l=self.list_of_combobox)
                
                self.combo.clear()
                
                
                self.combo.addItems(self.list_of_combobox)
                

        

    
    def print_selected_command(self):
    
        selected_command = self.combo.currentText()
    
        counter_0 = 0
        
        while ((counter_0 < len(self.unity_3)) and (self.unity_3[counter_0][0] != selected_command)):
        
            counter_0 += 1
    
        if (counter_0 < len(self.unity_3)):
        
            self.unity_terme = self.unity_3[counter_0]
    

    
    
    def set_label_font_size(self, size):
        font = self.label.font()
        font.setPointSize(size)
        self.label.setFont(font)
    
        
    def i_number_to_str(self, number):
    
        string_0 = str(number)
    
        counter_4 = len(string_0) - 1
    
        counter_5 = 0
    
        string_1 = ""
    
        while (counter_4 >= 0):
    
            if (counter_5 == 3):
    
                string_1 = "_" + string_1
    
                counter_5 = 0
    
            string_1 = string_0[counter_4] + string_1
    
    
            counter_4 -= 1
    
            counter_5 += 1
    
    
        return string_1
    

    def update_clock(self):




        
        current_text = ""
        
        
        self.unity_terme[1] += self.incrimentor
        
#        self.unity_1[0][1] += self.incrimentor
        
        current_text += f"-> ( {self.unity_terme[0]} ) {self.i_number_to_str(self.unity_terme[1])} (0, 1)\n"
        
        
        current_text += f"-> the quality of ( {self.unity_terme[0]} ) {self.i_number_to_str(self.unity_terme[1])} (0, 1)\n"
        
        
        
        self.unity_1[1][1] += self.incrimentor
        
        current_text += f"-> ( {self.unity_1[1][0]} ) {self.i_number_to_str(self.unity_1[1][1])} (0, 1)\n"
        
        
        current_text += f"-> the quality of ( {self.unity_1[1][0]} ) {self.i_number_to_str(self.unity_1[1][1])} (0, 1)\n"
        
        
        self.unity_1[2][1] += self.incrimentor
        
        current_text += f"-> ( {self.unity_1[2][0]} ) {self.i_number_to_str(self.unity_1[2][1])} (0, 1)\n"
        
        
        current_text += f"-> the quality of ( {self.unity_1[2][0]} ) {self.i_number_to_str(self.unity_1[2][1])} (0, 1)\n"
        
       
                
        with open(self.file_of_store, "w") as f_:
        
            
            
            content = ""
    
            
            counter_1 = 0
            
            
            while (counter_1 < len(self.unity_1)):
                
                content += str(self.unity_1[counter_1][0]) + ";" + str(self.unity_1[counter_1][1]) + "\n"
                
                counter_1 += 1
                
            

            counter_1 = 0
                        
            while (counter_1 < len(self.unity_3)):
                
                content += str(self.unity_3[counter_1][0]) + ";" + str(self.unity_3[counter_1][1]) + "\n"
                
                counter_1 += 1
                
            
                                    
            
            f_.write(content)
                    
        
        
        
        try:
        
            current_text += f"\n{time.strftime("%Y / %m / %d  %A / %B  %H : %M : %S")}\n"
        
        except:
        
            semaphore = True
        
        
        self.label.setText(f"{current_text}")


from PyQt5.QtCore import QTimer


import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar
from PyQt5.QtGui import QPalette, QColor



from PyQt5.QtWidgets import QInputDialog, QMessageBox
    


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




class MainWindow(QMainWindow):
    
    
    def closeEvent(self, event):
        
        
        reply = QMessageBox.question(
            self,
            "Confirm closure",
            "Are you sure you want to close the editor?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            
            event.accept()
            
            
            self.function_of_close()
            

        else:
            event.ignore()


    def function_of_close(self):


                
        
        with open(os.path.join(cwd, "path_of_root.txt"), "w") as f:
        
            f.write(self.path_of_root)
 
 

        content = ""
        
        counter_0 = 0 
        
        while (counter_0 < self.tabs.count()):
        
        
            editor = self.tabs.widget(counter_0)
    
            if hasattr(editor, "file_path") and editor.file_path:
        
                cursor = editor.textCursor()
            
                line_number = cursor.blockNumber()
            
                content += editor.file_path + ";" + str(line_number) + "\n"
            
        
            counter_0 += 1      
        

        file = os.path.join(cwd, "file_of_lines.txt")
        
        with open(file, "w") as f_:
        
            f_.write(content)


        with open(os.path.join(cwd, "last_active_tab.txt"), "w") as f:
            
            f.write(str(self.tabs.currentIndex()))
        
        
        
        self.write_list_of_path_on_file()
        
        self.save_expanded_paths()
        
        
        
    def save_expanded_paths(self):
        expanded_paths = []
    
        def recurse(index):
            if not index.isValid():
                return
            if self.tree.isExpanded(index):
                path = self.model.filePath(index)
                expanded_paths.append(path)
            for row in range(self.model.rowCount(index)):
                child = self.model.index(row, 0, index)
                recurse(child)
    
        root_index = self.tree.rootIndex()
        recurse(root_index)
    
        with open(os.path.join(cwd, "expanded_paths.txt"), "w") as f:
            for path in expanded_paths:
                f.write(path + "\n")
    
    
    
    def restore_expanded_paths(self):
        try:
            with open(os.path.join(cwd, "expanded_paths.txt"), "r") as f:
                paths = [line.strip() for line in f if line.strip()]
    
            for path in paths:
                index = self.model.index(path)
                if index.isValid():
                    self.tree.expand(index)
        except FileNotFoundError:
            pass
    

    def move_cursor_to_line(self, editor, line_number):

        doc = editor.document()
        
        # الحصول على الـ QTextBlock المقابل للسطر المطلوب
        block = doc.findBlockByNumber(line_number)
        
        if block.isValid():
            cursor = editor.textCursor()
            cursor.setPosition(block.position())
            editor.setTextCursor(cursor)
            
            # ⭐ تمرير العرض تلقائيًا للسطر الحالي
            editor.centerCursor()
    


    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("edit-or of code ==> file : " + sys.argv[0])
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
        self.tree.setColumnWidth(0, 1000)

        self.model.setRootPath(QDir.rootPath())
        self.tree.setModel(self.model)


        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        
        self.tree.customContextMenuRequested.connect(self.show_explorer_context_menu)
        
        self.tree.clicked.connect(self.open_file_from_tree)


        self.number_theme = 4

        self.theme = 0  # تتبع الثيم الحالي

        try:
            
            self.file_of_theme = os.path.join(os.getcwd(), "theme.txt")
        
            with open(self.file_of_theme, "r") as f_:
            
                s = f_.read(os.path.getsize(self.file_of_theme))
                
            
        
            self.theme = int(s)  # تتبع الثيم الحالي
        
        
        except Exception as e:
        
            semaphore = True
            
            

        self.make_theme(theme=self.theme)
             
        

        # 3. التبويبات
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab_by_index)
        self.tabs.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabs.customContextMenuRequested.connect(self.show_tab_context_menu)
    
                
        self.tabs.setStyleSheet("""
            QTabBar::tab {
                background: #222;
                color: #ccc;
                padding: 6px;
            }
            QTabBar::tab:selected {
                background: #444;
                color: white;
            }
            QTabWidget::pane {
                border: 1px solid #333;
            }
        """)
        



        self.tab_file_paths = []

        self.new_tab()



        # ⬅️ 1. مستعرض بنية الكود
        self.structure_view = QTreeWidget()
        self.structure_view.setHeaderHidden(True)
        self.structure_view.itemClicked.connect(lambda item: self.go_to_line_in_editor(item))

        # ⬅️ 2. تقسيم رأسي: ملفات + بنية الكود
        left_panel = QSplitter(Qt.Vertical)
        left_panel.addWidget(self.tree)
        left_panel.addWidget(self.structure_view)
        left_panel.setStretchFactor(0, 3)
        left_panel.setStretchFactor(1, 2)




        # ⬅️ تقسيم عمودي: تبويبات المحرر + التيرمينال
        right_panel = QSplitter(Qt.Vertical)
        right_panel.addWidget(self.tabs)

        # التيرمينال في الأسفل
#        self.terminal = TerminalWidget()
        
#        
#        self.terminal = TerminalPanel()
#        
#        
#        right_panel.addWidget(self.terminal)
#        right_panel.setStretchFactor(0, 4)
#        right_panel.setStretchFactor(1, 1)
#
        
        
        self.terminal_tabs = QTabWidget()
        
        # إنشاء أول تبويب للتيرمينال
        terminal1 = TerminalPanel()
        self.terminal_tabs.addTab(terminal1, "horloge")
        
        # إذا أردت تبويبات أخرى لاحقاً:
        
        terminal2 = TerminalPanel()
        
        self.terminal_tabs.addTab(terminal2, "Tab 2")
        
        # إضافة التبويبات إلى right_panel بدلاً من self.terminal
        right_panel.addWidget(self.terminal_tabs)
        right_panel.setStretchFactor(0, 4)
        right_panel.setStretchFactor(1, 1)







                
        # ⬅️ تقسيم أفقي: يسار (شجرتين) ويمين (المحرر + التيرمينال)
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.addWidget(left_panel)
        main_splitter.addWidget(right_panel)
        main_splitter.setStretchFactor(1, 3)
        
        
        
        



        # ⬅️ 4. إعداد التخطيط العام
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(main_splitter)
        container.setLayout(layout)
        self.setCentralWidget(container)



        # # 5. الحاوية
        # container = QWidget()
        # layout = QVBoxLayout()
        
        # layout.addWidget(splitter)

        layout.addWidget(main_splitter)

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

        file_menu.addAction(self.create_action("change theme", "Ctrl+T+C", self.toggle_theme))


        file_menu.addAction(self.create_action("🔄 Refresh Explorer", "F5", self.refresh_tree_view))
        



        file_menu.addAction(self.create_action("Download From github", "Ctrl+U+D", self.Download_from_github))
        
        
        file_menu.addAction(self.create_action("UpDate", "Ctrl+U+D+R", self.UpDate_file))
        
        
        file_menu.addAction(self.create_action("restart", "Ctrl+U+D+R+S", self.restart))
        
        
        

        
        



        # 🎯 اختصارات التراجع والإعادة
        
        undo_shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        undo_shortcut.activated.connect(self.trigger_undo)

        redo_shortcut = QShortcut(QKeySequence("Ctrl+Shift+Z"), self)
        redo_shortcut.activated.connect(self.trigger_redo)

        replace_shortcut = QShortcut(QKeySequence("Ctrl+H"), self)
        
        replace_shortcut.activated.connect(self.show_replace_widget)


        edit_menu = menu.addMenu("edit")
        
        edit_menu.addAction(self.create_action("Undo", "Ctrl+Z", self.trigger_undo))
        edit_menu.addAction(self.create_action("Redo", "Ctrl+Shift+Z", self.trigger_redo))


        edit_menu.addAction(self.create_action("highlighter of Python", "Ctrl+H+P", self.highlighter_of_Python))
        edit_menu.addAction(self.create_action("highlighter of C", "Ctrl+H+C", self.highlighter_of_C))


        self.lines_in_codeEditer = []

        try:

                        
            file_0 = os.path.join(cwd, "file_of_lines.txt")
            
            with open(file_0, "r") as f_:
            
                content = f_.read(os.path.getsize(file_0))
            
            
            v_0 = content.split("\n")
            
            
            counter_0 = 0
            
            while (counter_0 < len(v_0)):
            
                if (v_0[counter_0] != ""):
            
                    v_1 = v_0[counter_0].split(";")
                    

                    if (len(v_1) == 2):

                        self.lines_in_codeEditer.append([v_1[0], int(v_1[1])])
                    
            
                counter_0 += 1
            
        
        except:
        
            semaphore = True



        # استرجاع الملفات المفتوحة سابقًا
        self.opened_files_path = os.path.join(os.getcwd(),"opened_files.json")

        if os.path.exists(self.opened_files_path):
            try:
                with open(self.opened_files_path, "r", encoding="utf-8") as f:
                    paths = json.load(f)
                for path in paths:
                    if os.path.exists(path):
                        with open(path, "r", encoding="utf-8") as file:


                            editor = CodeEditor()


                            text = file.read()

                            editor.setPlainText(text)

                            editor.document().modificationChanged.connect(lambda modified, ed=editor: self.on_editor_modification_changed(ed))
                            


                            editor.file_path = path

                            editor.file_of_tabs = self.opened_files_path

                            editor.time_of_last_modification_of_file = os.path.getmtime(path)

                            index = self.tabs.addTab(editor, os.path.basename(path))
                            
                            # print("editor.file_path = ", editor.file_path)

#                            self.tab_file_paths[index] = path
                            
                            
                                

                            self.tab_file_paths.append(path)
                            
                            editor.index = index

                if self.tabs.count() > 0:
                    self.tabs.setCurrentIndex(0)

            except Exception as e:
                print("error upload-ing the file :", e)


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



        self.find_widget = FindWidget(self)
        self.find_widget.set_editor(self.current_editor())
        self.find_widget.hide()

        # ربط Ctrl+F لفتح نافذة البحث
        self.find_shortcut = QShortcut(QKeySequence("Ctrl+F"), self)
        self.find_shortcut.activated.connect(self.toggle_find)


        self.file_check_timer = QTimer(self)
        self.file_check_timer.timeout.connect(self.refrech_load)
        self.file_check_timer.start(3000)  # كل 3 ثواني

        self.ctrl_s_press_ed = False


        self.setStatusBar(QStatusBar())


        self.tabs.currentChanged.connect(lambda _: self.function_of_tabs_currentChanged_connect())


                
        try:
        
            file_path = os.path.join(cwd, "last_active_tab.txt")
        
            if os.path.exists(file_path):
        
                with open(file_path, "r") as f:
        
                    index = int(f.read())
        
                    if 0 <= index < self.tabs.count():
        
                        self.tabs.setCurrentIndex(index)
        
        except:
         
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            



        self.restore_expanded_paths()



    def restart(self):
    
          
                

    


        try:
            reply = QMessageBox.question(
                self,
                "Notification",
                "You are sure you want restart?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
    
            if reply == QMessageBox.Yes:
    
    
                
                self.function_of_close()
                
    
    

                                
                                
                system = platform.system()
                
                if system == "Windows":
                
                    subprocess.run(["cmd", "/c", f"python \"{NAME_OF_FILE}\""])
                
                elif system == "Linux":
                
                    subprocess.run(["gnome-terminal", "--", "bash", "-c", f"python3 \"{NAME_OF_FILE}\"; exit"])
                
                elif system == "Darwin":
                
                    subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "python3 \"{NAME_OF_FILE}\"; exit"'])
                
                



                QApplication.quit()
    
        except:


            
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
            

    
    
    
    
    
    def dupliquor(self, duplication_place, folder_of_source):
    
    

        dirs = [""]
        
        srcs = [""]
        

        counter_1 = 0
        
        while (counter_1 < len(dirs)):
        
        
            files = []
            
            
            dirs_ = []
        
        
            for root, dirs_, files in os.walk(os.path.join(folder_of_source, dirs[counter_1])):
        
                break
        

        
            counter_0 = 0
        
            while (counter_0 < len(dirs_)):
        
                dirs.append(os.path.join(dirs[counter_1], dirs_[counter_0]))
        
                srcs.append(os.path.join(srcs[counter_1], dirs_[counter_0]))
        
                counter_0 += 1
        

                        
            

                
            src_ = os.path.join(folder_of_source, srcs[counter_1])
            
            dist_ = os.path.join(duplication_place, dirs[counter_1])
        
            if (not (os.path.exists(dist_))):
        
                os.makedirs(dist_)
        



            

            counter_0 = 0
        
            while (counter_0 < len(files)):
        
                try:
        




                    d = Path(os.path.join(src_, files[counter_0]))
    
                    d_ = Path(os.path.join(dist_, files[counter_0]))
    
    
                    d_.write_bytes(d.read_bytes())
    

                        
        
                except:
        
                                
                    traceback.print_exc()
                    
                    error = traceback.format_exc()
                    
                    semaphore = True
        
                    print(f"Erreur : {str(error)}")
        
        
        
                
                counter_0 += 1
        
        
            counter_1 += 1
        
        


    
    
    


    def UpDate_file(self):
    
    
        # Special_Link_0/i_principal_central_1-main/i_nuclus/i_editor_of_code
        
        
        
        try:
            
            path_to = os.getcwd()
            
            path_from = os.path.join(os.getcwd(), "Special_Link_0", "i_principal_central_1-main", "i_nuclus", "i_editor_of_code")
        
        
            print(f"path_to = {path_to} . path_from = {path_from} .")
            
            
            self.dupliquor(duplication_place=path_to, folder_of_source=path_from)

                        
            reply = QMessageBox.question(
                self,
                "UpDate",
                "UpDate is finish-ed with success .\nYou should restart",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            
            if reply == QMessageBox.Yes:
                
                

                
                self.function_of_close()
                



                                 
                                
                system = platform.system()
                
                if system == "Windows":
                
                    subprocess.run(["cmd", "/c", f"python \"{NAME_OF_FILE}\""])
                
                elif system == "Linux":
                
                    subprocess.run(["gnome-terminal", "--", "bash", "-c", f"python3 \"{NAME_OF_FILE}\"; exit"])
                
                elif system == "Darwin":
                
                    subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "python3 \"{NAME_OF_FILE}\"; exit"'])
                
                
                



         
                QApplication.quit()
                
                
        except Exception as e:
            
            print(f"error :  {e}")
    

    def get_expanded_dirs(self):
        expanded_dirs = []
        model = self.tree.model()
        root_index = self.tree.rootIndex()
    
        def recurse(index):
            if not index.isValid():
                return
            if self.tree.isExpanded(index):
                dir_path = model.filePath(index)
                expanded_dirs.append(dir_path)
            for i in range(model.rowCount(index)):
                child = model.index(i, 0, index)
                recurse(child)
    
        recurse(root_index)
        return expanded_dirs
    
    def restore_expanded_dirs(self, dirs_to_expand):
        model = self.tree.model()
    
        for dir_path in dirs_to_expand:
            index = model.index(dir_path)
            if index.isValid():
                self.tree.expand(index)
    
    
    def open_popup_terminal(self, command):
        
        
        system = platform.system()

        if system == "Windows":

            subprocess.run(["cmd", "/c", f"{command} && timeout 10"])

        elif system == "Linux":

            subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command}; sleep 10; exit"])

        elif system == "Darwin":

            subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command}; sleep 10; exit"'])

    


    def Download_from_github(self):
    
    
    


        content = r"""



import os


os.system("pip install requests")





import requests

import zipfile

import io


# https://github.com/IPrincipalCentral1/i_principal_central_1


url = "https://github.com/IPrincipalCentral1/i_principal_central_1/archive/refs/heads/main.zip"


try:
    
    
    
    
    
    print("download from github is in start ...")
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
    
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
    
            zip_ref.extractall("Special_Link_0")
    
    
        print("finish : ", "Download complete with success .")

    

    else:
    
    
        print("finish : ", f"Download Fail-ed: {response.status_code} ")

except Exception as e:    

        semaphore = True

        print("finish : ", f"Download Fail-ed: {e} ")

            """
            
            
            
        path = os.path.join(os.getcwd(), "editor_of_code", "program")
            
            
        os.makedirs(path, exist_ok=True)
        
        file = os.path.join(path, "downloader_from_github.py")
        
        with open(file, "w") as f_:
        
            f_.write(content)
            
           
           
        
                
        system = platform.system()
        
        if system == "Windows":
        
        
            self.open_popup_terminal(command="python " + file)

        elif system == "Linux":
        
        
            self.open_popup_terminal(command="python3 " + file)
            
                    
        elif system == "Darwin":
        
            self.open_popup_terminal(command="python3 " + file)
        
    
    
    def on_editor_modification_changed(self, editor):
        index = self.tabs.indexOf(editor)
        if index == -1:
            return
    
        file_name = os.path.basename(editor.file_path) if editor.file_path else "new tab"
        if editor.document().isModified():
            file_name += "*"
    
        self.tabs.setTabText(index, file_name)
    

    
    def setNightModeStyle(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1e1e1e;
            }
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                selection-background-color: #264f78;
                font-family: 'Courier New';
                font-size: 12pt;
            }
            QMenuBar {
                background-color: #2b2b2b;
                color: #ffffff;
            }
            QMenuBar::item:selected {
                background-color: #3c3c3c;
            }
            QTabBar::tab {
                background-color: #2e2e2e;
                color: #cccccc;
                padding: 5px;
            }
            QTabBar::tab:selected {
                background-color: #444444;
                color: #ffffff;
            }
        """)



    
    
        
    def make_theme(self, theme):    
    
                
        if (self.theme == 0):
        
            apply_light_theme(QApplication.instance())
        
        
        elif (self.theme == 1):
        
            apply_night_classic(QApplication.instance())
        
                
        elif (self.theme == 2):
        
            apply_night_violet(QApplication.instance())
        
                
        elif (self.theme == 3):
        
            apply_night_hacker(QApplication.instance())
        
             
    

    
    def toggle_theme(self):
        
                
        self.theme += 1
        
        if (self.theme >= self.number_theme):
        
            self.theme = 0
        
        
        print(f"self.theme = {self.theme}")
        
    
        self.make_theme(theme=self.theme)
        
        with open(self.file_of_theme, "w") as f_:
        
            f_.write(str(self.theme))
    
    

    def function_of_tabs_currentChanged_connect(self):



        editor = self.current_editor()





    

        if ((hasattr(editor, "file_path")) and (editor.file_path) and (editor.position_of_curser == -1)):

  

  
            counter_0 = 0
            
            while ((counter_0 < len(self.lines_in_codeEditer)) and (self.lines_in_codeEditer[counter_0][0] != editor.file_path)):
            
                counter_0 += 1
                
                

            if (counter_0 < len(self.lines_in_codeEditer)):
            
                
                self.move_cursor_to_line(editor=editor, line_number=self.lines_in_codeEditer[counter_0][1])
    

        self.update_code_structure_view()

        self.connect_cursor_movement()

        

        
    
    def on_cursor_moved(self):
        
        cursor = self.textCursor()
        
        line = cursor.blockNumber() + 1
        
        column = cursor.positionInBlock() + 1
    
    
        return column, line
    


    def on_cursor_position_changed(self):
        editor = self.current_editor()
        if editor:
            cursor = editor.textCursor()
            current_line = cursor.blockNumber()
            self.select_structure_item_by_line(current_line)



    # def connect_cursor_movement(self):
    #     editor = self.current_editor()
    #     if editor:
    #         editor.cursorPositionChanged.disconnect() if editor.cursorPositionChanged.receivers() > 0 else None
    #         editor.cursorPositionChanged.connect(self.on_cursor_position_changed)



    def update_structure_selection(self):
        editor = self.current_editor()
        if not editor:
            return
        
        
        
        cursor = editor.textCursor()
        line = cursor.blockNumber()
        self.select_structure_item_by_line(line)

        editor.position_of_curser = line



    def connect_cursor_movement(self):
        editor = self.current_editor()
        if editor:
            try:
                editor.cursorPositionChanged.disconnect()
            except TypeError:
                pass
            editor.cursorPositionChanged.connect(self.update_structure_selection)



    # def select_structure_item_by_line(self, line):
    #     def recursive_search(item):
    #         selected_item = None
    #         for i in range(item.childCount()):
    #             child = item.child(i)
    #             if hasattr(child, "line_number") and child.line_number <= line:
    #                 candidate = recursive_search(child)
    #                 selected_item = candidate if candidate else child
    #         return selected_item

    #     root = self.structure_view.invisibleRootItem()
    #     item_to_select = None
    #     for i in range(root.childCount()):
    #         top_item = root.child(i)
    #         if hasattr(top_item, "line_number") and top_item.line_number <= line:
    #             found = recursive_search(top_item)
    #             item_to_select = found if found else top_item

    #     if item_to_select:
    #         self.structure_view.setCurrentItem(item_to_select)





    def select_structure_item_by_line(self, line):
        def recursive_search(item):
            selected_item = None
            for i in range(item.childCount()):
                child = item.child(i)
                child_line = child.data(0, Qt.UserRole)
                if child_line is not None and child_line <= line:
                    candidate = recursive_search(child)
                    selected_item = candidate if candidate else child
            return selected_item

        root = self.structure_view.invisibleRootItem()
        item_to_select = None
        for i in range(root.childCount()):
            top_item = root.child(i)
            top_line = top_item.data(0, Qt.UserRole)
            if top_line is not None and top_line <= line:
                found = recursive_search(top_item)
                item_to_select = found if found else top_item

        if item_to_select:
            self.structure_view.setCurrentItem(item_to_select)




    def highlighter_of_Python(self):


        editor = self.current_editor()

        editor.hoghlight_Python()


    def highlighter_of_C(self):


        
        editor = self.current_editor()

        editor.hoghlight_C()



    def go_to_line_in_editor(self, item):
        
                
        editor = self.current_editor()
        if not editor:
            return

        
        if (os.path.exists(editor.file_path) == True):
        
            if (editor.time_of_last_modification_of_file != os.path.getmtime(editor.file_path)):
            
                editor.time_of_last_modification_of_file = os.path.getmtime(editor.file_path)
        
        
        line = item.data(0, Qt.UserRole)
        

        cursor = editor.textCursor()
        cursor.movePosition(cursor.Start)
        for _ in range(line):
            cursor.movePosition(cursor.Down)

        editor.setTextCursor(cursor)

        # 🟡 هذه تجعل السطر في منتصف الشاشة
        editor.centerCursor()

        # ⬆️ اختياري: نمرر قليلًا لأعلى ليبدو في أعلى الشاشة بدل المنتصف
        scrollbar = editor.verticalScrollBar()
        scrollbar.setValue(scrollbar.value() - 5)  # عدّل الرقم حسب ذوقك

        editor.setFocus()






    def update_code_structure_view(self):
        
        editor = self.current_editor()
        
        if not editor:
            return



        
        if (editor.file_path is not None):

            if (editor.file_path.endswith(".py")):

                self.highlighter_of_Python()


            elif (editor.file_path.endswith(".c")):

                self.highlighter_of_C()



        
        


        code = editor.toPlainText()
        
        structure = self.parse_code_structure(code)
        self.structure_view.clear()

        def add_items(parent_widget, nodes):
            for node in nodes:
                item_text = f"{node['type']}: {node['name']}"
                tree_item = QTreeWidgetItem([item_text])
                tree_item.setData(0, Qt.UserRole, node['line'])

                if parent_widget is None:
                    self.structure_view.addTopLevelItem(tree_item)
                else:
                    parent_widget.addChild(tree_item)

                if node['children']:
                    add_items(tree_item, node['children'])

        add_items(None, structure)
        self.structure_view.expandAll()


        


    def parse_code_structure(self, code_text):
        import re

        lines = code_text.split('\n')
        stack = []  # يمثل المسار الهرمي الحالي
        root = []

        # العناصر القابلة للتداخل
        patterns = [
            r'(class)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            r'(def)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            r'(if)\s+(.*):',
            r'(elif)\s+(.*):',
            r'(else)\s*:?',
            r'(for)\s+(.*):',
            r'(while)\s+(.*):',
            r'(try)\s*:?',
            r'(except)\s*(.*)',
            r'(finally)\s*:?',
            r'(with)\s+(.*):',
            
            r'(if)\s+(.*)',
            
            r'(while)\s+(.*)',
            
            
            r'(enum)\s+(.*)',
            
            r'(else)\s*?',
            
            r'(int)\s+([a-zA-Z_][a-zA-Z0-9_]*)',

            r'(void)\s+([a-zA-Z_][a-zA-Z0-9_]*)',

            r'(int64_t)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        
            r'(int32_t)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
       
            r'(int16_t)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            
            r'(int8_t)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        
            r'(bool)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            
            
            r'(struct)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            
            
            r'(char)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            
            
            r'(char*)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            
            r'(enum)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            
            
            
        ]

        combined_pattern = re.compile('|'.join([f'({p})' for p in patterns]))

        def create_node(node_type, name, line, indent):
            return {
                'type': node_type,
                'name': name.strip(),
                'line': line,
                'indent': indent,
                'children': []
            }

        for i, line in enumerate(lines):
            stripped = line.lstrip()
            if not stripped or stripped.startswith('#'):
                continue

            indent = len(line) - len(stripped)
            match = combined_pattern.match(stripped)

            if match:
                for group_idx in range(1, len(match.groups()) + 1, 3):
                    node_type = match.group(group_idx)
                    if node_type:
                        name = match.group(group_idx + 1) or ''
                        node = create_node(node_type, name, i, indent)

                        while stack and stack[-1]['indent'] >= indent:
                            stack.pop()

                        if stack:
                            stack[-1]['children'].append(node)
                        else:
                            root.append(node)

                        stack.append(node)
                        break

        return root






    def write_list_of_path_on_file(self):


        # حفظ الملفات المفتوحة

        open_files = []

        for i in range(self.tabs.count()):

            editor = self.tabs.widget(i)

            if hasattr(editor, "file_path") and editor.file_path:

                open_files.append(editor.file_path)



        with open(self.opened_files_path, "w", encoding="utf-8") as f:

            json.dump(open_files, f, ensure_ascii=False, indent=2)



    def revealFileInTree(self, file_path):
        if not os.path.exists(file_path):
            return

        index = self.model.index(file_path)
        if not index.isValid():
            return

        # توسيع المجلدات حتى الملف
        parent = index.parent()
        while parent.isValid():
            self.treeView.expand(parent)
            parent = parent.parent()

        # تحديد الملف وتتمركز عليه
        self.treeView.setCurrentIndex(index)
        self.treeView.scrollTo(index)


    def refrech_load(self):




        # try:

        editor = self.current_editor()




        if editor is None or not hasattr(editor, "file_path") or editor.file_path is None :

            return  # لا يوجد محرر نشط أو لا يوجد مسار ملف

        if (os.path.exists(editor.file_path) == False):
        
            return

        semaphore_of_refrech = False

        try:

            if ((os.path.getmtime(editor.file_path) > editor.time_of_last_modification_of_file)):
                
                editor.time_of_last_modification_of_file = os.path.getmtime(editor.file_path)

                semaphore_of_refrech = True


            if (self.ctrl_s_press_ed == True):

                semaphore_of_refrech = False


            self.ctrl_s_press_ed = False

            

        except:

            semaphore_of_refrech = True



        if (semaphore_of_refrech == True):


            cursor = editor.textCursor()
            old_position = cursor.position()
        
            # إعادة تحميل الملف
            with open(editor.file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        
            editor.setPlainText(content)
        
            # محاولة إعادة وضع المؤشر لمكانه القديم
            new_cursor = editor.textCursor()
            max_pos = len(content)
            if old_position > max_pos:
                old_position = max_pos  # تأكد أن الموضع لا يتجاوز نهاية النص
            new_cursor.setPosition(old_position)
            editor.setTextCursor(new_cursor)



        # except Exception as e:

        #     semaphore_of_error = True

        #     print("e = ", e)




    def show_replace_widget(self):
        editor = self.current_editor()  # تأكد أن لديك هذه الدالة
        if editor:
        
            self.replace_widget = ReplaceWidget(editor)
            self.replace_widget.setWindowTitle("Replace in File")
            cursor = editor.textCursor()
            selected_text = cursor.selectedText()
            self.replace_widget.search_input.setText(selected_text)
            self.replace_widget.setFixedSize(300, 200)
            self.replace_widget.show()





    def toggle_find(self):
        self.find_widget.set_editor(self.current_editor())
        self.find_widget.show()
        self.find_widget.raise_()
        self.find_widget.activateWindow()
        self.find_widget.line_edit.setFocus()

        # ➕ تموضع في أعلى اليمين داخل MainWindow
        parent_geom = self.geometry()
        find_width = self.find_widget.width()
        find_height = self.find_widget.height()

        margin = 20  # هامش بسيط من الأعلى واليمين
        x = parent_geom.x() + parent_geom.width() - find_width - margin
        y = parent_geom.y() + margin

        self.find_widget.move(x, y)

        self.find_widget.open_with_selected_text()




    def trigger_undo(self):

#        print("i_hello .")
        editor = self.current_editor()
        if editor:
            editor.undo()

    def trigger_redo(self):
        
#        print("i_hello .")
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


        editor.document().modificationChanged.connect(lambda modified, ed=editor: self.on_editor_modification_changed(ed))

#
#    def close_tab_by_index(self, index):
#
#
#
#        self.tabs.removeTab(index)
#
#        
#        
#        if self.tabs.count() == 0:
#            self.new_tab()
#
#        



    def close_tab_by_index(self, index):
        self.tabs.removeTab(index)
    
        # إذا لم تبقَ تبويبات، أنشئ تبويبة جديدة
        if self.tabs.count() == 0:
            self.new_tab()
    
        print(f"index - 1 = {index - 1} . self.tab_file_paths[index - 1] = {self.tab_file_paths[index - 1]}")
    

        

        self.tab_file_paths.pop(index - 1)

#        list_0 = list(self.tab_file_paths.items())
#
#        
#
#        self.tab_file_paths = {v_0[0]: v_0[1] for v_0 in list_0}
#


    def close_current_tab(self, index):


        # index = self.tabs.currentIndex()
        # if index != -1:
        #     self.tabs.removeTab(index)
        #     if self.tabs.count() == 0:
        #         self.new_tab()

#        del self.tab_file_paths[index]

        widget = self.tabs.widget(index)
        if widget:
            widget.deleteLater()
        self.tabs.removeTab(index)

        self.tab_file_paths.pop(index - 1)

#        self.tab_file_paths = {i: v for i, v in enumerate(self.tab_file_paths.values())}

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
#            self.tab_file_paths[index] = file_path
            
            
            self.tab_file_paths.append(file_path)

            self.write_list_of_path_on_file()

            editor.file_of_tabs = self.opened_files_path

            editor.document().modificationChanged.connect(lambda modified, ed=editor: self.on_editor_modification_changed(ed))


        except Exception as e:
            QMessageBox.warning(self, "error", f"File opening failed:\n{e}")


    # def convert_tabs_to_spaces(self, spaces_per_tab=4, editor=None):
        
    def convert_tabs_to_spaces(self, text):

        

        spaces_per_tab = 4


        # cursor = self.textCursor()
        # cursor.beginEditBlock()

        # text = editor.toPlainText()




        tab__ = " " * 4


        try:

            with open(os.path.join(os.getcwd(), "tab__.txt"), "r") as f_:

                tab__ = f_.read(os.path.getsiae(os.path.join(os.getcwd(), "tab__.txt")))

        except:

            semaphore = True


        new_text = text.replace('\t', ' ' * spaces_per_tab)
        
        new_text = new_text.replace(tab__, ' ' * spaces_per_tab)




        # print("i_hello .")

        # self.setPlainText(new_text)

        # cursor.endEditBlock()

        return new_text


    def save_file(self):

        self.ctrl_s_press_ed = True

        editor = self.current_editor()
        if editor:
            if hasattr(editor, "file_path") and editor.file_path:
                try:
                    with open(editor.file_path, 'w', encoding='utf-8') as f:
                        # print("i_hello_1 . convert_tabs_to_spaces(editor.toPlainText()) = ", self.convert_tabs_to_spaces(editor.toPlainText()))
                        
                        f.write(self.convert_tabs_to_spaces(editor.toPlainText()))


                
                    self.tabs.setTabText(self.tabs.currentIndex(), os.path.basename(editor.file_path))
                
                       
                    self.update_code_structure_view()
                    
                    self.connect_cursor_movement()
                     
                    editor.document().setModified(False)
                    
                    self.on_editor_modification_changed(editor)
                                        
                    
                    self.tab_file_paths[self.tabs.currentIndex() - 1] = editor.file_path
                    
                    self.tabs.setTabText(self.tabs.currentIndex(), os.path.basename(editor.file_path))
                    
                    
                
                except Exception as e:
                    QMessageBox.warning(self, "error", f"Failed to save file:\n{e}")
            else:
                path, _ = QFileDialog.getSaveFileName(self, "save file", "", "Text Files (*.txt);;All Files (*)")
                if path:
                    try:
                        with open(path, 'w', encoding='utf-8') as f:
                        
                            # print("i_hello_2 .")
                        
                            f.write(self.convert_tabs_to_spaces(editor.toPlainText()))

                        editor.file_path = path

#                        print(f"self.tabs.currentIndex() = {self.tabs.currentIndex()}")


                        self.tab_file_paths[self.tabs.currentIndex() - 1] = editor.file_path
                    
                        self.tabs.setTabText(self.tabs.currentIndex(), os.path.basename(path))
            
                        
                        
                        self.update_code_structure_view()
                        
                        self.connect_cursor_movement()
                        
                    
                    except Exception as e:
                        QMessageBox.warning(self, "error", f"Failed to save file:\n{e}")

    def open_file_from_tree(self, index):
        file_path = self.model.filePath(index)
        if QDir(file_path).exists():
            # إذا هو مجلد لا نفعل شيء
            return
        self.open_file_in_tab(file_path)





    def show_explorer_context_menu(self, position):
        if self.tree.columnAt(position.x()) != 0:
            return
    
        index = self.tree.indexAt(position)
        if not index.isValid():
            return
    
        file_path = self.model.filePath(index)
        is_dir = QDir(file_path).exists() and os.path.isdir(file_path)
    
        menu = QMenu()
    
        # الإجراءات العادية
        terminal_action = QAction("open terminal from here", self)
        
        explorer_action = QAction("open explorer from here", self)
        
        copy_action = QAction("📋 Copy", self)
        cut_action = QAction("✂️ Cut", self)
        paste_action = QAction("📎 Paste", self)
       
        paste_content_action = QAction("📎 Paste content", self)

        delete_action = QAction("❌ Delete", self)
        rename_action = QAction("✏️ Rename", self)
        


        get_size_action = QAction("✏️ get size", self)
        
        copy_link_action = QAction("✏️ copy link", self)
    
        # ✅ الإجراء الجديد: مجلد وملف
        new_folder_action = QAction("📁 Create New Folder", self)
        new_file_action = QAction("📄 Create New File", self)
    
        # ربط الوظائف
        terminal_action.triggered.connect(lambda: self.open_terminal_at(file_path))
        
        explorer_action.triggered.connect(lambda: self.open_os_explorer(file_path))
        
        copy_action.triggered.connect(lambda: self.copy_item(file_path))
        cut_action.triggered.connect(lambda: self.cut_item(file_path))
        paste_action.triggered.connect(lambda: self.paste_item(file_path))
        
        paste_content_action.triggered.connect(lambda: self.copy_content(self.clipboard_path, file_path))
        
        delete_action.triggered.connect(lambda: self.delete_item(file_path))
        rename_action.triggered.connect(lambda: self.rename_item(file_path))
    
    
        get_size_action.triggered.connect(lambda: self.get_folder_size(file_path))
    
        copy_link_action.triggered.connect(lambda: self.copy_link(file_path))
    
        new_folder_action.triggered.connect(lambda: self.create_new_folder(file_path))
        new_file_action.triggered.connect(lambda: self.create_new_file(file_path))
    
        # بناء القائمة
        menu.addAction(terminal_action)
        menu.addAction(explorer_action)
        menu.addSeparator()
        menu.addAction(copy_action)
        menu.addAction(cut_action)
        menu.addAction(paste_action)
        menu.addAction(paste_content_action)
        menu.addAction(delete_action)
        menu.addSeparator()
        menu.addAction(get_size_action)
        menu.addAction(rename_action)
        menu.addSeparator()
        menu.addAction(copy_link_action)
        menu.addSeparator()
        menu.addAction(new_folder_action)
        menu.addAction(new_file_action)
    
        menu.exec_(self.tree.viewport().mapToGlobal(position))
    


        
    def get_folder_size(self, path):
       
        total_size = 0
        
        if (os.path.isfile(path) == True):
        
            total_size = os.path.getsize(path)       
        
        else:
        
            
            dirs = [""]
            
            srcs = [""]
            
            
    
            counter_1 = 0
            
            while (counter_1 < len(dirs)):
            
                for root, dirs_, files in os.walk(os.path.join(path, dirs[counter_1])):
            
                    break
            
            
            
                counter_0 = 0
            
                while (counter_0 < len(dirs_)):
            
                    dirs.append(os.path.join(dirs[counter_1], dirs_[counter_0]))
            
                    srcs.append(os.path.join(srcs[counter_1], dirs_[counter_0]))
            
                    counter_0 += 1
            
                    
                src_ = os.path.join(path, srcs[counter_1])
            
    
    
                counter_0 = 0
            
                while (counter_0 < len(files)):
            
                    try:
            
                        total_size += os.path.getsize(os.path.join(src_, files[counter_0]))
                       
            
                    except:
                                    
                        traceback.print_exc()
                        
                        error = traceback.format_exc()
                        
                        semaphore = True
            
                        print(f"Erreur : {str(error)}")
            
            
            
                    
                    counter_0 += 1
            
            
                counter_1 += 1
            
            
            
            
            
        
        QMessageBox.information(
            self,
            "size",
            f"the size is : {i_number_to_str(number=total_size)} Byte "
        )
        


    def open_os_explorer(self, path):
        
        if not os.path.exists(path):
        
            return
          
        
        
        if os.path.isfile(path):
         
            path = os.path.dirname(path)



        semaphore = False        
    
        try:
    
#            os.startfile(path)
    
            subprocess.Popen(f'explorer "{path}"')

    
        except:
        
            semaphore = True


        if (semaphore == True):

    
            semaphore = False        
    
            try:
    
                subprocess.Popen(["open", path])
                
            except:
            
                semaphore = True
        
        
        if (semaphore == True):
        
        
            semaphore = False        
            
            
            try:
        
                subprocess.Popen(["xdg-open", path])
        
                    
            except:
            
                semaphore = True
            


    def create_new_folder(self, base_path):
        
        if not os.path.isdir(base_path):
            base_path = os.path.dirname(base_path)
    
        name, ok = QInputDialog.getText(self, "Create New Folder", "Folder name:")
        if ok and name:
            new_folder_path = os.path.join(base_path, name)
            try:
                os.makedirs(new_folder_path)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not create folder:\n{str(e)}")
    
    def create_new_file(self, base_path):
        if not os.path.isdir(base_path):
            base_path = os.path.dirname(base_path)
    
        name, ok = QInputDialog.getText(self, "Create New File", "File name:")
        if ok and name:
            new_file_path = os.path.join(base_path, name)
            try:
                with open(new_file_path, "w") as f:
                    f.write("")  # ملف فارغ
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not create file:\n{str(e)}")
    





    def rename_item(self, old_path):
        old_name = os.path.basename(old_path)
        old_dir = os.path.dirname(old_path)

        new_name, ok = QInputDialog.getText(self, "Rename", "Enter new name:", text=old_name)
        if ok and new_name and new_name != old_name:
            new_path = os.path.join(old_dir, new_name)
            try:
                os.rename(old_path, new_path)
                # self.model.refresh()

                # تحديث أو إغلاق التبويبات حسب الحالة
                for i in reversed(range(self.tabs.count())):
                    editor = self.tabs.widget(i)
                    if hasattr(editor, 'file_path'):
                        # إذا كان التبويب يشير للملف الذي أُعيدت تسميته
                        
                        if editor.file_path is not None:
                            
                            if editor.file_path == old_path:
                                if os.path.dirname(editor.file_path) == old_dir:
                                    # ✅ نفس المسار الأب → تحديث فقط
                                    editor.file_path = new_path
                                    self.tabs.setTabText(i, new_name)
                                else:
                                    # ❌ تغيّر المجلد → نحذف التبويبة
                                    self.tabs.removeTab(i)

                            # ملفات داخل مجلد تم إعادة تسميته
                            elif editor.file_path.startswith(old_path + os.sep):
                                self.tabs.removeTab(i)



            except Exception as e:
                QMessageBox.critical(self, "Rename Failed", f"Could not rename:\n{str(e)}")





    def copy_link(self, text):

        clipboard = QApplication.clipboard()

        clipboard.setText(text)


    def copy_item(self, file_path):
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "error", "Path not found.")
            return

        self.clipboard_mode = "copy"
        self.clipboard_path = file_path
        print("📋 تم النسخ:", file_path)



    def cut_item(self, path):
        self.clipboard_action = "cut"
        self.clipboard_path = path



    def paste_item(self, target_path):
        if not hasattr(self, "clipboard_path") or not os.path.exists(self.clipboard_path):
            QMessageBox.warning(self, "⚠️ error", "No item to paste.")
            return

        # إذا ضغطت على ملف، نأخذ المجلد الذي يحتويه
        if os.path.isfile(target_path):
            target_path = os.path.dirname(target_path)

        base_name = os.path.basename(self.clipboard_path)
        dest_path = os.path.join(target_path, base_name)

        if os.path.exists(dest_path):
            QMessageBox.warning(self, "⚠️ existing", f"element '{base_name}' already exists.")
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
            QMessageBox.critical(self, "❌ error", f"Failed to paste:\n{e}")



    def delete_item(self, path):
        reply = QMessageBox.question(self, "Confirm deletion", f"Do you want to delete? '{os.path.basename(path)}'؟",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            
            
                        
            self.expanded_dirs_before_action = self.get_expanded_dirs()

            
            try:    
            
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)

#                QTimer.singleShot(100, self.refresh_tree_view)

            except Exception as e:
                QMessageBox.warning(self, "error", f"File deletion failed:\n{e}")


            self.restore_expanded_dirs(self.expanded_dirs_before_action)



#        QTimer.singleShot(100, self.refresh_tree_view)



    def open_terminal_at(self, path):




        if os.path.isfile(path):
 
            path = os.path.dirname(path)
        

        semaphore = False        
        

        try:
        
            subprocess.Popen(["gnome-terminal", "--working-directory", path])
        
        except:
        
            semaphore = True
            
                
        if (semaphore == True):
        
            semaphore = False        
            
               
            try:
            
    
                subprocess.Popen(f'start cmd /K "cd /d {path}"', shell=True)
            
            except:
            
                semaphore = True
                
                
        if (semaphore == True):
        
            semaphore = False        
                
                    
            try:
                
                script = f'''
                tell application "Terminal"
                    activate
                    do script "cd \\"{path}\\""
                end tell
                '''
                subprocess.Popen(["osascript", "-e", script])
    
            
            except:
            
                semaphore = True
                
                   


    def show_tab_context_menu(self, pos):
        
        index = self.tabs.tabBar().tabAt(pos)
        
        if index == -1:
            return

        file_name = self.tabs.tabText(index)
        
        print("file_name = ", file_name)

        # نحصي عدد التبويبات التي تحمل نفس الاسم
        
        # count_same_name = sum(1 for i in range(self.tabs.count()) if self.tabs.tabText(i) == file_name)

        # if count_same_name > 1:
        
        menu = QMenu()

        open_location_action = QAction("open_place_in_explorer", self)

        menu.addAction(open_location_action)

    
        action = menu.exec_(self.tabs.mapToGlobal(pos))
    
        if action == open_location_action:
    
            file_path = self.tab_file_paths[index - 1]
            
            print(f"file_path = {file_path} . index - 1 = {index - 1}")
    
            if file_path or True:
    
               self.expand_tree_to_file(file_path)
                
                # self.expand_tree_to_file(file_name)

    
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



        self.flash_tree_item(index)


    def flash_tree_item(self, index):

        # حفظ النموذج واللون الأصلي

        original_brush = self.model.data(index, Qt.BackgroundRole)

        # تلوين مؤقت (مثلاً أصفر)

        self.model.setData(index, QBrush(QColor("#ffff99")), Qt.BackgroundRole)

        # إزالة اللون بعد 1 ثانية

        # QTimer.singleShot(1000, lambda: self.model.setData(index, original_brush, Qt.BackgroundRole))

        self.model.setData(index, original_brush, Qt.BackgroundRole)


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
    
    
    
    
    
    
    def refresh_tree_view(self):
        current_path = self.model.rootPath()
    
        # احفظ موقع التمرير الحالي
        scroll_position = self.tree.verticalScrollBar().value()
    
        # افصل النموذج مؤقتًا
        self.tree.setModel(None)
    
        # أعد ربط النموذج مع إعادة تعيين الجذر
        self.model = QFileSystemModel()
        self.model.setRootPath(current_path)
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(current_path))
    
        # أعد موقع التمرير
        self.tree.verticalScrollBar().setValue(scroll_position)
    
        # تحديث العمود الأول فقط
        self.tree.setColumnWidth(0, 400)
    


    def copy_content(self, file_of_from, file_of_target):
    
    
                
        if not os.path.isfile(file_of_from):
            
            return
    
                
        if not os.path.isfile(file_of_target):
            
            return
        
    
    
        d = Path(file_of_from)
        
        d_ = Path(file_of_target)
        
        d_.write_bytes(d.read_bytes())
    
        QMessageBox.information(self, "success ✅", "the paste of content is with success")
        
        
        
        
        
    
    
    def check_focused_widget(self):
        
        
        focused_0 = QApplication.focusWidget()
        
        while (True):
            
            focused_1 = QApplication.focusWidget()
            
            if (focused_0 != focused_1):
            
                print(f"widget select-ed : {focused_1}")
        
        
                focused_0 = focused_1
    
    
    
        
        


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
    
    s = os.path.join("a", "b")

    if (s[1] == "/" ):

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













