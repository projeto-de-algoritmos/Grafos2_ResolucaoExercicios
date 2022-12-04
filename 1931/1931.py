import sys
import heapq

ORIG = 1

DIST = 0
N_CIDADE = 1

DIST_PAR = 0
DIST_IMPAR = 1

class Grafo:
    # Inicia a estrutura básica do grafo
    def __init__(self, V) -> None:
        self.nVertices = V
        self.grafo = [[] for i in range(V)]
    
    # Cria a aresta em ambos os sentidos (problema com grafo direcionado)
    def criaAresta (self, cidadeA, cidadeB, precoPedagio):
        self.grafo[cidadeA].append([cidadeB, precoPedagio])
        self.grafo[cidadeB].append([cidadeA, precoPedagio])

    # Algortimo de Dijkstra alterado para a solução do problema. São monitoradas duas
    # distâncias: par e ímpar. As distâncias ímpar dizem respeito, primeiramente, ao valor 
    # do pedágio para as cidades imediatamente alcançáveis (ou seja, um só pedágio). Desta
    # forma, é possível calcular a distância par dos seus vizinhos como a distância entre 
    # eles + a distância ímpar da cidade atual, assim como a distância ímpar é a distância
    # entre eles + a distância par da cidade atual.
 
    def algDijkstra(self, cidadeB):
        # Inicializa as distâncias com o maior valor possível
        distancias = [[sys.maxsize, sys.maxsize] for i in range(self.nVertices)]        

        # Define as distâncias da cidade de origem para ela mesma 
        # A par é 0, pois a cidade está a 0 pedágios dela mesma, e a ímpar não existe (inalcançável)
        # pois não é possível permanecer na cidade passando por um pedágio 
        distancias[ORIG] = [0, sys.maxsize]

        # Cria a fila para a ordem de visitação dos nós, partindo do nó de origem com distância 0
        fila = [[0, ORIG]]
        heapq.heapify(fila)

        # Enquanto a fila não estiver vazia
        while len(fila) > 0:
            # Retira o primeiro item da fila como a cidade sendo analisada no momento
            pop = heapq.heappop(fila)
            cidadeAtual = pop[N_CIDADE]
            distancia = pop[DIST]
            
            # Se a distância da cidade contida no item da fila for maior que a contida no vetor de distâncias,
            # esta cidade já foi visitada, então passa para o próximo item. 
            if distancia > distancias[cidadeAtual][DIST_PAR] and distancia > distancias[cidadeAtual][DIST_IMPAR]:
                continue

            # Para cada vizinho da cidada atual, a distância é analisada
            for vizinho in self.grafo[cidadeAtual]:
                # Se a distância par da cidade atual + a distância para o vizinho for menor que a distância ímpar
                # do vizinho, esta é substituída e este par é colocado na fila 
                if distancias[cidadeAtual][DIST_PAR] + vizinho[1] < distancias[vizinho[0]][DIST_IMPAR]:
                    distancias[vizinho[0]][DIST_IMPAR] = distancias[cidadeAtual][DIST_PAR] + vizinho[1]
                    heapq.heappush(fila, [distancias[vizinho[0]][DIST_IMPAR], vizinho[0]])
                
                # Se a distância ímpar da cidade atual + a distância para o vizinho for menor que a distância par
                # do vizinho, esta é substituída e este par é colocado na fila
                if distancias[cidadeAtual][DIST_IMPAR] + vizinho[1] < distancias[vizinho[0]][DIST_PAR]:
                   distancias[vizinho[0]][DIST_PAR] = distancias[cidadeAtual][DIST_IMPAR] + vizinho[1]
                   heapq.heappush(fila, [distancias[vizinho[0]][DIST_PAR], vizinho[0]]) 
        
        # Por fim, é retornada as distâncias par e ímpar para a cidade B (o destino)
        return distancias[cidadeB]

C, V = input().split(' ')
C = int(C)
V = int(V)

grafo = Grafo(C + 1)

for i in range(V):
    A, B, peso = input().split(' ')
    grafo.criaAresta(int(A), int(B), int(peso))

# Calcula as distâncias para o destino partindo da origem através do algoritmo de Dijkstra modificado
distanciasDestino = grafo.algDijkstra(C)

# Se a distância par para o destino for o maior valor possível, não existe caminho da origem para o destino
# passando por um valor par de pedágios. 
if distanciasDestino[DIST_PAR] == sys.maxsize:
    print(-1)
else:
    print(distanciasDestino[DIST_PAR])