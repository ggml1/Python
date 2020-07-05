from queue import Queue # documentação: https://docs.python.org/3/library/queue.html

def busca_em_largura(lista_de_adjacencia, vertice_inicial, numero_de_vertices):
  """
    Essa função recebe como parâmetros as especificações do grafo e o ponto de partida
    da busca em largura, e retorna uma lista "distancia", onde distancia[x] é
    a distância do ponto de partida até o vértice "x".
    
    Assumimos, aqui, que os vértices do grafo são numerados de 0 a numero_de_vertices - 1.
  
    :param lista_de_adjacencia: lista de listas, onde cada lista interior representa a lista de adjacência de um vértice do grafo
    :param vertice_inicial: vértice pelo qual a busca será iniciada
    :param numero_de_vertices: total de vértices no grafo
  """
  fila = Queue()
  distancia = [ -1 for i in range(numero_de_vertices) ]
  
  distancia[vertice_inicial] = 0
  fila.put(vertice_inicial)
  
  while not fila.empty():
    vertice_da_vez = fila.get()
    
    for vertice_adjacente in lista_de_adjacencia[vertice_da_vez]:
      if distancia[vertice_adjacente] == -1:
        distancia[vertice_adjacente] = distancia[vertice_da_vez] + 1
        fila.put(vertice_adjacente)
  
  return distancia
