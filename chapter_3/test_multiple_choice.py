from .multiple_choice import student_right_answers


def test_student_right_answers_1():
    output = student_right_answers(3, 'ABC', 'ACB')
    assert output == 1


def test_student_right_answers_2():
    output = student_right_answers(3, 'ABC', 'ABA')
    assert output == 2


def test_student_right_answers_3():
    output = student_right_answers(4, 'ABCD', 'ABAD')
    assert output == 3