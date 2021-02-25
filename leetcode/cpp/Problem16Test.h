#pragma once
#include "UnitTest.h"
#include "Problem16.h"

class Problem16Test:UnitTest{
    public:
        void runTest(){
            vector<int> nums{-1,2,1,-4};
            UT_ASSERT(find_closest_sum(nums, 2) == 2);
        }
};