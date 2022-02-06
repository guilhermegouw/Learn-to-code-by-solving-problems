"""
Due to overwhelming demand, the principal has installed one of those 
"take a number" dispensers to help the attendance secretary manage the line for
late slips. 
The dispenser is filled with slips of paper numbered in order from 1 to 999. 
The principal has made sure to order lots of refills! 
The attendance desk opens at 8:00 am every morning and closes at 3:00 pm. 
When a late student arrives they take the next number from the machine, and when 
the attendance secretary is ready, he calls the next number in order. 
When a student takes the last number, the secretary immediately refills the 
machine with a new set of numbers from 1 to 999. At 3:00 pm, he removes the 
dispenser and stores it for the next day, then serves any students who are still 
waiting with numbers in their hands before closing for the day.

You will be given detailed data for a number of days in the late slip lineup. 

The first line contains an integer (1-1000) representing the next number in the 
take a number machine. 
This will be followed by some number of lines (up to 1 000 000) representing the 
activity at the attendance desk. 

If a line contains the word TAKE, it means a student has arrived and taken the 
next number (when a student takes the last number available, the machine is 
immediately refilled). 

If a line contains the word SERVE it means that the attendance secretary has 
served the next student in line (this word will only appear in the file when 
there is at least one student waiting). 

If a line contains the word CLOSE it means that the desk has closed for the day 
and the attendance secretary will serve the students remaining in line and then 
go home. 

At no time will there be more than 999 students waiting in line to be served.

Your job is to keep track of the line. 
Each time you encounter the word CLOSE, you must print three integers on a 
single line, each separated by a single space. 

The first integer represents the number of students who were late that day, 

the second integer represents the number of students who remained in line after 
the desk was closed, 

and the third integer represents the next number in the take a number machine 
for the next day.

Sample Input

23
TAKE,
TAKE,
SERVE,
TAKE
SERVE,
SERVE,
CLOSE,
TAKE
TAKE,
TAKE,
SERVE,
CLOSE,
TAKE
SERVE
TAKE
SERVE
TAKE
TAKE
TAKE
TAKE
TAKE
TAKE
SERVE
CLOSE

Sample Output

3 0 26
3 2 29
8 5 37
"""


def take_a_number(next_num: int, activities: list[int]) -> list[tuple[int]]:
    late_students = 0
    served_students = 0
    in_line_students = 0
    prints = []
    for activity in activities:
        if activity == "TAKE":
            late_students += 1
            next_num += 1
            in_line_students += 1
        if activity == "SERVE":
            served_students += 1
            in_line_students -= 1
        if activity == "CLOSE":
            prints.append((late_students, in_line_students, next_num))
            late_students = 0
            served_students = 0
            in_line_students = 0
    return prints


if __name__ == "__main__":
    print(
        take_a_number(
            23,
            [
                "TAKE",
                "TAKE",
                "SERVE",
                "TAKE",
                "SERVE",
                "SERVE",
                "CLOSE",
                "TAKE",
                "TAKE",
                "TAKE",
                "SERVE",
                "CLOSE",
            ],
        )
    )
