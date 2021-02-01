#include "Problem5.h"

string getLongestPalindrome(string s){
        int bestStartIndex = 0;
        int bestEndIndex = 0;
        for (int i = 0; i < s.size(); ++i){
            // pali substring is odd length
            int y = i;
            int z = i;
            while (z < s.size() && y >= 0){
                if (s[y] == s[z]){
                    --y;
                    ++z;
                    continue;
                }
                else{
                    break;
                }
            }
            ++y;
            --z;
            if ((z - y) > (bestEndIndex - bestStartIndex)) {
                bestStartIndex = y;
                bestEndIndex = z;
            }
            y = i;
            z = i+1;
            while (z < s.size() && y >= 0){
                if (s[y] == s[z]){
                    --y;
                    ++z;
                    continue;
                }
                else{
                    break;
                }
            }
            ++y;
            --z;
            if ((z - y) > (bestEndIndex - bestStartIndex)) {
                bestStartIndex = y;
                bestEndIndex = z;
            }
    }
    return s.substr(bestStartIndex, bestEndIndex- bestStartIndex+1);
}