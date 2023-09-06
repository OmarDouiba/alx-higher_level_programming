#include "main.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/**
 * insert_node - that inserts a number into a sorted singly linked list
 * @head: double pointer, pointer to the pointer to a node (struct)
 * @number = value stored in the node
 * Return: address of the new node, or NULL if it failed
 */
listint_t* insert_node(listint_t **head, int number)
{
	listint_t *tmp, *slow = *head, *fast = (*head)->next;

	if (head == NULL)
		return (NULL);

	tmp = malloc(sizeof(listint_t*));
	if (tmp == NULL)
		return (NULL);

	tmp->n = number;
	tmp->next = NULL;

	if (*head == NULL)
		*head = tmp;

	else
	{
		while (fast->next)
		{
			if (fast->n >= number)
			{
				tmp->next = fast;
				slow->next = tmp;
				break;
			}
			slow = slow->next;
			fast = fast->next;
		}
	}
}
