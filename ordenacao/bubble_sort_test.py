from ordenacao.bubble_sort import bubble_sort

def test_invertidos():
  input = [3, 2, 1]
  bubble_sort(input)
  assert input == [1, 2, 3]

def test_ja_ordenado():
  input = [1, 2, 3, 4, 5]
  bubble_sort(input)
  assert input == [1, 2, 3, 4, 5]

def test_misturados():
  input = [1, 3, 2, 7, 5]
  bubble_sort(input)
  assert input == [1, 2, 3, 5, 7]

def test_vetor_vazio():
  input = []
  bubble_sort(input)
  assert input == []