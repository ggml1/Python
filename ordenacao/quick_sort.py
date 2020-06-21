import random

def quick_sort(lista):
  # Se a lista tiver tamanho 1 ou menor, ela já está ordenada
  if len(lista) <= 1:
    return lista

  # Define um pivot de posição aleatória
  # É muito comum ver algoritmos definirem um pivot de posição fixa, como o primeiro elemento ou o elemento do meio
  # Mas decidimos aqui ficar com o algoritmo clássico 
  pivot = random.randint(0, len(lista) - 1)
  valor_pivot = lista[pivot]

  menores = []
  maiores = []

  # Separa a lista entre os menores e os maiores que o valor pivot
  for valor in lista:
    if valor <= valor_pivot:
      menores.append(valor)
    else:
      maiores.append(valor)

  # Retorna a chamada recursiva de cada uma das listas concatenadas
  return quick_sort(menores) + quick_sort(maiores)