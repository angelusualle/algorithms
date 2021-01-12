#include "UnitTest.h"
#include <string.h>

class ChapterOneTest : public UnitTest {
 public:
   void runTest( ) {
      UT_ASSERT(!strcmp("Cosmos", "Cosmos"));
   }

};