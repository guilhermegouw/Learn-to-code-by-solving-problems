from .need_more_money import need_to_raise_more_money


def test_yes():
    assert need_to_raise_more_money(4000, '0.5 0.2 0.1 0.2', 400) == 'YES'

def test_no():
    assert need_to_raise_more_money(6000, '0.1 0.1 0.45 0.35', 2000) == 'NO'