#pragma once
#include "ChapterFour.h"
#include "UnitTest.h"
#include <stdio.h>


class ChapterFourTest: UnitTest {
    public:
        void runTest(){
            int test[7] = {6, 0, 5, 4, 1, 2, 3};
            quickSort(test, 7);
            for (int i = 0; i < 7; ++i){
                UT_ASSERT(i == test[i]);
            }
        }
};