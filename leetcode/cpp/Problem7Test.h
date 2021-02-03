#pragma once

#include "UnitTest.h"
#include "Problem7.h"

class Problem7Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(reverse(321) == 123);
        }
};