'''
The Challenge

We have ﬁve favorite songs named A, B, C, D, and E. We’ve created a playlist
of these songs and are using an app to manage the playlist. The songs start oﬀ 
in the order A, B, C, D, E. The app has four buttons:

Button 1: Moves the ﬁrst song of the playlist to the end of the playlist. 
For example, if the playlist is currently A, B, C, D, E, then it changes 
to B, C, D, E, A.

Button 2: Moves the last song of the playlist to the beginning of the playlist. 
For example, if the playlist is currently A, B, C, D, E, then it changes 
to E, A, B, C, D.

Button 3: Swaps the ﬁrst two songs of the playlist. 
For example, if the playlist is currently A, B, C, D, E, then it changes to 
be B, A, C, D, E.

Input

The input consists of pairs of lines, where the ﬁrst line of a pair gives the 
number of a button ( 1 , 2 , 3 , or 4 ), and the second gives the number of 
times that the user pressed this button (between 1 and 10). That is, the ﬁrst 
line is the number of a button, the second line is the number of times it is 
pressed, the third line is the number of a button, the fourth line is the number 
of times it is pressed, and so on.

The input ends with these two lines:
3
1

indicating that the user pressed button
3
once.

Output

Output the order of songs in the playlist after all button presses. 
The output must be on one line, with a space separating each pair of songs.
'''

def playlist(moves: list[str]) -> str:
    playlist = 'ABCDE'
    for move in moves:
        button = move[0]
        times_pressed = int(move[1])
        if button == '1':
            for _ in range(times_pressed):
                playlist = playlist[1:] + playlist[0]
        if button == '2':
            for _ in range(times_pressed):
                playlist = playlist[-1] + playlist[:4]
        if button == '3':
            for _ in range(times_pressed):
                playlist = playlist[1] + playlist[0] + playlist[2:]
    return playlist
