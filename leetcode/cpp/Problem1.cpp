#include "Problem1.h"
#include <unordered_map>

using std::unordered_map;

vector<int> twoSum(vector<int> nums, int target){
    unordered_map<int, int> diffs;
    for (int i = 0; i < nums.size(); i++){
        int diff = target - nums[i];
        if (diffs.find(diff) != diffs.end()){
            return vector<int>{i, diffs[diff]};
        }
        else{
            diffs[nums[i]] = i;
        }
    }
    return vector<int>{};
}