#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: a pointer to the head of the list
 *
 * Return: the pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}
	(*head) = prev;
	return (*head);
}

/**
 * get_nodeint_at_index - returns the nth node of a listint_t linked list.
 * @head: the head of the list
 * @index: the nth node to be extracted
 *
 * Return: Nothing.
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	if (!head)
		return (NULL);
	if (index > 0)
		return (get_nodeint_at_index(head->next, index - 1));
	return (head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the head of the list
 *
 * Return: : 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *left, *right, *ptr;
	int count, mid;

	if (*head)
	{
		count = 0;
		ptr = (*head);
		while (ptr != NULL) /* number of elements in the list */
		{
			count++;
			ptr = ptr->next;
		}
		mid = (count % 2 == 0) ? (count / 2)  - 1 : count / 2;
		ptr = get_nodeint_at_index(*head, mid);
		ptr->next = reverse_listint(&(ptr->next));
		left = (*head);
		right = ptr->next;
		while (right)
		{
			if (left->n != right->n)
				return (0);
			left = left->next;
			right = right->next;
		}
	}
	return (1);
}
