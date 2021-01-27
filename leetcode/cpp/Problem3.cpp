#include "Problem3.h"
#include <unordered_map>

using std::unordered_map;

// O(N) time and space where N is number of chars in input string
int lengthOfLongestSubstring(string s){
    unordered_map<char, int> charToPosition;
    int answer = 0;
    int startIndex = 0;
    int endIndex = 0;
    for (int i = 0; i < s.size(); ++i){
        char c = s[i];
        if (charToPosition.find(c) == charToPosition.end()){
            charToPosition[c] = i;
        }
        else if (charToPosition[c] >= startIndex){
            startIndex = charToPosition[c] + 1;
            charToPosition[c] = i;
        }
        else {
            charToPosition[c] = i;
        }
        endIndex ++;
        if ((endIndex - startIndex) > answer){
            answer = endIndex - startIndex;
        }
    }
    return answer;
}