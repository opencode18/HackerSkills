import matplotlib.pyplot as plt
import numpy as np

x = np.arange(start = 0, stop = 1, step = 0.01)
y = np.sin(x * 2 * np.pi)
plt.plot(x, y)
plt.title('Sine Wave')
plt.xlabel('2 * pi * x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('sine')
plt.show()