












import os



os.system("pip install pyqtgraph")



os.system("pip install PyQt5")



os.system("pip install PyOpenGL PyOpenGL_accelerate")



os.system("pip install imageio")


os.system("pip install pillow")






import sys
import os
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt
import pyqtgraph.opengl as pgl
from OpenGL import GL
from PIL import Image





def create_image(path_of_file, width, height, color):
    
    
    # صورة شفافة تماماً

    image = Image.new("RGBA", (width, height), color)

    
    y = 0
    
    while (y < height):
    
        x = 0
        
        while (x < width):
        
            image.putpixel((x, y), color)
                        
            x += 1
            
            
        y += 1
    



    image.save(path_of_file)

















class ImagePlane(pgl.GLMeshItem):
    def __init__(self, image_path, size=10.0, pos=(0, 0, 0)):
        # إنشاء مستطيل بمقاسات size*size على XY plane (Z=0)
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
        self.setGLOptions('translucent')  # مهم جداً لتمكين الشفافية

        self.image_path = image_path
        self.texture_id = self.load_texture()

    def load_texture(self):
        img = Image.open(self.image_path).convert("RGBA")
        img_data = img.tobytes("raw", "RGBA", 0, -1)

        texture_id = GL.glGenTextures(1)
        GL.glBindTexture(GL.GL_TEXTURE_2D, texture_id)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR)
        GL.glTexImage2D(GL.GL_TEXTURE_2D, 0, GL.GL_RGBA,
                        img.size[0], img.size[1], 0,
                        GL.GL_RGBA, GL.GL_UNSIGNED_BYTE, img_data)
        return texture_id

    def paint(self):
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glEnable(GL.GL_TEXTURE_2D)
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.texture_id)
        super().paint()
        GL.glDisable(GL.GL_TEXTURE_2D)
        GL.glDisable(GL.GL_BLEND)


class CustomGLViewWidget(pgl.GLViewWidget):
    def keyPressEvent(self, event):
        # تعطيل تحكم الأسهم في المشهد
        if event.key() in (Qt.Key_Up, Qt.Key_Down, Qt.Key_Left, Qt.Key_Right):
            return
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

        # إنشاء صورة شفافة لونها سماوي (RGBA)
        file_of_image = os.path.join(os.getcwd(), "image.png")
        create_image(path_of_file=file_of_image, color=(0, 255, 255, 128), width=100, height=100)  # alpha=128 نصف شفاف

        # إضافة الصورة كـ textured plane في المشهد
        if os.path.exists(file_of_image):
            image_item = ImagePlane(file_of_image, size=10.0, pos=(5, 5, 0))
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
        self.setWindowTitle("3D Viewer with Transparent Image")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: black;")

        self.viewer = My3DViewer()
        self.setCentralWidget(self.viewer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
















