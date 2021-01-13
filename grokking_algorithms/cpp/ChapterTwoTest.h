#pragma once
#include "UnitTest.h"
#include "ChapterTwo.h"

class ChapterTwoTest : public UnitTest {
 public:
   void runTest( ) {
      int arr[6] = {2, 1, 0, 3, 4, 5};
      selectionSort(arr, 6);
      for (int i = 0; i < 6; i++){
         UT_ASSERT(arr[i] == i);
      }
   }

};