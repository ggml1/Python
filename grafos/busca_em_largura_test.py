from grafos.grafo import Grafo
from grafos.busca_em_largura import busca_em_largura

def teste_grafo_um_vertice():
  grafo = Grafo(1)
  grafo.adiciona_aresta(0, 0, bidirecional = True)
  distancias = busca_em_largura(grafo.lista_de_adjacencia, 0, 1)
  assert(distancias[0] == 0)
  
def teste_grafo_linear():
  grafo = Grafo(5)
  
  for i in range(4):
    grafo.adiciona_aresta(i, i + 1, bidirecional = True)
    
  distancias = busca_em_largura(grafo.lista_de_adjacencia, 0, 5)
  
  for i in range(5):
    assert(distancias[i] == i)

def teste_grafo_completo()
  grafo = Grafo(50)
  
  for i in range(50):
    for j in range(50):
      if i != j:
        grafo.adiciona_aresta(i, j)
        
  distancias = busca_em_largura(grafo.lista_de_adjacencia, 0, 50)
  
  for i in range(50):
    if i == 0:
     assert(distancias[i] == 1)
    else:
     assert(distancias[i] == 0)
