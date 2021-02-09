#include "UnitTest.h"
#include "Problem11.h"

class Problem11Test:UnitTest{
    public:
        void runTest(){
            vector<int> heights;
            heights.push_back(1);
            heights.push_back(8);
            heights.push_back(6);
            heights.push_back(2);
            heights.push_back(5);
            heights.push_back(4);
            heights.push_back(8);
            heights.push_back(3);
            heights.push_back(7);
            UT_ASSERT(maxArea(heights) == 49);
        }
};