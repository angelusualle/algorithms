#pragma once
#include "UnitTest.h"
#include "ChapterNine.h"
#include <iostream>

class ChapterNineTest:UnitTest{
    public:
        void runTest(){
            std::vector<int> itemsWeight{10, 5, 12, 3, 5};
            std::vector<int> cost{20, 5, 17, 40, 25};
            std::vector<bool> inclusions;
            std::vector<bool> answer = knapsackSolver(itemsWeight, cost, 0, inclusions, 30, 0);
            std::vector<bool> trueAnswer{true, false, true, true, true};
            for (int i = 0; i < cost.size(); i++){
                UT_ASSERT(answer[i] == trueAnswer[i]);
            }

        }
};