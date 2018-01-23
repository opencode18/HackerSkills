import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

x = np.arange(0, 3*np.pi, 0.1)
graph = 2*np.sin((np.pi/4)*x)

style.use('ggplot')
plt.plot(x,graph, 'c')

plt.title('Graph of y=2*sin((pi*x)/4)')
plt.savefig('sinecurve.png')
