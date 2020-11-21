from collections import deque

def find_shortest_path_bi_dfs(graph, start, end):
    start_queue = deque([start])
    end_queue = deque([end])

    start_node_parent = {start: None}
    end_node_parent = {end: None}

    path_found = None
    while start_queue or end_queue:
        if start_queue:
            item = start_queue.pop()
            if item in end_node_parent:
                path_found = item
                break
            else:
                children = graph[item]
                for child in children:
                    if child not in start_node_parent:
                        start_node_parent[child] = item
                        start_queue.appendleft(child)
        if end_queue:
            item = end_queue.pop()
            if item in start_node_parent:
                path_found = item
                break
            else:
                children = graph[item]
                for child in children:
                    if child not in end_node_parent:
                        end_node_parent[child] = item
                        end_queue.appendleft(child)
    if item is not None:
        ans = []
        next_one = item
        while next_one is not None:
            ans.append(next_one)
            next_one = start_node_parent[next_one]
        ans = list(reversed(ans))
        next_one = end_node_parent[item]
        while next_one is not None:
            ans.append(next_one)
            next_one = end_node_parent[next_one]
        return ans
    else:
        return None