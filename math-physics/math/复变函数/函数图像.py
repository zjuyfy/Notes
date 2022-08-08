
import numpy as np
import matplotlib.pyplot as plt


x = y = np.arange(-10, 10, 0.1)
x, y = np.meshgrid(x,y)
c = 4
for a in np.arange(1, 10, 0.3):
    plt.contour(x, y, ( (x-c)**2 + y**2)*( (x+c)**2 + y**2), [a**4])     

plt.axis('scaled')
plt.show()
