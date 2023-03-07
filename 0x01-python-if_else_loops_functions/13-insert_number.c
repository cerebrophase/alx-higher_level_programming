#include "lists.h"
#include <stdlib.h>

/**
 * inser_node - inserts a number into a sorted singly linked list.
 * @head: a pointer to the head of the linked list
 * @number: the number to insert
 * Return: NULL if allocation fails else address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev = NULL;
	listint_t *curr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return new;
	}

	while (curr != NULL && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}
	if (prev == NULL)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		new->next = prev->next;
		prev->next = new;
	}
	return (new);
}
