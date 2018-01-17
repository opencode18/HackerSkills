def factorial(n):
    fact=1
    i=1
    while(i<=n):
        fact=fact*i
        i=i+1
    return fact
def exponential(n):
    ans=pow(n,n)
    return ans
    


n=int(input())
print("factorial of the given number is:-")
print(factorial(n)%1000000007)
print("exponential of the given number is:-")
print(exponential(n)%1000000007)
