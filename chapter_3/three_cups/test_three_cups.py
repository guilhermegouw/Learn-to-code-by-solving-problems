from .three_cups import get_ball_location


def test_get_ball_location_one_move_A():
    output = get_ball_location('A')
    assert output == 2


def test_get_ball_location_one_move_B():
    output = get_ball_location('B')
    assert output == 1


def test_get_ball_location_one_move_C():
    output = get_ball_location('C')
    assert output == 3


def test_get_ball_location_two_moves_AA():
    output = get_ball_location('AA')
    assert output == 1


def test_get_ball_location_two_moves_BB():
    output = get_ball_location('BB')
    assert output == 1


def test_get_ball_location_two_moves_CC():
    output = get_ball_location('CC')
    assert output == 1


def test_get_ball_location_two_moves_AB():
    output = get_ball_location('AB')
    assert output == 3


def test_get_ball_location_two_moves_AC():
    output = get_ball_location('AC')
    assert output == 2


def test_get_ball_location_two_moves_BA():
    output = get_ball_location('BA')
    assert output == 2


def test_get_ball_location_two_moves_BC():
    output = get_ball_location('BC')
    assert output == 3


def test_get_ball_location_two_moves_CA():
    output = get_ball_location('CA')
    assert output == 3


def test_get_ball_location_two_moves_CB():
    output = get_ball_location('CB')
    assert output == 2


def test_get_ball_location_three_moves_ABC():
    output = get_ball_location('ABC')
    assert output == 1


def test_get_ball_location_two_moves_ACB():
    output = get_ball_location('ACB')
    assert output == 3


def test_get_ball_location_three_moves_BAC():
    output = get_ball_location('BAC')
    assert output == 2


def test_get_ball_location_two_moves_BCA():
    output = get_ball_location('BCA')
    assert output == 3


def test_get_ball_location_three_moves_CAB():
    output = get_ball_location('CAB')
    assert output == 2


def test_get_ball_location_two_moves_CBA():
    output = get_ball_location('CBA')
    assert output == 1