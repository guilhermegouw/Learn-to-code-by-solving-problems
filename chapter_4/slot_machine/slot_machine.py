"""
Martha takes a jar of quarters to the casino with the intention of becoming rich. 
She plays three machines in turn. Unknown to her, the machines are entirely predictable. 
Each play costs one quarter. 

The first machine pays 30 quarters every 35 th time it is played; 
the second machine pays 60 quarters every 100 th time it is played; 
the third pays 9 quarters every 10 th time it is played.

Input Specification

Your program should take as input the number of quarters in Martha's jar (there will be at least one and fewer than 1000), 
and the number of times each machine has been played since it last paid.

Output Specification

Your program should output the number of times Martha plays until she goes broke.

Sample Input

48
3
10
4

Sample Output

Martha plays 66 times before going broke.
"""


def slot_machine(quaters_left: int, machine_1_attempts_made, machine_2_attempts_made, machine_3_attempts_made):
    attempts_to_win_1 = 35 - machine_1_attempts_made
    attempts_to_win_2 = 100 - machine_2_attempts_made
    attempts_to_win_3 = 10 - machine_3_attempts_made
    plays = 0
    while quaters_left:
        attempts_to_win_1 -= 1
        quaters_left -= 1
        plays += 1
        if attempts_to_win_1 == 0:
            quaters_left += 30
            attempts_to_win_1 = 35
        if quaters_left > 0:
            attempts_to_win_2 -= 1
            quaters_left -= 1 
            plays += 1
            if attempts_to_win_2 == 0:
                quaters_left += 60
                attempts_to_win_2 = 100
        if quaters_left > 0:
            attempts_to_win_3 -= 1
            quaters_left -= 1 
            plays += 1
            if attempts_to_win_3 == 0:
                quaters_left += 9
                attempts_to_win_3 = 10
    return f'Martha plays {plays} times before going broke.'