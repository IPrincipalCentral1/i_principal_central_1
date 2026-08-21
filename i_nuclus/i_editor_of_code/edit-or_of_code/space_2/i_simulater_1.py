

















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



















class GLBoxWidget(QOpenGLWidget):


    def __init__(self, parent=None):

        super().__init__(parent)











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
























