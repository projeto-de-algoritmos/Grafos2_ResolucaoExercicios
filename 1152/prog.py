import sys

class UnionFindSet:
  def __init__(self, n):
    self.fa = [i for i in range(n)]

  def find(self, v):
    if v != self.fa[v]:
      self.fa[v] = self.find(self.fa[v])
    return self.fa[v]

  def union(self, a, b):
    pa = self.find(a)
    pb = self.find(b)
    self.fa[pb] = pa


def kruskal(edges, v):
  edges.sort()
  ufset = UnionFindSet(v)
  ret = 0

  for w, a, b in edges:
    pa, pb = ufset.find(a), ufset.find(b)
    if pa != pb:
      ret += w
      ufset.union(pa, pb)
  
  return ret

def resolve(edges, vertices, valor_total):
  # Aplica o kruskal que irá retornar o valor total da árvore geradora mínima
  # E subtrai pelo total
  return valor_total - kruskal(edges, vertices)

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


    edges.append((valor, c1, c2))
    total += valor # Soma o valor total que a cidade gasta com a iluminação de todas as ruas

  print(resolve(edges, V, total))
