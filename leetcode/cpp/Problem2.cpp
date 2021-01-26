#include "Problem2.h"

// O(max(n,m)) time and space where n,m are number of list nodes per number
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2){
    ListNode* answer = new ListNode;
    ListNode* next = answer;
    int carryover = 0;
    while (l1 != nullptr || l2 != nullptr || carryover > 0){
        int sum = carryover;
        if (l1 != nullptr){
            sum += l1->val;
        }
        if (l2 != nullptr){
            sum += l2->val;
        }
        next->val = sum % 10;
        carryover = sum / 10;
        if ((l1 != nullptr && l1->next != nullptr) || (l2 != nullptr && l2->next != nullptr || carryover > 0)){
            ListNode* nextOne = new ListNode;
            next->next = nextOne;
            next = nextOne;
        }
        if (l1 != nullptr){
            l1 = l1->next;
        }
        if (l2 != nullptr ){
            l2 = l2->next;
        }
    }
    return answer;
}