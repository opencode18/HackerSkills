import matplotlib.pyplot as plt
import numpy as np

xRange = np.arange(0.0,2.0,0.01)
sinGraph = np.sin(2*np.pi*xRange)

plt.plot(xRange,sinGraph)

plt.title('A sin graph plot')
plt.grid(True)
plt.savefig("sin.png")
plt.show()

