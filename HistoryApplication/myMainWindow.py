# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import  QApplication, QMainWindow

##from PyQt5.QtCore import  pyqtSlot,pyqtSignal,Qt

##from PyQt5.QtWidgets import  

##from PyQt5.QtGui import

##from PyQt5.QtSql import 

##from PyQt5.QtMultimedia import

##from PyQt5.QtMultimediaWidgets import

from myFigureWindow import QmyFigureWindow
from ui_MainWindow import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot,Qt
import numpy as np
from Algorithm import visitVisible

class QmyMainWindow(QMainWindow): 

   def __init__(self, parent=None):
      super().__init__(parent)   # 调用父类构造函数，创建窗体
      self.ui=Ui_MainWindow()    # 创建UI对象
      self.ui.setupUi(self)      # 构造UI界面
#       mplStyle.use("classic")    #使用样式，必须在绘图之前调用,修改字体后才可显示汉字

#       mpl.rcParams['font.sans-serif']=['KaiTi','SimHei']   #显示汉字为 楷体， 汉字不支持 粗体，斜体等设置
#       mpl.rcParams['font.size']=12  
# ##  Windows自带的一些字体
# ##  黑体：SimHei 宋体：SimSun 新宋体：NSimSun 仿宋：FangSong  楷体：KaiTi 
#       mpl.rcParams['axes.unicode_minus'] =False    #减号unicode编码

#       self.__fig=None      #Figue对象
#       self.__curAxes=None  #当前操作的Axes，为了方便单独用变量
#       self.__curLine=None  #当前操作的曲线
      
#       self.__createFigure()  #创建Figure和FigureCanvas对象，初始化界面
#       self.__drawFig2X1()    #绘图

#       axesList=self.__fig.axes   #子图列表
#       for one in axesList:       #添加到工具栏上的下拉列表框里
#          self.__comboAxes.addItem(one.get_label())

#       legendLocs=['best','upper right','upper left', 'lower left',
#                   'lower right', 'right', 'center left','center right',
#                   'lower center', 'upper center', 'center']  #图例位置
#       self.ui.combo_LegendLoc.addItems(legendLocs)    #添加选项
      
#       styleList=mplStyle.available     #可用样式列表，字符串列表
#       self.ui.comboFig_Style.addItems(styleList)
##  ==============自定义功能函数========================


##  ==============event处理函数==========================
        
        
##  ==========由connectSlotsByName()自动连接的槽函数============        
   def on_DataIntegration_clicked(self):
      self.ui.textEdit.setText("搜索引擎使用占比")
        
##  =============自定义槽函数===============================        
#    def __createFigure(self):
#    ##      self.__fig=mpl.figure.Figure(figsize=(8, 5),constrained_layout=True, tight_layout=None)  #单位英寸
#    ##      self.__fig=mpl.figure.Figure(figsize=(8, 5))  #单位英寸
#       self.__fig=mpl.figure.Figure() 
#       figCanvas = FigureCanvas(self.__fig)  #创建FigureCanvas对象，必须传递一个Figure对象
#       self.__fig.suptitle("suptitle:matplotlib in Qt GUI",fontsize=16, fontweight='bold')  # 总的图标题

#       naviToolbar=NavigationToolbar(figCanvas, self)  #创建NavigationToolbar工具栏
#       actList=naviToolbar.actions()  #关联的Action列表
#       count=len(actList)       #Action的个数
#       lastAction=actList[count-1]   #最后一个Action

#       labCurAxes=QLabel("当前子图")
#       naviToolbar.insertWidget(lastAction,labCurAxes)
#       self.__comboAxes=QComboBox(self)    #子图列表，用于选择子图
#       self.__comboAxes.setToolTip("选择当前子图")
#       self.__comboAxes.currentIndexChanged.connect(self.do_currentAxesChaned)
#       naviToolbar.insertWidget(lastAction,self.__comboAxes)

#       naviToolbar.insertAction(lastAction,self.ui.actQuit)  #在最后一个Action之前插入一个Action
#    ##      naviToolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  #ToolButtonTextUnderIcon
#       self.addToolBar(naviToolbar)  #添加作为主窗口工具栏

#       splitter = QSplitter(self)
#       splitter.setOrientation(Qt.Horizontal)
#       splitter.addWidget(self.ui.toolBox)    #左侧控制面板
#       splitter.addWidget(figCanvas)          #右侧FigureCanvas对象
#       self.setCentralWidget(splitter)


   
#    def __drawFig2X1(self):  ##初始化绘图
# ##      gs=self.__fig.add_gridspec(2,1)  #2行，1列
# ##
# ##      ax1=self.__fig.add_subplot(gs[0,0],label="sin-cos plot")  #子图1
#       ax1=self.__fig.add_subplot(2,1,1,label="sin-cos plot")  #子图1
#       t = np.linspace(0, 10, 40)
#       y1=np.sin(t)
#       y2=np.cos(2*t)
#       ax1.plot(t,y1,'r-o',label="sin", linewidth=2, markersize=5)    #绘制一条曲线
#       ax1.plot(t,y2,'b--',label="cos",linewidth=2)    #绘制一条曲线
#       ax1.set_xlabel('X 轴')      # X轴标题
#       ax1.set_ylabel('Y 轴')      # Y轴标题
#       ax1.set_xlim([0,10])        # X轴坐标范围
#       ax1.set_ylim([-1.5,1.5])    # Y轴坐标范围
#       ax1.set_title("三角函数曲线")
#       ax1.legend()         #自动创建图例
#       self.__curAxes=ax1   #当前操作的Axes对象
      

# ##      ax2=self.__fig.add_subplot(gs[1,0],label="magnitude plot") #子图2
#       ax2=self.__fig.add_subplot(2,1,2,label="magnitude plot")    #子图2
#       w = np.logspace(-1, 1, 100)   # 10^(-1,1)之间，100个点
#       mag=self.__getMag(w,zta=0.1,wn=1)   #阻尼比=0.1
#       ax2.semilogx(w,mag,'g-',label=r"$\zeta=0.2$", linewidth=2)  #绘制一条曲线, 

#       mag=self.__getMag(w,zta=0.4,wn=1)   #阻尼比=0.4
#       ax2.semilogx(w,mag,'r:',label=r"$\zeta=0.4$", linewidth=2)  #绘制一条曲线

#       mag=self.__getMag(w,zta=0.8,wn=1)   #阻尼比=0.8
#       ax2.semilogx(w,mag,'b--',label=r"$\zeta=0.8$", linewidth=2) #绘制一条曲线

#       ax2.set_xlabel('角频率(rad/sec)')   # X轴标题
#       ax2.set_ylabel('幅度(dB)')          # Y轴标题
#       ax2.set_title("二阶系统幅频曲线")
#       ax2.legend()    #自动创建Axes的图例


   def on_pushButton_clicked(self):
      figure = QmyFigureWindow(self)
      figure.setAttribute(Qt.WA_DeleteOnClose)
      figure.setWindowTitle('figure')
      figure.show()
   
##  ============窗体测试程序 ================================
if  __name__ == "__main__":        #用于当前窗体测试
   app = QApplication(sys.argv)    #创建GUI应用程序
   form=QmyMainWindow()            #创建窗体
   form.show()
   sys.exit(app.exec_())
