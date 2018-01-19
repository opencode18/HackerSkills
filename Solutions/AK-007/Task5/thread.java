import java.util.*;
import java.lang.*;
import java.io.*;
class Factorial extends Thread{
	int k;
	
	Factorial(int a)
	{
		this.k=a;
	}
	@Override
	public void run()
	{
		if(k==1)System.out.println("Factorial : 1");
		else
		{
			int i=1,ans=1;
			while(i<=k)
			{
				ans*=i;
				i++;
			}
			System.out.println("Factorial : "+ans);
		}
	}
}
class Exponential extends Thread{
	
	int k;
	Exponential(int a)
	{
		this.k=a;
	}
	@Override
	public void run()
	{
		int ans=(int) Math.pow(k,k);
		System.out.println("Exponential : "+ans);
	}
}
class Ideone
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		
		Factorial f=new Factorial(n);
		Exponential e=new Exponential(n);
		
		f.start();
		e.start();
		f.join();
		e.join();
	}
}