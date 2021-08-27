from .occupied_spaces import get_number_of_spaces_occupied_in_both_days


def test_get_number_of_spaces_occupied_in_both_days_one_space_0_occupied_in_both_days():
    output = get_number_of_spaces_occupied_in_both_days(1, '.', '.')
    assert output == 0


def test_get_number_of_spaces_occupied_in_both_days_one_space_0_occupied_in_both_days_1_yesterday_0_today():
    output = get_number_of_spaces_occupied_in_both_days(1, 'C', '.')
    assert output == 0


def test_get_number_of_spaces_occupied_in_both_days_one_space_0_occupied_in_both_days_0_yesterday_1_today():
    output = get_number_of_spaces_occupied_in_both_days(1, '.', 'C')
    assert output == 0


def test_get_number_of_spaces_occupied_in_both_days_one_space_1_occupied_in_both_days():
    output = get_number_of_spaces_occupied_in_both_days(1, 'C', 'C')
    assert output == 1


def test_get_number_of_spaces_occupied_in_both_days_2_spaces_0_occupied_in_both_days():
    output = get_number_of_spaces_occupied_in_both_days(2, '..', '..')
    assert output == 0


def test_get_number_of_spaces_occupied_in_both_days_2_spaces_0_occupied_in_both_days_ver_2():
    output = get_number_of_spaces_occupied_in_both_days(2, 'C.', '.C')
    assert output == 0


def test_get_number_of_spaces_occupied_in_both_days_2_spaces_1_occupied_in_both_days_first_day():
    output = get_number_of_spaces_occupied_in_both_days(2, 'C.', 'C.')
    assert output == 1


def test_get_number_of_spaces_occupied_in_both_days_2_spaces_1_occupied_in_both_days_second_day():
    output = get_number_of_spaces_occupied_in_both_days(2, '.C', '.C')
    assert output == 1