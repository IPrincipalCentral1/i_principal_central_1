

















list_of_liberary_to_install = [
                            
                            ["PyQt5"] ,
                            
                            
                            ["pyqtgraph"] ,
                            
                            
                            ["PyOpenGL"] ,
                            
                            
                            ["PyOpenGL_accelerate"] ,
                            
                            
                            ["imageio"] ,
                            
                            
                            ["pillow"] ,
                            



]










import os


import traceback

import sys


import subprocess




path_0 = os.path.dirname(cwd)

sys.path.append(os.path.join(path_0, "files_1"))


sys.path.append(cwd)



print(f"sys.path {sys.path} .")


#import i_principal_central_1


#import i_principal_central


try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
        
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
        
            
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
        
        
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
        
        
        counter_0 += 1
        
        
    
except:
    
        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    
    


print("\n" * 10)












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




def create_image(path_of_file, width, height, color, flip, border):
    
    
    
    
    # صورة شفافة تماماً

    image = Image.new("RGBA", (width, height), color)



    y = 0
    
    while (y < height):
    
    
        x = 0
        
        
        while (x < width):
        
            
            if (x == y):
            
                
                #pass
            
                if (border > 0):


                    image.putpixel((x, y), (255, 0, 0, color[3]))

                #put_point(image=image, x_0=x, y_0=y, color=(255, 0, 0, color[3]), border=1)
        
        
            x += 1
    
    
        y += 1


    if (flip == True):
    
        image = image.transpose(Image.FLIP_LEFT_RIGHT)



    image.save(path_of_file)
        




'''




file_of_image = os.path.join(os.getcwd(), "image.png")

create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128))





'''






