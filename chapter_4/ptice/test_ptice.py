from .ptice import who_is_right


def test_sample_1():
    output = who_is_right(5, 'BAACC')
    assert output == '3 Bruno'

def test_sample_2():
    output = who_is_right(9, 'AAAABBBBB')
    assert output == '4 Adrian Bruno Goran'