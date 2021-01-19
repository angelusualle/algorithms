#include <map>
#include <string>

using namespace std;

map<char,int> get_char_counts(string str){
    map<char, int> mapper;
    for (int i = 0; i < str.size(); ++i){
        map<char,int>::iterator it = mapper.find(str[i]);
        if (it == mapper.end()){
            mapper[str[i]] = 1;
        }
        else {
            mapper[str[i]] ++;
        }
    }
    return mapper;

}