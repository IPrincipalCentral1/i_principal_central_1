












import os



os.system("pip install pyqtgraph")



os.system("pip install PyQt5")



os.system("pip install PyOpenGL PyOpenGL_accelerate")







import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph.opengl as gl

# صنف مخصص يعطل تفاعل لوحة المفاتيح (الأسهم وغيرها)
class CustomGLViewWidget(gl.GLViewWidget):
    
    
    def keyPressEvent(self, event):

        
#
#        if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
#        
#            return
#        
#        else:
#        


        super().keyPressEvent(event)




class My3DViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: black;")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # استخدمنا النسخة المخصصة
        self.view = CustomGLViewWidget()
        self.view.setBackgroundColor('k')
        self.view.setCameraPosition(distance=40)
        self.view.setWindowTitle('3D Viewer')

        # شبكة الأرض
        grid = gl.GLGridItem()
        self.view.addItem(grid)

        # نقاط ثلاثية الأبعاد عشوائية
        pos = np.random.normal(size=(1000, 3))
        scatter = gl.GLScatterPlotItem(pos=pos, color=(1, 1, 1, 1), size=2)
        self.view.addItem(scatter)

        self.layout.addWidget(self.view)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Viewer - Keyboard Disabled")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black;")

        self.viewer = My3DViewer()
        self.setCentralWidget(self.viewer)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())































