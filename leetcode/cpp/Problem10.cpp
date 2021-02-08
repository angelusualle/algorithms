#include "Problem10.h"

bool _isMatch(string s, string p, int i, int j){
    while (i < s.size() || j < p.size()){
        if (j >= p.size()){
            return false;
        }
        if (i >= s.size() && !(j +1 < p.size() && p[j+1] == '*')){
            return false;
        }
        else if (p[j] != '*' && p[j] != '.' && !(j +1 < p.size() && p[j+1] == '*')){
            if (s[i] != p[j]){
                return false;
            };
            ++i;
            ++j;
        }
        else if (p[j] == '.' && !(j +1 < p.size() && p[j+1] == '*')){
            ++j;
            ++i;
        }
        else if (j + 1 < p.size() && p[j+1] == '*'){
            if (p[j] != '.'){
                char let = p[j];
                int y = i;
                if (_isMatch(s,p,i,j+2))
                    return true;
                if (y < s.size()){
                    while (let == s[y]){
                        if (_isMatch(s,p,y+1,j+2)){
                            return true;
                        }
                        y += 1;
                        if (y >= s.size())
                            break;
                    }
                }
                return false;
            }
            else{
                for (int ij = 0; ij < s.size()-i+1; ++ij){
                    if (_isMatch(s,p,i+ij,j+2)) return true;
                }
                return false;
            }
        }
    }
    return true;
}

bool isMatch(string s, string p){
    return _isMatch(s,p,0,0);
}