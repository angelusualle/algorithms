#include "ChapterSix.h"

vector<char> topologicalSort(unordered_map<char, vector<char> > dependencies){
    vector<char> output;
    unordered_map<char, vector<char> >::iterator it;

    while (true){
        vector<char> toBeProcessed;
        for (it = dependencies.begin(); it != dependencies.end(); it++){
            if (it->second.size() == 0){
                toBeProcessed.push_back(it->first);
            }
        }
        for (int i = 0; i < toBeProcessed.size(); i++){
            for (it = dependencies.begin(); it != dependencies.end(); it++){
                if (find(it->second.begin(), it->second.end(), toBeProcessed[i]) != it->second.end()){
                    it->second.erase(find(it->second.begin(), it->second.end(), toBeProcessed[i]));
                }
            }
            output.push_back(toBeProcessed[i]);
            dependencies.erase(toBeProcessed[i]);
        }
        if (toBeProcessed.size() == 0){
            break;
        }
    }
    return output;
}