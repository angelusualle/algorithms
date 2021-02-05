#include "Problem9.h"
#include <cmath>

using std::pow;
using std::log10;

// O(log10(n)) where n is number time, O(1) space
bool isPalindrome(int x) {
    if (x < 0){
        return false;
    }
    if (x == 0){
        return true;
    }
    int lDigit = (int)log10(x);
    int rDigit = 0;
    while (rDigit < lDigit){
        if ((x % (long)pow(10,rDigit+1) / (long)pow(10,rDigit)) != (x % (long)pow(10,lDigit+1) / (long)pow(10,lDigit))){
            return false;
        }
        ++rDigit;
        --lDigit;
    }
    return true;
}