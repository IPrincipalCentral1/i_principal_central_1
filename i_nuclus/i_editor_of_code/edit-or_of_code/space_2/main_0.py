












import os



os.system("pip install pyqtgraph")











import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PyQt5.QtWidgets import QApplication
import numpy as np
import sys

app = QApplication(sys.argv)
w = gl.GLViewWidget()
w.show()
w.setWindowTitle('3D Example')
w.setCameraPosition(distance=40)

# رسم شبكة
g = gl.GLGridItem()
w.addItem(g)

# رسم نقاط ثلاثية الأبعاد
pos = np.random.normal(size=(1000, 3))
sp = gl.GLScatterPlotItem(pos=pos, color=(1,1,1,1), size=2)
w.addItem(sp)

sys.exit(app.exec_())














