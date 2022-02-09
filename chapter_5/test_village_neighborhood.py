from .village_neighborhood import village_neighborhood


def test_sample_1():
    output = village_neighborhood(7, [6, 20, 50, 4, 19, 15, 1])
    assert output == 2.5