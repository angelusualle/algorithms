#include <stdio.h>
#include "Problem1Test.h"
#include "Problem2Test.h"
#include "Problem3Test.h"
#include "Problem4Test.h"
#include "Problem5Test.h"
#include "Problem6Test.h"
#include "Problem7Test.h"
#include "Problem8Test.h"
#include "Problem9Test.h"
#include "Problem10Test.h"
#include "Problem11Test.h"

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

    Problem8Test prob8;
    prob8.runTest();

    Problem9Test prob9;
    prob9.runTest();

    Problem10Test prob10;
    prob10.runTest();

    Problem11Test prob11;
    prob11.runTest();

    printf("Success!");
}