#include <stdio.h>
#include "Problem1Test.h"
#include "Problem2Test.h"
#include "Problem3Test.h"
#include "Problem4Test.h"
#include "Problem5Test.h"
#include "Problem6Test.h"
#include "Problem7Test.h"

int main(){
    Problem1Test prob1;
    prob1.runTest();

    Problem2Test prob2;
    prob2.runTest();

    Problem3Test prob3;
    prob3.runTest();

    Problem4Test prob4;
    prob4.runTest();

    Problem5Test prob5;
    prob5.runTest();

    Problem6Test prob6;
    prob6.runTest();

    Problem7Test prob7;
    prob7.runTest();

    printf("Success!");
}