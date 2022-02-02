from .song_playlist import playlist

def test_button_1Pressed_once():
    output = playlist(['11'])
    assert output == 'BCDEA'