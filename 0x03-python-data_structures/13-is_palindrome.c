#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: A double pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	listint_t *prev = NULL;
	listint_t *curr = slow;
	while (curr != NULL)
	{
		listint_t *next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}

	listint_t *ptr1 = *head;
	listint_t *ptr2 = prev;
	while (ptr2 != NULL)
	{
		if (ptr1->n != ptr2->n)
		{
			return (0);
		}
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}

	curr = prev;
	prev = NULL;
	while (curr != NULL)
	{
		listint_t *next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	*head = prev;

	return (1);
}

