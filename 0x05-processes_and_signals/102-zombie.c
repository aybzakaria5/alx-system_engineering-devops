#include <sys/types.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - loop
 *
 * Description: loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates a 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			exit(0);
	}

	infinite_while();

	return (0);
}
