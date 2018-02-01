import math
import threading
x= input(int())
def fac(x):
	value = 1
	for i in range (1,x+1):
		value=value*i
	print(value)
def power(x):
	this= math.pow(x,x)
	print(this)


thread1 = threading.Thread(target=fac, args=(x,))
thread2 = threading.Thread(target=power, args=(x,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
