#include "UnitTest.h"
#include "Problem6.h"

class Problem6Test:UnitTest{
    public:
        void runTest(){
            UT_ASSERT(convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR");
        }
};