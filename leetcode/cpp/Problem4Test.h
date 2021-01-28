#include "UnitTest.h"
#include "Problem4.h"

class Problem4Test:UnitTest{
    public:
        void runTest(){
            vector<int> nums1{1, 3};
            vector<int> nums2{2};
            UT_ASSERT(findMedianSortedArrays(nums1, nums2) == 2);
        }
};