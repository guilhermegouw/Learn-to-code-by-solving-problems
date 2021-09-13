"""
Luka is writing a secret sentence in class. He doesn’t want the teacher to be able to read it, 
so instead of writing down the original sentence, he writes down an encoded version. 
After each vowel in the sentence (a, e, i, o, or u), he adds the letter p and that vowel again. 
For example, rather than write down the sentence: 

i like you 

He would write:

ipi lipikepe yopoupu.

The teacher acquires Luka’s encoded sentence. Recover Luka’s original sentence for the teacher.

Input

The input is one line of text, Luka’s encoded sentence. It consists of lowercase letters and spaces. 
There is exactly one space between each pair of words. The maximum length of the line is 100 characters.

Output

Output Luka’s original sentence.
"""

def lukas_decoder(encoded_phrase):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in encoded_phrase:
        if letter in vowels:
            pass
    return encoded_phrase
