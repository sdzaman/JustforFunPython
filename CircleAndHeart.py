# Date: 2017-11-03
# here's a simple code that show you a plot of a cirlce and a heart in python 
# author: Saad Zaman
# e-mail: za-man@dataman.ca


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as aplt

#%%
numPoints = 1000
Radius = 1



x = np.linspace(-1.0, 1.0, numPoints)
y = np.linspace(-1.0, 1.0, numPoints)
print("vector x is:-",x)
print("vecotr y is:-",y)
X, Y = np.meshgrid(x,y)


#%%
# Circle:


F = X**2 + Y**2 - Radius
plt.contour(X,Y,F,[0])
plt.show()


#%%
# Heart:

F = (X**2 + Y**2 - Radius)**3-X**2*Y**3
plt.contour(X,Y,F,[0], colors='r', origin='upper', corner_mask=True)
plt.show()
