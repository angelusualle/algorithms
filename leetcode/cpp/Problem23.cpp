#include <queue>
#include "Problem23.h"

using std::priority_queue;

ListNode* mergeKLists(vector<ListNode*>& lists) {
    if (lists.size() == 0){
        return nullptr;
    }
    auto comp = [&](ListNode *a, ListNode *b) {
        return a->val > b->val;
    };
    priority_queue<ListNode *, vector<ListNode *>, decltype(comp)> pq(comp);
    for (int i = 0; i < lists.size(); i++){
        if (lists[i] != nullptr){
            pq.push(lists[i]);
        }
    }
    if (pq.size() == 0){
        return nullptr;
    }
    ListNode* head;
    head = pq.top();
    pq.pop();
    ListNode* original = head;
    if (head->next != nullptr){
        pq.push(head->next);
    }
    while (pq.size() > 0){
        ListNode* next_head = pq.top();
        pq.pop();
        head->next = next_head;
        head = head->next;
        if (head->next != nullptr){
            pq.push(head->next);
        }
    }
    head->next = nullptr;
    return original;
}