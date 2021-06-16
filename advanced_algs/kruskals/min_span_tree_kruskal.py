# O(ElogE)
def min_span_tree_kruskal(graph):
   min_tree = []
   edges= []
   visited = set()
   for k in graph:
       for i, pair in enumerate(graph[k]):
           edge = sorted([k,pair[0]])
           if str(edge) not in visited:
               edges.append((pair[1], edge[0], edge[1]))
               visited.add(str(edge))
   visited.clear()
   edges = sorted(edges, key=lambda x: x[0])
   for wt, n1, n2 in edges:
       if n1 not in visited or n2 not in visited:
           min_tree.append((wt, n1, n2))
           visited.add(n1)
           visited.add(n2)
   return min_tree