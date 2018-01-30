import threading

def exp(x):
    print("Square:", x**2)

def fact(x):
    i = 1
    ans = 1
    while(i <= x):
        ans *= i
        i += 1
    print("Factorial:", ans)

x = int(input())
thread1 = threading.Thread(target=exp, args=(x,))
thread2 = threading.Thread(target=fact, args=(x,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

