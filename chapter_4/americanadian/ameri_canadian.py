"""
Canadian Computing Competition: 2002 Stage 1, Junior #2

Americans spell differently from Canadians. 
Americans write neighbor and color while Canadians write neighbour and colour. 
Write a program to help Americans translate to Canadian.

Your program should interact with the user in the following way. 
The user should type a word (not to exceed 64 letters) and if the word appears 
to use American spelling, the program should echo the Canadian spelling for 
the same word. 
If the word does not appear to use American spelling, it should be output 
without change. 
When the user types quit! the program should terminate.

The rules for detecting American spelling are quite naive: 
If the word has more than four letters and has a suffix consisting of a consonant 
followed by 'or', you may assume it is an American spelling, and that the equivalent 
Canadian spelling replaces the or by our. Note: you should treat the letter y as 
a vowel.

Sample Input

color
for
taylor
quit!

Sample Output

colour
for
taylour
"""

def american_to_canadian(sentence: str) -> str:
    # import ipdb; ipdb.sset_trace()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    words = sentence.split()
    canadian_words = []
    for word in words:
        if len(word) > 3 and word[-3] not in vowels and word[-2:] == 'or':
            word = word[:-2] + 'our'
        canadian_words.append(word)
    return ' '.join(canadian_words)

if __name__=='__main__':
    american_to_canadian('color')