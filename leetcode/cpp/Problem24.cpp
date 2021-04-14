#include "Problem24.h"

// O(N) time and O(1) space
ListNode* swapPairs(ListNode* head) {
    ListNode* temp=head; int temp1;
    while(temp && temp->next)
    {
        temp1=temp->val;
        temp->val=temp->next->val;
        temp->next->val=temp1;
        temp=temp->next->next;
    }
    return head;
}