#pragma once
#include "Problem9.h"
#include "UnitTest.h"

class Problem9Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(isPalindrome(121));
            UT_ASSERT(!isPalindrome(35));
        }
};