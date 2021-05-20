# O(V+E) run time
def dag_single_source_shortest_path(source, graph):
   # O(V+E)
   # inverse adj list
   inverted_adj = {k:set() for k in graph}
   for node in graph:
       for e, _ in graph[node]:
           inverted_adj[e].add(node)
 
   # O(V+E)
   # topological sort
   sorted_vertexes = []
   next_nodes = [source]
   while len(sorted_vertexes) < len(graph):
       sorted_vertexes.extend(next_nodes)
       for n in inverted_adj:
           for v in next_nodes:
               if v in inverted_adj[n]:
                   inverted_adj[n].remove(v)
       for n in next_nodes:
           del inverted_adj[n]
       next_nodes.clear()
       for n in inverted_adj:
           if len(inverted_adj[n]) == 0:
               next_nodes.append(n)
  
   # O(V+E)
   # dag single source shortest path
   vertex_map = {c:i for i,c in enumerate(sorted_vertexes)}
   dist = [0]+[float('inf')]*(len(graph)-1)
   parent = ['-']*len(graph)
   for i in range(len(sorted_vertexes)):
       n = sorted_vertexes[i]
       for c,d in graph[n]:
           if d+dist[i] < dist[vertex_map[c]]:
               dist[vertex_map[c]] = d + dist[i]
               parent[vertex_map[c]] = n
   return sorted_vertexes, dist, parent, vertex_map
