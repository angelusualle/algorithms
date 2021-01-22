#include "ChapterNine.h"

using std::vector;


int getValue(vector<int> prices, vector<bool> inclusion){
    int value = 0;
    for (int i = 0; i < prices.size();i++){
        if (inclusion[i]){
            value += prices[i];
        }
    }
    return value;
}

vector<bool> knapsackSolver(vector<int> itemsWeight, vector<int> cost, int position, vector<bool> inclusions, int maxWeight, int weight){
    if (weight > maxWeight){
        return inclusions;
    }
    if (inclusions.size() == 0){
        vector<bool> v1(cost.size());
        inclusions = v1;
    }
    vector<bool> withPositionBestInclusions = inclusions;
    vector<bool> withoutPositionBestInclusions = inclusions;
    withoutPositionBestInclusions[position] = 0;
    withPositionBestInclusions[position] = 1;

    if (position < cost.size() - 1){
        withPositionBestInclusions = knapsackSolver(itemsWeight, cost, position + 1, withPositionBestInclusions, maxWeight, weight + itemsWeight[position]);
        withoutPositionBestInclusions = knapsackSolver(itemsWeight, cost, position + 1, withoutPositionBestInclusions, maxWeight, weight);
    }

    int includedValue = getValue(cost, withPositionBestInclusions);
    if (weight + itemsWeight[position] > maxWeight){
        includedValue = 0;
    }
    int notIncludedValue = getValue(cost, withoutPositionBestInclusions);
    if (weight > maxWeight){
        notIncludedValue = 0;
    }
    
    if (includedValue > notIncludedValue){
        return withPositionBestInclusions;
    }
    else{
        return withoutPositionBestInclusions;
    }

}
