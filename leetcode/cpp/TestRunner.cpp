#include <stdio.h>
#include "Problem1Test.h"
#include "Problem2Test.h"

int main(){
    Problem1Test prob1;
    prob1.runTest();

    Problem2Test prob2;
    prob2.runTest();

    printf("Success!");
}