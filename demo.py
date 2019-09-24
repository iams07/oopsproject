import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QGraphicsScene
import points

class SimpleWindow(QtWidgets.QMainWindow, points.Ui_Dialog):

    def __init__(self, parent=None):
        super(SimpleWindow, self).__init__(parent)
        self.setupUi(self)
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.posx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.posy = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.stat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.edget = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.edgef = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.index = 0
        self.graphicsView.scene = QGraphicsScene()
        self.graphicsView.setScene(self.graphicsView.scene)
        self.graphicsView.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.graphicsView.mousePressEvent = self.pixelSelect
        self.graphicsView.mouseReleaseEvent = self.move

    def pixelSelect(self, event):
        pen = QPen(QtCore.Qt.black)
        erase = QPen(QtCore.Qt.white)
        eraseb = QBrush(QtCore.Qt.white)
        brush = QBrush(QtCore.Qt.black)
        font = 
        self.x1 = event.globalX()
        self.y1 = event.globalY()
        if self.radioButton.isChecked():
            self.graphicsView.scene.addEllipse(self.x1, self.y1, 10, 10, pen, brush)
            self.graphicsView.scene.addText()
            self.posx[self.index] = self.x1
            self.posy[self.index] = self.y1
            self.stat[self.index] = 1
            self.index = self.index + 1
        if self.radioButton_3.isChecked():
            self.f2=0
            for i in range(self.index):
                self.ni1 = abs(self.x1-self.posx[i])
                self.ni2 = abs(self.y1-self.posy[i])
                if self.ni1<10:
                    if self.ni2<10:
                        self.i1 = i
                        self.f2= 1
                        self.stat[i] = 0

            #item = self.graphicsView.scene.itemAt(self.posx[i],self.posy[i],self.graphicsView.transform())
            if self.f2==1:
                self.graphicsView.scene.addEllipse(self.posx[self.i1]-2,self.posy[self.i1]-2,13,13,erase,eraseb)
                for i in range(self.index):
                    self.graphicsView.scene.addLine(self.posx[self.i1]+5,self.posy[self.i1]+5,self.posx[i]+5,self.posy[i]+5,erase)
                    if self.stat[i]==1:
                        self.graphicsView.scene.addEllipse(self.posx[i],self.posy[i],10,10,pen,brush)

    def move(self,event):
        pen = QPen(QtCore.Qt.black)
        brush = QBrush(QtCore.Qt.black)
        self.x2 = event.globalX()
        self.y2 = event.globalY()
        self.min1 = 0
        self.mini1=0
        self.min2 = 0
        self.mini2=0
        self.mini3=0
        self.mini4=0
        self.f1=0
        self.f2=0
        if self.radioButton_2.isChecked():
            for i in range(self.index):
                self.mini1 = abs(self.x1-self.posx[i])
                self.mini2 = abs(self.y1-self.posy[i])
                if self.mini1<10:
                    if self.mini2<10:
                        self.min1 = i
                        self.f1=1
                self.mini3 = abs(self.x2-self.posx[i])
                self.mini4 = abs(self.y2-self.posy[i])
                if self.mini3<10:
                    if self.mini4<10:
                        self.min2 = i
                        self.f2=1
                if self.f1==1:
                    if self.f2==1:
                        self.graphicsView.scene.addLine(self.posx[self.min1]+5,self.posy[self.min1]+5,self.posx[self.min2]+5,self.posy[self.min2]+5,pen)
                

app = QtWidgets.QApplication(sys.argv)
form = SimpleWindow()
form.show()
app.exec_()