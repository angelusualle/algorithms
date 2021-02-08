#pragma once
#include "UnitTest.h"
#include "Problem10.h"

class Problem10Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(isMatch("aabbcc", "a*b*c*"));
        }
};