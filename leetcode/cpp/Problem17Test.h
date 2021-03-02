#pragma once
#include "UnitTest.h"
#include "Problem17.h"

class Problem17Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(letterCombinations("23")[0] == "ad");
        }
};