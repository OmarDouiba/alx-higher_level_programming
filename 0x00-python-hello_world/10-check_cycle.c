#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
* check_cycle - Function That check if the linke list
* is a cyclique or not.
* @head: Node
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *head)
{
	listint_t *tmp;

	tmp = head;
	while (tmp->next)
	{
		if (tmp->next == head)
		{
			return (1);
		}
		tmp = tmp->next;
	}

	return (0);
}
