from .magnus import how_many_honi_blocks


def test_how_many_honi_blocks_0():
    output = how_many_honi_blocks('MAGNUS')
    assert output == 0


def test_how_many_honi_blocks_0_empty_string():
    output = how_many_honi_blocks('')
    assert output == 0


def test_how_many_honi_blocks_1():
    output = how_many_honi_blocks('HONI')
    assert output == 1


def test_how_many_honi_blocks_1_different_word_than_HONI():
    output = how_many_honi_blocks('HHHHOOOONNNNIIII')
    assert output == 1


def test_how_many_honi_blocks_2():
    output = how_many_honi_blocks('HONIHONI')
    assert output == 2


def test_how_many_honi_blocks_2_messed_word():
    output = how_many_honi_blocks('PROHODNIHODNIK')
    assert output == 2


def test_how_many_honi_blocks_3():
    output = how_many_honi_blocks('HONIHONIHONI')
    assert output == 3


def test_how_many_honi_blocks_3_messed_word():
    output = how_many_honi_blocks('HUIlOTRNERIUIHOUllONIHYTYTYlONYTYTYTI')
    assert output == 3