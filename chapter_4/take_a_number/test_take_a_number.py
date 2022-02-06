from .take_a_number import take_a_number


def test_sample_input():
    output = take_a_number(
        23,
        ["TAKE",
        "TAKE",
        "SERVE",
        "TAKE",
        "SERVE",
        "SERVE",
        "CLOSE",
        "TAKE",
        "TAKE",
        "TAKE",
        "SERVE",
        "CLOSE",
        "TAKE",
        "SERVE",
        "TAKE",
        "SERVE",
        "TAKE",
        "TAKE",
        "TAKE",
        "TAKE",
        "TAKE",
        "TAKE",
        "SERVE",
        "CLOSE"]
    )
    assert output == [(3, 0, 26), (3, 2, 29), (8, 5, 37)]
