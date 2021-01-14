#include "ChapterThree.h"

int factorial(int n){
    int answer = 1;
    for (int i = n; i > 1; i--){
        answer *= i;
    }
    return answer;
}