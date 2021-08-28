"""
One day, little Mirko came across a funny looking machine! It consisted of a very very large screen and a single button. 
When he found the machine, the screen displayed only the letter A. 
After he pressed the button, the letter changed to B. 
The next few times he pressed the button, the word transformed from B to BA, then to BAB, then to BABBA. 
When he saw this, Mirko realized that the machine alters the word in a way that all the letters B get transformed to BA 
and all the letters A get transformed to B.

Amused by the machine, Mirko asked you a very difficult question! After K times of pressing the button, 
how much letters A and how much letters B will be displayed on the screen?

Input Specification

The first line of input contains the integer K ( 1 ≤ K ≤ 45 ) (1 \leq K \leq 45) , the number of times Mirko pressed the button.

Output Specification

The first and only line of output must contain two space-separated integers, the number of letters A and the number of letter B.
Scoring


Sample Input 1

1

Sample Output 1

0 1

Sample Input 2

4

Sample Output 2

2 3

Sample Input 3

10

Sample Output 3

34 55
"""


def how_much_letters_A_and_B(times_pressed: int) -> str:
    word = 'A'
    for i in range(times_pressed):
        new_word = ''
        for letter in word:
            if letter == 'A':
                new_word += 'B'
            if letter == 'B':
                new_word += 'BA'
        word = new_word
    a_letter = word.count('A')
    b_letter = word.count('B')
    return f'{a_letter} {b_letter}'

