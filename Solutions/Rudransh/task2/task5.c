#include<stdio.h>
#include<math.h>
int factorial(int);
int main()
{
    int n,i,j;
    scanf("%d",&n);
    int result1;
    result1=factorial(n);
    printf("%d\n",result1);
    printf("%f",pow(n,n));
    return 0;
}
int factorial(int num)
{
    if (num == 0 || num == 1)
    {
        return 1;
    }
    else
    {
        return(num * factorial(num - 1));
    }
}
