#pragma once
#include <string>
#include <unordered_map>
#include <vector>

using std::string;
using std::unordered_map;
using std::vector;
using std::tuple;

string dijkstras(unordered_map<char, vector<tuple<int, char> > > graph, char start, char end);

struct ComparableTuple
{
    int i;
    char c;
    ComparableTuple(int iz, char z) : i(iz), c(z)
    {
    }

    bool operator<(const struct ComparableTuple& other) const
    {
        return i > other.i; // shorthand way of making it a minimum queue
    }
};