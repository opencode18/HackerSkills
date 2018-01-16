import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0.0,2.0,0.04)
y=2*np.sin(np.pi*0.785*x)
plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
