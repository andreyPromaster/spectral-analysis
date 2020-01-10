
import sys
from functools import partial
from myinterface import *
from PyQt5 import QtCore, QtGui, QtWidgets
import scipy as sp
import matplotlib.pylab as plt
from PyQt5.QtCore import Qt,QPointF
from PyQt5.QtWidgets import QSlider,QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem,QGraphicsSceneMouseEvent, QStyleOptionSlider, QStyle, QWidget, QFormLayout, QLabel ,QGraphicsScene,QGraphicsView, QFrame, QColorDialog
from PyQt5.QtGui import QColor,QBrush,QImage,QPainter,QPen


class MyWin(QtWidgets.QMainWindow):
    color = QColor(0,0,0)
    coeffIncreaseX = 1
    coeffIncreaseY = 1
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.horizontalSlider.setRange(0,120)
        self.ui.horizontalSlider.setSliderPosition(20)
        self.ui.horizontalSlider_2.setRange(0,360)
        self.ui.horizontalSlider_3.setRange(1,5)
        self.ui.horizontalSlider_4.setRange(1,5)
        scene = QGraphicsScene()
        scene.setSceneRect(0,0,364,510)
        
        self.ui.graphicsView.setScene(scene)
        self.ui.graphicsView.setRenderHint (QPainter.Antialiasing)
        self.ui.graphicsView.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)

        self.ui.horizontalSlider.valueChanged.connect(partial(self.performScale,scene = scene))
        self.ui.horizontalSlider.valueChanged.connect(self.showScale)

        self.ui.horizontalSlider_2.valueChanged.connect(partial(self.performRotation,scene = scene))
        self.ui.horizontalSlider_2.valueChanged.connect(self.showAngle)

        self.ui.horizontalSlider_3.valueChanged.connect(self.showCoeffX)
        self.ui.horizontalSlider_3.valueChanged.connect(self.getIncreaseCoeffX)
        self.ui.horizontalSlider_3.setToolTip('Вытягивает фигуру горизонтально')

        self.ui.horizontalSlider_4.valueChanged.connect(self.showCoeffY)
        self.ui.horizontalSlider_4.valueChanged.connect(self.getIncreaseCoeffY)
        self.ui.horizontalSlider_4.setToolTip('Вытягивает фигуру вертикально')

        self.ui.frame_2.setStyleSheet("QWidget { background-color: %s}" % self.color.name())
        
        self.ui.pushButton_3.clicked.connect(partial(self.makePhaseProcessing,scene = scene))
        self.ui.pushButton_5.setToolTip('Настаивает цвет фигуры')
        self.ui.pushButton_5.clicked.connect(self.showColorDialog)
        self.ui.pushButton.clicked.connect(partial(self.createSelectedGeometricItem,scene = scene))
        self.ui.pushButton.setToolTip('Создаем выбранную фигуру на сцене')
        self.ui.pushButton_2.clicked.connect(partial(self.changeColorItem,scene = scene))
        self.ui.pushButton_2.setToolTip('Изменить цвет выбранной фигуры')
        scene.selectionChanged.connect(partial(self.setCurrentTransform,scene = scene))
        self.ui.pushButton_4.clicked.connect(partial(self.makeSpectralProcessing,scene = scene))
    def setCurrentTransform(self,scene):
        items = scene.selectedItems()
        for shape in items:
            self.ui.horizontalSlider.setSliderPosition(shape.scale()*20)
            self.ui.label_4.setText(str(shape.scale()))   
            self.ui.horizontalSlider_2.setSliderPosition(shape.rotation())
            self.ui.label_3.setText(str(shape.rotation()))
    def makeSpectralProcessing(self,scene):
        self.saveScene(scene)
        analysis = FourierTransforms()
        analysis.showSpectr()
    def makePhaseProcessing(self,scene):
        self.saveScene(scene)
        analysis = FourierTransforms()
        analysis.showPhaseFreq()
    def performScale(self, scene):
        _scale = self.ui.horizontalSlider.value()/20
        items = scene.selectedItems()
        for shape in items:
            shape.setTransformOriginPoint(30,30)
            shape.prepareGeometryChange()
            shape.setScale(_scale)
    def getIncreaseCoeffY(self):
        self.coeffIncreaseY = self.ui.horizontalSlider_4.value()
    def getIncreaseCoeffX(self):
        self.coeffIncreaseX = self.ui.horizontalSlider_3.value()
    def showCoeffY(self):
        self.ui.label_7.setText(str(self.ui.horizontalSlider_4.value()))
    def showCoeffX(self):
        self.ui.label_8.setText(str(self.ui.horizontalSlider_3.value()))
    def showAngle(self):
        self.ui.label_3.setText(str(self.ui.horizontalSlider_2.value()))
    def showScale(self):
        self.ui.label_4.setText(str(self.ui.horizontalSlider.value()/20))
    def performRotation(self,scene):
        angleOfRotation = self.ui.horizontalSlider_2.value()
        items = scene.selectedItems()
        for shape in items:
            shape.setTransformOriginPoint(30,30)
            shape.prepareGeometryChange()
            shape.setRotation(angleOfRotation)

    def changeColorItem(self,scene):
        items = scene.selectedItems()
        for i in items:
            brush = QBrush(self.color)
            i.setBrush(brush)
    def saveScene(self,scene):
        area = scene.sceneRect()
        image = QImage(scene.width(),scene.height(), QImage.Format_ARGB32_Premultiplied)
        image.fill(0)
        painter = QPainter(image)
        painter.setRenderHint(QPainter.Antialiasing)
        scene.update(area)
        scene.render(painter)
        painter.end()
    # Save the image to a file.
        image.save("capture.bmp")
    def showColorDialog(self):
        self.color = QColorDialog.getColor()
        if self.color.isValid():
            self.ui.frame_2.setStyleSheet("QWidget { background-color: %s}" % self.color.name())
    def createSelectedGeometricItem(self,scene):
        if self.ui.radioButton.isChecked()==True:
            brush = QBrush(self.color)
            rect = QGraphicsRectItem(30,30,self.coeffIncreaseX*20,self.coeffIncreaseY*20)
            rect.setBrush(brush)
            pen = QPen(Qt.NoPen)
            rect.setPen(pen)
            rect.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            scene.addItem(rect)
        else:
            brush = QBrush(self.color)
            elps = QGraphicsEllipseItem(30,30,self.coeffIncreaseX*30,self.coeffIncreaseY*30)
            elps.setBrush(brush)
            pen = QPen(Qt.NoPen)
            elps.setPen(pen)
            elps.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
            scene.addItem(elps)
    def createRect (self,scene):
        brush = QBrush(self.color)
        rect = QGraphicsRectItem(30,30,self.coeffIncreaseX*20,self.coeffIncreaseY*20)
        rect.setBrush(brush)
        pen = QPen(Qt.NoPen)
        rect.setPen(pen)
        rect.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        scene.addItem(rect)
    def createElp(self,scene):
        brush = QBrush(self.color)
        elps = QGraphicsEllipseItem(30,30,self.coeffIncreaseX*30,self.coeffIncreaseY*30)
        elps.setBrush(brush)
        pen = QPen(Qt.NoPen)
        elps.setPen(pen)
        elps.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        scene.addItem(elps)
    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self,"Confirm Dialog", "Действительно выйти?", QtWidgets.QMessageBox.Yes 
                                                |QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

