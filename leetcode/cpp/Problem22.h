#pragma once
#include <vector>
#include <string>

using std::vector;
using std::string;

vector<string> generateParenthesis(int n);
void genPar(string prefix, int n_open, int len, vector<string>& answer);