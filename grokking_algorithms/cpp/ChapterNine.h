#pragma once
#include <vector>

std::vector<bool> knapsackSolver(std::vector<int> itemsWeight, std::vector<int> cost, int position, std::vector<bool> inclusions, int maxWeight, int weight);