#pragma once
#include "Problem22.h"
#include "UnitTest.h"

class Problem22Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(generateParenthesis(3)[0] == "()()()");
        }
};