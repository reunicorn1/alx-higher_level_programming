#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer of the head of the list
 * @number: the number of the node to be added
 *
 * Return: the address of the new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *backward, *forward;

	if (head)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = number;
		new->next = NULL; /* to not leave a dangling pointer */
		if (*head == NULL || (*head)->n > new->n) /* adding at the very beginning */
		{
			new->next = *head;
			*head = new;
			return (new);
		}
		backward = *head;
		forward = (*head)->next;
		while(forward) /* adding at the middle of the list */
		{
			if (forward->n > new->n)
			{
				backward->next = new;
				new->next = forward;
				return (new);
			}
			backward = backward->next;
			forward = forward->next;
		}
		backward->next = new; /*adding at the very end */
		return (new);
	}
	return (NULL);
}
