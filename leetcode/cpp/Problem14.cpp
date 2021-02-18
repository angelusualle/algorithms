#include "Problem14.h"

// O(ns) where n is number of strings and s is size of shortest string
string longestCommonPrefix(vector<string>& strs) {
    if (strs.size() == 0 || strs[0].size() == 0){
        return "";
    }
    int i = 0;
    while (true){
        for (int j = 0; j < strs.size(); ++j){
            if (i >= strs[j].size()){
                return strs[j].substr(0,i);
            }
            if (strs[j][i] != strs[0][i]){
                return strs[j].substr(0,i);
            }
        }
        ++i;
    }
}