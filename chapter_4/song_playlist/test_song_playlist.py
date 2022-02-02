from .song_playlist import playlist

def test_button_1_pressed_once():
    output = playlist(['11'])
    assert output == 'BCDEA'

def test_button_1_pressed_twice():
    output = playlist(['12'])
    assert output == 'CDEAB'

def test_button_2_pressed_once():
    output = playlist(['21'])
    assert output == 'EABCD'

def test_button_2_pressed_twice():
    output = playlist(['22'])
    assert output == 'DEABC'

def test_button_3_pressed_once():
    output = playlist(['31'])
    assert output == 'BACDE'

def test_button_3_pressed_twice():
    output = playlist(['32'])
    assert output == 'ABCDE'

def test_button_1_once_and_button_2_once():
    output = playlist(['11', '21'])
    assert output == 'ABCDE'

def test_button_1_once_and_button_2_twice():
    output = playlist(['11', '22'])
    assert output == 'EABCD'

def test_button_1_once_button_2_once_button3_once():
    output = playlist(['11', '21', '31'])
    assert output == 'BACDE'

def test_button_1_once_button_2_once_button3_twice():
    output = playlist(['11', '21', '32'])
    assert output == 'ABCDE'