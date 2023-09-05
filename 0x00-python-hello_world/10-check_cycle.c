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
	listint_t *slow = head, *fast = head;

	while (fast != NULL)
	{
		slow = slow->next;
		if (fast->next == NULL)
			break;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
