#include "Problem7.h"
#include <cmath>

using std::log10;
using std::pow;

int reverse(int x) {
    if (x == 0 || x <= -1*pow(2,31) || x >= pow(2,31)){
        return 0;
    }
    bool neg = false;
    if (x < 0){
        neg = true;
        x *= -1;
    }
    int max = log10(x);
    long answer = 0;
    for (int i = max; i >= 0; --i){
        int power = pow(10,i);
        int digit = x / power;
        answer += pow(10,max-i)*digit;
        if (answer < -1*pow(2,31) || answer > pow(2,31)){
            return 0;
        }
        x -= digit*pow(10,i);
    }
    if (neg){
        answer *= -1;
    }
    return answer;
}