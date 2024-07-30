'''Write a program that determines if a given year is a leap year or not. A year is considered a leap year if it satisfies the following conditions:

It is divisible by 400, or
It is divisible by 4 but not divisible by 100.'''

year=input("Enter a year to check if a given year is a leap year or not")
year=int(year)
if(year % 400==0) or (year % 100 != 0 and year % 4 == 0):
    print("Leap year")
else:
    print("Not a Leap year")