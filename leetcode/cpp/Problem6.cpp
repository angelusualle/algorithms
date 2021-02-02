#include "Problem6.h"
// O(N) where n is length of string
string convert(string s, int numRows){
    if (numRows == 1){
        return s;
    }
    string ret;
    int cycle_len = 2*numRows -2;
    int n = s.size();
    for (int i = 0; i < numRows; ++i){
        for (int j = 0; i+j < n; j += cycle_len){
            ret += s[i+j];
            if (i != 0 && i != numRows-1 && i + j < n && j + cycle_len -i < n){
                ret += s[j + cycle_len -i];
            }
        }
    }
    return ret;
}