#include "Problem21.h"

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    if (l1 == nullptr){
        return l2;
    }
    if (l2 == nullptr){
        return l1;
    }
    ListNode* head;
    if (l1->val < l2->val){
        head = l1;
        l1 = head->next;
    }
    else{
        head = l2;
        l2 = head->next;
    }
    ListNode* original_head = head;
    while ((l1 != nullptr) || (l2 != nullptr)){
        if (l1 == nullptr){
            head->next = l2;
            l2 = head->next->next;
        }
        else if (l2 == nullptr){
            head->next = l1;
            l1 = head->next->next;
        }
        else{
            if (l1->val < l2->val){
                head->next = l1;
                l1 = head->next->next;
            }
            else{
                head->next = l2;
                l2 = head->next->next;
            }
        }
        head = head->next;
    }
    return original_head;
}