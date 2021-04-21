#include "Problem25.h"
#include "UnitTest.h"

class Problem25Test:UnitTest{
    public:
        void runTest(){
            ListNode l1 = ListNode(1);
            ListNode temp = ListNode(2);
            l1.next = &temp;
            ListNode temp2 = ListNode(4);
            l1.next->next = &temp2;
            ListNode* ans = reverseKGroup(&l1, 2);
            UT_ASSERT(ans->val == 2);
            UT_ASSERT(ans->next->val == 1);
            UT_ASSERT(ans->next->next->val == 4);
        }
};