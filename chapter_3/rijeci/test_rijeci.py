from .rijeci import how_much_letters_A_and_B


def test_how_much_letters_A_and_B_1_time():
    output = how_much_letters_A_and_B(1)
    assert output == '0 1'


def test_how_much_letters_A_and_B_2_time():
    output = how_much_letters_A_and_B(2)
    assert output == '1 1'


def test_how_much_letters_A_and_B_3_time():
    output = how_much_letters_A_and_B(3)
    assert output == '1 2'


def test_how_much_letters_A_and_B_4_time():
    output = how_much_letters_A_and_B(4)
    assert output == '2 3'