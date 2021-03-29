#include "Problem22.h"

// O(4^n/sqrt(n)) where n is num of parenthesis
vector<string> generateParenthesis(int n) {
    vector<string> answer;
    genPar("", 0, n*2, answer);
    return answer;
}
void genPar(string prefix, int n_open, int len, vector<string>& answer){
    if (prefix.size() == len){
        if (n_open == 0){
            answer.push_back(prefix);
        }
        return;
    }
    if (n_open > 0){
        string new_one = prefix + ')';
        genPar(new_one, n_open - 1, len, answer);
    }
    string new_one2 = prefix + '(';
    genPar(new_one2, n_open + 1, len, answer);
}