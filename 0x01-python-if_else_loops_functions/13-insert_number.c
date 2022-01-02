#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a new node
 * @head: head node
 * @number: the number that will be added
 * Return: new node or Null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *current = NULL, *tmp = NULL;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	if (number < current->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	tmp = *head;
	current = current->next;

	while (number > current->n)
	{
		current = current->next;
		tmp = tmp->next;
		if (current == NULL)
			break;
	}
	new->next = tmp->next;
	tmp->next = new;
	return (new);
}

