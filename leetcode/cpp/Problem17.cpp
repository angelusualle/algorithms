#include "Problem17.h"
#include <unordered_map>

using std::unordered_map;

// O(3.11^n) where n is number of digits
vector<string> letterCombinations(string digits){
    unordered_map<char, vector<string> > digitMap{
        {'2', {"a", "b", "c"}},
        {'3', {"d", "e", "f"}},
        {'4', {"g", "h", "i"}},
        {'5', {"j", "k", "l"}},
        {'6', {"m", "n", "o"}},
        {'7', {"p", "q", "r", "s"}},
        {'8', {"t", "u", "v"}},
        {'9', {"w", "x", "y", "z"}}
    };
    
    vector<string> combos;
    
    for (int i = 0; i < digits.size(); ++i){
        char digit = digits[i];
        if (combos.size() == 0){
            for (int j = 0; j < digitMap[digit].size(); ++j){
                combos.push_back(digitMap[digit][j]);
            }
        }
        else {
            vector<string> new_combos;
            for (int j = 0; j < digitMap[digit].size(); ++j){
                for (int z = 0; z < combos.size(); ++z){
                    new_combos.push_back(combos[z] + digitMap[digit][j]);
                }
            }
            combos = new_combos;
        }
    }
    return combos;
}