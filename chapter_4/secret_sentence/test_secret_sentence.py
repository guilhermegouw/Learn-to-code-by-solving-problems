from .secret_sentence import lukas_decoder


def test_lukas_decoder():
    output = lukas_decoder('ipi lipikepe yopoupu.')
    assert output == 'i like you'


def test_lukas_decoder_single_consoant():
    output = lukas_decoder('b')
    assert output == 'b'


def test_lukas_decoder_single_vowel():
    output = lukas_decoder('apa')
    assert output == 'a'