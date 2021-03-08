#include "Problem18.h"

vector<vector<int> > twoSum(vector<int>& nums, int startIndex, int target){
    int l = startIndex;
    int h = nums.size() - 1;
    vector<vector<int> > answer;
    while (l < h){
        int sum = nums[l] + nums[h];
        if (sum < target || (l > startIndex && nums[l] == nums[l-1])){
            l += 1;
        }
        else if (sum > target || (h < nums.size() - 1 && nums[h] == nums[h+1])){
            h -= 1;
        }
        else{
            answer.push_back({nums[l], nums[h]});
            l += 1;
            h -= 1;
        }
    }
    return answer;
}
// O(n^(k-1)) time, O(n) space
vector<vector<int> > kSum(vector<int>& nums, int startIndex, int target, int k){
    vector<vector<int> > answer;
    if (startIndex == nums.size()-1){
        return answer;
    }
    if (k == 2){
        return twoSum(nums, startIndex, target);
    }
    for (int i = startIndex; i < nums.size(); ++i){
        if (i > startIndex && nums[i] == nums[i-1]){
            continue;
        }
        vector<vector<int> > subAnswers = kSum(nums, i+1, target - nums[i], k - 1);
        for (int z = 0; z < subAnswers.size(); ++z){
            vector<int> ans{nums[i]};
            for (int y = 0; y < subAnswers[z].size(); ++y){
                ans.push_back(subAnswers[z][y]);
            }
            answer.push_back(ans);
        }
    }
    return answer;
}

vector<vector<int> > fourSum(vector<int>& nums, int target) {
    vector<vector<int> > answer; 
    sort(nums.begin(), nums.end());
    return kSum(nums, 0, target, 4);
}