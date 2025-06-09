












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
        




'''




file_of_image = os.path.join(os.getcwd(), "image.png")

create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128))





'''






class GLWidget(QOpenGLWidget):
    def __init__(self):
        
        super().__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.texture = None
        self.aspect = 1
        
        

    def initializeGL(self):
        
        
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)

        
        
        
        

        # لإظهار كلا الوجهين (الأمامي والخلفي)
        glDisable(GL_CULL_FACE)
        
        # أو لو تريد تحسين الأداء وإظهار وجه واحد:
        # glEnable(GL_CULL_FACE)
        # glCullFace(GL_BACK)
        
        # تحسين جودة الصورة (فلترة)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
         
        
        file_of_image = os.path.join(os.getcwd(), "image.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 255))
                
        
        
        self.texture, self.aspect = self.loadTexture(file_of_image)

    

        self.texture_id = self.load_texture(file_of_image)
    


        
    def load_texture(self, path):
        img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM).convert("RGBA")
        img_data = img.tobytes()
        
        width, height = img.size
    
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)
    
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    
        return texture_id




    #def load_texture(self, path):
        #img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM).convert("RGBA")
        #img_data = img.tobytes()

        #width, height = img.size

        #texture_id = glGenTextures(1)
        #glBindTexture(GL_TEXTURE_2D, texture_id)

        ## إعدادات النسيج
        #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        #glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0,
                     #GL_RGBA, GL_UNSIGNED_BYTE, img_data)

        #return texture_id



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
        
        
        #self.drawTexturedQuad()
        
        self.drawTexturedBox(self.texture_id, thickness=0.2)



    

    def loadTexture(self, path):
        image = Image.open(path).convert("RGB")
        image = image.transpose(Image.FLIP_TOP_BOTTOM)  # قلب الصورة رأسياً

        image_data = image.tobytes()

        width, height = image.size
        aspect = width / height

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)

        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)  # ضروري لتفادي تشوه الألوان

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                     GL_RGB, GL_UNSIGNED_BYTE, image_data)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        return tex_id, aspect

    #def drawTexturedBox(self, thickness=0.1):
        #glBindTexture(GL_TEXTURE_2D, self.texture)
        #a = self.aspect
        #d = thickness / 2

        ## Front face (with texture)
        #glBegin(GL_QUADS)
        #glTexCoord2f(0, 0); glVertex3f(-a, -1,  d)
        #glTexCoord2f(1, 0); glVertex3f( a, -1,  d)
        #glTexCoord2f(1, 1); glVertex3f( a,  1,  d)
        #glTexCoord2f(0, 1); glVertex3f(-a,  1,  d)
        #glEnd()

        ## Other faces (no texture, simple color)
        #glDisable(GL_TEXTURE_2D)
        #glColor3f(0.2, 0.2, 0.2)  # رمادي غامق

        #glBegin(GL_QUADS)
        ## Back face
        #glVertex3f(-a, -1, -d)
        #glVertex3f( a, -1, -d)
        #glVertex3f( a,  1, -d)
        #glVertex3f(-a,  1, -d)

        ## Left
        #glVertex3f(-a, -1, -d)
        #glVertex3f(-a, -1,  d)
        #glVertex3f(-a,  1,  d)
        #glVertex3f(-a,  1, -d)

        ## Right
        #glVertex3f( a, -1, -d)
        #glVertex3f( a, -1,  d)
        #glVertex3f( a,  1,  d)
        #glVertex3f( a,  1, -d)

        ## Top
        #glVertex3f(-a,  1, -d)
        #glVertex3f( a,  1, -d)
        #glVertex3f( a,  1,  d)
        #glVertex3f(-a,  1,  d)

        ## Bottom
        #glVertex3f(-a, -1, -d)
        #glVertex3f( a, -1, -d)
        #glVertex3f( a, -1,  d)
        #glVertex3f(-a, -1,  d)
        #glEnd()

        #glEnable(GL_TEXTURE_2D)




    def drawTexturedBox(self, texture_id, thickness=0.1):
        a = 1.0  # نصف عرض الصورة
        b = 1.0  # نصف طول الصورة
        d = thickness / 2.0  # نصف السُمك
    
        glBindTexture(GL_TEXTURE_2D, texture_id)
    
        # ----- Front face (with texture) -----
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-a, -b,  d)
        glTexCoord2f(1, 0); glVertex3f( a, -b,  d)
        glTexCoord2f(1, 1); glVertex3f( a,  b,  d)
        glTexCoord2f(0, 1); glVertex3f(-a,  b,  d)
        glEnd()
    
        # ----- Back face (same texture, flipped) -----
        glBegin(GL_QUADS)
        glTexCoord2f(1, 0); glVertex3f(-a, -b, -d)
        glTexCoord2f(0, 0); glVertex3f( a, -b, -d)
        glTexCoord2f(0, 1); glVertex3f( a,  b, -d)
        glTexCoord2f(1, 1); glVertex3f(-a,  b, -d)
        glEnd()
    
        # ----- Other faces (optional: color only, no texture) -----
        glColor3f(0.5, 0.5, 0.5)  # رمادي
    
        # Right
        glBegin(GL_QUADS)
        glVertex3f(a, -b, -d)
        glVertex3f(a, -b,  d)
        glVertex3f(a,  b,  d)
        glVertex3f(a,  b, -d)
        glEnd()
    
        # Left
        glBegin(GL_QUADS)
        glVertex3f(-a, -b,  d)
        glVertex3f(-a, -b, -d)
        glVertex3f(-a,  b, -d)
        glVertex3f(-a,  b,  d)
        glEnd()
    
        # Top
        glBegin(GL_QUADS)
        glVertex3f(-a, b,  d)
        glVertex3f( a, b,  d)
        glVertex3f( a, b, -d)
        glVertex3f(-a, b, -d)
        glEnd()
    
        # Bottom
        glBegin(GL_QUADS)
        glVertex3f(-a, -b, -d)
        glVertex3f( a, -b, -d)
        glVertex3f( a, -b,  d)
        glVertex3f(-a, -b,  d)
        glEnd()
    
        glColor3f(1, 1, 1)  # إعادة اللون للأبيض
    



    #def drawTexturedQuad(self):
        #glBindTexture(GL_TEXTURE_2D, self.texture)
        #a = self.aspect
        #glBegin(GL_QUADS)
        #glTexCoord2f(0, 0); glVertex3f(-a, -1, 0)
        #glTexCoord2f(1, 0); glVertex3f( a, -1, 0)
        #glTexCoord2f(1, 1); glVertex3f( a,  1, 0)
        #glTexCoord2f(0, 1); glVertex3f(-a,  1, 0)
        #glEnd()





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















