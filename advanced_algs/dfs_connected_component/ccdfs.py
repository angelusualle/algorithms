# O(V+E) overall
def ccdfs(graph):
   v = {k:(-1, False) for k in graph.keys()}
   cc = 0
   for k in v:
       if not v[k][1]:
           cc+= 1
           explore(cc, k, v, graph)
   return v
 
def explore(cc, k, v, graph):
   v[k]  = (cc, True)
   for c in graph[k]:
       if not v[c][1]:
           explore(cc, c, v, graph)
