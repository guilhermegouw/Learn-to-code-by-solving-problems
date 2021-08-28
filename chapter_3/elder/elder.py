"""
After having watched all eight Harry Potter movies in a week, Nikola finally realized how 
the famous Elder Wand changes the wizard it obeys. If wizard A, whom the wand is currently 
obeying, is defeated by wizard B in a duel, then the wand will start obeying the wizard B.

Nikola is now wondering what would happen if 26 wizards labeled with uppercase letters of 
the English alphabet from A to Z began fighting in duels for the fondness of the Elder Wand. 
If we know the label of the wizard that the wand had obeyed before all duels and the outcomes 
of all N duels that were held one after another, answer the following questions:

    Which wizard did the wand obey after all N duels?
    How many different wizards did the wand obey?

Input

The first line contains an uppercase letter of the English alphabet, the label of the wizard 
that the wand obeyed at the beginning.
The second line contains an integer number N, the number of duels from the text of the task.

In the next N rows there are two different uppercase letters of the English alphabet Z1 and Z2 
separated by a space, whereas the wizard with the label Z1 defeated the wizard with the label 
Z2 in the ith duel.

Output

In the first line print an uppercase letter of the English alphabet, answer to the first question 
from the task description.

In the second line print an integer number, answer to the second question from the task description.

Scoring

Correct answer to the first question is worth 2 points and the correct answer to the second question 
is worth 3 points. If you do not know how to solve some part of the task, then print any value in 
the corresponding line.

Sample Input 1

A
3
B A
C B
D A

Sample Output 1

C
3

Explanation for Sample Output 1

Before the first duel, the Elder Wand obeyed wizard A. After the first duel, it obeyed wizard B, and 
after the second wizard C. The third duel didn't change anything.

Sample Input 2

N
5
D A
N B
B A
C D
F A

Sample Output 2

N
1

Sample Input 3

X
4
A X
B X
X A
D A

Sample Output 3

X
2
"""


from typing import List


def elder(wand_obey_to: str, num_of_duels: int, duels: List) -> str:
    masters = wand_obey_to
    for duel in duels:
        if duel[1] == wand_obey_to:
            wand_obey_to = duel[0]
            if wand_obey_to not in masters:
                masters += wand_obey_to
    return f'{wand_obey_to}{len(masters)}'