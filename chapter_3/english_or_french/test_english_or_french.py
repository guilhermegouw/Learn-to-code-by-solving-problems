from .english_or_french import is_english_or_french


def test_is_english_or_french_english():
    sentence = """The red cat sat on the mat.\
    Why are you so sad cat?\
    Don't ask that."""
    output = is_english_or_french(sentence)
    assert output == 'English'


def test_is_english_or_french_french_more_s_than_t():
    sentence = """
    Lorsque j'avais six ans j'ai vu, une fois,
    une magnifique image,
    dans un livre
    """
    output = is_english_or_french(sentence)
    assert output == 'French'


def test_is_english_or_french_english_more_t_than_s():
    sentence = """
    Si je discernais ta voix encore
    Connaissant ce coeur qui doute,
    Tu me dirais de tirer un trait
    Quoi que partir me coute.
    """
    output = is_english_or_french(sentence)
    assert output == 'English'