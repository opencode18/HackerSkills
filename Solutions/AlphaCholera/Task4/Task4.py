import matplotlib.pyplot as pt
import numpy as np
 
x = np.arange(0.0,12.0,0.01)
sinGraph = 2*np.sin((np.pi/4)*x)

pt.plot(x,sinGraph)
 
pt.title('A sin graph plot of 2*sin((pi*x)/4)')
pt.grid(True)
pt.savefig("sin.png")
pt.show()