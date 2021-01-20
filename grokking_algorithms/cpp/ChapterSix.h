#pragma once
#include <unordered_map>
#include <vector>
#include <unordered_set>
#include <queue>
#include <string>

std::vector<char> topologicalSort(std::unordered_map<char, std::vector<char> > dependencies);
std::string breadthFirstSearch(std::unordered_map<char, std::vector<char> > graph, char start, char end);