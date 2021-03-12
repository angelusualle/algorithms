#pragma once
#include "Problem19.h"
#include "UnitTest.h"

class Problem19Test:UnitTest{
    public:
        void runTest(){
            ListNode* head = new ListNode();
            head->val = 1;
            head->next = new ListNode(2);
            head->next->next = new ListNode(3);
            head->next->next->next = new ListNode(4);
            head->next->next->next->next = new ListNode(5);
            head = removeNthFromEnd(head, 2);
            UT_ASSERT(head->next->next->next->val == 5);
        }
};