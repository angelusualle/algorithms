#pragma once
#include "Problem12.h"
#include "UnitTest.h"

class Problem12Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(intToRoman(3000) == "MMM");
        }
};