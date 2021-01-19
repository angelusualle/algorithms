#pragma once
#include "UnitTest.h"
#include "ChapterFive.h"

class ChapterFiveTest:UnitTest{
    public:
        void runTest(){
            unordered_map<char, int> ans = get_char_counts("Whats up happy people, my name is Robert Arrington");
            UT_ASSERT(ans['a'] == 3);
        }
};