#pragma once
#define UT_ASSERT( condition ) \
        assertTrue(condition,__FILE__,__LINE__,#condition)

class UnitTest {

 public:

   virtual ~UnitTest( ) {}
   virtual void runTest( ) = 0;

 protected:

   void assertTrue(bool condition, const char *file, 
                  int line, const char *msg);
   static int num_test_success;

};
