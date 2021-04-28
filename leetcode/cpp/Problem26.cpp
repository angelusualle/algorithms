#include "Problem26.h"

// O(N) time and O(1) space
int removeDuplicates(vector<int>& nums){
        if (nums.size() == 1){
            return 1;
        }
        if (nums.size() == 0){
            return 0;
        }
        int pos = 1;
        int next = 1;
        int prev = nums[0];
        int popEnd = 0;
        while (pos < nums.size()){
            if (next >= nums.size()){
                popEnd++;
                pos++;
            }
            else if (prev != nums[next]){
                nums[pos] = nums[next];
                prev = nums[next];
                pos++;
                next++;
            }
            else {
                next++;
            }
        }
        nums.resize(nums.size()- popEnd);
        return nums.size();
}