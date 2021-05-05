#include "Problem27.h"

// O(N) time O(1) space
int removeElement(vector<int>& nums, int val){
    int posIndex = 0;
    int nextIndex = 0;
    while (nextIndex < nums.size()){
        if (nums[nextIndex] != val){
            nums[posIndex] = nums[nextIndex];
            posIndex++;
            nextIndex++;
        }
        else {
            nextIndex++;
        }
    }
    return posIndex;
}