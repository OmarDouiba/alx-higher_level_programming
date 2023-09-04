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
	if (head == NULL)
	{
		return (0);
	}

	tmp = head;

	while (tmp)
	{
		tmp = tmp->next;
		if (tmp == head)
		{
			return (1);
		}
	}

	return (0);
}
