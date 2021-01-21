#pragma once
#include "ChapterSeven.h"
#include "UnitTest.h"
#include <iostream>

using std::unordered_map;
using std::vector;
using std::tuple;
using std::make_tuple;

class ChapterSevenTest:UnitTest{
    public:
        void runTest(){
            unordered_map<char, vector<tuple<int, char> > > graph;
            graph['a'].push_back(make_tuple(5, 'b'));

            graph['b'].push_back(make_tuple(1, 'c'));
            graph['b'].push_back(make_tuple(5, 'd'));

            graph['c'].push_back(make_tuple(5, 'f'));

            graph['d'].push_back(make_tuple(1, 'e'));

            graph['e'].push_back(make_tuple(1, 'f'));
            graph['f'].push_back(make_tuple(0, ' '));
            string answer = dijkstras(graph, 'a', 'f');
            UT_ASSERT("f<-c<-b<-a<- Distance: 22" == answer);
        }
};