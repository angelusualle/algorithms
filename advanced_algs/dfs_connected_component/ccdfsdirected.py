# O(V+E)
def ccdfsdirected(graph):
  v = {k:(-1, -1, False) for k in graph.keys()}
  clock = [1]
  for k in v:
      if not v[k][2]:
          explore(clock, k, v, graph)
  return v

def explore(clock, k, v, graph):
   pre = clock[0]
   clock[0] += 1
   v[k]  = (pre, -1, True)
   for c in graph[k]:
       if not v[c][2]:
           explore(clock, c, v, graph)
   v[k]  = (pre, clock[0], True)
   clock[0] += 1