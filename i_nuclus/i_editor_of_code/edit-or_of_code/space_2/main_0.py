












import os



os.system("pip install pyqtgraph")



os.system("pip install PyQt5")



os.system("pip install PyOpenGL PyOpenGL_accelerate")



os.system("pip install imageio")


os.system("pip install pillow")





import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph.opengl as gl



from pyqtgraph.opengl import GLMeshItem
from pyqtgraph import Vector
from PyQt5.QtGui import QImage
from PyQt5.QtOpenGL import QGLWidget
import OpenGL.GL as gl
from PIL import Image


def create_image(path_of_file, color, width, height):

    
    
    # أبعاد الصورة (عرض × ارتفاع)
    #width, height = 512, 512
    
    # إنشاء صورة بلون أبيض (RGBA أو RGB)
    #white_color = (255, 255, 255, 255)  # يمكنك استخدام (255, 255, 255) لـ RGB فقط
    
    
    
    image = Image.new("RGBA", (width, height), color)
    
    # حفظ الصورة باسم image.png
    
    image.save(path_of_file)
    




class ImagePlane(GLMeshItem):
    def __init__(self, image_path, size=10.0, pos=(0, 0, 0)):
        verts = np.array([
            [0, 0, 0],
            [size, 0, 0],
            [size, size, 0],
            [0, size, 0]
        ])

        faces = np.array([
            [0, 1, 2],
            [0, 2, 3]
        ])

        meshdata = gl.MeshData(vertexes=verts, faces=faces)

        super().__init__(meshdata=meshdata, smooth=False, drawFaces=True, drawEdges=False)
        self.translate(*pos)
        self.setGLOptions('additive')

        self.image_path = image_path
        self.texture_id = self.load_texture()

    def load_texture(self):
        img = Image.open(self.image_path).convert("RGBA")
        img_data = img.tobytes("raw", "RGBA", 0, -1)

        texture_id = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, texture_id)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA,
                        img.size[0], img.size[1], 0,
                        gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, img_data)
        return texture_id

    def paint(self):
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)
        super().paint()
        gl.glDisable(gl.GL_TEXTURE_2D)






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


        
        file_of_image = os.path.join(os.getcwd(), "image.png")

        
        create_image(path_of_file=file_of_image, color=(255, 255, 255, 255), width=100, height=100)
        
        # بعد الشبكة والنقاط العشوائية

        image_path = file_of_image

        if os.path.exists(image_path):
            image_item = ImagePlane(image_path, size=10.0, pos=(5, 5, 5))
            self.view.addItem(image_item)
        

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































