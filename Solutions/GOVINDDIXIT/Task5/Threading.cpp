#include<iostream>
#include<thread.h>
using namespace std;

int main()
{
	long long int number;
	cout<<"Enter the number:-"
	cin>>a;
    thread facto(&factorial,a);
    thread exponent(&exponential,a);
    facto.join();
    exponent.join();
	return 0;
}


void factorial(long long int number)
{
	long long int answer1=1;
	long long int i;
	for(i=2;i<=n;i++)
	{
		ans=(ans*i)%1000000005;
	}
	cout<<"The factorial of given number is"<<answer1<<"\n";
}


void exponential(long long int m)
{
	long long int bottom,exp,answer2=1;
	bottom=m;
	exp=m;
	while(exp>0)
	{
		if(exp%2!=0)
		{
			answer=(answer*bottom)%1000000005;
		}
		else
		{
		bottom=(bottom*bottom)%1000000005;
		exp/=2;
		}
	}
	cout<<"Exponential of given no raised to itself is:-"<<answer2<<endl;
}

