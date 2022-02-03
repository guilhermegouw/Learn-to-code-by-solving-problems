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

def lukas_encoder(msg):
    vowels = ['a', 'e', 'i', 'o', 'u']
    encoded_phrase = ''
    for letter in msg:
        if letter in vowels:
            encoded_phrase += f'{letter}p{letter}'
        else:
            encoded_phrase += letter
    return encoded_phrase

def lukas_decoder(msg):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for count, letter in enumerate(msg, 1):
        if letter in vowels:
            msg = msg[:count] + msg[count + 2:]
    return msg


if __name__=='__main__':
    print(lukas_encoder('i like you'))
    print(lukas_decoder('ipi lipikepe yopoupu'))
