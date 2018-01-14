import matplotlib.pyplot as plt
import numpy as np

xRange = np.arange(0.0,2.0,0.01)
sinGraph = 2*np.sin((np.pi/4)*xRange)

plt.plot(xRange,sinGraph)

plt.title('A sin graph plot')
plt.grid(True)
plt.savefig("sin.png")
plt.show()

