#pragma once
#include "UnitTest.h"
#include "Problem20.h"

class Problem20Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(isValid("(())"));
            UT_ASSERT(!isValid("(([)])"));
        }
};