def busca_linear(lista, alvo):
  # Verifica todos os elementos
  for index, valor in enumerate(lista):
    # Se o valor da posição for igual ao alvo, retorna o indíce
    if valor == alvo:
      return index

  # Caso valor não tenha sido encontrado, retorna -1
  return -1