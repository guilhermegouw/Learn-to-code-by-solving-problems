"""
Borko has a row of three opaque cups: one at the left (location 1), one at the middle (location 2), and one at the right (location 3).
There is a ball under the cup at the left. It’s our job to keep track of the location of the ball as Borko swaps the locations of the cups.

Borko can make three types of swap:

A Swap the left and middle cups
B Swap the middle and right cups
C Swap the left and right cups

For example, if Borko’s first swap is type A, then he swaps the left and middle cups; 
because the ball starts at the left, this swap moves it to the middle. 

If instead his first swap is type B, then he swaps the middle and right cups; the left cup stays where it is, so the ball doesn’t change locations.

Input

The input is one line of at most 50 characters. Each character specifies a type of swap that Borko makes: A , B , or C .

Output

Output the final location of the ball:
• 1 if the ball is at the left
• 2 if the ball is at the middle
• 3 if the ball is at the right
"""


def get_ball_location(swaps):
    current_ball_location = 1
    for swap in swaps:
        if swap == 'A' and current_ball_location == 1:
            current_ball_location = 2
        elif swap == 'A' and current_ball_location == 2:
            current_ball_location = 1
        elif swap == 'B' and current_ball_location == 2:
            current_ball_location = 3
        elif swap == 'B' and current_ball_location == 3:
            current_ball_location = 2
        elif swap == 'C' and current_ball_location == 1:
            current_ball_location = 3
        elif swap == 'C' and current_ball_location == 3:
            current_ball_location = 1
    return current_ball_location