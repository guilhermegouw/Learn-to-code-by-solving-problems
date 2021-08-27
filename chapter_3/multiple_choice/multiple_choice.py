"""
Your teacher likes to give multiple choice tests. One benefit of giving these tests 
is that they are easy to mark, given an answer key. 
The other benefit is that students believe they have a one-in-five chance of getting 
the correct answer, assuming the multiple choice possibilities are A, B, C, D or E.

Write a program that your teacher can use to grade one multiple choice test.

Input Specification

n: Number of questions
student: Student answers
answers: right answers

Output Specification

Output the integer which corresponds to the number of questions the student answered correctly.

Sample Input 1

student_right_anwers(3, 'ABC', 'ACB')

Output for Sample Input 1

1

Sample Input 2

student_right_anwers(3, 'AAA', 'ABA')

Output for Sample Input 2

2
"""


def student_right_answers(n: int, student: str, answers: str) -> int:
    right_answers = 0
    for i in range(n):
        if student[i] == answers[i]:
            right_answers += 1
    return right_answers
