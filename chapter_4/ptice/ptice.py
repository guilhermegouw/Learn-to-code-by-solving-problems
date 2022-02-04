'''
Adrian, Bruno and Goran wanted to join the bird lovers' club. 
However, they did not know that all applicants must pass an entrance exam. 
The exam consists of N questions, each with three possible answers: A, B and C.

Unfortunately, they couldn't tell a bird from a whale so they are trying to 
guess the correct answers. 
Each of the three boys has a theory of what set of answers will work best:

Adrian claims that the best sequence is: A, B, C, A, B, C, A, B, C, A, B, C, ...

Bruno is convinced that this is better: B, A, B, C, B, A, B, C, B, A, B, C,...

Goran laughs at them and will use this sequence: C, C, A, A, B, B, C, C, A, A, B, B,...

Write a program that, given the correct answers to the exam, determines who 
of the three was right whose sequence contains the most correct answers.

Input Specification

The first line contains an integer N, the number of questions on the exam. 
The second line contains a string of N letters A, B and C. 
These are, in order, the correct answers to the questions in the exam.

Output Specification

On the first line, output M, the largest number of correct answers one of the 
three boys gets. 
After that, output the name of the boy whose sequences result in more correct answers.

Sample Input 1

5
BAACC

Sample Output 1

3
Bruno

Sample Input 2

9
AAAABBBBB

Sample Output 2

4
Adrian
Bruno
Goran
'''

def who_is_right(num_letters, sequence):
    adrian_answer = (num_letters // 3) * 'ABC' +  'ABC'[:(num_letters % 3)]
    bruno_answer = (num_letters // 4) * 'BABC' +  'BABC'[:(num_letters % 4)]
    goran_answer = (num_letters // 6) * 'CCAABB' +  'CCAABB'[:(num_letters % 6)]
    adrian_points = {'points': 0, 'name': 'Adrian'}
    bruno_points = {'points': 0, 'name': 'Bruno'}
    goran_points = {'points': 0, 'name': 'Goran'}
    for i in range(len(sequence)):
        if adrian_answer[i] == sequence[i]:
            adrian_points['points'] += 1
        if bruno_answer[i] == sequence[i]:
            bruno_points['points'] += 1
        if goran_answer[i] == sequence[i]:
            goran_points['points'] += 1
    scores = [adrian_points, bruno_points, goran_points]
    highest_score = max([adrian_points['points'], bruno_points['points'], goran_points['points']])
    winners = []
    for score in scores:
        if score['points'] == highest_score:
            winners.append(score['name'])
    who_is_the_winner = f'{highest_score}'
    for winner in winners:
        who_is_the_winner += f' {winner}'
    return who_is_the_winner