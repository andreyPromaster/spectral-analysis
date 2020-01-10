#import numpy as np
#from matplotlib import pyplot as plt

#x = np.linspace(-3, 3, 200)
#y = x*(x + 2)*(x - 2)

#fig, ax = plt.subplots()

#ax.plot(x, y)


#plt.axis('off')
#fig.savefig('мой график.svg', bbox_inches='tight')
#plt.axis('on')
#plt.show()


from skimage import io
from scipy.fftpack import fft, fftfreq, fftshift,fftn
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
plt.imshow(np.random.random((10,10)), cmap='magma')
plt.colorbar()#Добавляет цветовую шкалу на график
#plt.set_cmap('viridis')
plt.show()
# number of signal points
img = io.imread("test.png")
n = 389
# sample spacing
t = 1.0 / 778.0
#x = np.linspace(0.0, n*t, n)
#y = np.exp(50.0 * 1.j * 2.0*np.pi*x) + 0.5*np.exp(-80.0 * 1.j * 2.0*np.pi*x)
yf = fftn(img)
xf = fftfreq(n, t)
xf = fftshift(xf)
yplot = np.abs(yf)
yplot = fftshift(yplot)
#
yf = fftshift(yf)
yf = yf[:, :, 2]
#
print(yf)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
axes = Axes3D(fig)
xgrid, ygrid = np.meshgrid(xf, xf)
print(ygrid)
axes.plot_surface(xgrid, ygrid,np.angle(yf), rstride=80, cstride=80, cmap = cm.Spectral )
plt.show()

#yplot = yplot[:, :, 0]
#fig, ax = plt.subplots()

#plt.bar(xf,yplot[0],width = 2)
##plt.hist(yplot, bins=1000)
##plot(kind='bar', x=xf, y=1.0/n * yplot, ax = ax)
##plt.plot(xf, 1.0/n * yplot)
#plt.grid()
#plt.show()
#print(np.angle(yf[0]))
#plt.bar(xf,np.angle(yf[0]),width = 1)
#plt.show()
##########################
#from scipy.fftpack import fft, fftfreq, fftshift, fftn
#import random, math
# #number of signal points
#N = 400
## sample spacing
#T = 1.0 / 800.0
#x = np.linspace(0.0, N*T, N)
#y = np.sin(2*np.pi*50*x) + 2 * np.sin(2*np.pi*120*x)
#yf = fft(y)
#xf = fftfreq(N, T)
#xf = fftshift(xf)
#yplot = fftshift(yf)
#import matplotlib.pyplot as plt
##plt.bar(xf,1.0/N * np.abs(yplot))
#plt.plot(xf, 2.0/N * np.abs(yplot))
#plt.grid()
#plt.show()
###############


#N = 400
## sample spacing
#T = 1.0 / 800.0
#discr = np.linspace(0.0, N*T, N)
#x = np.sin(2*np.pi*50*discr) + 2 * np.sin(2*np.pi*120*discr)
#y1 = x + 2*random.choice(discr)
#y2 = x + 2*random.choice(discr)
#y = np.vstack((y1,y2))
##plt.subplot(211)
#plt.plot(discr,y1,'r-')
##plt.subplot(212)
#plt.plot(discr,y2,'b-')
#plt.show()
#yf = fftn(y)
#print(yf)
#xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
##yplot = yplot[:, :, 2]
##yf = fftshift(yf)
#plt.plot(xf, 2.0/N * np.abs(yf[0, 0:N//2]))
#plt.plot(xf, 2.0/N * np.abs(yf[1, 0:N//2]))
#plt.grid()
#plt.show()
#####
#xf = fftfreq(n, t)
#xf = fftshift(xf)
#yplot = np.abs(yf)
#yplot = fftshift(yplot)

############
#from scipy.fftpack import fftn,fftshift
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
#from skimage import io
#from mpl_toolkits.mplot3d import Axes3D
#img = io.imread("test.png")
#M, N = 389, 389
#reform = fftn(img)
#print(reform)
#friq= fftshift(reform)
#F_magnitude = np.abs(reform)
#F_magnitude = fftshift(F_magnitude)
#f, ax = plt.subplots(figsize=(4.8, 4.8))

#ax.imshow(np.log(1 + F_magnitude).astype(np.uint8), cmap='viridis',
#          extent=(-N // 2, N // 2, -M // 2, M // 2))
#ax.set_title('Spectrum magnitude');
#plt.show()
##fig = plt.figure()
##ax=Axes3D(fig)

