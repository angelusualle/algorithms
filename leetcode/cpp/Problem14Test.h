#pragma once
#include "Problem14.h"
#include "UnitTest.h"

class Problem14Test:UnitTest{
    public:
        void runTest(){
            vector<string> strs;
            strs.push_back("flower");
            strs.push_back("flow");
            strs.push_back("flight");
            UT_ASSERT(longestCommonPrefix(strs) == "fl");
        }
};