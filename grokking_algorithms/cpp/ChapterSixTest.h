#pragma once
#include "UnitTest.h"
#include "ChapterSix.h"
#include <unordered_map>
#include <vector>
#include <string>
#include <iostream>

using namespace std;
class ChapterSixTest:UnitTest{
    public:
        void runTest(){
            unordered_map<char, vector<char> > deps;
            deps['a'].push_back('b');
            deps['a'].push_back('c');
            deps['b'].push_back('c');
            vector<char> c;
            deps['c'] = c;
            vector<char> answer = topologicalSort(deps);
            UT_ASSERT(answer[0] == 'c');
            UT_ASSERT(answer[1] == 'b');
            UT_ASSERT(answer[2] == 'a');

            unordered_map<char, vector<char> > graph;
            graph['a'].push_back('b');

            graph['b'].push_back('c');
            graph['b'].push_back('d');

            graph['c'].push_back('a');
            graph['c'].push_back('e');

            graph['d'].push_back('f');

            string path = breadthFirstSearch(graph, 'a', 'f');
            UT_ASSERT(path == "a-->b-->c-->d-->f");
        }
};