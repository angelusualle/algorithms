#include "UnitTest.h"
#include "Problem18.h"

class Problem18Test:UnitTest{
    public:
        void runTest(){
            vector<int> nums{1,0,-1,0,-2,2};
            vector<vector<int> > answer = fourSum(nums, 0);
            UT_ASSERT(answer.size() == 3);
            UT_ASSERT(answer[0][0] == -2);
        }
};