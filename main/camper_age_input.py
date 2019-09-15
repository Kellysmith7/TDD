"""
Program: camper_age_input.py
Author: Kelly Smith
Last date updated: 09/03/2019

Program to convert a child's age from years to months
"""


def convert_to_months(x):
    months_years = 12
    years_in_months = x * months_years
    return years_in_months


if __name__ == '__main__':
    age = input('Please enter child age in years')
    y = convert_to_months(age)
    print(y)
