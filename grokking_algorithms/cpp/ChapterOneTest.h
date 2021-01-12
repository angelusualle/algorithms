#include "UnitTest.h"
#include "ChapterOne.h"
#include <string.h>

class ChapterOneTest : public UnitTest {
 public:
   void runTest( ) {
      int arr[7] = {1,2,3,4,5,6,7};
      UT_ASSERT(binary_search(arr, 7, 3) == 2);
      UT_ASSERT(binary_search(arr, 7, 9) == -1);
   }

};