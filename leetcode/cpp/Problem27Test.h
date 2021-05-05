#include "UnitTest.h"
#include "Problem27.h"

class Problem27Test:UnitTest{
    public:
        void runTest(){
            vector<int> nums{1,2,3,4,4};
            UT_ASSERT(removeElement(nums, 4) == 3);
        }
};