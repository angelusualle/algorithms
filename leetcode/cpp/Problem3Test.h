#pragma once
#include "UnitTest.h"
#include "Problem3.h"

class Problem3Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(lengthOfLongestSubstring("abcabcbb") == 3);
        }
};