#include "stdio.h"
#include "ChapterOneTest.h"
#include <iostream>

using namespace std;

int main( ) {
   ChapterOneTest test;
   std::string s;
   test.runTest();
   printf("SUCCESS!\n");
   return 0;
}