#include "Problem8.h"
#include <vector>

using std::vector;

// O(n) space and time where n is num of chars
int myAtoi(string s) {
    vector<char> nums;
    bool neg = false;
    bool started = false;
    for (int i = 0; i < s.size(); ++i){
        if (s[i] == ' ' && started){
            break;
        }
        if (s[i] == ' '){
            continue;
        }
        if ((s[i] == '-' || s[i] == '+') && started){
            break;
        }
        if (s[i] == '-'){
            neg = true;
            started = true;
            continue;
        }
        if (s[i] == '+'){
            started = true;
            continue;
        }
        if (!isdigit(s[i])){
            break;
        }
        else{
            started = true;
            nums.push_back(s[i]);
        }
    }
    long answer = 0;
    for (int i = 0; i < nums.size(); ++i){
        if (int(nums[i]- '0')*pow(10, nums.size()-1 - i) > pow(2,31)){
            return neg ? -1*pow(2,31) : pow(2,31) -1;
        }
        answer += int(nums[i]- '0')*pow(10, nums.size()-1 - i);
    }
    if (neg){
        answer *= -1;
    }
    if (answer > pow(2,31)-1){
        return pow(2,31)-1;
    }
    if (answer < -1*pow(2,31)){
        return -1*pow(2,31);
    }
    return answer;
}