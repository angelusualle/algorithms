#include "UnitTest.h"
#include "Problem24.h"

class Problem24Test:UnitTest{
    public:
        void runTest(){
            ListNode l1 = ListNode(1);
            ListNode temp = ListNode(2);
            l1.next = &temp;
            ListNode temp2 = ListNode(4);
            l1.next->next = &temp2;
            ListNode* ans = swapPairs(&l1);
            UT_ASSERT(ans->val == 2);
        }
};