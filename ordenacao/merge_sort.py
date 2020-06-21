def merge_sort(lista):
  # Se a lista tiver tamanho 1 ou menor, ela já está ordenada
  if len(lista) <= 1:
    return lista

  meio = len(lista) // 2

  # Separa a lista em duas metades
  parte1 = lista[0:meio]
  parte2 = lista[meio:]

  # Juntas as de maneira ordenada as duas metades e retorna
  return juntar_ordenados(merge_sort(parte1), merge_sort(parte2))

def juntar_ordenados(lista1, lista2):
  # Cria um ponteiro no inicio de cada lista
  res = []
  index_lista1 = 0
  index_lista2 = 0

  # Vai adicionando no resultado o menor elemento de cada iteracao
  while index_lista1 < len(lista1) or index_lista2 < len(lista2):
    if index_lista1 >= len(lista1):
      res.append(lista2[index_lista2])
      index_lista2 += 1
    elif index_lista2 >= len(lista2):
      res.append(lista1[index_lista1])
      index_lista1 += 1
    elif lista2[index_lista2] < lista1[index_lista1]:
      res.append(lista2[index_lista2])
      index_lista2 += 1
    else:
      res.append(lista1[index_lista1])
      index_lista1 += 1

  return res