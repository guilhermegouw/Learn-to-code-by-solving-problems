from .data_plan import get_data_available_for_following_month


def test_get_data_available_for_following_month():
    output = get_data_available_for_following_month(10, 3, '567')
    assert output == 12
