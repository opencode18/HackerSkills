import threading,math

def factorial(n):
    print("Factorial of " +  str(n) + " is: " + str(math.factorial(n)) )

def square(n):
    print("Exponent of " + str(n) + " is: " + str(n**n))


n = int(raw_input())
thread1 = threading.Thread(target=factorial, args=(n,))
thread2 = threading.Thread(target=square, args=(n,))
thread1.start()
thread2.start()
