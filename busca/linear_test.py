from busca.linear import busca_linear

def test_primeiro_index():
  assert busca_linear([2, 1, 3, 7, 1, 5], 2) == 0

def test_ultimo_index():
  assert busca_linear([2, 1, 3, 7, 1, 5], 5) == 5

def test_meio_index():
  assert busca_linear([2, 1, 3, 7, 1, 5], 3) == 2

def test_nao_encontrado():
  assert busca_linear([2, 1, 3, 7, 1, 5], 77) == -1
