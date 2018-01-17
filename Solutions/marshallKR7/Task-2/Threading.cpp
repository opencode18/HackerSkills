#include<iostream.h>
#include<thread.h>
using namespace std;

void fact(long long int n)
{
	long long int ans=1,i;
	for(i=2;i<=n;i++)
	{
		ans=(ans*i)%1000000007;
	}
	cout<<"The factorial is"<<ans<<"\n";
}

void expo(long long int t)
{
	long long int base,exp,final=1;
	base=t;
	exp=t;
	while(exp>0)
	{
		if(exp%2!=0)
			final=(final*base)%1000000007;
		base=(base*base)%1000000007;
		exp/=2;
	}
	cout<<"The exponential of number with respect to itself is"<<final<<"\n";
}

int main()
{
	long long int a;
	cin>>a;
    thread t1(&fact,a);
    thread t2(&expo,a);
    t1.join();
    t2.join();
	return 0;
}