#class GLWidget(QOpenGLWidget):
    #def __init__(self):
        #super().__init__()
        #self.setFocusPolicy(Qt.StrongFocus)  # السماح باستقبال أحداث لوحة المفاتيح
        #self.xRot = 0
        #self.yRot = 0
        #self.zRot = 0
        #self.texture = None
        #self.aspect = 1  # نسبة العرض إلى الارتفاع

    #def initializeGL(self):
        #glEnable(GL_DEPTH_TEST)
        #glEnable(GL_TEXTURE_2D)

        #file_of_image = os.path.join(os.getcwd(), "image.png")


        #create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128))





        #self.texture, self.aspect = self.loadTexture(file_of_image)

    #def resizeGL(self, w, h):
        #glViewport(0, 0, w, h)
        #glMatrixMode(GL_PROJECTION)
        #glLoadIdentity()
        #gluPerspective(45.0, w / h if h else 1, 0.1, 100.0)
        #glMatrixMode(GL_MODELVIEW)

    #def paintGL(self):
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glLoadIdentity()
        #glTranslatef(0.0, 0.0, -5.0)
        #glRotatef(self.xRot, 1.0, 0.0, 0.0)
        #glRotatef(self.yRot, 0.0, 1.0, 0.0)
        #glRotatef(self.zRot, 0.0, 0.0, 1.0)
        #self.drawTexturedQuad()

    #def loadTexture(self, path):
        #image = Image.open(path).convert("RGB")
        #image_data = image.transpose(Image.FLIP_TOP_BOTTOM).tobytes()
        #width, height = image.size
        #aspect = width / height

        #tex_id = glGenTextures(1)
        #glBindTexture(GL_TEXTURE_2D, tex_id)
        #glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0,
                     #GL_RGB, GL_UNSIGNED_BYTE, image_data)
        #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        #return tex_id, aspect

    #def drawTexturedQuad(self):
        #glBindTexture(GL_TEXTURE_2D, self.texture)
        #a = self.aspect
        #glBegin(GL_QUADS)
        #glTexCoord2f(0, 0); glVertex3f(-a, -1, 0)
        #glTexCoord2f(1, 0); glVertex3f( a, -1, 0)
        #glTexCoord2f(1, 1); glVertex3f( a,  1, 0)
        #glTexCoord2f(0, 1); glVertex3f(-a,  1, 0)
        #glEnd()

    #def keyPressEvent(self, event):
        #if event.key() == Qt.Key_Left:
            #self.yRot -= 5
        #elif event.key() == Qt.Key_Right:
            #self.yRot += 5
        #elif event.key() == Qt.Key_Up:
            #self.xRot -= 5
        #elif event.key() == Qt.Key_Down:
            #self.xRot += 5
        #self.update()

#class MainWindow(QMainWindow):
    #def __init__(self):
        #super().__init__()
        #self.setWindowTitle("OpenGL 3D Image Viewer")
        #self.setGeometry(100, 100, 800, 600)
        #self.widget = GLWidget()
        #self.setCentralWidget(self.widget)

#if __name__ == "__main__":
    #app = QApplication(sys.argv)
    #window = MainWindow()
    #window.show()
    #sys.exit(app.exec_())







