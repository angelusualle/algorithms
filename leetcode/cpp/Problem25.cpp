#include "Problem25.h"

// O(N) time O(1) space
ListNode* reverseKGroup(ListNode* head, int k) {
    if (k == 1){
        return head;
    }
    ListNode *innerGroupEnd = 0, *currentHead = 0, *tmp = 0, *link = 0, *next = head;

    int listSize = 0;
    while (next != nullptr){
        ++listSize;
        next = next->next;
    }

    next = head->next;
    innerGroupEnd = head;
    currentHead = head;
    int cnt = 1;
    int globalCnt = 1;
    while (true){
        if (cnt < k){
            innerGroupEnd->next = next->next;
            
            next->next = currentHead;
            
            currentHead = next;
            next = innerGroupEnd->next;

            ++cnt;
        }
        else {
            if (link==nullptr){
                link = head;
                head = currentHead;
            }
            else {
                link->next = currentHead;
                link = innerGroupEnd;
            }
            innerGroupEnd = next;
            currentHead = next;
            if (listSize - globalCnt < k){
                break;
            }
            next = next->next;
            cnt = 1;
        }
        ++globalCnt;
    }
    return head;
}