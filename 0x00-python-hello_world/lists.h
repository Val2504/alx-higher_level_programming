#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - ListNode
 * @val: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 *
 */
typedef struct ListNode {
    int val;
    struct ListNode *next;
} listint_t;


int check_cycle(listint_t *list);
#endif
