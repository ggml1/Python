"""
  Em cada etapa da busca, estando em um intervalo [inicio, fim],
  onde o meio é igual a (inicio + fim) / 2 (valor arredondado para baixo)
  temos os seguintes cenários:

  - Se o valor do elemento central for o alvo, podemos apenas
    retornamos o seu índice;

  - Se o valor do elemento central for maior que o alvo,
    restringimos o intervalo de busca para antes dele, já que todos à
    sua frente serão maiores do que ele e, portanto, maiores que o alvo.
    Fazemos essa restrição colocando o fim do intervalo como "meio - 1";

  - Se o valor do elemento central for menor que o alvo,
    restringimos o intervalo de busca para depois dele, já que todos
    elementos de trás serão menores do que ele e, portanto, menores que o alvo.
    Fazemos essa restrição colocando o começo do intervalo como "meio + 1". 
"""

def busca_binaria(lista, alvo):
  # return busca_binaria_iterativa(lista, alvo)
  return busca_binaria_recursiva(lista, 0, len(lista), alvo)

def busca_binaria_recursiva(lista, inicio, fim, alvo):
  # Se os ponteiros de inicio e fim colidirem, significa que estamos buscando em um intervalo vazio. 
  # Logo o alvo não está na lista
  if inicio >= fim:
    return -1

  # Salva o ponto do meio da lista
  meio = (inicio + fim) // 2

  # Define os limites da busca dependendo se o alvo for igual, menor ou maior que o ponto do meio atual
  if lista[meio] == alvo:
    return meio
  elif lista[meio] > alvo:
    return busca_binaria_recursiva(lista, inicio, meio, alvo)
  else:
    return busca_binaria_recursiva(lista, meio + 1, fim, alvo)
  
def busca_binaria_iterativa(lista, alvo):
  inicio = 0
  fim = len(lista) - 1
  
  while inicio <= fim:
    meio = (inicio + fim) // 2
    
    if lista[meio] == alvo:
      return meio
    elif lista[meio] > alvo:
      fim = meio - 1
    else:
      inicio = meio + 1
  
  # Sair do while significa que não mais possuímos um intervalo
  # válido de buscas e, portanto, o elemento não foi encontrado.
  return -1
