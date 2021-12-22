#include "lists.h"

/**
 *check_cycle - checks if there is a loop in given linked list
 *@head: head of given linked list
 *Return: 1 if there is a loop 0 if there is not
 */
int check_cycle(listint_t *head)
{
	listint_t *list1, *list2;

	list1 = head;
	list2 = head;

	while (list1 != NULL && list2 != NULL && list2->next != NULL)
	{
		list1 = list1->next;
		list2 = list2->next->next;
		if (list1 == list2)
			return (1);
	}
	return (0);
}
