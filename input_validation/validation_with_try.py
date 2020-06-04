"""
Program: validation_with_try.py
Author: Michael Skyberg, mskyberg@dmacc.edu
Last date modified: June 2020

Purpose: calculate the average test scores
"""


def average(score1, score2, score3):
    # calculate the average of 3 scores and return
    try:
        if score1 < 0 or score2 < 0 or score3 < 0:
            raise ValueError
        avg = (float(score1) + float(score2) + float(score3)) / 3
    except:
        raise ValueError
    else:
        return avg


if __name__ == '__main__':
    # prompt the user to enter last name, first name and age
    last_name = input('Please enter last name:')
    first_name = input('Please enter first name:')
    age = input('Please enter age:')

    # get score 1 from user input
    score_one = input('Please enter score 1:')
    # get score 2 from user input
    score_two = input('Please enter score 2:')
    # get score 3 from user input
    score_three = input('Please enter score 3:')

    # calculate the average of scores
    average_scores = average(score_one, score_two, score_three)

    # output the formatted score with person information
    print(f'{last_name}, {first_name} age: {age} average grade: '
          f'{average_scores:.2f}')

# Test Cases
# Last Name     First Name      Age     Score1 Score2 Score3    Output
# Skyberg       Michael         30      98     90     92        Skyberg, Michael age: 30 average grade: 93.33
# Smith         Jack            13      99     89     79        Smith, Jack age: 13 average grade: 89.00
