#include "Problem20.h"
#include <vector>

using std::vector;

bool isValid(string s) {
    vector<char> stack;
    for (int i = 0; i < s.size(); ++i){
        char c = s[i];
        if (c == ')' || c == '}' || c == ']'){
            if (stack.size() == 0){
                return false;
            }
            else if (c == ')' && stack[stack.size()-1] != '('){
                return false;
            }
            else if (c == '}' && stack[stack.size()-1] != '{'){
                return false;
            }
            else if (c == ']' && stack[stack.size()-1] != '['){
                return false;
            }
            else{
                stack.pop_back();
            }
        }
        else{
            stack.push_back(c);
        }
    }
    if (stack.size() == 0){
        return true;
    }
    else {
        return false;
    }
}
