"""
Veronica attends a music academy. She was given a music sheet of a composition with only notes (without annotations), 
and needs to recognise the scale used. 
In this problem, we will limit ourselves to only the two most frequently used (and usually taught in schools first) scales: 
A-minor and C-major. 
This doesn't make them simpler or more basic than other minor and major scales – all minor scales are mutually equivalent 
save for translation, and so are major scales.

Still, out of the 12 tones of an octave {A,A#,B,C,C#,D,D#,E,F,F#,G,G#} used in modern music, A-minor and C-major scales do 
use the tones with shortest names: A-minor is defined as an ordered septuple (A,B,C,D,E,F,G), and C-major as (C,D,E,F,G,A,B).

Notice that the sets of tones of these two scales are equal. What's the difference? 
The catch is that not only the set of tones, but also their usage, determines a scale. 
Specifically, the tonic (the first tone of a scale), subdominant (the fourth tone) and dominant (the fifth tone) are the primary 
candidates for accented tones in a composition. In A-minor, these are A, D, and E, and in C-major, they are C, F, and G. 
We will name these tones main tones.

Aren't the scales still equivalent save for translation? 
They are not: for example, the third tone of A-minor (C) is three half-tones higher than the tonic (A), 
while the third tone of C-major (E) is four halftones higher than the tonic (C). The difference, therefore, lies in the intervals. 
This makes minor scales "sad" and major scales "happy".

Write a program to decide if a composition is more likely written in A-minor or C-major by counting whether there are more main 
tones of A-minor or of C-major among the accented tones (the first tones in each measure). 
If there is an equal number of main tones, determine the scale based on the last tone (which is guaranteed to be either A for A-minor 
or C for C-major in any such test case).

For example, examine the well-known melody "Frère Jacques":

CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C

The character | separates measures, so the accented tones are, in order: C,E,C,E,E,G,E,G,G,E,G,E,C,C,C,C. 
Ten of them (C,C,G,G,G,G,C,C,C,C) are main tones of C-major, while six (E,E,E,E,E,E) are main tones of A-minor. 
Therefore, our best estimate is that the song was written in C-major.


Input Specification

The first and only line of input contains a sequence of at least 5, and at most 100, characters from the set {A, B, C, D, E, F, G, |}. 
This is a simplified notation for a composition, where the character | separates measures. The characters | will never appear adjacent 
to one another, at the beginning, or at the end of the sequence.

Output Specification

The first and only line of output must contain the text C-dur (for C-major) or A-mol (for A-minor).

Sample Input 1

AEB|C

Sample Output 1

C-dur

Sample Input 2

CD|EC|CD|EC|EF|G|EF|G|GAGF|EC|GAGF|EC|CG|C|CG|C

Sample Output 2

C-dur
"""