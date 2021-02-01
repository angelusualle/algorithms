#include "UnitTest.h"
#include "Problem5.h"

class Problem5Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(getLongestPalindrome("babad") == "bab");
        }
};