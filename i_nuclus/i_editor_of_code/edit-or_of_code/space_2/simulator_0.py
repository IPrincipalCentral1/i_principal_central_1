












import os



os.system("pip install pyqtgraph")



os.system("pip install PyQt5")



os.system("pip install PyOpenGL PyOpenGL_accelerate")



os.system("pip install imageio")


os.system("pip install pillow")







import sys
from PyQt5.QtWidgets import QApplication, QOpenGLWidget, QMainWindow
from PyQt5.QtCore import Qt
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
import numpy as np



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


                #image.putpixel((x, y), (255, 0, 0, color[3]))

                #put_point(image=image, x_0=x, y_0=y, color=(255, 0, 0, color[3]), border=1)
        
        
        
            x += 1
    
    
        y += 1



    image.save(path_of_file)
        



class GLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.texture = None

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        
        
        file_of_image = os.path.join(os.getcwd(), "image.png")
        
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128))
        

        self.texture = self.loadTexture(file_of_image)  
        
        # تأكد من وجود الصورة في نفس المجلد

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, w / h if h else 1, 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -5.0)
        glRotatef(self.xRot, 1.0, 0.0, 0.0)
        glRotatef(self.yRot, 0.0, 1.0, 0.0)
        glRotatef(self.zRot, 0.0, 0.0, 1.0)
        self.drawTexturedQuad()

    def loadTexture(self, path):
        image = Image.open(path).convert("RGB")
        image_data = image.transpose(Image.FLIP_TOP_BOTTOM).tobytes()
        width, height = image.size

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, image_data)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return tex_id

    def drawTexturedQuad(self):
        glBindTexture(GL_TEXTURE_2D, self.texture)
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-1, -1, 0)
        glTexCoord2f(1, 0); glVertex3f(1, -1, 0)
        glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
        glTexCoord2f(0, 1); glVertex3f(-1, 1, 0)
        glEnd()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.yRot -= 5
        elif event.key() == Qt.Key_Right:
            self.yRot += 5
        elif event.key() == Qt.Key_Up:
            self.xRot -= 5
        elif event.key() == Qt.Key_Down:
            self.xRot += 5
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("OpenGL 3D Image Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.widget = GLWidget()
        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())