class GLBoxWidget(QOpenGLWidget):


    def __init__(self, parent=None):

        super().__init__(parent)

        self.texture_id = None

        self.angle_x = 0

        self.angle_y = 0

        self.zoom = -5.0  # مستوى الزووم المبدئي (مسافة الكاميرا)
    
        self.pos_x = 0.0  # إزاحة المكعب على محور X
    
        self.pos_y = 0.0  # إزاحة المكعب على محور Y (ارتفاع)

    

        self.setFocusPolicy(Qt.StrongFocus) 
        

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.1, 0.1, 0.1, 1.0)


        #faces = ['front', 'back', 'left', 'right', 'top', 'bottom']
  
        faces = []
  
        
        file_of_image = os.path.join(os.getcwd(), "image.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=True, border=0)
        
        
                
        file_of_image = os.path.join(os.getcwd(), "front.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=False, border=1)
        
        
        
        faces.append([file_of_image, "front"])
            
                
        file_of_image = os.path.join(os.getcwd(), "back.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=True, border=1)
                
        
        
        faces.append([file_of_image, "back"])
        
        
                
        file_of_image = os.path.join(os.getcwd(), "left.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=True, border=0)
                
                
         
        faces.append([file_of_image, "left"])
        
        
                
        file_of_image = os.path.join(os.getcwd(), "right.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=True, border=0)
                
        
        
                
        
        faces.append([file_of_image, "right"])
                
                
        file_of_image = os.path.join(os.getcwd(), "top.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=True, border=0)
        
        
        
        faces.append([file_of_image, "top"])
        
        
                
        file_of_image = os.path.join(os.getcwd(), "bottom.png")
        
        create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 128), flip=True, border=0)
        
        
        faces.append([file_of_image, "bottom"])
        
        
        
        
        self.textures = {}

      
        for face in faces:
      
            path = f"{face[0]}"

            self.textures[face[1]] = self.load_texture(path)
        
        
        

        #self.texture_id = self.load_texture(file_of_image)

        glDisable(GL_CULL_FACE)  # Render both sides of faces







    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h if h != 0 else 1, 1, 100)
        glMatrixMode(GL_MODELVIEW)





    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
    
        glTranslatef(0.0, 0.0, self.zoom)
    
        # تحريك المكعب على محور X و Y
        glTranslatef(self.pos_x, self.pos_y, 0.0)
    
        glTranslatef(0.0, 0.0, -10)
        glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        glRotatef(self.angle_y, 0.0, 1.0, 0.0)
    
        self.drawTexturedBox()
    


    #def paintGL(self):
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        #glLoadIdentity()

        ## تكبير/تصغير
        #glTranslatef(0.0, 0.0, self.zoom)

        ## تحريك المكعب على محور X
        #glTranslatef(self.pos_x, 0.0, 0.0)

        ## الترجمة الخلفية الثابتة والدوران
        #glTranslatef(0.0, 0.0, -10)
        #glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        #glRotatef(self.angle_y, 0.0, 1.0, 0.0)

        #self.drawTexturedBox()





    #def paintGL(self):
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #glLoadIdentity()  # أبدأ بمصفوفة هوية جديدة

        ## حرك الكاميرا بمقدار zoom (التكبير/التصغير)
        #glTranslatef(0.0, 0.0, self.zoom)  

        ## بعدها طبق ترجمة ثابتة لتحريك المشهد للخلف قليلاً
        #glTranslatef(0.0, 0.0, -10)

        ## طبق الدوران بناءً على الزوايا
        #glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        #glRotatef(self.angle_y, 0.0, 1.0, 0.0)

        ## ارسم الصندوق أو المجسم
        #self.drawTexturedBox()



    #def paintGL(self):

        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #glLoadIdentity()
        #glTranslatef(0.0, 0.0, self.zoom)


        #glLoadIdentity()

        #glTranslatef(0.0, 0.0, -10)
        #glRotatef(self.angle_x, 1.0, 0.0, 0.0)
        #glRotatef(self.angle_y, 0.0, 1.0, 0.0)



        ##self.draw_textured_box(2.0, 2.0, 1.0)



        #self.drawTexturedBox()






    def load_texture(self, path):
        img = Image.open(path).transpose(Image.FLIP_TOP_BOTTOM)
        img_data = img.convert("RGBA").tobytes()
        width, height = img.size

        tex_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, tex_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height,
                     0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        return tex_id




    def drawTexturedBox(self):
        
        w, h, d = 2, 2, 0.2 #self.depth
    
        glEnable(GL_TEXTURE_2D)
    
        # FRONT
        glBindTexture(GL_TEXTURE_2D, self.textures['front'])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-w, -h, d)
        glTexCoord2f(1, 0); glVertex3f(w, -h, d)
        glTexCoord2f(1, 1); glVertex3f(w, h, d)
        glTexCoord2f(0, 1); glVertex3f(-w, h, d)
        glEnd()
    
        # BACK
        glBindTexture(GL_TEXTURE_2D, self.textures['back'])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(w, -h, -d)
        glTexCoord2f(1, 0); glVertex3f(-w, -h, -d)
        glTexCoord2f(1, 1); glVertex3f(-w, h, -d)
        glTexCoord2f(0, 1); glVertex3f(w, h, -d)
        glEnd()
    
        # LEFT
        glBindTexture(GL_TEXTURE_2D, self.textures['left'])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
        glTexCoord2f(1, 0); glVertex3f(-w, -h, d)
        glTexCoord2f(1, 1); glVertex3f(-w, h, d)
        glTexCoord2f(0, 1); glVertex3f(-w, h, -d)
        glEnd()
    
        # RIGHT
        glBindTexture(GL_TEXTURE_2D, self.textures['right'])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(w, -h, d)
        glTexCoord2f(1, 0); glVertex3f(w, -h, -d)
        glTexCoord2f(1, 1); glVertex3f(w, h, -d)
        glTexCoord2f(0, 1); glVertex3f(w, h, d)
        glEnd()
    
        # TOP
        glBindTexture(GL_TEXTURE_2D, self.textures['top'])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-w, h, d)
        glTexCoord2f(1, 0); glVertex3f(w, h, d)
        glTexCoord2f(1, 1); glVertex3f(w, h, -d)
        glTexCoord2f(0, 1); glVertex3f(-w, h, -d)
        glEnd()
    
        # BOTTOM
        glBindTexture(GL_TEXTURE_2D, self.textures['bottom'])
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(-w, -h, -d)
        glTexCoord2f(1, 0); glVertex3f(w, -h, -d)
        glTexCoord2f(1, 1); glVertex3f(w, -h, d)
        glTexCoord2f(0, 1); glVertex3f(-w, -h, d)
        glEnd()
    
        glDisable(GL_TEXTURE_2D)
    
    
    
    def keyPressEvent(self, event):
        key = event.key()
        modifiers = event.modifiers()
    
    
        if modifiers == Qt.ShiftModifier:
            if key == Qt.Key_Left:
                self.zoom += 0.5  # Zoom in
                self.update()
                return
            elif key == Qt.Key_Right:
                self.zoom -= 0.5  # Zoom out
                self.update()
                return
    
    
    
        elif modifiers == Qt.ControlModifier:
            if key == Qt.Key_Right:
                self.pos_x += 0.5  # تحريك يمين
                self.update()
            elif key == Qt.Key_Left:
                self.pos_x -= 0.5  # تحريك يسار
                self.update()
            elif key == Qt.Key_Up:
                self.pos_y += 0.5  # ارتفاع لأعلى
                self.update()
            elif key == Qt.Key_Down:
                self.pos_y -= 0.5  # نزول لأسفل
                self.update()
    
        # تحريك الدوران بدون Ctrl
        else:
            if key == Qt.Key_Left:
                self.angle_y -= 5
                self.update()
            elif key == Qt.Key_Right:
                self.angle_y += 5
                self.update()
            elif key == Qt.Key_Up:
                self.angle_x -= 5
                self.update()
            elif key == Qt.Key_Down:
                self.angle_x += 5
                self.update()
    


    #def keyPressEvent(self, event):
        #key = event.key()
        #modifiers = event.modifiers()

        #if modifiers == Qt.ControlModifier:
            #if key == Qt.Key_Right:
                #self.pos_x += 0.5  # حرك المكعب لليمين
                #self.update()
            #elif key == Qt.Key_Left:
                #self.pos_x -= 0.5  # حرك المكعب لليسار
                #self.update()

        ## تحريك الدوران بدون ctrl
        #if modifiers != Qt.ControlModifier:
            #if key == Qt.Key_Left:
                #self.angle_y -= 5
                #self.update()
            #elif key == Qt.Key_Right:
                #self.angle_y += 5
                #self.update()
            #elif key == Qt.Key_Up:
                #self.angle_x -= 5
                #self.update()
            #elif key == Qt.Key_Down:
                #self.angle_x += 5
                #self.update()




    #def keyPressEvent(self, event):
        #key = event.key()
        #modifiers = event.modifiers()

        ## Zoom with Shift + Left/Right
        #if modifiers == Qt.ShiftModifier:
            #if key == Qt.Key_Left:
                #self.zoom += 0.5  # Zoom in
                #self.update()
                #return
            #elif key == Qt.Key_Right:
                #self.zoom -= 0.5  # Zoom out
                #self.update()
                #return

        ## Rotate with arrow keys only (no Shift)
        #if key == Qt.Key_Left:
            #self.angle_y -= 5
        #elif key == Qt.Key_Right:
            #self.angle_y += 5
        #elif key == Qt.Key_Up:
            #self.angle_x -= 5
        #elif key == Qt.Key_Down:
            #self.angle_x += 5

        #self.update()







class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("simulator")
        self.setGeometry(100, 100, 800, 600)
        self.viewer = GLBoxWidget()
        self.setCentralWidget(self.viewer)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())



































