#include "Problem11.h"
#include <algorithm>

using std::min;

// O(n) time where n is number of bars, O(1) space
int maxArea(vector<int> height){
    int i = 0;
    int j = height.size() - 1;
    int max_area = 0;
    while (i != j){
        if (min(height[i], height[j])*(j-i) > max_area){
            max_area= min(height[i], height[j])*(j-i);
        }
        if (height[i] > height[j]){
            --j;
        }
        else{
            ++i;
        }
    }
    return max_area;
}