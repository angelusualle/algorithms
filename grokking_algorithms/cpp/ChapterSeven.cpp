#include "ChapterSeven.h"
#include <tuple>
#include <queue>

using std::string;
using std::unordered_map;
using std::vector;
using std::tuple;
using std::make_tuple;
using std::priority_queue;
using std::get;

string dijkstras(unordered_map<char, vector<tuple<int, char> > > graph, char start, char end){
    unordered_map<char,  tuple<char, int> > distanceTable;
    for (unordered_map<char, vector<tuple<int, char> > >::iterator i = graph.begin(); i != graph.end(); i++){
        distanceTable[i->first] = make_tuple('-', std::numeric_limits<int>::max());
    }
    priority_queue<ComparableTuple> q;
    q.push(ComparableTuple(0, start));
    while (q.size() > 0){
        ComparableTuple item = q.top();
        q.pop();
        int dist = item.i;
        for (int i = 0; i < graph[item.c].size(); ++i){
            if (dist+get<0>(graph[item.c][i]) < get<1>(distanceTable[get<1>(graph[item.c][i])])){
                distanceTable[get<1>(graph[item.c][i])] = make_tuple(item.c, dist+get<0>(graph[item.c][i]));
                if (get<1>(graph[item.c][i]) == end){
                    string answer = string(1, end);
                    answer.append("<-");
                    int dist = 0;
                    char node = end;
                    while (node != start){
                        answer.append(string(1, get<0>(distanceTable[node])));
                        answer.append("<-");
                        dist += get<1>(distanceTable[node]);
                        node = get<0>(distanceTable[node]);
                    }
                    answer.append(" Distance: ");
                    answer.append(std::to_string(dist));
                    return answer;
                }
                q.push(ComparableTuple(dist+get<0>(graph[item.c][i]), get<1>(graph[item.c][i])));
            }
        }
    }
    return "No path";
}