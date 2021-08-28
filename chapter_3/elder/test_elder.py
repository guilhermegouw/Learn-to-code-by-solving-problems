from .elder import elder


def test_elder_case_1():
    output = elder('A', 3, ['BA', 'CB', 'DA'])
    assert output == 'C3'


def test_elder_case_2():
    output = elder('N', 5, ['DA', 'NB', 'BA', 'CD', 'FA'])
    assert output == 'N1'


def test_elder_case_3():
    output = elder('X', 4, ['AX', 'BX', 'XA', 'DA'])
    assert output == 'X2'