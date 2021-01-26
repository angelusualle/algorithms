#include "UnitTest.h"
#include "Problem2.h"
#include <stdio.h>

class Problem2Test:UnitTest{
    public:
        void runFirstTest(){
            ListNode l1;
            l1.val=2;
            ListNode l12;
            l12.val = 4;
            ListNode l13;
            l13.val=3;

            l1.next = &l12;
            l12.next = &l13;

            ListNode l2;
            l2.val=5;
            ListNode l21;
            l21.val=6;
            ListNode l22;
            l22.val=4;
            
            l2.next = &l21;
            l21.next = &l22;

            ListNode* answer = addTwoNumbers(&l1, &l2);
            int right[] {7, 0, 8};
            int i = 0;
            while (true){
                UT_ASSERT(right[i] == answer->val);
                i += 1;
                if (answer->next == nullptr){
                    break;
                }
                answer = (answer->next);
            }
        }
        void runSecondTest(){
            ListNode l1;
            l1.val=9;
            ListNode l12;
            l12.val = 9;

            l1.next = &l12;

            ListNode l2;
            l2.val=9;

            ListNode* answer = addTwoNumbers(&l1, &l2);
            int right[] {8, 0, 1};
            int i = 0;
            while (true){
                UT_ASSERT(right[i] == answer->val);
                i += 1;
                if (answer->next == nullptr){
                    break;
                }
                answer = (answer->next);
            }
        }
        void runTest(){
            runFirstTest();
            runSecondTest();
        }
};