import math
import threading

n=input(int())
def factorial(n):
    fact = 1
    for i in range (1,n+1):
        fact=fact*i
    print(fact)

def square(n):
    print(n*n)
 
f = threading.Thread(target=factorial, args=(n,))
s = threading.Thread(target=square, args=(n,))
f.start()
s.start()
f.join()
s.join()