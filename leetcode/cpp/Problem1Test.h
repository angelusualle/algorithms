#include "UnitTest.h"
#include "Problem1.h"

class Problem1Test:UnitTest{
    public:
        void runTest(){
            vector<int> nums{10, 5, 7, 3, 4, 8};
            vector<int> answer = twoSum(nums, 12);
            UT_ASSERT(answer.size() == 2);
            UT_ASSERT(answer[0] == 2);
            UT_ASSERT(answer[1] == 1);
        }
};