from PIL import Image
from scipy.fftpack import fft, fftfreq, fftshift,fftn
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class FourierTransforms:
    freqX = 0
    freqY = 0
    image = None
    fft_result = None
    def __init__(self):
        self.image = Image.open('capture.bmp')
        self.image = self.image.convert("F")
        self.image =np.array(self.image)
        self.getFreq()
        self.makefft2()
    def getImageSize(self):    
         size = self.image.shape
         return size
    def getFreq(self):
        size_x = self.getImageSize()[1] #размер по х
        size_y = self.getImageSize()[0] #размер по у
        self.freqX = fftfreq(size_x,1./(2*size_x))
        self.freqY = fftfreq(size_y,1./(2*size_y))
        self.freqX=fftshift(self.freqX)
        self.freqY= fftshift(self.freqY)
    def makefft2(self):
        self.fft_result = fftn(self.image)
        self.fft_result = fftshift(self.fft_result)
    def showSpectr(self):
        fig = plt.figure(1)
        axes = Axes3D(fig)
        xgrid, ygrid = np.meshgrid(self.freqX, self.freqY)
        axes.plot_surface(xgrid, ygrid,np.abs(self.fft_result), rstride=20, cstride=20, cmap = cm.Spectral )
        fig2 = plt.figure(2)
        plt.imshow(np.abs(self.fft_result), cmap='Spectral')
        plt.colorbar()
        plt.show()
    def showPhaseFreq(self):
        fig = plt.figure(1)
        axes = Axes3D(fig)
        xgrid, ygrid = np.meshgrid(self.freqX, self.freqY)
        axes.plot_surface(xgrid, ygrid,np.angle(self.fft_result), rstride=80, cstride=80, cmap = cm.Spectral )
        fig2= plt.figure(2)
        plt.imshow(np.angle(self.fft_result), cmap='plasma')
        plt.colorbar()
        plt.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    myapp = MyWin()
    myapp.show()
    try:
        sys.exit(app.exec_())
    except:
        print(0)