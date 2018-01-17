import matplotlib.pyplot as plot
import numpy as np



x = np.arange(0, 10, 0.001)  
y = 2 * np.sin(np.pi *x /4)

plot.title('Sine Wave')
plot.xlabel('x')
plot.ylabel('y')

plot.plot(x, y)
plot.show()