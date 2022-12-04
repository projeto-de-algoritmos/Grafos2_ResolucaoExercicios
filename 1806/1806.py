import sys
import heapq

DIST = 0
LOCAL = 1


class Grafo:
    # Inicia a estrutura básica do grafo
    def __init__(self, V) -> None:
        self.nVertices = V
        self.grafo = [[] for i in range(V)]
    
    # Cria a aresta em ambos os sentidos (problema com grafo direcionado)
    def criaAresta (self, localA, localB, metros):
        self.grafo[localA].append([localB, metros])
        self.grafo[localB].append([localA, metros])

    # Algoritmo de Dijkstra sem nenhuma necessidade de adaptação para o 
    # problema
    def algDijkstra(self, local):
        visitado = [False for i in range(self.nVertices)]
        distancias = [sys.maxsize for i in range(self.nVertices)]
        distancias[local] = 0

        fila = [[0, local]]
        heapq.heapify(fila)

        while len(fila) > 0:
            pop = heapq.heappop(fila)
            localAtual = pop[LOCAL]
            
            if visitado[localAtual]:
                continue

            visitado[localAtual] = True

            for vizinho in self.grafo[localAtual]:
                if distancias[localAtual] + vizinho[1] < distancias[vizinho[0]]:
                    distancias[vizinho[0]] = distancias[localAtual] + vizinho[1]
                    heapq.heappush(fila, [distancias[vizinho[0]], vizinho[0]])
            
        return distancias

N, C, S, B = input().split(' ')
N = int(N)
C = int(C)
S = int(S)
B = int(B)


grafoBino = Grafo(N+1)
rotasSecretas = []

# Adiciona as rotas que o Bino conhece
for i in range(C):
    a, b, v = input().split(' ')
    grafoBino.criaAresta(int(a), int(b), int(v))

for i in range(S):
    a, b, v = input().split(' ')
    rotasSecretas.append([a, b, v])

L = list(input().split(' '))

K, F = input().split(' ')
K = int(K)
F = int(F)

# Calcula a menor distância que o Bino está do destino com base nas rotas que ele conhece
distancias = grafoBino.algDijkstra(F)
distBino = distancias[K]

# Adiciona ao grafo as rotas conhecidas somente pelos criminosos
for a, b, v in rotasSecretas:
    grafoBino.criaAresta(int(a), int(b), int(v))

# Calcula a distância entre todos os locais (incluindo as rotas dos criminosos) para o local de origem
distanciasCriminosos = grafoBino.algDijkstra(F)

criminososEliminados = 0

# Percorre o vetor contendo a posição dos criminosos
for l in L:
    # Se a distância do criminoso para o destino for menor ou igual à distância do agente Bino para o destino, 
    # significa que eles irão se encontrar no caminho e o Bino precisará eliminá-lo. Logo, incrementa-se o número 
    # de criminosos eliminados
    if distanciasCriminosos[int(l)] <= distBino:
        criminososEliminados+=1

print(criminososEliminados)