import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#x∈(-10;10); y∈(-0,5;0,5); z=tg(x+y)

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
z = y * np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()