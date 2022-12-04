from collections import defaultdict
import heapq as heap
import sys

def dijkstra(graph, start, end):
  q, seen, mins = [(0, start,())], set(), { start: 0 }
  while q:
    (cost,v1,path) = heap.heappop(q)
    if v1 not in seen:
      seen.add(v1)
      path = (v1, path)
      if v1 == end: return (cost, path)
      for v2, c in graph[v1].items():
        if v2 in seen: continue
        prev = mins.get(v2, None)
        next = cost + c
        if prev is None or next < prev:
          mins[v2] = next
          heap.heappush(q, (next, v2, path))

  return float("inf"), None

def prim(graph, origem):
  mst = defaultdict(dict)
  visited = set([origem])
  edges = [
    (cost, origem, destino)
    for destino, cost in graph[origem].items()
  ]
  heap.heapify(edges)

  while edges:
    cost, ori, dest = heap.heappop(edges)
    if dest not in visited:
      visited.add(dest)

      if ori not in mst:
        mst[ori] = {}
      # mst[ori].append((dest, abs(cost)))
      mst[ori].update({ dest: cost })

      if dest not in mst:
        mst[dest] = {}
      mst[dest].update({ ori: cost })

      for to_next, cost in graph[dest].items():
        if to_next not in visited:
          heap.heappush(edges, (cost, dest, to_next))

  return mst

def resolve(graph, interseccao):
  origem, destino = interseccao

  make_path = lambda tup: (*make_path(tup[1]), tup[0]) if tup else ()

  out = dijkstra(graph, origem, destino)
  path = make_path(out[1])

  maior_altura = -999999
  for i in range(len(path) - 1):
    valor = graph[path[i]][path[i+1]] 
    if maior_altura < valor:
      maior_altura = valor
    
  return maior_altura if maior_altura != -999999 else 0 

instancia = 1
while True:
  line = sys.stdin.readline()

  V, E = line.split()
  V, E = int(V), int(E)

  if not (V and E):
    break

  edges = []

  total = 0

  # Cadastra as edges
  for i in range(E):
    line = sys.stdin.readline()
    c1, c2, valor = line.split()
    c1, c2, valor = int(c1), int(c2), int(valor)

    edges.append((c1, c2, valor))
    edges.append((c2, c1, valor))
  
  # Cadastra os números de pares
  interseccoes = []
  k = int(input())

  for i in range(k):
    line = sys.stdin.readline()
    origem, destino = line.split()
    origem, destino = int(origem), int(destino)

    interseccoes.append((origem, destino))
  
  print(f"Instancia {instancia}")

  # Vai gerar a arvore geradora mínima
  origem, destino = interseccoes[0]
  g = {}
  for node1, node2, value in edges:
    if node1 not in g.keys():
      g[node1] = {}
    g[node1][node2] = value
  mst = prim(g, origem)
  for i in range(k):
    print(resolve(mst, interseccoes[i]))

  instancia += 1
  sys.stdout.write("\n")
