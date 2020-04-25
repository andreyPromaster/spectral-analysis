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