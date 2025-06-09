












import os



os.system("pip install pyqtgraph")



os.system("pip install PyQt5")



os.system("pip install PyOpenGL PyOpenGL_accelerate")



os.system("pip install imageio")


os.system("pip install pillow")





import sys
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QMainWindow
from PyQt5.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import math




def put_point(image, x_0, y_0, color, border):


    y_1 = 0
    
    while (y_1 < image.size[1]):
    
    
        x_1 = 0
        
        while (x_1 < image.size[0]):
        
            
            
            var_bool_0 = (x_0 <= x_1 - border)
            
            
            var_bool_1 = (x_1 + border <= x_0)
            
            
            var_bool_2 = (y_0 <= y_1 - border)
                
            
            var_bool_3 = (y_1 + border <= y_0)
        
        
            if (var_bool_0 or var_bool_1 or var_bool_2 or var_bool_3):
            
                image.putpixel((x_1, y_1), color)
        
        
            x_1 += 1


        y_1 += 1




def create_image(path_of_file, width, height, color):
    
    
    
    
    # صورة شفافة تماماً

    image = Image.new("RGBA", (width, height), color)



    y = 0
    
    while (y < height):
    
    
        x = 0
        
        
        while (x < width):
        
            if (x == y):
            
                pass

                image.putpixel((x, y), (255, 0, 0, color[3]))

                #put_point(image=image, x_0=x, y_0=y, color=(255, 0, 0, color[3]), border=1)
        
        
        
            x += 1
    
    
        y += 1



    image.save(path_of_file)
        


class RotatingImage3D(QOpenGLWidget):
    def __init__(self, image_path):
        super().__init__()
        self.image_path = image_path
        self.angle = 0
        self.texture_id = None

        # تدوير تلقائي كل 16ms
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_rotation)
        self.timer.start(16)

    def update_rotation(self):
        self.angle += 1
        if self.angle > 360:
            self.angle -= 360
        self.update()

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        self.texture_id = self.load_texture(self.image_path)
        glClearColor(0.0, 0.0, 0.0, 1.0)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, w / h if h != 0 else 1, 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # الكاميرا
        gluLookAt(0, 0, 5,   0, 0, 0,   0, 1, 0)

        # تدوير المستوي حول Y
        glRotatef(self.angle, 0, 1, 0)

        # رسم المستوي مع الصورة
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.0, -1.0, 0.0)

        glTexCoord2f(1.0, 0.0)
        glVertex3f(1.0, -1.0, 0.0)

        glTexCoord2f(1.0, 1.0)
        glVertex3f(1.0, 1.0, 0.0)

        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.0, 1.0, 0.0)
        glEnd()

    def load_texture(self, path):
        image = Image.open(path).convert("RGBA")
        img_data = image.tobytes("raw", "RGBA", 0, -1)
        width, height = image.size

        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        return texture_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3D Image Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.image_path = os.path.join(os.getcwd(), "image.png") 

        
        create_image(path_of_file=self.image_path, width=10, height=10, color=(0, 255, 255, 128))
        
        self.glWidget = RotatingImage3D(self.image_path)
        self.setCentralWidget(self.glWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
















