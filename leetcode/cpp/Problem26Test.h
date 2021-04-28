#include "Problem26.h"
#include "UnitTest.h"

class Problem26Test:UnitTest{
    public:
        void runTest(){
            vector<int> t{1,1,2,3,4,5,5,6};
            int s = removeDuplicates(t);
            UT_ASSERT(s == 6);
        }
};