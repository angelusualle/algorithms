#include "Problem19.h"
using std::unordered_map;

ListNode* removeNthFromEnd(ListNode* head, int n) {
    unordered_map<int, ListNode*> posToNode;
    int cnt = 1;
    posToNode[cnt] = head;
    head = head->next;
    while (head != nullptr){
        cnt++;
        posToNode[cnt] = head;
        head = head->next;
    }
    int num = cnt - n;
    if(num == 0){
        return posToNode[1]->next;
    }
    else{
        posToNode[num]->next = posToNode[num+1]->next;
        return posToNode[1];
    }
}