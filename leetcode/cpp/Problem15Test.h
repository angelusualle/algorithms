#include "UnitTest.h"
#include "Problem15.h"

class Problem15Test:UnitTest{
    public:
        void runTest(){
            vector<int> t{1,0,1,2,-1,-4};
            UT_ASSERT(threeSum(t)[0][0] == -1);
        }
};