#pragma once
#include "UnitTest.h"
#include "Problem23.h"

class Problem23Test:UnitTest{
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
            vector<ListNode*> test;
            test.push_back(&l1);
            test.push_back(&l2);
            vector<int> answer;
            ListNode* next = mergeKLists(test);
            while (next != nullptr){
                answer.push_back(next->val);
                next = next->next;
            }

            UT_ASSERT(answer[0] == 1);
            UT_ASSERT(answer[1] == 1);
            UT_ASSERT(answer[2] == 2);
            UT_ASSERT(answer[3] == 3);
            UT_ASSERT(answer[4] == 4);
            UT_ASSERT(answer[5] == 4);
        }
};