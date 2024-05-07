#include <stdio.h>

int check_cycle(listint_t *list) {
    if (list == NULL)
        return 0;  /* No cycle in an empty list */

    listint_t *slow = list;  /* Slow pointer moves 1 step at a time */
    listint_t *fast = list->next;  /* Fast pointer moves 2 steps at a time */

    /* Traverse the list until slow pointer meets fast pointer or fast reaches end of list */
    while (fast != NULL && fast->next != NULL) {
        if (slow == fast) {
            return 1;  /* Cycle detected */
        }
        slow = slow->next;
        fast = fast->next->next;
    }

    return 0;  /* No cycle found */
}
