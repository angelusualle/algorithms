#pragma once
#include "Problem21.h"
#include "UnitTest.h"

class Problem21Test:UnitTest{
    public:
        void runTest(){
            ListNode l1 = ListNode(1);
            ListNode temp = ListNode(2);
            l1.next = &temp;
            ListNode temp2 = ListNode(4);
            l1.next->next = &temp2;

            ListNode l2 = ListNode(1);
            ListNode temp3 = ListNode(3);
            l2.next = &temp3;
            ListNode temp4 = ListNode(4);
            l2.next->next = &temp4;

            ListNode *answer = mergeTwoLists(&l1, &l2);
            UT_ASSERT(answer->val == 1);
            UT_ASSERT(answer->next->val == 1);
            UT_ASSERT(answer->next->next->val == 2);
        }
};