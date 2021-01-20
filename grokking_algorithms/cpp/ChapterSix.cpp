#include "ChapterSix.h"
using std::vector;
using std::unordered_map;
using std::unordered_set;
using std::queue;
using std::string;

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

string breadthFirstSearch(unordered_map<char, vector<char> > graph, char start, char end) {
    unordered_set<char> visited;
    queue<string> q;
    q.push(string(1, start));
    while (q.size() > 0){
        string path = q.front();
        char node = path[path.size()-1];
        q.pop();
        visited.insert(node);
        for (int i = 0; i < graph[node].size(); i++){
            if (visited.find(graph[node][i]) == visited.end()){
                path.append("-->");
                path.append(string(1, graph[node][i]));
                if (graph[node][i] == end){
                    return path;
                }
                q.push(path);
            }
        }
    }
    return "NO PATH";
}