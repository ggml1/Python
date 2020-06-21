from ordenacao.merge_sort import merge_sort

def test_invertidos():
  assert merge_sort([3, 2, 1]) == [1, 2, 3]

def test_ja_ordenado():
  assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_misturados():
  assert merge_sort([1, 3, 2, 7, 5]) == [1, 2, 3, 5, 7]

def test_vetor_vazio():
  assert merge_sort([]) == []