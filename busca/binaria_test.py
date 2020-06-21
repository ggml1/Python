from busca.binaria import busca_binaria

def test_primeiro_index():
  assert busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 1) == 0

def test_ultimo_index():
  assert busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 8) == 7

def test_meio_index():
  assert busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 3) == 2

def test_nao_encontrado():
  assert busca_binaria([1, 2, 3, 4, 5, 6, 7, 8], 77) == -1