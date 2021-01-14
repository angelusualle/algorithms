#include "UnitTest.h"
#include "ChapterThree.h"

class ChapterThreeTest : UnitTest{
    public:
        void runTest(){
            UT_ASSERT(factorial(3) == 6);
        }
};