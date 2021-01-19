#include "stdio.h"
#include "ChapterOneTest.h"
#include "ChapterTwoTest.h"
#include "ChapterThreeTest.h"
#include "ChapterFourTest.h"
#include "ChapterFiveTest.h"

int main( ) {
   ChapterOneTest test;
   test.runTest();
   
   ChapterTwoTest test2;
   test2.runTest();

   ChapterThreeTest test3;
   test3.runTest();

   ChapterFourTest test4;
   test4.runTest();

   ChapterFiveTest test5;
   test5.runTest();
   printf("Success!\n");
   return 0;
}