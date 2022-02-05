from .ameri_canadian import american_to_canadian


def test_one_word_more_than_4_letters():
    assert american_to_canadian('color') == 'colour'

def test_one_word_less_than_4_letters():
    assert american_to_canadian('for') == 'for'

def test_two_words():
    assert american_to_canadian('color for') == 'colour for'

def test_three_words():
    assert american_to_canadian('color for taylor') == 'colour for taylour'