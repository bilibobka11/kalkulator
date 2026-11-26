from polski import calculate, to_rpn, tokenize

def test_one_operator():
    assert calculate("11 + 8") == 19

def test_many_operator():
    assert calculate("3 + 4 * 2 / 2") == 7

def test_scobki():
    assert calculate("(5 + 5) * 2") == 20

def test_rpn():
    assert to_rpn("6 - 4 * 3") == [6, 4, 3, '*', '-']

def test_rpn1():
    assert to_rpn("6 - (4 + 1) * 3") == [6, 4, 1, '+', 3, '*', '-']

def test_minus():
    assert calculate("5 - 8") == -3

def test_tokenize():
    assert tokenize("3 + 4 * (3 - 1) / 2") == ["3","+","4","*","(","3","-","1",")","/","2"]