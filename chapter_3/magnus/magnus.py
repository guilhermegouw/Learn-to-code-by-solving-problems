"""
Magnus lost a game of chess to Kile so he found comfort in competitive programming. 
Very soon, he heard of the iconic COCI competition and decided to try his luck there.

He wrote a mail to Kile: "Dear Kile, please, prepare me for COCI. Magnus".

Kile replied: "You want to participate in COCI? All right, here's your warm-up task. 
A series of four consecutive letters of some word that make up the subword HONI 
(Croatian acronym for COCI) is called the HONI-block. I will send you the word of length 
N and you will throw out as many letters as you want (it might be none as well) so that 
in the end there are as many HONI-blocks as possible in the word. Kile".

Magnus was very worried and asked you, COCI competitive scene, for help. 
Help him determine the maximum number of HONI-blocks he can get in the final word.


Input

The first line contains a word of length N (1≤N≤100000), consisting of uppercase letters of the English alphabet.

Output

In the first and only line print out the required number of HONI-blocks.

Sample Input 1

MAGNUS

Sample Output 1

0

Sample Input 2

HHHHOOOONNNNIIII

Sample Output 2

1

Explanation for Sample Output 2

By throwing out three letters H, O, N or I Magnus can get the word HONI, which contains one HONI-block.

Sample Input 3

PROHODNIHODNIK

Sample Output 3

2
"""


def how_many_honi_blocks(word):
    honis = 0
    block = ''
    for letter in word:
        if letter in 'HONI':
            if letter == 'HONI'[len(block)]:
                block += letter
                if block == 'HONI':
                    block = ''
                    honis += 1
    return honis
