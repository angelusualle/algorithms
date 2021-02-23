#include "Problem15.h"

vector<vector<int>> threeSum(vector<int>& nums) {
    
    const size_t len = nums.size();
    if (len < 3)
        return {};
    
    std::sort(nums.begin(), nums.end());
    
    std::vector<vector<int>> results;
    
    for(int i = 0; i < len - 2; i++) {
        if (i > 0 && nums[i] == nums[i-1]){
            continue;
        }
        int j = i + 1;
        int k = len - 1;
        
        while (j < k) {
        
            const int sum = nums[i] + nums[j] + nums[k];
            if (0 == sum) {
                results.push_back({nums[i], nums[j], nums[k]});
                j++;
                k--;
                while (j < k && nums[j] == nums[j-1]){
                    j++;
                }
                while (j < k && nums[k] == nums[k+1]){
                    k--;
                }
            }
            else if (0 > sum)
                j++;
            else if (0 < sum)
                k--;
        }
    }
    
    
    return results;
}