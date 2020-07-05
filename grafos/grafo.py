class Grafo:
  """
    Este objeto implementa as estruturas para um grafo, representado
    através de uma lista de adjacência.
  """
  def __init__(self, numero_de_vertices):
    self.numero_de_vertices = numero_de_vertices
     
    # Inicializa uma lista de adjacência vazia para cada um dos vértices do grafo
    self.lista_de_adjacencia = [ [] for i in range(self.numero_de_vertices) ]
  
  def adiciona_aresta(self, vertice_a, vertice_b, bidirecional = False):
    self.lista_de_adjacencia[vertice_a].append(vertice_b)
    
    if bidirecional:
      self.adiciona_aresta(vertice_b, vertice_a)
