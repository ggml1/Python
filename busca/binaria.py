def busca_binaria(lista, alvo):
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