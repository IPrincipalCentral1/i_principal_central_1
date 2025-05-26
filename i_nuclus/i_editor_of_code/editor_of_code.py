





# i_hello




color_of_mode_of_night = ["#A0A0A0", "#FFFFFF"]


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------






# section of ai 



from PyQt5.QtWidgets import QDialog


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


class CodeEditor(QPlainTextEdit):
   
   
   
    def __init__(self):
        super().__init__()
        self.lineNumberArea = LineNumberArea(self)


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

            '(' : '#FFBF00',

            ')' : '#FFBF00',


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

        self.setUndoRedoEnabled(True)

        # --- تم إزالة استدعاء الدوال غير الضرورية هنا ---


        self.lineNumberArea = LineNumberArea(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        # self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()


        # self.cursorPositionChanged.connect(self.matchBrackets)


        self.textChanged.connect(self.highlight_unmatched_brackets)







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
            text = block.text()
            lines.append(text)

        all_commented = all(line.strip().startswith("#") for line in lines if line.strip())

        cursor.beginEditBlock()
        for i in range(start_block, end_block + 1):
            block = self.document().findBlockByNumber(i)
            cursor.setPosition(block.position())
            cursor.movePosition(QTextCursor.StartOfBlock)
            cursor.movePosition(QTextCursor.EndOfBlock, QTextCursor.KeepAnchor)
            text = cursor.selectedText()

            # if all_commented:
            #     # إزالة التعليق
            #     new_text = text.lstrip("#").lstrip()
            # else:
            #     # إضافة تعليق
            #     new_text = "# " + text


            if all_commented:
                # إزالة التعليق من بداية السطر فقط
                if text.lstrip().startswith("#"):
                    index = text.index("#")
                    new_text = text[:index] + text[index+1:]
                    if new_text.startswith(" "):
                        new_text = new_text[1:]  # إزالة الفراغ بعد #
                else:
                    new_text = text
            else:
                # إضافة # بعد الهوامش
                leading_spaces = len(text) - len(text.lstrip())
                new_text = " " * leading_spaces + "# " + text.lstrip()




            cursor.insertText(new_text)
        cursor.endEditBlock()



    def hoghlight_Python(self):

        self.highlighter = PythonHighlighter(self.document(), self.word_colors_Python)



    def hoghlight_C(self):

        self.highlighter = CHighlighter(self.document(), self.word_colors_C)


    def get_project_files(self):



        opened_files_path = self.file_of_tabs

        list_of_path = []

        if os.path.exists(opened_files_path):
            try:
                with open(opened_files_path, "r", encoding="utf-8") as f:
                    paths = json.load(f)
                for path in paths:
                
                    list_of_path.append(path)

            except Exception as e:
                print("فشل تحميل الملفات المفتوحة:", e)


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
                if os.path.isfile(file_path) and file_path.endswith((".py", ".txt", ".md", ".c", ".cpp")):
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



    def cursorPositionChanged_(self):






        self.highlightCurrentLine()

        self.matchBrackets()


    def highlight_unmatched_brackets(self):
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




    def matchBrackets(self):
        cursor = self.textCursor()
        doc = self.document()
        pos = cursor.position()

        if pos == 0:
            self.setExtraSelections([])
            return

        text = doc.toPlainText()

        char_prev = doc.characterAt(pos - 1) if pos - 1 >= 0 else ''
        char_curr = doc.characterAt(pos) if pos < len(text) else ''

        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        opening = bracket_pairs.keys()
        closing = bracket_pairs.values()

        match = None
        highlight_pos = None

        # إذا المؤشر على قوس مفتوح
        if char_curr in opening:
            match = self.findMatchingBracket(pos, forward=True)
            highlight_pos = pos

        # إذا المؤشر مباشرة بعد قوس مفتوح
        elif char_prev in opening:
            match = self.findMatchingBracket(pos - 1, forward=True)
            highlight_pos = pos - 1

        # إذا المؤشر على قوس مغلق
        elif char_curr in closing:
            match = self.findMatchingBracket(pos, forward=False)
            highlight_pos = match
            match = pos

        # إذا المؤشر مباشرة بعد قوس مغلق
        elif char_prev in closing:
            match = self.findMatchingBracket(pos - 1, forward=False)
            highlight_pos = match
            match = pos - 1

        else:
            self.setExtraSelections([])
            return

        if match is not None and highlight_pos is not None:
            extraSelections = []

            sel1 = QTextEdit.ExtraSelection()
            sel1.cursor = QTextCursor(doc)
            sel1.cursor.setPosition(highlight_pos)
            sel1.cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            sel1.format.setBackground(QColor("#444444"))
            extraSelections.append(sel1)

            sel2 = QTextEdit.ExtraSelection()
            sel2.cursor = QTextCursor(doc)
            sel2.cursor.setPosition(match)
            sel2.cursor.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            sel2.format.setBackground(QColor("#444444"))
            extraSelections.append(sel2)

            self.setExtraSelections(extraSelections)
        else:
            self.setExtraSelections([])




    def findMatchingBracket(self, pos, forward=True):
        text = self.toPlainText()
        stack = []
        brackets = {'(': ')', '{': '}', '[': ']'}
        if not forward:
            brackets = {v: k for k, v in brackets.items()}

        open_b = brackets.keys()
        close_b = brackets.values()

        i = pos
        while 0 <= i < len(text):
            char = text[i]
            if char in open_b:
                stack.append(char)
            elif char in close_b:
                if not stack:
                    return None
                last = stack.pop()
                if brackets[last] != char:
                    return None
                if not stack:
                    return i
            i += 1 if forward else -1
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



        # تحقق من الضغط على Ctrl + C وعدم وجود تحديد
        if event.matches(QKeySequence.Copy) and not self.textCursor().hasSelection():
            cursor = self.textCursor()
            cursor.select(QTextCursor.LineUnderCursor)
            self.setTextCursor(cursor)  # مؤقتًا لتفعيله
            self.copy()  # نسخ السطر
            cursor.clearSelection()  # إزالة التحديد بعد النسخ (اختياري)
            self.setTextCursor(cursor)

        # else:

        #     super().keyPressEvent(event)

        #     return


        cursor = self.textCursor()

        if event.key() == Qt.Key_Tab:
            if cursor.hasSelection():
                self.indentSelectedText()
            else:
                cursor.insertText("\t")
            return

        elif event.key() == Qt.Key_Backtab:  # Shift + Tab
            if cursor.hasSelection():
                self.unindentSelectedText()
                return









        if (semaphore_of_hide == True):

            self.completer.popup().hide()
            self.suggestion_visible = False



        super().keyPressEvent(event)
        




    def indentSelectedText(self):
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
        lines = ["\t" + line for line in lines]

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


    def unindentSelectedText(self):
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
        lines = [line[1:] if line.startswith("\t") else line for line in lines]

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





    def selectCurrentWord(self):
        
        cursor = self.textCursor()
        
        if not cursor.hasSelection():
            
            cursor.select(QTextCursor.WordUnderCursor)
            
            self.setTextCursor(cursor)


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

    # def update_completer_words(self):
    #     text = self.toPlainText()
    #     words = list(set(re.findall(r'\b[a-zA-Z_]\w{2,}\b', text)))  # كلمات بطول ≥3 فقط
    #     words.sort()
    #     self.completer.model().setStringList(words)


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


    # def set_editor(self, editor):
    #     self.editor = editor


    # def find_next(self):
    #     text = self.line_edit.text()
    #     if not text:
    #         return

    #     document = self.editor.document()
    #     cursor = self.editor.textCursor()
    #     found_cursor = document.find(text, cursor)

    #     if not found_cursor.isNull():
    #         self.editor.setTextCursor(found_cursor)
    #         self.editor.centerCursor()
    #     else:
    #         QMessageBox.information(self, "Not Found", f"'{text}' not found.")



    def find_next(self):
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




    # def find_prev(self):
    #     text = self.line_edit.text()
    #     if not text:
    #         return

    #     document = self.editor.document()
    #     cursor = self.editor.textCursor()
    #     found_cursor = document.find(text, cursor, QTextDocument.FindBackward)

    #     if not found_cursor.isNull():
    #         self.editor.setTextCursor(found_cursor)
    #         self.editor.centerCursor()
    #     else:
    #         QMessageBox.information(self, "Not Found", f"'{text}' not found.")




    def find_prev(self):
        if not self.matches:
            self.highlight_all()
        if not self.matches:
            return

        self.current_index = (self.current_index - 1 + len(self.matches)) % len(self.matches)
        pos = self.matches[self.current_index]

        cursor = self.editor.textCursor()
        cursor.setPosition(pos)
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.line_edit.text()))
        self.editor.setTextCursor(cursor)
        self.editor.centerCursor()

        self.counter_label.setText(f"{self.current_index + 1} of {len(self.matches)}")




    def highlight_all(self):
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



    def set_editor(self, editor):
        self.editor = editor
        self.matches.clear()
        self.current_index = -1
        self.counter_label.setText("0 of 0")





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


