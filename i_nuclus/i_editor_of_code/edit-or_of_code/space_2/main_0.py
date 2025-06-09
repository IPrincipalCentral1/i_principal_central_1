












import os



os.system("pip install pyqtgraph")



os.system("pip install PyQt5")



os.system("pip install PyOpenGL PyOpenGL_accelerate")



os.system("pip install imageio")


os.system("pip install pillow")


import os
import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph.opengl as pgl  # pyqtgraph.opengl
import OpenGL.GL as gl           # مكتبة OpenGL المنخفضة

from PIL import Image


def create_image(path_of_file, color, width, height):
    """
    تنشئ صورة بلون معين وتحفظها في المسار المحدد
    """
    image = Image.new("RGBA", (width, height), color)
    image.save(path_of_file)


class ImagePlane(pgl.GLMeshItem):
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

        meshdata = pgl.MeshData(vertexes=verts, faces=faces)

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

        gl.glEnable(gl.GL_BLEND)

        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

        gl.glEnable(gl.GL_TEXTURE_2D)

        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)

        super().paint()

        gl.glDisable(gl.GL_TEXTURE_2D)

        gl.glDisable(gl.GL_BLEND)
    




    #def paint(self):
        #gl.glEnable(gl.GL_TEXTURE_2D)
        #gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture_id)
        #super().paint()
        #gl.glDisable(gl.GL_TEXTURE_2D)


class CustomGLViewWidget(pgl.GLViewWidget):
    def keyPressEvent(self, event):
        # منع تحريك العرض بلوحة المفاتيح (يمكن تفعيل التعليق لإلغاء الحظر)
        # if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
        #     return
        super().keyPressEvent(event)


class My3DViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: black;")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.view = CustomGLViewWidget()
        self.view.setBackgroundColor('k')
        self.view.setCameraPosition(distance=40)
        self.view.setWindowTitle('3D Viewer')

        # مسار الصورة
        file_of_image = os.path.join(os.getcwd(), "image.png")

        # إنشاء صورة بيضاء 100x100 بكسل
        create_image(path_of_file=file_of_image, color=(255, 255, 255, 0), width=100, height=100)

        # إضافة صورة ثلاثية الأبعاد كطبقة (Plane)
        if os.path.exists(file_of_image):
            image_item = ImagePlane(file_of_image, size=10.0, pos=(5, 5, 5))
            self.view.addItem(image_item)

        # شبكة الأرض
        grid = pgl.GLGridItem()
        self.view.addItem(grid)

        # نقاط ثلاثية الأبعاد عشوائية
        pos = np.random.normal(size=(1000, 3))
        scatter = pgl.GLScatterPlotItem(pos=pos, color=(1, 1, 1, 1), size=2)
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
    # تثبيت الحزم (يمكن إزالتها إذا كانت منصبة مسبقًا)
    os.system("pip install pyqtgraph PyQt5 PyOpenGL Pillow")

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())





















