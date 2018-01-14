#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int fact(int a)
{
	int factVal = a;
	if(a==0 || a==1)
	printf("The factorial is 1");
	else
	{
		for(int i=a-1;i>1;i--)
		factVal*=i;
	}
	
}

int main()
{
	pid_t pid;
	int input,factVal;

	printf("Enter a value of your choice: ");
	scanf("%d",&input);
	pid = fork();	
	/*Creates 2 different processes (child and parent)
	So only one process goes on at a particular time!
	Therefore both are calculated separately*/

	if(pid == 0)	//Enters when the process is child process
	printf ("The exponential of %d wrt itself is %d\n",input,input*input);

	else if(pid>0)	//Enter when the process is parent process
	{
		factVal = fact(input);
		printf("The factorial of %d is %d\n",input,factVal);
		wait(NULL);
	}

	else //if pid returns a negative value then it means process creation failed
	printf("Process creation failed");

	return 0;

}
