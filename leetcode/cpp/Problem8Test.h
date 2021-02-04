#include "UnitTest.h"
#include "Problem8.h"

class Problem8Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(myAtoi("413") == 413);
        }
};