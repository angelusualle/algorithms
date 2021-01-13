#include "stdio.h"
#include "ChapterOneTest.h"
#include "ChapterTwoTest.h"

int main( ) {
   ChapterOneTest test;
   test.runTest();
   ChapterTwoTest test2;
   test2.runTest();
   printf("Success!\n");
   return 0;
}