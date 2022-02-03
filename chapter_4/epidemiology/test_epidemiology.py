
from epidemiology.epidemiology import epidemiology_estimation


def test_sample_1():
    output = epidemiology_estimation(750, 1, 5)
    assert output == 4

def test_sample_2():
    output = epidemiology_estimation(10, 2, 1)
    assert output == 5