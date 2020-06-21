def bubble_sort(lista):
  for i in range(0, len(lista)):
    for j in range(i+1, len(lista)):
      # Compara o valor da posição i com todos os valores que estão à frente.
      # Se o valor comparado é menor, troca o valor da posição i com o de posição j
      if lista[j] < lista[i]:
        lista[i], lista[j] = lista[j], lista[i]

