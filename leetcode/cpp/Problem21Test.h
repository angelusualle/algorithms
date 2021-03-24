#pragma once
#include "Problem21.h"
#include "UnitTest.h"

class Problem21Test:UnitTest{
    public:
        void runTest(){
            ListNode *l1 = new ListNode(1);
            l1->next = new ListNode(2);
            l1->next->next = new ListNode(4);

            ListNode *l2 = new ListNode(1);
            l2->next = new ListNode(3);
            l2->next->next = new ListNode(4);

            ListNode *answer = mergeTwoLists(l1, l2);
            UT_ASSERT(answer->val == 1);
        }
};