from PyQt5.QtCore import QModelIndex

from PyQt5.QtWidgets import QStatusBar


from PyQt5.QtGui import QColor, QBrush



from PyQt5.QtWidgets import QInputDialog, QMessageBox
import os

from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QSplitter, QWidget, QVBoxLayout


from PyQt5.QtWidgets import QSplitter





import sys





class MainWindow(QMainWindow):
    
    
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




            self.write_list_of_path_on_file()


        else:
            event.ignore()


    
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
        self.tree.setColumnWidth(0, 400)

        self.model.setRootPath(QDir.rootPath())
        self.tree.setModel(self.model)


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

        # ⬅️ 3. تقسيم أفقي: يسار (شجرتين) ويمين (التبويبات)
        main_splitter = QSplitter(Qt.Horizontal)
        main_splitter.addWidget(left_panel)
        main_splitter.addWidget(self.tabs)
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


        edit_menu.addAction(self.create_action("highlighter of Python", "Ctrl+H+P", self.highlighter_of_Python))
        edit_menu.addAction(self.create_action("highlighter of C", "Ctrl+H+C", self.highlighter_of_C))


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
                            editor.setPlainText(file.read())

                            editor.file_path = path

                            editor.file_of_tabs = self.opened_files_path

                            editor.time_of_last_modification_of_file = os.path.getmtime(path)

                            index = self.tabs.addTab(editor, os.path.basename(path))
                            
                            # print("editor.file_path = ", editor.file_path)

                            self.tab_file_paths[index] = path

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


        self.file_check_timer = QTimer(self)
        self.file_check_timer.timeout.connect(self.refrech_load)
        self.file_check_timer.start(3000)  # كل 3 ثواني

        self.ctrl_s_press_ed = False


        self.setStatusBar(QStatusBar())


        self.tabs.currentChanged.connect(lambda _: self.function_of_tabs_currentChanged_connect())





    def function_of_tabs_currentChanged_connect(self):

        self.update_code_structure_view()

        self.connect_cursor_movement()




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
        line = item.data(0, Qt.UserRole)
        editor = self.current_editor()
        if not editor:
            return

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
            r'(except)\s*(.*):',
            r'(finally)\s*:?',
            r'(with)\s+(.*):'
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




        editor = self.current_editor()

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

            if editor and hasattr(editor, "file_path") and editor.file_path:
                try:
                    with open(editor.file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    editor.setPlainText(content)
                except Exception as e:

                    semaphore_of_error = True

                    # QMessageBox.warning(self, "خطأ", f"فشل تحديث الملف:\n{e}")


    def show_replace_widget(self):
        editor = self.current_editor()  # تأكد أن لديك هذه الدالة
        if editor:
            self.replace_widget = ReplaceWidget(editor)
            self.replace_widget.setWindowTitle("Replace in File")
            self.replace_widget.setFixedSize(300, 200)
            self.replace_widget.show()




    # def toggle_find(self):

    #     self.find_widget.set_editor(self.current_editor())

    #     self.find_widget.hide()

    #     if self.find_widget.isVisible():
    #         self.find_widget.hide()
    #     else:
    #         self.find_widget.show()
    #         self.find_widget.line_edit.setFocus()



    # def toggle_find(self):
        
    #     self.find_widget.set_editor(self.current_editor())  # ضروري
    #     # self.find_widget.line_edit.selectAll()
        
    #     # self.find_widget.exec_()

    #     # self.find_widget.show()
    #     # self.find_widget.raise_()
    #     # self.find_widget.activateWindow()
    #     # self.find_widget.line_edit.setFocus()


    #     self.find_widget.show()
    #     self.find_widget.raise_()
    #     self.find_widget.activateWindow()
    #     self.find_widget.line_edit.setFocus()





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

            self.write_list_of_path_on_file()

            editor.file_of_tabs = self.opened_files_path

        except Exception as e:
            QMessageBox.warning(self, "خطأ", f"فشل فتح الملف:\n{e}")

    def save_file(self):

        self.ctrl_s_press_ed = True

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





    def show_explorer_context_menu(self, position):
        if self.tree.columnAt(position.x()) != 0:
            return

        index = self.tree.indexAt(position)
        if not index.isValid():
            return

        file_path = self.model.filePath(index)
        is_dir = QDir(file_path).exists() and os.path.isdir(file_path)

        menu = QMenu()

        # الإجراءات
        terminal_action = QAction("open terminal from here", self)
        copy_action = QAction("📋 Copy", self)
        cut_action = QAction("✂️ Cut", self)
        paste_action = QAction("📎 Paste", self)
        delete_action = QAction("❌ Delete", self)

        # ➕ زر إعادة التسمية (Rename)
        rename_action = QAction("✏️ Rename", self)
        rename_action.triggered.connect(lambda: self.rename_item(file_path))

        # ربط الإجراءات
        terminal_action.triggered.connect(lambda: self.open_terminal_at(file_path))
        copy_action.triggered.connect(lambda: self.copy_item(file_path))
        cut_action.triggered.connect(lambda: self.cut_item(file_path))
        paste_action.triggered.connect(lambda: self.paste_item(file_path))
        delete_action.triggered.connect(lambda: self.delete_item(file_path))

        # إضافة للقائمة
        menu.addAction(terminal_action)
        menu.addSeparator()
        menu.addAction(copy_action)
        menu.addAction(cut_action)
        menu.addAction(paste_action)
        menu.addAction(delete_action)
        menu.addSeparator()
        menu.addAction(rename_action)

        menu.exec_(self.tree.viewport().mapToGlobal(position))









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




    def copy_item(self, file_path):
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "خطأ", "المسار غير موجود.")
            return

        self.clipboard_mode = "copy"
        self.clipboard_path = file_path
        print("📋 تم النسخ:", file_path)



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
        
        print("file_name = ", file_name)

        # نحصي عدد التبويبات التي تحمل نفس الاسم
        
        # count_same_name = sum(1 for i in range(self.tabs.count()) if self.tabs.tabText(i) == file_name)

        # if count_same_name > 1:
        
        menu = QMenu()
        open_location_action = QAction("open_place_in_explorer", self)
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













