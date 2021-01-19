#include "stdio.h"
#include "ChapterOneTest.h"
#include "ChapterTwoTest.h"
#include "ChapterThreeTest.h"
#include "ChapterFourTest.h"
#include "ChapterFiveTest.h"
#include "ChapterSixTest.h"

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

   ChapterSixTest test6;
   test6.runTest();
   printf("Success!\n");
   return 0;
}