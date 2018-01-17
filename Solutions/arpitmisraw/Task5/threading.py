import threading

def factorial(n):
    i = 1
    ans = 1
    while(i <= n):
        ans *= i
        i += 1
    print("Factorial of", n, "is", ans)


def square(n):
    print("Square of", n, "is", n**2)


n = int(input())
t1 = threading.Thread(target=factorial, args=(n,))
t2 = threading.Thread(target=square, args=(n,))
t1.start()
t2.start()
t1.join()
t2.join()




