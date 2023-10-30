#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there's a loop in the linked list
 * @list: is the header of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *rabbit, *snail;

	if (list)
	{
		rabbit = list;
		snail = list;
		while (rabbit && rabbit->next)
		{
			snail = snail->next;
			rabbit = rabbit->next->next;

			if (snail == rabbit)
				return (1);
		}
	}
	return (0);
}
