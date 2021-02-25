#include "Problem16.h"
#include <algorithm>

using std::sort;

int find_closest_sum(vector<int>& nums, int target){
    sort(nums.begin(), nums.end());
    int answer = 0;
    bool answered = false;
    for (int i = 0; i < nums.size() - 2; ++i){
        int j = i + 1;
        int k = nums.size() - 1;
        while (j < k){
            int sum = nums[i] + nums[j] + nums[k];
            if (not answered || (abs(target-sum) < abs(target-answer))){
                answered = true;
                answer = sum;
            }
            if (target >= sum){
                j += 1;
            }
            else if (target < sum){
                k -= 1;
            }
        }
    }
    return answer;
}