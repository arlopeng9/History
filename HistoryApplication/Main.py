

# -*- coding: utf-8 -*-

from IndexForm import Ui_MainWindow
# import PyQt5
import Algorithm
import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QImage, QPixmap

class MyWindow(QMainWindow, Ui_MainWindow):
 def __init__(self, *args, **kwargs):
     super().__init__(*args, **kwargs)
     self.setupUi(self)
     self.pushButton.clicked.connect(self.OnPushButton1)
     
 num = 0

 def OnPushButton1(self):
     self.textEdit.append("HellowPyQt5")
     self.num += 1
     self.setWindowTitle("pushbutton has been clicked {0} times".format(self.num))
     return None

if __name__ == "__main__":
 app = QApplication(sys.argv)
 mainWindow = MyWindow()
 mainWindow.show()
 sys.exit(app.exec_())

