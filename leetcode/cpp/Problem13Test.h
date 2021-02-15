#include "UnitTest.h"
#include "Problem13.h"

class Problem13Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(romanToInt("MMM") == 3000);
        }
};