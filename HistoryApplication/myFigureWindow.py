# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import  QApplication, QMainWindow

##from PyQt5.QtCore import  pyqtSlot,pyqtSignal,Qt

##from PyQt5.QtWidgets import  

from PyQt5 import QtGui

##from PyQt5.QtSql import 

##from PyQt5.QtMultimedia import

##from PyQt5.QtMultimediaWidgets import


from Ui_Figure import Ui_FigureWindow
from PyQt5 import QtCore

class QmyFigureWindow(QMainWindow): 

   def __init__(self, parent=None):
      super().__init__(parent)   # 调用父类构造函数，创建窗体
      self.ui=Ui_FigureWindow()    # 创建UI对象
      self.ui.setupUi(self)      # 构造UI界面
      self.setAutoFillBackground(True)
      # if n == 0:
      #   window_pale = QtGui.QPalette()
      #   window_pale.setBrush(self.backgroundRole(),  QtGui.QBrush(QtGui.QPixmap("F:\A_code\PyQT_Demo\\back_ground.png"))) 
      #   self.ui.setPalette(window_pale)
      #   self._pic = QPixmap('')
##  ==============自定义功能函数========================


##  ==============event处理函数==========================
        
        
##  ==========由connectSlotsByName()自动连接的槽函数============        
   def on_DataIntegration_clicked(self):
      self.ui.textEdit.setText("搜索引擎使用占比")
        
##  =============自定义槽函数===============================        


   
